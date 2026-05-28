# AI 视觉学习进度

用这个文件记录每天 1 小时学习后的结果。每天晚上自动化会基于这里的最新进度生成第二天学习内容。

## 当前进度

- 当前天数：Day 2
- 当前主题：学习图像矩阵、宽高通道、`cv2.imread`、`cv2.imwrite`、灰度图
- 最近更新：2026-05-28

## 每日记录

### Day 1

- 是否完成：是
- 运行过的命令：
  - `python src/01_read_show_save.py`
- 生成的输出文件：
  - `output/01_original.jpg`
  - `output/01_gray.jpg`
- 今天最重要的概念：
  - OpenCV 读入的彩色图像是 NumPy 三维数组，`image.shape` 的顺序是 `(height, width, channels)`。
  - `cv2.imread()` 读取图片，`cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` 生成灰度图，`cv2.imwrite()` 负责保存文件。
  - `src/common.py` 会在 `assets/sample.jpg` 不存在时生成 demo 图，保证入门流程可以跑通。
- 遇到的问题：
  - 自动化 Linux 环境没有 GUI，直接调用 `cv2.imshow()` 不适合；本次通过临时跳过窗口函数验证保存流程。
- 明天想继续学习：
  - 继续理解图像矩阵、BGR/RGB 通道顺序、像素访问、通道拆分合并和局部区域修改。

### Day 2

- 是否完成：否
- 运行过的命令：
- 生成的输出文件：
- 今天最重要的概念：
- 遇到的问题：
- 明天想继续学习：
