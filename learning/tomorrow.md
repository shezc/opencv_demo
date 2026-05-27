# 明日学习内容

## Day 1：跑通项目并理解 OpenCV 入门流程

### 学习目标

用 1 小时在本地 PowerShell 跑通第一个 OpenCV 脚本，理解项目如何读取 `assets/sample.jpg`、在缺少图片时生成 demo 图、查看图像宽高通道、转换灰度图并保存到 `output/`。学习结束后，把完成状态、运行命令、输出文件和关键概念补充到 `learning/progress.md`。

### 时间安排

- 10 分钟：阅读 `README.md`，确认环境准备、运行方式和 Day 1 在学习顺序中的位置。
- 15 分钟：阅读 `src/common.py`，理解路径定位、`assets/sample.jpg`、demo 图生成和 `output/` 保存逻辑。
- 15 分钟：阅读 `src/01_read_show_save.py`，理解 `image.shape`、`cv2.cvtColor()`、`cv2.imwrite()` 和 GUI 显示相关代码。
- 15 分钟：运行脚本，观察终端输出和 `output/01_original.jpg`、`output/01_gray.jpg`。
- 5 分钟：更新 `learning/progress.md`，记录是否完成、运行过的命令、输出文件、最重要概念和遇到的问题。

### 需要阅读的文件

- `README.md`：环境准备、运行方式、学习顺序和建议练习方法。
- `learning/progress.md`：补充 Day 1 的完成状态和学习记录。
- `src/common.py`：`load_image_or_demo()`、`create_demo_image()`、`save_image()`。
- `src/01_read_show_save.py`：读取图片、打印尺寸、灰度转换、保存输出和窗口预览。
- `assets/README.md`：理解为什么建议放置 `assets/sample.jpg`。

### 需要运行的 PowerShell 命令

如果还没有创建虚拟环境，先运行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

如果 PowerShell 阻止激活虚拟环境，先运行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

运行 Day 1 脚本：

```powershell
.\.venv\Scripts\Activate.ps1
python src/01_read_show_save.py
```

如果 `cv2.imshow()` 窗口打开，点击图片窗口并按任意键关闭。若在无图形界面的环境中运行，可以临时注释 `cv2.imshow()`、`cv2.waitKey()` 和 `cv2.destroyAllWindows()` 三行，只验证保存文件。

### 动手练习

1. 运行脚本并确认生成 `output/01_original.jpg` 和 `output/01_gray.jpg`。
2. 对比原图与灰度图：观察颜色信息消失后，亮度和边缘是否仍然明显。
3. 把自己的图片放到 `assets/sample.jpg` 后再次运行，比较终端输出的尺寸和生成结果。
4. 临时注释 GUI 预览代码，只保留保存逻辑，验证脚本是否仍能生成输出文件。
5. 可选：临时改名 `assets/sample.jpg`，观察 `src/common.py` 是否会生成 demo 图。

### 观察重点

- `image.shape` 的顺序是 `(height, width, channels)`，不是 `(width, height, channels)`。
- OpenCV 默认颜色顺序是 BGR；后续学习 RGB/HSV 时要特别注意通道顺序。
- 灰度图通常是二维数组，保存后视觉上只剩黑白/灰阶亮度。
- `cv2.imwrite()` 不需要窗口环境，`cv2.imshow()` 和 `cv2.waitKey()` 需要本地图形界面。
- 如果没有 `assets/sample.jpg`，项目仍能通过 demo 图跑通流程。

### 复盘问题

- OpenCV 读入的彩色图片为什么是一个三维数组？
- `width`、`height`、`channels` 分别来自 `image.shape` 的哪一部分？
- `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` 做了什么？
- `cv2.imwrite()` 和 `cv2.imshow()` 的作用有什么区别？
- 如果 `assets/sample.jpg` 不存在，项目为什么仍然可以运行？
