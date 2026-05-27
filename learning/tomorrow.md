# Day 1：搭建环境，运行现有脚本，理解项目目录、`assets/sample.jpg`、`output/` 和 `src/common.py`

### 学习目标

用 1 小时跑通当前 OpenCV 项目，知道代码从哪里读取图片、在没有示例图片时如何生成练习图、结果保存到哪里，并能说清楚 `src/01_read_show_save.py` 中“读取图片 -> 查看尺寸 -> 转灰度 -> 保存输出”的基本流程。

### 10/20/20/10 分钟时间安排

- 10 分钟：阅读 `README.md`，重点看“环境准备”“运行方式”和“学习顺序”，确认这个仓库的脚本入口和输出目录。
- 20 分钟：阅读 `src/common.py` 和 `src/01_read_show_save.py`，先理解函数职责，再把主流程按顺序写成 4 个短句。
- 20 分钟：在 PowerShell 中创建或激活虚拟环境，运行 Day 1 脚本，观察终端输出和 `output/` 中生成的图片。
- 10 分钟：在 `learning/progress.md` 的 Day 1 记录中补充运行命令、输出文件、最重要概念和遇到的问题。

### 需要阅读的项目文件

- `README.md`：了解如何安装依赖、运行脚本，以及本仓库建议的学习顺序。
- `src/common.py`：关注 `DEFAULT_IMAGE_PATH`、`load_image_or_demo()`、`create_demo_image()` 和 `save_image()`。
- `src/01_read_show_save.py`：关注 `image.shape`、`cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`、`save_image()`、`cv2.imshow()` 和 `cv2.waitKey(0)`。
- `learning/progress.md`：学习结束后用它记录今天是否完成、跑过哪些命令、生成了哪些文件。

### 要运行的 PowerShell 命令

如果还没有虚拟环境，先执行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

如果 PowerShell 阻止激活虚拟环境，先临时放开当前窗口的执行策略：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

运行 Day 1 脚本：

```powershell
python src/01_read_show_save.py
```

如果弹出的图片窗口挡住流程，在窗口中按任意键关闭；如果当前环境不能打开 GUI 窗口，先记录报错，重点确认终端是否已经打印图片尺寸和保存路径。

### 动手练习

1. 先不放自己的图片，直接运行 `python src/01_read_show_save.py`，观察 `src/common.py` 是否提示使用自动生成的 demo image。
2. 打开 `output/01_original.jpg` 和 `output/01_gray.jpg`，比较彩色图和灰度图的区别。
3. 把一张自己的 JPG 图片放到 `assets/sample.jpg`，再次运行同一个脚本，确认终端从 `Loaded image:` 开始提示，并比较新的输出图片。
4. 用自己的话写下主流程：`load_image_or_demo()` 得到图片，`image.shape` 读尺寸，`cv2.cvtColor()` 转灰度，`save_image()` 保存结果。

### 输出文件或观察重点

- `output/01_original.jpg`：原图或自动生成的彩色练习图。
- `output/01_gray.jpg`：由 `cv2.COLOR_BGR2GRAY` 转换得到的灰度图。
- 终端输出中的 `Image size: 宽x高` 和 `Channels: 3`。
- 当 `assets/sample.jpg` 不存在时，代码会生成一张包含矩形、圆形、线条和文字的练习图；当它存在时，代码会优先读取这张图片。

### 复盘问题

- 今天你运行脚本时，读取的是自己的 `assets/sample.jpg`，还是自动生成的 demo image？你从哪一行终端输出判断出来的？
- `image.shape` 返回的高度、宽度、通道数分别对应代码中的哪个变量？
- 为什么 `output/01_gray.jpg` 看起来只有明暗变化，没有彩色信息？
- `src/common.py` 把“读取图片”和“保存图片”封装成函数，对后面每天继续学习有什么好处？
