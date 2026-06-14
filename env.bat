@echo off
set "PROJECT_DIR=%~dp0"
set "CONDA_ENV=%PROJECT_DIR%.glut"

if not defined AI_TOOLS_DIR set "AI_TOOLS_DIR=%PROJECT_DIR%..\Tools"
set "ARIA2_HOME=%AI_TOOLS_DIR%\aria2\aria2-1.37.0-win-64bit-build1"
set "FFMPEG_HOME=%AI_TOOLS_DIR%\ffmpeg\ffmpeg-8.1.1-essentials_build\bin"

set "PATH=%CONDA_ENV%;%CONDA_ENV%\Scripts;%CONDA_ENV%\Library\bin;%ARIA2_HOME%;%FFMPEG_HOME%;%PATH%"
set "PYTHONPATH=%PROJECT_DIR%;%PYTHONPATH%"
set "PYTHONNOUSERSITE=1"

set "PIP_CACHE_DIR=%PROJECT_DIR%.cache\pip"
set "HF_HOME=%PROJECT_DIR%.cache\huggingface"
set "HF_HUB_CACHE=%PROJECT_DIR%.cache\huggingface\hub"
set "HUGGINGFACE_HUB_CACHE=%PROJECT_DIR%.cache\huggingface\hub"
set "TRANSFORMERS_CACHE=%PROJECT_DIR%.cache\huggingface\transformers"
set "DIFFUSERS_CACHE=%PROJECT_DIR%.cache\huggingface\diffusers"
set "HF_HUB_ENABLE_HF_TRANSFER=1"
set "MODELSCOPE_CACHE=%PROJECT_DIR%.cache\modelscope"
set "TORCH_HOME=%PROJECT_DIR%.cache\torch"
set "XDG_CACHE_HOME=%PROJECT_DIR%.cache"
set "PYTHONUTF8=1"
