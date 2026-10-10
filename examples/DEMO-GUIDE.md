# 四套 DEMO 使用指南

所有人物、学校、导师、公司、奖项、研究和数字均为教学虚构。PDF 中机构标注 Fictional，JSON 与本说明一起分发。example.com 项目地址只演示可点击链接，不指向真实项目。

四套均使用现有制式模板，未改变字体、颜色、页边距、章节样式或生成脚本。研究型优先研究经历；就业型优先工作经历。

| 示例 | 人物背景与申请方向 | 学习重点 |
|---|---|---|
| 01-research-ai | Maya Chen，2026 年计算机本科毕业，成绩优秀；先参与数据质量研究，再开展可靠机器学习实验，并有机器学习实习。拟申请研究型 CS 硕士，关注模型鲁棒性与校准。 | 两段研究、对照实验、随机种子、指标与评估条件；无论文则不设论文栏目。 |
| 02-research-scientific-computing | Owen Patel，应用数学本科、计算机辅修；毕业后继续做科学计算研究，有本科论文和数值方法助教经历。拟转向 CS 科学计算与优化方向。 | 通过课程、算法实现、收敛验证、求解器比较和可复现基准展示跨专业准备。部门毕业论文不冒称发表论文。 |
| 03-professional-backend | Daniel Rivera，软件工程本科，四年电商后端工作，参与订单服务、数据库性能优化与迁移，早期有实习。拟申请职业导向 CS 硕士，提升分布式系统能力。 | 工作职责与贡献、性能指标的测试环境、可靠性处理、协作和运维；项目名称可点击。 |
| 04-professional-mobile | Sofia Kim，计算机本科，三年移动端开发，兼有前端实习；关注离线体验、性能与无障碍，参与用户测试。拟申请职业导向 CS/HCI 硕士。 | 展示不同于后端的技术栈、设备基准、用户体验实验、可访问性和移动端项目链接。 |

## 照着使用

1. 选择接近自己目标的 JSON，复制到技能包以外的个人工作目录。
2. 替换 personal_info、education 和各段经历。姓名、邮箱、GPA、日期、导师、贡献、指标、论文状态必须来自自己的真实材料。删除不适用的条目；不能复制 DEMO 数字或经历。
3. profile 为 research 或 professional。字段含义见 ../references/schema.md。
4. 若使用 AI，可输入：`$english-resume-skill-agent 请参考这份 DEMO 的字段结构，依据我的材料生成简历。保留制式排版，不要使用 DEMO 的个人事实；不确定内容单独列出。`
5. 在技能根目录执行以下命令。macOS/Linux 使用 python3；Windows 可改为 py -3。

```bash
python3 scripts/generate_resume.py examples/01-research-ai.json -o generated/01-research-ai.tex --pdf
python3 scripts/generate_resume.py examples/02-research-scientific-computing.json -o generated/02-research-scientific-computing.tex --pdf
python3 scripts/generate_resume.py examples/03-professional-backend.json -o generated/03-professional-backend.tex --pdf
python3 scripts/generate_resume.py examples/04-professional-mobile.json -o generated/04-professional-mobile.tex --pdf
```

只需 LaTeX 或未安装编译器时，去掉 --pdf。Python 与编译器官方下载安装入口见 ../SKILL.md 的“用户环境与下载”。

JSON 是完整的虚构输入，TEX 是可编辑生成结果，PDF 是排版成品。四套案例已在 macOS + XeLaTeX 下生成并逐页检查。正式简历仍需核对事实、链接与最终排版。

## 充实版说明

本次四套均扩展为两页完整案例，涵盖研究/工作经历、多个技术项目、方法与测试条件、量化结果、合作和局限。长版用于学习字段和表达，不要求真实申请人必须填满两页。项目链接均为演示地址。
