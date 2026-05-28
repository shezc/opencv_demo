# 明日学习内容

## Day 2：学习图像矩阵、宽高通道、`cv2.imread`、`cv2.imwrite`、灰度图

### 学习目标

用 1 小时理解 OpenCV 图片在 Python 中就是 NumPy 数组，掌握 `height`、`width`、`channels` 的来源，复习 `cv2.imread()`、`cv2.imwrite()` 和灰度图保存流程，并开始观察 BGR/RGB、通道拆分和像素区域修改。

### 时间安排

- 10 分钟：复盘 Day 1 输出的 `output/01_original.jpg` 和 `output/01_gray.jpg`，确认原图尺寸、通道数和灰度图变化。
- 15 分钟：阅读 `src/01_read_show_save.py`，重点理解 `image.shape`、`cv2.cvtColor()`、`save_image()`。
- 20 分钟：阅读并运行 `src/02_pixels_and_channels.py`，观察 BGR 通道拆分、RGB 转换和局部像素修改。
- 10 分钟：修改一个局部区域或输出文件名，再运行一次并比较输出。
- 5 分钟：把运行结果、观察结论和疑问补充到 `learning/progress.md`。

### 需要阅读的文件

- `README.md`：复习运行方式、输出目录和建议练习方法。
- `src/common.py`：理解 `load_image_or_demo()`、`save_image()` 如何连接输入和输出。
- `src/01_read_show_save.py`：复习图片读取、尺寸打印、灰度转换和保存。
- `src/02_pixels_and_channels.py`：重点学习 BGR 通道、像素值、通道拆分合并和局部区域修改。

### 需要运行的 PowerShell 命令

```powershell
.\.venv\Scripts\Activate.ps1
python src/01_read_show_save.py
python src/02_pixels_and_channels.py
```

如果 PowerShell 阻止激活虚拟环境，先运行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 动手练习

1. 运行 `src/02_pixels_and_channels.py`，确认生成 `output/02_only_blue.jpg`、`output/02_only_green.jpg`、`output/02_only_red.jpg`、`output/02_marked_region.jpg`、`output/02_rgb_converted.jpg`。
2. 打印并记录 `image[0, 0].tolist()` 的结果，说明它为什么是 BGR 顺序。
3. 修改 `marked[y1:y2, x1:x2] = (0, 0, 255)` 中的颜色值，例如改为 `(255, 0, 0)` 或 `(0, 255, 0)`，观察标记区域颜色变化。
4. 修改局部区域范围，例如把 `h // 4, h // 2` 改成 `h // 3, h * 2 // 3`，观察标记区域大小和位置变化。
5. 如果使用自己的 `assets/sample.jpg`，再次运行并比较不同输入图片上的通道输出差异。

### 观察重点

- `image.shape` 的顺序是否始终是 `(height, width, channels)`。
- `cv2.split(image)` 得到的 `blue`、`green`、`red` 是否都是二维数组。
- 只保留单个通道时，输出图片为什么仍然可以保存为三通道彩色图。
- OpenCV 的 BGR 顺序和常见 RGB 顺序有什么区别。
- 局部区域赋值 `marked[y1:y2, x1:x2] = (...)` 如何改变矩形区域内的像素。

### 复盘问题

- `image.shape` 返回的三个值分别代表什么？为什么打印宽高时常写成 `width x height`？
- OpenCV 为什么说彩色图是 BGR，而不是 RGB？
- `cv2.split(image)` 和 `cv2.merge([...])` 分别解决什么问题？
- `np.zeros_like(blue)` 在生成单通道可视化图时起什么作用？
- 直接修改 `marked[y1:y2, x1:x2]` 会影响原始 `image` 吗？为什么代码里先用了 `image.copy()`？
