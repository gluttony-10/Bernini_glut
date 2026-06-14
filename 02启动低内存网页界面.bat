@echo off
chcp 65001 >nul
call "%~dp0env.bat"

title Bernini Gradio WebUI Launcher (Low Memory Mode)
echo ===================================================
echo   Starting Bernini Gradio Demo on Single GPU...
echo   Low Memory Mode (skip_transformer_2) Enabled
echo ===================================================

:: Force single GPU execution
set CUDA_VISIBLE_DEVICES=0

:: Run Gradio demo in low memory mode using local conda environment python executable
"%CONDA_ENV%\python.exe" gradio_demo.py --config models/Bernini-Diffusers --port 7860 --low_vram

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Gradio launcher exited with code %errorlevel%
    pause
)
