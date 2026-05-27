# 明日学习内容

## Day 1：搭建环境，运行现有脚本，理解项目目录

### 学习目标

用 1 小时跑通当前 OpenCV 项目，理解 `assets/sample.jpg`、`output/`、`src/common.py` 和第一个脚本之间的关系，确认图片读取、灰度转换和结果保存的完整流程。

### 10/20/20/10 分钟时间安排

- 10 分钟：阅读 `README.md` 的环境准备、运行方式和学习顺序，确认虚拟环境、依赖安装和脚本入口。
- 20 分钟：阅读 `assets/README.md`、`src/common.py` 和 `src/01_read_show_save.py`，画出“输入图片 -> 读取/生成演示图 -> 灰度转换 -> 保存到 output”的流程。
- 20 分钟：在 PowerShell 中运行 Day 1 命令，观察终端输出和 `output/01_original.jpg`、`output/01_gray.jpg` 的变化。
- 10 分钟：把运行结果、输出文件、遇到的问题和 Day 2 想理解的“图像矩阵/宽高通道”记录到 `learning/progress.md`。

### 需要阅读的项目文件

- `README.md`：环境准备、运行方式、输出目录和建议练习方法。
- `assets/README.md`：为什么默认图片命名为 `assets/sample.jpg`，没有图片时会发生什么。
- `src/common.py`：`DEFAULT_IMAGE_PATH`、`OUTPUT_DIR`、`load_image_or_demo()`、`create_demo_image()` 和 `save_image()`。
- `src/01_read_show_save.py`：`image.shape`、`cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`、`cv2.imshow()`、`cv2.waitKey()` 和两个输出文件名。

### 要运行的 PowerShell 命令

第一次运行或环境不存在时：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/01_read_show_save.py
```

如果 PowerShell 阻止激活虚拟环境，先运行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

以后环境已准备好时：

```powershell
.\.venv\Scripts\Activate.ps1
python src/01_read_show_save.py
```

### 动手练习

1. 先不放自己的图片，直接运行脚本，确认程序会生成演示图并保存 `output/01_original.jpg` 和 `output/01_gray.jpg`。
2. 把一张自己的图片复制为 `assets/sample.jpg`，再次运行脚本，比较新的原图输出和灰度输出。
3. 观察终端打印的 `Image size` 和 `Channels`，在 `learning/progress.md` 里记录宽、高、通道数。
4. 如果本机没有图形界面或 `cv2.imshow()` 窗口无法正常显示，临时注释 `cv2.imshow()`、`cv2.waitKey()`、`cv2.destroyAllWindows()` 三段代码，再确认保存文件是否仍然成功。

### 复盘问题

- `assets/sample.jpg` 存在和不存在时，`load_image_or_demo()` 的行为有什么不同？
- `output/` 目录中的 `01_original.jpg` 和 `01_gray.jpg` 分别来自哪一行代码？
- `image.shape` 打印出的高、宽、通道数分别表示什么？
- 为什么 Day 2 要继续学习“图像矩阵、宽高通道和灰度图”？
