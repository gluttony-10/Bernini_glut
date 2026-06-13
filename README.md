<div align="center">

<img src="assets/bernini-icon.png" width="560" alt="Bernini"/>

<h4 align="center">Latent Semantic Planning for Video Diffusion</h4>
<h5 align="center">🚀 Optimized for Consumer Hardware (32GB RAM / 24GB VRAM) 🚀</h5>

[English Version](README.md) | [中文版](README_zh.md)

</div>

## ✨ Introduction

**Bernini** is a unified framework for video generation and editing that combines an MLLM-based semantic planner with a DiT-based renderer. By decomposing complex instructions and planning semantic changes before rendering, Bernini achieves top-tier performance in video generation and editing tasks.

**This repository (`Bernini_glut`) is a specialized fork of the Full Bernini (MLLM + Renderer) pipeline**, heavily optimized to run on consumer hardware, specifically targeting systems with **32GB of physical RAM and 24GB of VRAM** (e.g., RTX 3090 / 4090).

### Key Optimizations in this Fork:
- **ModelScope Integration**: We have pre-converted the massive Safetensors into `mmgp` formats and hosted them on ModelScope, drastically reducing download sizes and disk footprints.
- **Low VRAM/RAM Mode (`--low_vram`)**: The original full Bernini pipeline requires over 34GB of physical RAM, forcing OS swapping that degrades inference speeds to minutes per step. We introduced a `--low_vram` toggle that safely skips the low-noise refinement model (`transformer_2`), cutting RAM usage by 13.6GB and restoring lightning-fast generation speeds.

## 📦 Installation & Setup

### Requirements
- **Python** 3.11.2
- **CUDA GPU** (Tested heavily on 24GB VRAM consumer GPUs)
- **CUDA toolkit** 12.4

### 1. Install Code
```bash
git clone https://github.com/gluttony-10/Bernini_glut.git
cd Bernini_glut
pip install -r requirements.txt
```

### 2. Download Optimized Models
We have prepared a streamlined version of the model on ModelScope that excludes the bloated raw safetensors, keeping only the optimized `mmgp` weights.

You can download the model easily using the `modelscope` Python package. This method is much faster and does not require Git LFS.

First, install modelscope:
```bash
pip install modelscope
```

Then, download the model directly into the required directory:
```python
from modelscope.hub.snapshot_download import snapshot_download
snapshot_download('Gluttony10/Bernini_glut', local_dir='models/Bernini-Diffusers')
```
*(Make sure the downloaded files are located exactly in the `models/Bernini-Diffusers` folder within your project)*

## 🚀 Usage

### Low RAM Optimization Mode (32GB RAM / 24GB VRAM)

**One-Click Startup:**
We have provided a ready-to-use startup script: `run_low_ram.bat`.
This script automatically sets `expandable_segments:True` to prevent PyTorch memory fragmentation and runs the inference script with the `--low_vram` flag.

Simply double-click **`run_low_ram.bat`** in Windows, or run it via command line:
```cmd
.\run_low_ram.bat
```

**Manual Command:**
Alternatively, you can manually run:
```bash
export PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True"
python infer_single_gpu.py --config models/Bernini-Diffusers --case assets/testcases/v2v/v2v_case1.json --low_vram
```

### Case files
A run is described by a **case file** — a small JSON under [`assets/testcases/`](assets/testcases/) that bundles one task's routing and inputs (`task_type`, `guidance_mode`, `prompt`, source media, `output`). This keeps long prompts out of the command line.

### Prompt Enhancer (Recommended)
`--use_pe` enhances the prompt through an OpenAI-compatible endpoint for the best generation quality. Configure the endpoint with environment variables:
```bash
export BERNINI_PE_API_KEY=...      # or OPENAI_API_KEY
export BERNINI_PE_BASE_URL=...     # or OPENAI_BASE_URL
export BERNINI_PE_MODEL=...        # vision-capable chat model
```

### Gradio GUI
You can also run the interactive Web UI using the provided batch script:
```cmd
.\run_gradio.bat
```

## 📑 Citation & Acknowledgements

If you use Bernini in your research, please cite the original paper:
```bibtex
@article{bernini,
  title   = {Bernini: Latent Semantic Planning for Video Diffusion},
  author  = {Chenchen Liu and Junyi Chen and Lei Li and Lu Chi and Mingzhen Sun and Zhuoying Li and Yi Fu and Ruoyu Guo and Yiheng Wu and Ge Bai and Zehuan Yuan},
  journal = {arXiv preprint arXiv:2605.22344},
  year    = {2026}
}
```
Bernini builds on outstanding open-source projects including Wan2.2, Qwen2.5-VL, and VeOmni.

## 📄 License
Apache License 2.0. See [LICENSE](LICENSE).
