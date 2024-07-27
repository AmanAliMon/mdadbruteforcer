@echo off
setlocal

REM Check if pip is installed
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pip...
    python -m ensurepip
)
cd engine
REM Create and activate a virtual environment
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

REM Install dependencies
pip install --upgrade pip
pip install selenium rich

REM Run k.py
python k.py

endlocal
