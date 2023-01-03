Set-Location .\venv\Scripts
./Activate
Set-Location ..
Set-Location ..
pyinstaller -F -w slicer-gui.py --additional-hooks=extra-hooks --additional-hooks-dir .\extra-hooks