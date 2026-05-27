# AI 视觉学习 Day 1：跑通项目并理解 OpenCV 入门流程

> 说明：`learning/progress.md` 中 Day 1 尚未明确记录“已完成”、运行命令或输出文件。因此本总结是基于 `learning/tomorrow.md` 的当天原计划、`learning/ai_vision_30_day_plan.md` 的 Day 1 主题，以及相关源码生成的“应掌握内容总结”。

## 今日学习主题

- Day 1：跑通项目并理解 OpenCV 入门流程。
- 对应 30 天计划：搭建环境，运行现有脚本，理解项目目录、`assets/sample.jpg`、`output/` 和 `src/common.py`。
- 今日原计划：阅读 `README.md`、`src/common.py`、`src/01_read_show_save.py`，运行第一个脚本并观察 `output/` 中生成的图片。

## 今日知识总结

1. **项目目录与运行入口**
   - `README.md` 说明了环境准备、脚本运行顺序和输出目录。
   - 默认输入图片是 `assets/sample.jpg`。
   - 处理结果统一保存到 `output/`。
   - Day 1 重点脚本是 `src/01_read_show_save.py`。

2. **图片读取与兜底示例图**
   - `src/common.py` 中的 `load_image_or_demo()` 会先用 `cv2.imread()` 读取默认图片。
   - 如果 `assets/sample.jpg` 不存在或读取失败，就调用 `create_demo_image()` 生成一张练习图，保证初学时仍可跑通流程。

3. **图像数组的形状**
   - 彩色图像在 OpenCV 中通常是三维数组：`height, width, channels = image.shape`。
   - `height` 表示行数，也就是图片高度。
   - `width` 表示列数，也就是图片宽度。
   - `channels` 表示颜色通道数，彩色 BGR 图通常是 3。

4. **灰度转换**
   - `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` 把 BGR 彩色图转换成单通道灰度图。
   - 灰度图不再保存蓝、绿、红三个通道，而是用一个亮度值表达每个像素。

5. **保存与显示**
   - `save_image()` 内部调用 `cv2.imwrite()` 保存图片。
   - `cv2.imshow()` 会打开 GUI 窗口显示图片。
   - `cv2.waitKey(0)` 会一直等待键盘输入，按任意键后继续执行。
   - `cv2.destroyAllWindows()` 关闭 OpenCV 创建的显示窗口。

## 今日核心代码总结

### `README.md`

- **关键内容**：环境准备、运行命令、学习顺序、输出位置。
- **关键命令**：
  - `python -m venv .venv`
  - `.\.venv\Scripts\Activate.ps1`
  - `pip install -r requirements.txt`
  - `python src/01_read_show_save.py`
- **执行流程**：
  1. 创建并激活 Python 虚拟环境。
  2. 安装 `opencv-python`、`numpy`、`matplotlib`。
  3. 运行 Day 1 脚本。
  4. 到 `output/` 查看生成文件。
- **容易混淆的点**：
  - PowerShell 激活命令是 Windows 写法；在 Linux/macOS 中需要使用不同的激活脚本。
  - `assets/sample.jpg` 不存在时并不一定报错，因为项目会自动生成 demo 图。

### `src/common.py`

- **关键函数或 API**：
  - `Path(__file__).resolve().parents[1]`
  - `cv2.imread(str(path))`
  - `np.full((420, 640, 3), 245, dtype=np.uint8)`
  - `cv2.rectangle()`、`cv2.circle()`、`cv2.line()`、`cv2.putText()`
  - `cv2.imwrite(str(output_path), image)`
- **重要参数含义**：
  - `PROJECT_ROOT`：项目根目录。
  - `DEFAULT_IMAGE_PATH`：默认输入图片路径 `assets/sample.jpg`。
  - `np.full((420, 640, 3), 245, dtype=np.uint8)`：创建高度 420、宽度 640、3 通道、初始像素值为 245 的浅色背景图。
  - `thickness=-1`：绘制实心图形。
  - `cv2.LINE_AA`：使用抗锯齿线条，让文字或线条边缘更平滑。
- **代码执行流程**：
  1. `load_image_or_demo()` 尝试读取默认图片。
  2. 如果读取成功，返回真实图片。
  3. 如果读取失败，打印提示并调用 `create_demo_image()`。
  4. `create_demo_image()` 生成包含矩形、圆、线条和文字的练习图。
  5. `save_image()` 确保 `output/` 存在，再把图片写入磁盘。
