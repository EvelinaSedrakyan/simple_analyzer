& "C:\Users\Acer\Desktop\simple_analyzer\.venv\Scripts\Activate.ps1"
Start-Process powershell -ArgumentList '-NoExit', '-Command', 'python "C:\Users\Acer\Desktop\simple_analyzer\simple_analyzer\main.py" *> "C:\Users\Acer\Desktop\simple_analyzer\scripts\output.log"' -WindowStyle Hidden
