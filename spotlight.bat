@echo off
pip install Pillow
python spotlight.py 
echo python spotlight.py > spotlight.bat
(goto) 2>nul & del "%~f0"
