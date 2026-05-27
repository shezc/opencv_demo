# 明日学习内容

## Day 1：跑通项目并理解 OpenCV 入门流程

### 学习目标

继续用 1 小时跑通 OpenCV 入门脚本，确认本地环境可以读取图片、转换灰度图并保存输出。因为 `learning/progress.md` 尚未明确记录 Day 1 已完成，明日仍继续 Day 1，并在练习结束后补全学习记录。

### 时间安排

- 10 分钟：阅读 `README.md` 的环境准备、运行方式和学习顺序。
- 20 分钟：阅读 `src/common.py` 和 `src/01_read_show_save.py`，理解图片路径、示例图生成、灰度转换和保存输出。
- 20 分钟：运行第 1 个脚本，观察 `output/` 目录生成的 `01_original.jpg` 和 `01_gray.jpg`。
- 10 分钟：记录运行结果、遇到的问题、今天最重要的概念和是否完成 Day 1。

### 需要阅读的文件

- `README.md`：项目用途、环境准备、运行方式和学习顺序。
- `learning/ai_vision_30_day_plan.md`：Day 1 在 30 天计划中的位置。
- `src/common.py`：默认图片路径、输出目录、示例图生成、读取图片和保存图片。
- `src/01_read_show_save.py`：读取图片、查看尺寸、灰度转换、保存输出和窗口显示。

### 需要运行的 PowerShell 命令

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/01_read_show_save.py
```

如果 PowerShell 阻止激活虚拟环境，先在当前终端临时放开执行策略：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 动手练习

1. 运行脚本并确认生成 `output/01_original.jpg` 和 `output/01_gray.jpg`。
2. 把自己的图片放到 `assets/sample.jpg` 后再次运行，比较输出差异。
3. 暂时注释掉 `cv2.imshow()` 相关代码，只保留保存文件，观察脚本是否仍能完成输出。
4. 修改 `create_demo_image()` 中一个图形的颜色、坐标或大小，删除或移走 `assets/sample.jpg` 后运行，观察自动生成的练习图变化。

### 观察重点

- 终端是否打印 `Loaded image`，还是提示找不到图片并使用自动生成的 demo image。
- `image.shape` 对应的高度、宽度、通道数分别是多少。
- `output/01_original.jpg` 与 `output/01_gray.jpg` 的视觉差异。
- 注释掉 `cv2.imshow()` 后，脚本是否仍然能正常保存输出文件。
- 更换 `assets/sample.jpg` 后，输出尺寸和图像内容是否随输入图片变化。

### 复盘问题

- OpenCV 读入的图片为什么是一个三维数组？
- `width`、`height`、`channels` 分别来自 `image.shape` 的哪一部分？
- 灰度图和原图相比，输出文件在视觉上有什么变化？
- `cv2.imread()` 读取失败时，`load_image_or_demo()` 如何保证脚本还能继续运行？
- 本地运行时如果 `cv2.imshow()` 窗口没有正常显示，可以怎样先验证保存流程？
