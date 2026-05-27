# Cursor 学习自动化

这个自动化使用 Cursor 原生 Automations / Cloud Agent。Agent 作为 AI 视觉学习助教，每天 21:00（GMT+8）运行。

请在当前 GitHub 仓库 `opencv_demo` 的 `master` 分支中工作。

触发后，Cursor 会根据学习记录、计划和源码总结当天学习内容，同步到 Notion，并生成明日学习计划。

## Notion 目标页面

```text
https://www.notion.so/36d480da35fe80a2b3b0effc5189def1
```

Notion 子页面标题格式：

```text
AI 视觉学习 Day N：当天主题
```

如果同标题页面已存在，则更新；否则新建。

## 任务一：读取学习上下文

读取以下文件，判断今天对应的 Day N 和学习主题：

- `learning/progress.md`
- `learning/tomorrow.md`
- `learning/ai_vision_30_day_plan.md`
- 与当天主题相关的源码文件，例如 `README.md`、`src/*.py`

## 任务二：生成今日学习总结

根据学习记录、计划和源码，总结今天应掌握的内容，并同步到 Notion。

Notion 页面内容只保留以下部分：

- 今日学习主题
- 核心知识点总结
- 核心代码摘录与解释
- 运行命令与输出观察
- 复盘问题与参考答案
- 明日学习计划摘要

要求：

- 核心代码必须摘录具体代码，使用 Markdown 代码块，例如 ` ```python `。
- 每段代码后用中文简要说明：作用、关键 API、重要参数、可尝试修改的参数。
- 如果 `progress.md` 记录不完整，可根据计划和源码生成“应掌握内容总结”，并注明来源于计划推断。

## 任务三：生成明日学习计划

根据 `progress.md` 判断下一天学习内容：

- 如果当天已完成，生成 Day N+1。
- 如果当天未明确完成，继续生成 Day N。

从 `learning/ai_vision_30_day_plan.md` 中找到对应主题，并更新 `learning/tomorrow.md`。

`tomorrow.md` 内容包括：

- Day N：主题
- 学习目标
- 时间安排
- 需要阅读的文件
- 需要运行的 PowerShell 命令
- 动手练习
- 观察重点
- 复盘问题

## 任务四：提交变更

只提交 `learning/tomorrow.md` 和必要的学习记录文件，不修改无关文件。

commit/PR 标题建议：

```text
Summarize AI vision Day N and generate next plan
```

最终用中文简要回复：

- 已总结的 Day N 和主题
- Notion 页面链接
- 下一天学习计划主题
- commit 或 PR 链接
- 如果 Notion 同步或提交失败，说明原因和下一步建议

## 注意

Cursor 原生 Automations 在云端运行，需要仓库文件已提交并推送到 GitHub。Notion 同步需要在 Automation 的 Tools 中启用 Notion MCP。
