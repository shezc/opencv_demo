# 明日学习内容

## Day 1：跑通项目并理解 OpenCV 入门流程

### 学习目标

根据 `learning/progress.md`，Day 1 尚未明确记录已完成，因此明日继续 Day 1，不跳到 Day 2。

用 1 小时确认环境可运行，理解当前项目如何读取图片、在缺少 `assets/sample.jpg` 时生成示例图、保存输出，并建立后续每天记录学习结果的习惯。

### 10/20/20/10 分钟时间安排

- 10 分钟：阅读 `README.md` 的环境准备、运行方式和学习顺序。
- 20 分钟：阅读 `src/common.py` 和 `src/01_read_show_save.py`，理解图片路径、示例图生成、灰度转换和保存输出。
- 20 分钟：运行第 1 个脚本，观察 `output/` 目录生成的图片；如果有自己的图片，可以放到 `assets/sample.jpg` 后再次运行。
- 10 分钟：记录运行结果、遇到的问题和明天想重点理解的概念。

### 需要阅读的项目文件

- `README.md`：环境准备、运行方式、学习顺序和建议练习方法。
- `src/common.py`：项目路径、默认输入图片、自动生成 demo 图、保存输出图片。
- `src/01_read_show_save.py`：读取图片、查看尺寸、灰度转换、保存和显示。

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

- `output/01_original.jpg`：应保存原图；如果没有 `assets/sample.jpg`，则保存自动生成的 demo 图。
- `output/01_gray.jpg`：应保存灰度图。
- 控制台输出：
  - 是否提示 `Loaded image` 或 `Image not found`。
  - `Image size` 中宽高的显示顺序。
  - `Channels` 是否为 3。
- 重点观察：
  - `image.shape` 返回顺序是 `(height, width, channels)`。
  - `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` 会把三通道 BGR 图转换成单通道灰度图。
  - `cv2.imshow()` 需要 GUI 环境；如果窗口无法显示，先确认输出文件是否已经生成。

### 复盘问题

- OpenCV 读入的图片为什么是一个三维数组？
- `width`、`height`、`channels` 分别来自 `image.shape` 的哪一部分？
- 灰度图和原图相比，输出文件在视觉上有什么变化？
- `assets/sample.jpg` 不存在时，脚本为什么仍然能保存输出图片？
- 为什么 `cv2.imshow()` 在没有图形界面的环境中可能无法使用？
