import importlib.util,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('resume',root/'scripts/generate_resume.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Checks(unittest.TestCase):
 def test_minimal(self):
  with tempfile.TemporaryDirectory() as t:
   j=Path(t)/'data.json';j.write_text(json.dumps({'personal_info':{'full_name':'A & B','email':'a@example.com'},'education':[{'institution':'Example','degree':'BS'}]}))
   o=Path(t)/'nested/resume.tex';m.generate_resume(j,root/'assets/templates/resume_template.tex',o);s=o.read_text()
   self.assertNotIn('Manuscripts',s);self.assertNotIn('PUBLICATIONS',s);self.assertNotIn('{{',s);self.assertNotIn('quad |',s);self.assertIn(r'A \& B',s)
 def test_validation(self):
  with self.assertRaisesRegex(ValueError,'full_name'):m.validate_data({'personal_info':{'email':'x'}})
  with self.assertRaisesRegex(ValueError,'list of strings'):m.validate_data({'personal_info':{'full_name':'A','email':'x'},'projects':[{'name':'P','description':'bad'}]})
 def test_url(self):
  self.assertNotIn('{',m.safe_url('https://example.com/{x}?a=1&b=2'))
  with self.assertRaises(ValueError):m.safe_url('file:///tmp/x')
 def test_empty_publications(self):self.assertEqual(m.format_publications({}), '')
 def test_stale_pdf(self):
  with tempfile.TemporaryDirectory() as t:
   tex=Path(t)/'r.tex';tex.write_text('bad');pdf=tex.with_suffix('.pdf');pdf.write_bytes(b'old')
   with patch.object(m.shutil,'which',return_value='/compiler'),patch('subprocess.run') as run:
    run.return_value.returncode=1;run.return_value.stdout='failure';run.return_value.stderr=''
    with self.assertRaisesRegex(RuntimeError,'compilation failed'):m.compile_latex(tex)
   self.assertEqual(pdf.read_bytes(),b'old')
if __name__ == '__main__':
 unittest.main()
