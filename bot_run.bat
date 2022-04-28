@echo off

call %~dp0(tlegram_bot\venv\Scripts\activate)

cd %~dp0(tlegram_bot)

set TOKEN=5246022132:AAHav2nuZmrGJNxwZHEQ2XqB3O0A3s5J_pw

python bot_telegram.py

pause