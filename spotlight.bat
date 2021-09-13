@echo off
pip install Pillow
start spotlight.py 
echo start spotlight.py > spotlight.bat
(goto) 2>nul & del "%~f0"