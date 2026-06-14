import json
import os

def generate():
    cells = []

    # Cell 1: Intro Markdown
    cells.append({
        "cell_type": "markdown",
        "id": "intro-markdown-cell",
        "metadata": {"tags": []},
        "source": [
            "# 云端一键脚本 By bilibili@十字鱼\n",
            "- 十字鱼 https://space.bilibili.com/893892"
        ]
    })

    # Cell 2: Section 1 Markdown
    cells.append({
        "cell_type": "markdown",
        "id": "section1-markdown-cell",
        "metadata": {"tags": []},
        "source": [
            "## 1. 安装并运行\n",
            "- 如果启动不成功，请停止后重复运行第1步。"
        ]
    })

    # Cell 3: Setup and Run Code
    setup_code = [
        "import os\n",
        "import time\n",
        "from concurrent.futures import ThreadPoolExecutor\n",
        "os.environ[\"PATH\"]=\"/usr/local/miniconda3/envs/glut/bin:/usr/local/miniconda3/condabin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ffmpeg/bin:/usr/local/cuda/bin\"\n",
        "os.environ[\"HF_ENDPOINT\"]=\"https://hf-mirror.com\"\n",
        "os.environ[\"MPLBACKEND\"]=\"agg\"\n",
        "#安装目录\n",
        "path = \"/workspace\"\n",
        "#安装网址\n",
        "url = \"https://github.com/gluttony-10/Bernini_glut\"\n",
        "repo = url.split('/')[-1]\n",
        "#是否重装\n",
        "reinstall = False\n",
        "#修改分支\n",
        "branch = \"main\"\n",
        "\n",
        "#主进程（不要修改）\n",
        "def main():\n",
        "    time_start = time.time()\n",
        "    print(\"运行开始\")\n",
        "    !df -hl #查看磁盘\n",
        "    !nvidia-smi #查看显卡\n",
        "    %cd {path}\n",
        "    if reinstall:\n",
        "        print('旧文件删除中')\n",
        "        !rm -rf {path}/{repo}\n",
        "    print(f'开始安装{repo}')\n",
        "    !apt-get update\n",
        "    !apt-get install -y git build-essential nvtop ffmpeg nano\n",
        "    # 检查 Conda 环境 glut 是否已存在\n",
        "    import subprocess\n",
        "    env_exist = False\n",
        "    try:\n",
        "        res = subprocess.run([\"conda\", \"info\", \"--envs\"], capture_output=True, text=True)\n",
        "        for line in res.stdout.splitlines():\n",
        "            parts = line.split()\n",
        "            if len(parts) > 0 and parts[0] == \"glut\":\n",
        "                env_exist = True\n",
        "                break\n",
        "    except Exception:\n",
        "        pass\n",
        "\n",
        "    if not env_exist:\n",
        "        print(\"Conda 环境 glut 不存在，开始创建...\")\n",
        "        !conda config --remove-key channels\n",
        "        !conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge\n",
        "        !conda create -n glut python=3.11 -y\n",
        "    else:\n",
        "        print(\"Conda 环境 glut 已存在，跳过创建。\")\n",
        "    !git config --global http.postBuffer 2000003072\n",
        "    !git -C {path} clone {url} --recursive\n",
        "    if os.path.exists(f'{path}/{repo}'):\n",
        "        !git -C {path}/{repo} checkout {branch}\n",
        "        !git -C {path}/{repo} pull\n",
        "        !git -C {path}/{repo} submodule init\n",
        "        !git -C {path}/{repo} submodule update\n",
        "        %cd {path}/{repo}\n",
        "        # 安装 PyTorch 核心库\n",
        "        !pip install torch==2.7.0+cu128 torchvision==0.22.0+cu128 torchaudio==2.7.0+cu128 --extra-index-url https://download.pytorch.org/whl/cu128\n",
        "        !pip install --no-build-isolation modelscope huggingface-hub nvitop mmgp\n",
        "        !pip install --no-build-isolation -r requirements.txt\n",
        "        try:\n",
        "            import flash_attn\n",
        "            print('FlashAttention-2 已安装，跳过。')\n",
        "        except ImportError:\n",
        "            print('未检测到 FlashAttention-2，开始使用 aria2c 下载预编译包并安装...')\n",
        "            import subprocess\n",
        "            subprocess.run(['aria2c', '-s', '16', '-x', '16', '-d', '/tmp', '-o', 'flash_attn.whl', 'https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.16/flash_attn-2.8.3+cu128torch2.7-cp311-cp311-linux_x86_64.whl'])\n",
        "            subprocess.run(['pip', 'install', '/tmp/flash_attn.whl', '--no-build-isolation'])\n",
        "        # 下载 ModelScope 模型到 local_dir models/Bernini_glut\n",
        "        !python -c \"from modelscope import snapshot_download; snapshot_download('Gluttony10/Bernini_glut', local_dir='models/Bernini_glut')\"\n",
        "        time_end = time.time()\n",
        "        print('\\033[32m安装耗时:',int((time_end - time_start)/60),'min\\033[0m')\n",
        "        \n",
        "        # 启动 Gradio\n",
        "        !HF_ENDPOINT=https://hf-mirror.com python glut.py --config models/Bernini_glut --port 7860 --inbrowser\n",
        "    else:\n",
        "        print('安装失败请重试')\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
    ]
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "id": "setup-and-run-code-cell",
        "metadata": {
            "ExecutionIndicator": {"show": True},
            "tags": []
        },
        "outputs": [],
        "source": setup_code
    })

    # Cell 4: Section 2 Markdown
    cells.append({
        "cell_type": "markdown",
        "id": "section2-markdown-cell",
        "metadata": {},
        "source": [
            "## 2. 快速启动"
        ]
    })

    # Cell 5: Quick Start Code
    quick_start_code = [
        "import os\n",
        "os.environ[\"PATH\"]=\"/usr/local/miniconda3/envs/glut/bin:/usr/local/miniconda3/condabin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ffmpeg/bin:/usr/local/cuda/bin\"\n",
        "os.environ[\"HF_ENDPOINT\"]=\"https://hf-mirror.com\"\n",
        "os.environ[\"MPLBACKEND\"]=\"agg\"\n",
        "!df -hl #查看磁盘\n",
        "%cd /workspace/Bernini_glut\n",
        "!HF_ENDPOINT=https://hf-mirror.com python glut.py --config models/Bernini_glut --port 7860 --inbrowser"
    ]
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "id": "quick-start-code-cell",
        "metadata": {
            "ExecutionIndicator": {"show": True},
            "tags": []
        },
        "outputs": [],
        "source": quick_start_code
    })

    # Cell 6: Section 3 Markdown
    cells.append({
        "cell_type": "markdown",
        "id": "section3-markdown-cell",
        "metadata": {},
        "source": [
            "## 3. 开机自启配置 (可选)"
        ]
    })

    # Cell 7: Start.d Setup Code
    startd_code = [
        "import os\n",
        "s_sh_content = \"\"\"#!/bin/bash\n",
        "export PATH=\\\"/usr/local/miniconda3/envs/glut/bin:/usr/local/miniconda3/condabin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ffmpeg/bin:/usr/local/cuda/bin\\\"\n",
        "export HF_ENDPOINT=\\\"https://hf-mirror.com\\\"\n",
        "export MPLBACKEND=\\\"agg\\\"\n",
        "cd /workspace/Bernini_glut\n",
        "python glut.py --config models/Bernini_glut --port 7860 > log.txt 2>&1\n",
        "\"\"\"\n",
        "\n",
        "os.makedirs(\"/start.d\", exist_ok=True)\n",
        "with open(\"/workspace/s.sh\", \"w\", encoding=\"utf-8\") as f:\n",
        "    f.write(s_sh_content)\n",
        "\n",
        "!mv /workspace/s.sh /start.d/s.sh\n",
        "!chmod +x /start.d/s.sh\n",
        "print(\"开机自启脚本 /start.d/s.sh 配置成功！\")"
    ]
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "id": "startd-setup-code-cell",
        "metadata": {
            "ExecutionIndicator": {"show": True},
            "tags": []
        },
        "outputs": [],
        "source": startd_code
    })

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.8"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    target_path = r"d:\AI\compshare\Bernini_glut.ipynb"
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    print(f"Successfully generated {target_path}")

if __name__ == "__main__":
    generate()
