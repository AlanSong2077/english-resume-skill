#!/usr/bin/env python3
"""
CS Graduate School Resume Generator
Generates professional LaTeX resume for US/UK CS MS applications
"""

import json
import re
import sys
import os
import shutil
from urllib.parse import urlsplit, quote
from pathlib import Path

def load_template(template_path):
    """Load LaTeX template file"""
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_data(data_path):
    """Load resume data from JSON"""
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def escape_latex(text):
    """Escape special LaTeX characters"""
    # First replace backslash to avoid double-escaping
    text = text.replace('\\', '\x00')  # Use placeholder
    replacements = [
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    # Now replace placeholder with actual backslash command
    text = text.replace('\x00', r'\textbackslash{}')
    return text

def safe_url(value):
    if urlsplit(value).scheme not in ('http', 'https'):
        raise ValueError('Project URLs must use http or https')
    return quote(value, safe=':/?=+@,;.-_').replace('%', r'\%').replace('&', r'\&').replace('#', r'\#')


def validate_data(data):
    if not isinstance(data, dict):
        raise ValueError('Resume JSON must be an object')
    personal = data.get('personal_info')
    if not isinstance(personal, dict):
        raise ValueError('personal_info must be an object')
    for key in ('full_name', 'email'):
        if not isinstance(personal.get(key), str) or not personal[key].strip():
            raise ValueError('personal_info.' + key + ' must be a nonempty string')
    if 'phone' in personal and not isinstance(personal['phone'], str):
        raise ValueError('personal_info.phone must be a string')
    required = {'education': ('institution', 'degree'), 'research': ('title',),
                'experience': ('company', 'role'), 'projects': ('name',),
                'publications': ('authors', 'title', 'venue'), 'awards': ('name',)}
    for section, fields in required.items():
        entries = data.get(section, [])
        if not isinstance(entries, list):
            raise ValueError(section + ' must be a list')
        for i, entry in enumerate(entries):
            label = f'{section}[{i}]'
            if not isinstance(entry, dict):
                raise ValueError(label + ' must be an object')
            for key in fields:
                if not isinstance(entry.get(key), str) or not entry[key].strip():
                    raise ValueError(label + '.' + key + ' must be a nonempty string')
            for key, value in entry.items():
                if key in ('description', 'courses') and not (section == 'awards' and key == 'description'):
                    if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
                        raise ValueError(label + '.' + key + ' must be a list of strings')
                elif not isinstance(value, str):
                    raise ValueError(label + '.' + key + ' must be a string')
            if section in ('research', 'experience', 'projects'):
                entry.setdefault('description', [])
            if entry.get('url'):
                safe_url(entry['url'])
    skills = data.get('skills', {})
    if not isinstance(skills, dict) or not all(isinstance(v, str) for v in skills.values()):
        raise ValueError('skills must be an object of strings')
    if set(skills) - {'languages', 'frameworks', 'systems', 'specialties'}:
        raise ValueError('Unsupported skills category')
    if data.get('profile', 'research') not in ('research', 'professional'):
        raise ValueError('profile must be research or professional')


def format_header(data):
    """Format personal info header - only Email and Phone, no headline"""
    p = data['personal_info']
    return {
        'FULL_NAME': escape_latex(p['full_name']),
        'EMAIL': escape_latex(p['email']),
        'PHONE': escape_latex(p.get('phone', ''))
    }

def format_education(data):
    """Format education section - location on separate line from coursework"""
    entries = []
    for edu in data.get('education', []):
        lines = []
        # Line 1: Institution and Date
        lines.append(f"\\textbf{{{escape_latex(edu['institution'])}}} \\hfill \\textit{{{escape_latex(edu.get('date', ''))}}}")
        # Line 2: Degree and Location
        lines.append(f"{escape_latex(edu['degree'])} \\hfill {escape_latex(edu.get('location', ''))}")
        
        # Line 3: GPA and ranking (if available)
        if any(k in edu for k in ('gpa', 'score', 'ranking')):
            info_parts = []
            if 'gpa' in edu and edu['gpa']:
                info_parts.append(f"GPA: {edu['gpa']}")
            if edu.get('score'):
                info_parts.append(f"Average: {edu['score']}")
            if 'ranking' in edu and edu['ranking']:
                info_parts.append(f"Class Ranking: {edu['ranking']}")
            if info_parts:
                lines.append(f"\\textit{{{escape_latex(', '.join(info_parts))}}}")
        
        # Line 4: Empty line before coursework
        lines.append("")
        
        # Line 5: Relevant courses (separate line with blank line before)
        if 'courses' in edu and edu['courses']:
            courses = [escape_latex(c) for c in edu['courses']]
            lines.append(f"\\textbf{{Relevant Coursework:}} {', '.join(courses)}")
        
        lines.append("\\vspace{4pt}")
        lines[0] += r'\\'
        lines[1] += r'\\'
        entries.append('\n'.join(lines))
    
    return '\n\n'.join(entries)

def format_research(data):
    """Format research experience section"""
    entries = []
    for research in data.get('research', []):
        lines = []
        # Title and lab
        title_line = f"\\textbf{{{escape_latex(research['title'])}}}"
        title_line += f" \\hfill \\textit{{{escape_latex(research.get('date', ''))}}}"
        lines.append(title_line)
        
        # Lab and advisor
        lab_info = ' | '.join(filter(None, [research.get('lab', ''), ('Advisor: ' + research['advisor']) if research.get('advisor') else '']))
        lines.append(f"\\textit{{{escape_latex(lab_info)}}}")
        
        # Bullet points
        desc_lines = [f"\\item {escape_latex(d)}" for d in research['description']]
        lines.append(f"\\begin{{itemize}}[leftmargin=*,noitemsep,topsep=2pt]")
        lines.extend(desc_lines)
        lines.append(f"\\end{{itemize}}")
        
        lines[0] += r'\\'
        entries.append('\n'.join(lines))
    
    return '\n\n'.join(entries)

def format_experience(data):
    """Format professional experience section"""
    entries = []
    for exp in data.get('experience', []):
        lines = []
        # Company and role
        lines.append(f"\\textbf{{{escape_latex(exp['company'])}}} \\hfill \\textit{{{escape_latex(exp.get('date', ''))}}}")
        lines.append(f"\\textit{{{escape_latex(exp['role'])}}} \\hfill {escape_latex(exp.get('location', ''))}")
        
        # Bullet points
        desc_lines = [f"\\item {escape_latex(d)}" for d in exp['description']]
        lines.append(f"\\begin{{itemize}}[leftmargin=*,noitemsep,topsep=2pt]")
        lines.extend(desc_lines)
        lines.append(f"\\end{{itemize}}")
        
        lines.append("\\vspace{4pt}")
        lines[0] += r'\\'
        entries.append('\n'.join(lines))
    
    return '\n\n'.join(entries)

def format_projects(data):
    """Format projects section with optional URL hyperlink"""
    entries = []
    for proj in data.get('projects', []):
        lines = []
        # Project name with optional URL hyperlink and tech
        name = escape_latex(proj['name'])
        if 'url' in proj and proj['url']:
            # Create hyperlink - do not escape the URL itself
            title_line = f"\\textbf{{\\href{{{safe_url(proj['url'])}}}{{{name}}}}}"
        else:
            title_line = f"\\textbf{{{name}}}"
        title_line += f" \\hfill \\textit{{{escape_latex(proj.get('date', ''))}}}"
        lines.append(title_line)
        lines.append(f"\\textit{{{escape_latex(proj.get('tech', ''))}}}")
        
        # Bullet points
        desc_lines = [f"\\item {escape_latex(d)}" for d in proj['description']]
        lines.append(f"\\begin{{itemize}}[leftmargin=*,noitemsep,topsep=2pt]")
        lines.extend(desc_lines)
        lines.append(f"\\end{{itemize}}")
        
        if not proj.get('tech'):
            del lines[1]
        else:
            lines[0] += r'\\'
        entries.append('\n'.join(lines))
    
    return '\n\n'.join(entries)

def format_publications(data):
    """Format publications section"""
    pubs = data.get('publications', [])
    if not pubs:
        return ""
    
    lines = []
    for i, pub in enumerate(pubs, 1):
        authors = escape_latex(pub['authors'])
        title = escape_latex(pub['title'])
        venue = escape_latex(pub['venue'])
        status = escape_latex(pub.get('status', ''))
        
        pub_line = f"[{i}] {authors}. \\textbf{{{title}}}. \\textit{{{venue}}}"
        if status:
            pub_line += f", {status}"
        pub_line += "."
        lines.append(pub_line)
    
    return '\n\n'.join(lines)

def format_skills(data):
    """Format technical skills section"""
    skills = data.get('skills', {})
    lines = []
    
    if 'languages' in skills:
        lines.append(f"\\textbf{{Programming Languages:}} {escape_latex(skills['languages'])}")
    if 'frameworks' in skills:
        lines.append(r"\textbf{Frameworks \& Libraries:} " + escape_latex(skills['frameworks']))
    if 'systems' in skills:
        lines.append(r"\textbf{Systems \& Tools:} " + escape_latex(skills['systems']))
    if 'specialties' in skills:
        lines.append(f"\\textbf{{Specializations:}} {escape_latex(skills['specialties'])}")
    
    return '\n\n'.join(lines)

def format_awards(data):
    """Format honors and awards section"""
    awards = data.get('awards', [])
    lines = []
    
    for award in awards:
        line = f"\\textbf{{{escape_latex(award['name'])}}}"
        if 'year' in award:
            line += f" \\hfill {escape_latex(award['year'])}"
        if 'description' in award:
            line += f" \\textit{{-- {escape_latex(award['description'])}}}"
        lines.append(line)
    
    return '\n\n'.join(lines)

def generate_resume(data_path, template_path, output_path):
    """Main function to generate resume"""
    # Load data and template
    data = load_data(data_path)
    validate_data(data)
    template = load_template(template_path)
    
    header = format_header(data)
    for key, value in header.items():
        template = template.replace('{{' + key + '}}', value)
    formatters = {
        'education': ('Education', format_education),
        'research': ('Research Experience', format_research),
        'experience': ('Professional Experience', format_experience),
        'projects': ('Selected Projects', format_projects),
        'publications': ('Publications', format_publications),
        'skills': ('Technical Skills', format_skills),
        'awards': (r'Honors \& Awards', format_awards),
    }
    default = list(formatters)
    if data.get('profile') == 'professional':
        default = ['education', 'experience', 'projects', 'research', 'publications', 'skills', 'awards']
    order = data.get('section_order', default)
    if len(order) != len(set(order)) or set(order) != set(formatters):
        raise ValueError('section_order must contain each supported section exactly once')
    sections = []
    for key in order:
        if data.get(key):
            title, formatter = formatters[key]
            content = formatter(data)
            if content:
                sections.append('\\section{' + title + '}\n' + content)
    template = template.replace('{{CONTACT}}', r' \quad | \quad '.join(
        escape_latex(value) for value in [data['personal_info']['email'], data['personal_info'].get('phone', '')] if value))
    template = template.replace('{{SECTIONS}}', '\n\n'.join(sections))
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"LaTeX resume generated: {output_path}")
    return output_path

