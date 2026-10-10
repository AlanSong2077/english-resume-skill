---
name: cs-resume-generator
description: Create or revise English resumes for US/UK Computer Science master's applications from supplied facts, with JSON and LaTeX output and optional PDF generation. Use for CS graduate application resumes or 申请简历.
---

# CS application resume

Turn supplied experiences into a clear, accurate English resume. Polish wording without inventing credentials or achievements.

## Fact integrity

- Use supplied facts only. Never invent dates, metrics, GPA scales, rankings, leadership, methods, publication status, advisors, or project scale.
- Preserve original GPA/average and its stated scale; do not convert 90/100 into a 4.0 GPA without an explicitly supplied official conversion.
- Preserve contribution level: participation does not imply ownership or leadership. Technical tools mentioned in one experience do not justify inventing an architecture or specialization.
- Resolve contradictory facts with the user; do not silently select a version. Mark uncertain items in a separate review note and omit them from the final resume until resolved.
- Examples are fictional syntax examples, never a source for the applicant's facts.

## Workflow

1. Read supplied documents using available extraction tools. Inspect tables and headers when relevant. Check extraction quality; scanned PDFs require OCR. Do not reject usable PDF tools or install dependencies automatically.
2. Create a fact inventory identifying source and unresolved questions. Apply the mandatory human verification gate below to every unclear, missing or contradictory item. Continue only with a clearly labelled draft of verified sections while awaiting the user; do not finalize until the gate is satisfied.
3. Select research or professional emphasis from the user's target. Program-specific requirements supplied by the user take priority; verify current requirements when making school-specific claims. Avoid universal school prestige rankings or invented admissions criteria.
4. Rewrite verified achievements using contribution, method and result when provided. Omit unsupported metrics. Do not manufacture research or publications to fill space.
5. Read references/schema.md and build JSON following assets/example_resume_data.json. Use score for original percentage averages and gpa only for a supplied GPA. Name and email are required for generation; other sections are optional. Dates, location, phone, advisor and metrics may be omitted. Keep unresolved facts outside resume JSON. Use profile research or professional; section_order may reorder all seven supported section keys.
6. Generate LaTeX using the command below. Produce a draft without stopping for cosmetic choices. Before calling the resume final, obtain explicit human resolution of every verification item, including approval to omit unavailable facts. Disclosure alone does not satisfy this requirement. Do not submit or share externally as part of generation.
7. If a compiler is available, generate PDF. Inspect rendered pages and extracted PDF text for clipping, page breaks, missing glyphs, empty headings, working links, and consistency with source facts. Aim for the user's page limit; shorten content before making text too small. If rendering is unavailable, deliver the source and state what remains unverified.
8. Deliver editable JSON, LaTeX and PDF when available, plus concise unresolved items. Keep personal data in the user's output location; do not copy it into this skill or distribute it with the skill package.

## Generation

```bash
python3 <skill_path>/scripts/generate_resume.py applicant.json -o <output_path>/resume.tex
# Add --pdf only when PDF compilation is desired.
```

The script uses Python's standard library. PDF generation tries tectonic, xelatex, lualatex, then pdflatex, and reports failure without treating an old PDF as successful. Tectonic may download missing packages; use an installed compiler or available platform compiler when network access is unavailable. The template uses Latin fonts; non-Latin text needs appropriate font configuration and visual checks. Unicode support depends on compiler and fonts.

Empty sections are omitted. Default header includes name, email and optional phone. Add verified portfolio/GitHub links when useful and requested; this default is a layout choice, not an admissions requirement. Custom templates must contain {{FULL_NAME}}, {{CONTACT}} and {{SECTIONS}}.

The former ReportLab backend is removed to avoid inconsistent schemas, unescaped markup and differing content. Use the single LaTeX backend or the host application's standalone LaTeX compiler when available.


## 用户环境与下载 / Python and LaTeX downloads

用 Python 生成 LaTeX；生成 PDF 则需要额外的 LaTeX 编译器。Python 脚本不需要 pip 第三方依赖。保留本技能现有制式排版、字段结构和内容，不为演示改字体、页边距、颜色、标题样式或模板。

