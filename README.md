# OpenCV Python Learning

这个仓库用于从 0 开始学习 OpenCV。当前路线先使用 Python 和 `opencv-python` 快速入门，重点理解图像处理的基本概念和常用 API。

## 环境准备

在 Windows PowerShell 中运行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

如果 PowerShell 不允许激活虚拟环境，可以临时运行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 运行方式

脚本默认读取 `assets/sample.jpg`。如果这个文件不存在，脚本会自动生成一张简单的练习图，方便你先跑通 OpenCV 流程。

```powershell
python src/01_read_show_save.py
python src/02_pixels_and_channels.py
python src/03_blur_edges.py
python src/04_contours.py
```

生成的结果会保存到 `output/` 目录。

## 学习顺序

1. `src/01_read_show_save.py`：读取图片、查看尺寸、灰度转换、保存结果。
2. `src/02_pixels_and_channels.py`：理解 OpenCV 的 BGR 通道、RGB 转换、拆分通道和局部像素修改。
3. `src/03_blur_edges.py`：学习高斯模糊和 Canny 边缘检测。
4. `src/04_contours.py`：学习阈值、查找轮廓和绘制轮廓。

## 建议练习方法

- 每次只改一个参数，例如模糊核大小、Canny 阈值或阈值分割的临界值。
- 每次运行后观察 `output/` 中生成的图片变化。
- 把自己的图片放到 `assets/sample.jpg`，再重复运行脚本。
- 如果遇到图片读不到，优先检查路径、文件名和扩展名。

## 下一阶段

完成静态图片基础后，可以继续添加：

- 摄像头实时读取。
- 视频文件逐帧处理。
- 人脸、二维码或特征点检测。
- 一个小项目，例如文档扫描、车道线检测或颜色追踪。
