<div align="center">

<img src="assets/bernini-icon.png" width="560" alt="Bernini"/>

<h4 align="center">Latent Semantic Planning for Video Diffusion</h4>
<h5 align="center">🚀 专为消费级硬件优化 (32GB 内存 / 24GB 显存) 🚀</h5>

[English Version](README.md) | [中文版](README_zh.md)

</div>

## ✨ 简介

**Bernini** 是一个统一的视频生成和编辑框架，结合了基于 MLLM（多模态大语言模型）的语义规划器和基于 DiT 的渲染器。通过在渲染前对复杂指令进行拆解和语义规划，Bernini 在视频生成与编辑任务上达到了行业顶尖水平。

**本仓库 (`Bernini_glut`) 是满血版 Bernini (MLLM + 渲染器) 流程的一个专项优化分支**，经过深度定制，使其能够在消费级硬件上流畅运行，特别针对 **32GB 物理内存 (RAM) 和 24GB 显存 (VRAM)**（如 RTX 3090 / 4090）的电脑进行了极限优化。

### 本分支的核心优化：
- **ModelScope (魔搭) 深度集成**：我们将庞大的原始 Safetensors 权重预转换成了内存友好的 `mmgp` 格式，并托管在魔搭社区，极大地减小了下载体积和硬盘占用。
- **低内存/显存模式 (`--low_vram`)**：原始的满血版 Bernini 流程需要占用超过 34GB 的物理内存，这会导致 32GB 内存的机器疯狂使用硬盘虚拟内存 (Swap)，使推理速度暴跌到“几分钟一步”。我们引入了 `--low_vram` 一键开关，能够安全地跳过低噪声细化模型 (`transformer_2`) 的加载，直接**节省 13.6GB 的内存占用**，让生成速度重回闪电般顺畅。

## 📦 安装与部署

### 环境要求
- **Python** 3.11.2
- **CUDA GPU** (在 24GB 显存的消费级显卡上经过深度测试)
- **CUDA toolkit** 12.4

### 1. 安装代码
```bash
git clone https://github.com/gluttony-10/Bernini_glut.git
cd Bernini_glut
pip install -r requirements.txt
```

### 2. 下载优化版模型
我们在魔搭社区上准备了该模型的精简版，彻底剔除了臃肿的原始 safetensors 文件，仅保留了优化后的 `mmgp` 权重。

我们强烈建议使用 `modelscope` 官方 Python 库来下载模型，这种方式既稳定又不需要依赖系统的 Git LFS 环境。

首先，安装魔搭官方库：
```bash
pip install modelscope
```

然后，运行以下 Python 代码，即可将模型极速拉取到指定目录：
```python
from modelscope.hub.snapshot_download import snapshot_download
snapshot_download('Gluttony10/Bernini_glut', local_dir='models/Bernini_glut')
```
*(请确保下载的文件最终准确位于项目内的 `models/Bernini_glut` 目录下)*

## 🚀 使用方法

### 单卡推理测试
项目底层会自动检测物理内存和可用显存，自适应配置模型加载和优化策略，无需手动指定参数：
```bash
# 建议先设置环境变量防止显存碎片化
set PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
# 运行单卡推理
python infer_single_gpu.py --config models/Bernini_glut --case assets/testcases/v2v/v2v_case1.json
```

### 样例文件 (Case files)
每次运行均由一个 **case file** 描述 — 这是一个位于 [`assets/testcases/`](assets/testcases/) 下的小型 JSON 文件，里面写好了任务参数（如 `task_type`, `guidance_mode`, `prompt`, 源媒体等）。这让您不必在命令行中输入冗长的提示词。

### 提示词增强器 (强烈推荐)
在命令后加上 `--use_pe` 能够通过兼容 OpenAI 的大语言模型接口来增强您的提示词，获得最佳的生成质量。配置方法如下：
```cmd
export BERNINI_PE_API_KEY=...      # 或 OPENAI_API_KEY
export BERNINI_PE_BASE_URL=...     # 或 OPENAI_BASE_URL
export BERNINI_PE_MODEL=...        # 支持视觉的聊天模型
```

### 网页图形界面 (Gradio GUI)
您可以通过提供的 batch 脚本一键启动交互式的网页版 UI（系统会自动判定内存与显存进行最优加载方案规划，无需手动传入配置参数）：
```cmd
.\01运行程序.bat
```

或者在终端手动执行以下命令启动：
```bash
python gradio_demo.py --config models/Bernini_glut --port 7860
```

## 📑 引用与致谢

如果您在研究中使用了 Bernini，请引用原论文：
```bibtex
@article{bernini,
  title   = {Bernini: Latent Semantic Planning for Video Diffusion},
  author  = {Chenchen Liu and Junyi Chen and Lei Li and Lu Chi and Mingzhen Sun and Zhuoying Li and Yi Fu and Ruoyu Guo and Yiheng Wu and Ge Bai and Zehuan Yuan},
  journal = {arXiv preprint arXiv:2605.22344},
  year    = {2026}
}
```
Bernini 建立在诸如 Wan2.2、Qwen2.5-VL 以及 VeOmni 等杰出的开源项目之上，感谢原作者们的贡献。

## 📄 许可证
Apache License 2.0. 参见 [LICENSE](LICENSE)。
