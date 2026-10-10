# JSON fields

Top-level object:
- personal_info: full_name and email are nonempty strings; phone is optional string.
- profile: research (default) or professional.
- section_order: optional list containing education, research, experience, projects, publications, skills, awards exactly once each. Empty sections still disappear.
- education: list; institution and degree required. Optional date, location, gpa, score (original percentage average), ranking; courses is a list of strings.
- research: list; title required. Optional date, lab, advisor; description is a list of strings.
- experience: list; company and role required. Optional date, location; description is a list of strings.
- projects: list; name required. Optional date, tech, http/https url; description is a list of strings.
- publications: list; authors, title and venue required. Optional status. Include only supplied bibliographic facts; empty means no Publications section.
- skills: object with optional languages, frameworks, systems, specialties; each value is a string.
- awards: list; name required. Optional year and description strings.

Use strings for numeric-looking display fields (e.g. "2025", "3.8/4.0", "90/100"). Omit unavailable facts rather than adding placeholders. Research/experience/project descriptions may be omitted or empty. Unsupported skills categories are rejected. The script validates structure, not factual truth; the host must verify source facts.
