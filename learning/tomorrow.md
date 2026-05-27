# 明日学习内容

## Day 1：跑通项目并理解 OpenCV 入门流程

### 学习目标

用 1 小时确认 OpenCV 环境可运行，理解当前项目如何读取输入图片、在没有输入图片时生成演示图、查看图像尺寸、转换灰度图并保存输出结果。

### 10/20/20/10 分钟时间安排

- 10 分钟：阅读 `README.md` 的环境准备、运行方式和学习顺序。
- 20 分钟：阅读 `src/common.py` 和 `src/01_read_show_save.py`，理解图片路径、示例图生成、灰度转换和保存输出。
- 20 分钟：运行第 1 个脚本，观察 `output/` 目录生成的图片。
- 10 分钟：记录运行结果、遇到的问题和明天想重点理解的概念。

### 需要阅读的项目文件

- `README.md`：项目目标、环境准备、运行方式和学习顺序。
- `src/common.py`：项目根目录定位、默认图片路径、输出目录创建、演示图生成、图片保存。
- `src/01_read_show_save.py`：读取图片、读取 `image.shape`、BGR 转灰度、保存结果、显示窗口。

### 要运行的 PowerShell 命令

```powershell
.\.venv\Scripts\Activate.ps1
python src/01_read_show_save.py
```

如果 PowerShell 阻止激活虚拟环境，先运行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 动手练习

1. 运行脚本并确认生成 `output/01_original.jpg` 和 `output/01_gray.jpg`。
2. 把自己的图片放到 `assets/sample.jpg` 后再次运行，比较输出差异。
3. 暂时注释掉 `cv2.imshow()` 相关代码，只保留保存文件，观察脚本是否仍能完成输出。

### 输出文件或观察重点

- `output/01_original.jpg`：原始 BGR 图片保存结果。
- `output/01_gray.jpg`：灰度转换后的单通道图片保存结果。
- 终端输出中的 `Image size: 宽x高` 和 `Channels: 3`。
- `image.shape` 的顺序是 `(height, width, channels)`，打印尺寸时通常显示为 `width x height`。
- 如果没有 `assets/sample.jpg`，程序会自动生成一张包含矩形、圆形、线条和文字的演示图。
- `cv2.imshow()` 需要桌面 GUI 窗口；如果只想保存文件，可以临时注释显示窗口相关代码。

### 复盘问题

- OpenCV 读入的图片为什么是一个三维数组？
- `width`、`height`、`channels` 分别来自 `image.shape` 的哪一部分？
- 灰度图和原图相比，输出文件在视觉上有什么变化？
- `cv2.imread()` 读不到图片时，当前项目为什么仍然可以继续运行？
