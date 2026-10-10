# English Resume Skill Agent

[中文](README.md) | **English**

**Turn your experiences and existing resume into an accurate, consistently formatted English resume.**

An AI Skill for CS and related master's applications, with research-oriented and professional profiles. The agent extracts and rewrites supplied facts; a standalone Python helper produces editable LaTeX and optional PDF. No invented credentials, dates, metrics or publications.

![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue)
![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)

## Start here

Choose **A** if you want AI to organize your materials and write English. Choose **B** if you already have structured JSON.

### A. Install and invoke the Skill

1. Download this repository as a ZIP and extract it.
2. Rename the extracted directory to `english-resume-skill-agent`. Keep SKILL.md, scripts and assets together.
3. For Codex, place the folder inside `~/.agents/skills/` for user-wide access, or `.agents/skills/` in your project. On Windows use `<user profile>/.agents/skills/`.
4. Check the final path: `.agents/skills/english-resume-skill-agent/SKILL.md`. Avoid an extra nested folder. Reopen Codex if the Skill is not discovered.
5. Attach your existing resume or experience notes and send:

```text
$english-resume-skill-agent
Create an English resume for my CS master's applications from the materials I provide.
Use the research-oriented (or professional) profile and preserve the fixed layout.
Ask me to verify all missing, unclear or contradictory facts before final delivery.
Deliver JSON, LaTeX and a PDF when compilation is available.
```

This requires a host that supports Skills and file execution. Other platforms use their own installation mechanism; ordinary chat interfaces may not execute scripts. See [OpenAI's Skill documentation](https://learn.chatgpt.com/docs/build-skills). Automatic matching is enabled; explicit invocation is more predictable.

### B. Run Python without an AI host

Requires Python 3.9+ with no pip dependencies. Prefer a currently supported Python release. From the repository root:

```bash
# Editable LaTeX only
python3 scripts/generate_resume.py examples/01-research-ai.json -o generated/resume.tex

# LaTeX and PDF, with a LaTeX compiler installed
python3 scripts/generate_resume.py examples/01-research-ai.json -o generated/resume.tex --pdf
```

On Windows replace `python3` with `py -3` if appropriate. The script formats supplied JSON; it does not parse raw documents or independently write resume prose. It needs no AI API key.

## Project-reported outcomes

**30+ Australian university admissions · 20+ US university admissions**

These application outcomes were supplied by the project author, as of October 2026. They have not been independently verified by this repository and do not attribute admission decisions solely to the resume tool. All public examples are fictional.

## Four complete examples

Each fictional resume is two pages, approximately 640–670 English words. People, institutions, advisors, achievements and numbers are invented for instruction. Links to example.com demonstrate clickable project titles rather than real repositories. Click an image to open the preview.

### 1. Research: machine learning and reliable AI

Maya Chen combines undergraduate research, data quality work and an ML internship. The example highlights calibration, controlled comparisons, evaluation protocols and reproducibility, with no invented publication entry.

[![Research resume: machine learning, two-page preview](docs/images/01-research-ai.png)](docs/images/01-research-ai.png)

[PDF](examples/01-research-ai.pdf) · [JSON](examples/01-research-ai.json) · [LaTeX](examples/01-research-ai.tex)

### 2. Research: mathematics to scientific computing

Owen Patel combines applied mathematics, a computing minor, numerical-methods research and teaching. The example shows convergence checks, solver comparisons and preparation for interdisciplinary study. A departmental thesis is not presented as a published paper.

[![Research resume: scientific computing, two-page preview](docs/images/02-research-scientific-computing.png)](docs/images/02-research-scientific-computing.png)

[PDF](examples/02-research-scientific-computing.pdf) · [JSON](examples/02-research-scientific-computing.json) · [LaTeX](examples/02-research-scientific-computing.tex)

### 3. Professional: backend and distributed systems

Daniel Rivera has four years of backend engineering experience. The example covers order services, database performance, task queues, migration checks and failure testing.

[![Professional resume: backend engineering, two-page preview](docs/images/03-professional-backend.png)](docs/images/03-professional-backend.png)

[PDF](examples/03-professional-backend.pdf) · [JSON](examples/03-professional-backend.json) · [LaTeX](examples/03-professional-backend.tex)

### 4. Professional: mobile, HCI and accessibility

Sofia Kim combines mobile development and frontend experience. The example covers startup performance, offline synchronization, usability research and accessible interactions.

[![Professional resume: mobile engineering, two-page preview](docs/images/04-professional-mobile.png)](docs/images/04-professional-mobile.png)

[PDF](examples/04-professional-mobile.pdf) · [JSON](examples/04-professional-mobile.json) · [LaTeX](examples/04-professional-mobile.tex)

See the [demo guide](examples/DEMO-GUIDE.md) and [field reference](references/schema.md). These extensive examples teach structure and wording; they are not a requirement to fill two pages in every application.

## Workflow and human verification

**Read materials → inventory facts → human verification → English rewriting → JSON → LaTeX/PDF → final review.**

The user must supply, confirm, correct, approve omission or mark inapplicable every unclear, missing or contradictory item. Until all items are resolved, only a clearly labelled draft and separate verification checklist may be delivered. Python validates structure; it cannot verify truth or human approval.

Research profiles prioritize research methods, experiments and academic preparation. Professional profiles prioritize employment and technical contributions. Both use the same fixed layout. Empty sections are omitted. Copy an example JSON, replace every fictional fact with verified personal information, and set `profile` to `research` or `professional`. Use `score` for an original percentage average and `gpa` for an explicitly supplied GPA; never invent a conversion.

## Downloads and PDF requirements

Python generates LaTeX. PDF generation additionally needs a compiler in PATH:

- [Python](https://www.python.org/downloads/)
- [MacTeX for macOS](https://tug.org/mactex/)
- [MiKTeX for Windows](https://miktex.org/download)
- [TeX Live for Linux](https://tug.org/texlive/)

The helper tries tectonic, xelatex, lualatex, then pdflatex. Missing packages may require network downloads. Without a compiler, omit `--pdf`. The default template targets English; non-Latin text needs suitable fonts.

## Validation and privacy

```bash
python3 -m unittest discover -s tests
```

The four PDFs were compiled and visually reviewed on macOS with XeLaTeX. Unit tests and relocated-directory checks passed. Windows, Linux, other compilers and other AI hosts have not been fully tested locally. Verify final facts and layout for each real application.

The helper does not upload resumes or call AI APIs. AI-host data handling depends on your selected provider. Keep personal applicant materials outside this repository.

## Contribute and license

Contributions to input handling, errors, portability and documentation are welcome. Discuss fixed-template or content-policy changes in an Issue first. Do not submit real personal data in examples or tests.

Licensed under [Apache-2.0](LICENSE).