def compile_latex(tex_path, output_dir=None):
    """Compile in isolation; publish only a fresh successful PDF."""
    import subprocess
    import tempfile
    source = Path(tex_path).resolve()
    target = Path(output_dir).resolve() if output_dir else source.parent
    compiler = next((name for name in ('tectonic', 'xelatex', 'lualatex', 'pdflatex') if shutil.which(name)), None)
    if not compiler:
        raise RuntimeError('No LaTeX compiler found; .tex source was preserved')
    with tempfile.TemporaryDirectory() as temp:
        local = Path(temp) / source.name
        local.write_text(source.read_text())
        if compiler == 'tectonic':
            command = [compiler, '--outdir', temp, str(local)]
        else:
            command = [compiler, '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-output-directory', temp, str(local)]
        for _ in range(1 if compiler == 'tectonic' else 2):
            result = subprocess.run(command, cwd=temp, capture_output=True, text=True, timeout=120)
            if result.returncode:
                raise RuntimeError('LaTeX compilation failed:\n' + (result.stdout + result.stderr)[-4000:])
        pdf = local.with_suffix('.pdf')
        if not pdf.is_file():
            raise RuntimeError('Compiler did not create a PDF')
        target.mkdir(parents=True, exist_ok=True)
        destination = target / pdf.name
        shutil.copy2(pdf, destination)
        print(f'PDF generated: {destination}')
        return str(destination)

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate CS grad school resume')
    parser.add_argument('data', help='Path to resume data JSON file')
    parser.add_argument('-t', '--template', default=None, help='Path to LaTeX template')
    parser.add_argument('-o', '--output', default='resume.tex', help='Output LaTeX file path')
    parser.add_argument('--pdf', action='store_true', help='Also compile to PDF')
    
    args = parser.parse_args()
    
    # Default template path
    if args.template is None:
        script_dir = Path(__file__).parent.parent
        args.template = script_dir / 'assets' / 'templates' / 'resume_template.tex'
    
    # Generate resume
    tex_path = generate_resume(args.data, args.template, args.output)
    
    # Compile to PDF if requested
    if args.pdf:
        compile_latex(tex_path)