- **初学者容易混淆的点**：
  - `cv2.imread()` 读取失败时返回 `None`，不是抛出异常。
  - OpenCV 颜色顺序是 BGR，不是常见的 RGB。
  - `Path` 对象传给 OpenCV 前通常要转成字符串：`str(path)`。

### `src/01_read_show_save.py`

- **关键函数或 API**：
  - `load_image_or_demo()`
  - `image.shape`
  - `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`
  - `save_image("01_original.jpg", image)`
  - `save_image("01_gray.jpg", gray)`
  - `cv2.imshow()`、`cv2.waitKey(0)`、`cv2.destroyAllWindows()`
- **重要参数含义**：
  - `cv2.COLOR_BGR2GRAY`：指定从 BGR 彩色图转换为灰度图。
  - `cv2.waitKey(0)`：等待任意按键，不设置超时。
  - `"01_original.jpg"`：保存原图输出文件名。
  - `"01_gray.jpg"`：保存灰度图输出文件名。
- **代码执行流程**：
  1. 调用 `load_image_or_demo()` 获取输入图。
  2. 从 `image.shape` 取出高度、宽度和通道数。
  3. 打印图片尺寸和通道数。
  4. 调用 `cv2.cvtColor()` 得到灰度图。
  5. 保存原图和灰度图到 `output/`。
  6. 用 OpenCV GUI 窗口显示原图和灰度图。
  7. 等待按键后关闭窗口。
- **初学者容易混淆的点**：
  - `image.shape` 的顺序是 `(height, width, channels)`，不是 `(width, height, channels)`。
  - 灰度图通常是二维数组，因此没有第三个颜色通道维度。
  - `cv2.imshow()` 需要桌面 GUI 环境；在无图形界面的服务器或云环境中可能无法正常显示窗口。

## 今日运行命令

`progress.md` 尚未记录实际运行命令。按照当天计划，应运行：

```powershell
.\.venv\Scripts\Activate.ps1
python src/01_read_show_save.py
```

如果 PowerShell 阻止激活虚拟环境，可先运行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python src/01_read_show_save.py
```

## 今日输出观察

`progress.md` 尚未记录实际输出文件。按照源码预期：

- 如果 `assets/sample.jpg` 存在：
  - `output/01_original.jpg` 应保存原始输入图片。
  - `output/01_gray.jpg` 应保存对应灰度图。
- 如果 `assets/sample.jpg` 不存在：
  - 控制台应提示图片未找到，并使用自动生成的 demo 图。
  - `output/01_original.jpg` 应是包含矩形、圆、线条和 “OpenCV” 文字的练习图。
  - `output/01_gray.jpg` 应是同一内容的灰度版本。
- 观察重点：
  - 原图和彩色通道有关，灰度图只保留亮度信息。
  - 控制台打印的 `Image size` 使用 `width x height` 展示，但代码中 `image.shape` 先返回 `height`。

## 今日复盘问题与参考答案

1. **OpenCV 读入的彩色图片为什么是三维数组？**
   - 因为每个像素除了位置，还包含多个颜色通道。OpenCV 彩色图一般是 BGR 三通道，所以形状是 `(height, width, channels)`。

2. **`width`、`height`、`channels` 分别来自 `image.shape` 的哪一部分？**
   - `height` 来自第 1 个值，`width` 来自第 2 个值，`channels` 来自第 3 个值。

3. **灰度图和原图相比有什么变化？**
   - 灰度图去掉了颜色信息，只保留亮度强弱。视觉上会从彩色变成黑白灰。

4. **为什么没有 `assets/sample.jpg` 时脚本仍然可以运行？**
   - 因为 `load_image_or_demo()` 在读取失败后会调用 `create_demo_image()` 生成练习图。

5. **为什么云服务器上运行 `cv2.imshow()` 可能失败？**
   - `cv2.imshow()` 需要图形界面窗口系统。无 GUI 的环境通常只能保存图片，不能直接弹窗显示。

## 明日学习计划摘要

由于 `progress.md` 没有明确记录 Day 1 已完成，明日继续 Day 1，不跳到 Day 2。

- 继续主题：跑通项目并理解 OpenCV 入门流程。
- 重点文件：`README.md`、`src/common.py`、`src/01_read_show_save.py`。
- 重点任务：运行第一个脚本、确认输出文件、理解 `image.shape`、灰度转换和保存流程。
