@echo off
REM Activate the virtual environment
call myenv\Scripts\activate

REM Install/update dependencies
pip install -r requirements.txt

echo Dependencies installed/updated successfully.
