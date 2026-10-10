# English Resume Skill Agent

**中文** | [English](README.en.md)

**把中文或零散经历，整理成事实准确、排版统一、可编辑的英文简历。**

面向计算机科学及相关专业的硕士申请，支持研究型与就业型英文简历。通过 AI Skill 整理和润色材料，再使用 Python 与 LaTeX 输出 JSON、LaTeX 源文件和 PDF。

English resume generation for CS graduate applications: a fact-preserving AI Skill workflow with a standalone JSON-to-LaTeX/PDF generator.

![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue)
![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)
![Output: English Resume](https://img.shields.io/badge/Output-English%20Resume-success)

## 第一次使用：选一种方式

**想让 AI 帮你整理材料、写英文？** 安装 Skill 后调用它。**已经有整理好的 JSON？** 直接运行 Python。

### A. 安装 Skill，让 AI 生成英文简历

下载本仓库 ZIP 并解压，将文件夹命名为 `english-resume-skill-agent`，确认 `SKILL.md` 在该文件夹根目录。把整个文件夹放到 Codex 的用户 Skill 目录 `~/.agents/skills/`，或当前项目的 `.agents/skills/` 中。Windows 使用 `<user profile>/.agents/skills/`。

安装后的目录应是 `.agents/skills/english-resume-skill-agent/SKILL.md`，避免多套一层文件夹。若没有发现 Skill，重新打开 Codex。

然后粘贴下面的指令，并附上你的经历或现有简历：

```text
$english-resume-skill-agent
请根据我提供的材料生成英文简历，用于 CS 硕士申请。
采用研究型（或就业型）顺序，保持制式排版。
缺失、不明确或矛盾的信息必须先让我人工核验。
请交付 JSON、LaTeX，以及编译条件允许时的 PDF。
```

**AI 使用者需要支持 Skill 和文件执行的工具；普通聊天窗口不一定能运行脚本。**其他平台的安装位置以其官方说明为准。

### B. 不使用 AI，直接生成文件

安装 Python，在本仓库根目录执行：

```bash
python3 scripts/generate_resume.py examples/01-research-ai.json -o generated/resume.tex
```

想生成 PDF，先安装 LaTeX 编译器，然后在命令末尾加 `--pdf`。Windows 可用 `py -3` 替换 `python3`。输入必须是已经整理好的 JSON；脚本不会自行理解原始简历或写英文。

## 项目应用成果

**30+ 澳大利亚院校录取 · 20+ 美国院校录取**

以上为项目作者提供的应用成果数据，更新于 2026 年 10 月。数据未经本仓库独立核验，也不表示录取结果由简历生成工具单独促成。公开示例均为虚构教学案例，不包含真实申请人的私人材料。

## 可以做什么

- 将已有简历、Word/PDF、中文笔记和零散经历整理为英文申请简历。
- 研究型：突出研究问题、方法、实验设计、个人贡献与学术背景。
- 就业型：优先展示工作经历、技术贡献、性能结果和可点击项目链接。
- 对不清楚、缺失或矛盾的信息进行必需的人工核验。
- 没有论文就省略论文栏目，不推测 GPA、日期或量化成果。
- 使用固定模板输出，保留统一字体、颜色、页边距和章节样式。
- 保留 JSON 与 LaTeX 源文件，便于后续更新和复用。

## 四套完整成果展示

每套示例均为两页，约 640–670 个英文词。人物、机构、经历、导师、指标和奖项均为教学虚构；项目链接使用 example.com 演示，不是真实项目地址。点击图片可查看完整预览，点击 PDF 可打开排版成品。

### 1. 研究型：机器学习与可靠 AI

Maya Chen：计算机本科，具备可靠机器学习、数据质量研究和机器学习实习经历。示例展示对照实验、模型校准、数据划分、评估指标和实验复现；没有虚构发表论文。

[![机器学习研究型英文简历：两页预览](docs/images/01-research-ai.png)](docs/images/01-research-ai.png)

[PDF](examples/01-research-ai.pdf) · [JSON 输入](examples/01-research-ai.json) · [LaTeX 源文件](examples/01-research-ai.tex)

### 2. 研究型：数学转科学计算

Owen Patel：应用数学本科、计算机辅修，具备数值求解研究、本科论文与助教经历。示例展示收敛验证、求解器比较、优化方法及跨专业准备；毕业论文不冒称发表论文。

[![科学计算研究型英文简历：两页预览](docs/images/02-research-scientific-computing.png)](docs/images/02-research-scientific-computing.png)

[PDF](examples/02-research-scientific-computing.pdf) · [JSON 输入](examples/02-research-scientific-computing.json) · [LaTeX 源文件](examples/02-research-scientific-computing.tex)

### 3. 就业型：后端与分布式系统

Daniel Rivera：软件工程本科，四年电商后端工作经历。示例展示订单服务、数据库优化、任务队列、迁移检查、故障测试和运维协作。

[![后端工程就业型英文简历：两页预览](docs/images/03-professional-backend.png)](docs/images/03-professional-backend.png)

[PDF](examples/03-professional-backend.pdf) · [JSON 输入](examples/03-professional-backend.json) · [LaTeX 源文件](examples/03-professional-backend.tex)

### 4. 就业型：移动端、HCI 与无障碍

Sofia Kim：计算机本科，三年移动端开发经历。示例展示启动性能、离线同步、可用性研究、屏幕阅读器体验和无障碍测试。

[![移动端就业型英文简历：两页预览](docs/images/04-professional-mobile.png)](docs/images/04-professional-mobile.png)

[PDF](examples/04-professional-mobile.pdf) · [JSON 输入](examples/04-professional-mobile.json) · [LaTeX 源文件](examples/04-professional-mobile.tex)

更多人物背景和复现命令见 [DEMO 使用指南](examples/DEMO-GUIDE.md)。这些长版示例用于展示填写方式，真实申请应根据院校要求和相关性取舍内容。

## 使用流程

**读取材料 → 整理事实 → 人工核验 → 英文润色 → JSON → LaTeX/PDF → 最终核对**

AI 负责理解和润色；Python 负责结构校验与固定排版。事实不明确时，用户必须补充、确认、更正、批准省略或确认不适用。全部疑点处理前只能交付待核验草稿，不能标为正式版。

## 方式一：作为 Skill 使用

下载或克隆整个仓库，把完整的 `english-resume-skill-agent` 文件夹安装到支持 Skill 的工具中，不能只复制 SKILL.md。

Codex 可安装到用户目录 `~/.agents/skills/english-resume-skill-agent`，或项目目录 `.agents/skills/english-resume-skill-agent`。Windows 用户目录对应 `<user profile>/.agents/skills/english-resume-skill-agent`。避免安装多个同名副本。

安装后输入：

```text
$english-resume-skill-agent
请根据我提供的材料生成英文 CS 硕士申请简历。
采用研究型（或就业型）顺序，保持制式排版。
不清楚或缺失的信息必须先让我人工核验，不要使用 DEMO 的经历或数字。
```

自动匹配已启用，显式调用更可控。安装位置参考 [OpenAI 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。其他平台需要遵循其 Skill 安装机制；本仓库没有声称已在所有平台完成实测。

## 方式二：直接使用 Python

结构化 JSON 已经准备好时，无需 AI 平台或 API 密钥。Python 脚本不负责从原始材料提取事实，也不自行生成英文文案。

### 下载与环境

- [Python 官方下载](https://www.python.org/downloads/)：使用当前受支持的 Python 3。脚本结构兼容 Python 3.9+，不需要 pip 包。
- [macOS：MacTeX](https://tug.org/mactex/)
- [Windows：MiKTeX](https://miktex.org/download)
- [Linux：TeX Live](https://tug.org/texlive/)

**Python 生成 LaTeX；生成 PDF 还需要 LaTeX 编译器。** 编译器需要位于 PATH；默认依次尝试 tectonic、xelatex、lualatex、pdflatex。Tectonic 或未安装的宏包可能需要联网下载。

在仓库根目录运行：

```bash
# 仅生成可编辑 LaTeX
python3 scripts/generate_resume.py examples/01-research-ai.json -o generated/resume.tex

# 同时生成 PDF
python3 scripts/generate_resume.py examples/01-research-ai.json -o generated/resume.tex --pdf
```

Windows 可用 `py -3` 替代 `python3`。没有编译器时去掉 `--pdf`。默认模板用于英文；非拉丁字符需要相应字体配置。

### 使用自己的资料

1. 将一个示例 JSON 复制到个人工作目录。
2. 替换为本人真实资料，删除不适用的条目。
3. 将 `profile` 设为 `research` 或 `professional`。
4. 人工解决缺失或不明确的事实，再生成并查看最终 PDF。

字段说明见 [JSON contract](references/schema.md)。原始百分制均分填入 `score`，正式 GPA 填入 `gpa`，不能自行换算。请将真实申请材料保存在仓库之外。

## 验证与兼容性

```bash
python3 -m unittest discover -s tests
```

已在 macOS 使用 XeLaTeX 生成四套两页 PDF 并进行视觉检查；单元测试和解压到不同目录后的运行检查通过。Windows/Linux、其他编译器及其他 AI 平台未完成本地实测。仓库提供可在不同系统运行的本地测试；测试不能代替 PDF 排版或事实核验。

本仓库的脚本不调用外部 AI API，也不上传简历。使用 AI Skill 时，数据处理取决于你选择的 AI 平台和账号配置。

## 项目结构

```text
SKILL.md                     AI 工作流与人工核验规则
agents/openai.yaml           Skill 展示和自动调用配置
scripts/generate_resume.py   JSON → LaTeX/PDF
assets/templates/            制式模板
examples/                    四套虚构案例及使用指南
docs/images/                 README 成果预览
references/schema.md         字段说明
tests/                       针对性测试
```

## 贡献与许可

欢迎提交输入处理、错误提示、可移植性和文档改进。排版与内容规则属于项目的制式规范，修改前请在 Issue 中说明需求；真实个人资料不得提交到示例或测试。

项目采用 [Apache License 2.0](LICENSE)，允许按照许可证条款使用、修改和分发。
