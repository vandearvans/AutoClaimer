@echo off
set VENV_DIR=.venv

REM Check if virtual environment exists
if not exist %VENV_DIR% (
    echo [INFO] Virtual environment not found. Creating one...
    python -m venv %VENV_DIR%
    
    echo [INFO] Activating virtual environment...
    call %VENV_DIR%\Scripts\activate

    echo [INFO] Installing requirements...
    pip install -r requirements.txt
) else (
    echo [INFO] Virtual environment found. Activating...
    call %VENV_DIR%\Scripts\activate
)

echo [INFO] Running main.py...
python main.py

pause
