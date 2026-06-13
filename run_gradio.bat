@echo off
title Bernini Gradio WebUI Launcher
echo ===================================================
echo   Starting Bernini Gradio Demo on Single GPU...
echo ===================================================

:: Force single GPU execution
set CUDA_VISIBLE_DEVICES=0

:: Run Gradio demo using local conda environment python executable
.glut\python.exe gradio_demo.py --config models/Bernini-Diffusers --port 7860

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Gradio launcher exited with code %errorlevel%
    pause
)