- Python 官方下载：[Python downloads](https://www.python.org/downloads/)。安装当前受支持的 Python 3；Windows 安装时启用 Python 的 PATH 选项。
- Windows：[MiKTeX 官方下载](https://miktex.org/download)。安装后确保 xelatex 在 PATH 中；缺少宏包时可能需要下载。
- macOS：[MacTeX 官方下载](https://tug.org/mactex/)。安装后重新打开终端，确认 xelatex 可用。
- Linux：[TeX Live 官方说明](https://tug.org/texlive/)。也可使用发行版软件管理器安装 TeX Live 和所需宏包。

下载页面提供安装程序；本技能不附带安装程序，也不自动安装软件。PDF 所需宏包包括 geometry、enumitem、titlesec、hyperref、xcolor、parskip。下载后按官方说明安装，执行 `python3 --version` 和 `xelatex --version` 检查环境；Windows 可用 `py -3 --version`。

```bash
# 在解压后的 cs-resume-generator 文件夹运行：只生成 LaTeX
python3 scripts/generate_resume.py examples/01-research-ai.json -o generated/resume.tex
# 安装编译器后：生成 LaTeX 和 PDF
python3 scripts/generate_resume.py examples/01-research-ai.json -o generated/resume.tex --pdf
```

Windows 可将上述 python3 替换为 py -3。没有编译器时省略 --pdf，仍可获得可编辑的 .tex。

## 四套虚构示例 / Four fictional demonstrations

阅读 examples/DEMO-GUIDE.md 获取人物背景、填写方法与命令。所有人物、机构、研究、量化成果及奖项均为教学虚构；示例中的 example.com 链接是格式演示，并非真实项目仓库。

- 研究型：突出研究方法、实验和学术背景，不添加申请人材料中不存在的论文。01 为机器学习本科生，02 为数学转计算机的科学计算申请人。两套案例均不设论文条目，展示有研究而无发表时如何填写。
- 就业型：工作经历优先，展示技术贡献和可点击的项目链接。03 为后端工程师，04 为移动端与无障碍产品工程师。

生成真实简历时，用使用者提供且已确认的事实替换虚构字段；保留原有制式排版，切勿复制示例经历或数字冒充真实材料。


## 必须人工校验 / Mandatory human verification gate

此环节位于信息提取之后、正式生成与交付之前，并贯穿润色和最终检查。凡是不清楚、缺失、矛盾或经过语义推断的信息，必须由提供材料的用户人工核验。禁止用默认值、上下文猜测或静默省略绕过核验。

### 建立待核验清单

逐项记录：字段或经历、原始材料及来源、具体疑点或缺失内容、需用户回答的问题、核验状态。尤其检查姓名与联系方式、学校与学位、日期、成绩及其量表、排名、导师与角色、技术方法、个人贡献、量化成果、论文状态和项目链接。

缺少可选信息也要核验：例如电话、日期或项目指标，用户可以补充，也可以明确要求省略。不要要求用户提供与本次简历无关的个人信息；不适用的章节由用户确认“不适用/无此经历”即可，不必逐个追问其内部字段。虚构 DEMO 不得作为核实真实申请人事实的来源。

### 收集人工决定

将问题合并成一份清晰清单，给每项提供可执行的回答方式：
- 补充准确内容；
- 确认现有表述准确；
- 更正冲突或误解；
- 明确批准省略；
- 确认该项不适用。

不得替用户自动选择。人工确认是用户对事实或省略的明确决定，不是要求每项都必须上传证明。若用户补充了新材料，重新检查其中尚未解决的疑点。

### 正式版门槛

只有全部待核验项都得到明确处理，才能将结果标为正式版或完成版。用户未回复、回复含糊、仅告知“缺资料”或等待超时，均不算核验通过。

等待期间可以整理已经确认的部分，生成明确标注“待人工核验草稿”的预览；草稿状态在交付说明和文件名中标明，不改变制式模板。必须同时附上未解决清单，不声称简历已完成。状态清单存放在用户工作目录，不能插入真实简历正文或随技能公开分发。

最终核对时检查英文润色是否改变角色、贡献或事实含义；若产生新疑点，重新进入人工核验。Python 脚本仅校验字段结构，不能判定事实准确或代替人工确认；即使直接运行脚本成功，也不代表人工核验通过。
