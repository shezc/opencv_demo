# 明日学习内容

## Day 1：跑通项目并理解 OpenCV 入门流程

### 学习目标

用 1 小时确认本地环境可运行，理解当前项目如何读取图片、在缺少输入图时生成示例图、查看图片尺寸、转换灰度图并保存输出；同时把当天运行结果补充到 `learning/progress.md`。

### 10/20/20/10 分钟时间安排

- 10 分钟：阅读 `README.md`，确认环境准备、运行方式、输出目录和学习顺序。
- 20 分钟：阅读 `src/common.py` 和 `src/01_read_show_save.py`，理解图片路径、示例图生成、`image.shape`、灰度转换和保存输出。
- 20 分钟：运行 Day 1 脚本，观察 `output/01_original.jpg` 与 `output/01_gray.jpg` 的差异；如果 `cv2.imshow()` 弹窗，按任意键关闭。
- 10 分钟：在 `learning/progress.md` 记录运行命令、输出文件、最重要概念、遇到的问题和明天想继续理解的点。

### 需要阅读的项目文件

- `README.md`：了解项目用途、虚拟环境准备、脚本运行方式和输出目录。
- `src/common.py`：理解 `PROJECT_ROOT`、`DEFAULT_IMAGE_PATH`、`load_image_or_demo()`、`create_demo_image()` 和 `save_image()`。
- `src/01_read_show_save.py`：理解 `image.shape`、`cv2.cvtColor()`、`cv2.imshow()`、`cv2.waitKey()` 和 `cv2.destroyAllWindows()`。
- `learning/progress.md`：完成学习后补充 Day 1 记录。

### 要运行的 PowerShell 命令

```powershell
.\.venv\Scripts\Activate.ps1
python src/01_read_show_save.py
```

如果 PowerShell 阻止激活虚拟环境，先运行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python src/01_read_show_save.py
```

如果还没有创建虚拟环境，先运行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/01_read_show_save.py
```

### 动手练习

1. 运行脚本并确认生成 `output/01_original.jpg` 和 `output/01_gray.jpg`。
2. 对比原图和灰度图：观察彩色信息消失后，亮暗关系是否仍然保留。
3. 把自己的图片放到 `assets/sample.jpg` 后再次运行，比较尺寸打印结果和输出图片变化。
4. 暂时注释掉 `cv2.imshow()`、`cv2.waitKey()` 和 `cv2.destroyAllWindows()`，只保留保存文件，观察脚本是否仍能完成输出。
5. 临时改名或移走 `assets/sample.jpg`，再次运行，观察 `load_image_or_demo()` 是否会生成 demo 图。

### 输出文件或观察重点

- `output/01_original.jpg`：原始输入图或自动生成的 demo 图。
- `output/01_gray.jpg`：由 `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` 生成的灰度图。
- 控制台输出中的 `Image size: 宽x高` 和 `Channels: 3`。
- 如果本地出现 OpenCV 窗口，确认 `Original` 与 `Gray` 两个窗口能通过按键关闭。
- 如果图片路径错误，观察是否打印 `Image not found` 并回退到生成 demo 图。

### 复盘问题

- OpenCV 读入的彩色图片为什么是一个三维数组？
- `height, width, channels = image.shape` 中，高和宽的顺序为什么容易写反？
- `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` 做了什么？
- 灰度图和原图相比，输出文件在视觉上有什么变化？
- `cv2.imshow()` 和 `cv2.imwrite()` 分别适合解决什么问题？为什么无 GUI 环境下更依赖保存文件观察结果？
