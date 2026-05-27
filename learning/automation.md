# Cursor 学习自动化

这个自动化已在本地 Cursor 终端中启动。它会每天晚上 21:00 输出唤醒信号：

```text
AGENT_LOOP_TICK_AI_VISION_LEARNING
```

触发后，Cursor 会根据以下文件生成第二天 1 小时学习内容：

- `learning/ai_vision_30_day_plan.md`
- `learning/progress.md`
- `learning/tomorrow.md`

## 触发后要做的事

1. 读取 `learning/progress.md` 的当前进度。
2. 从 `learning/ai_vision_30_day_plan.md` 找到下一天主题。
3. 更新 `learning/tomorrow.md`，包含学习目标、时间安排、运行命令、动手练习和复盘问题。
4. 在 Cursor 聊天中提醒第二天学习内容。

## 注意

本自动化依赖当前电脑、Cursor 和后台终端保持运行。如果电脑关机、Cursor 关闭或终端进程结束，需要重新启动自动化。
