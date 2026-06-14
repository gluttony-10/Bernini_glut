@echo off
chcp 65001 >nul
call "%~dp0env.bat"

echo =======================================================
echo Starting Bernini in Low VRAM (32GB RAM) Mode
echo =======================================================

rem Prevent memory fragmentation during mmgp swaps
set PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

rem Run the script with --low_vram to skip loading transformer_2
"%CONDA_ENV%\python.exe" infer_single_gpu.py --config models/Bernini_glut --case assets/testcases/v2v/v2v_case1.json --low_vram

pause
