"""
Скрипт для создания exe файла с помощью PyInstaller
"""

import sys
import subprocess

# Параметры для PyInstaller
command = [
    "pyinstaller",
    "--onefile",                    # Один exe файл
    "--windowed",                   # Без консоли
    "--name=ComputerAlgebra",       # Имя exe файла
    "--add-data=natural.py:.",      # Включить модули
    "--add-data=integer.py:.",
    "--add-data=rational.py:.",
    "--add-data=polynomial.py:.",
    "--clean",                      # Очистить кэш
    "gui_app.py"                    # Главный файл
]

result = subprocess.run(command, capture_output=False)

if result.returncode == 0:
    print()
    print("EXE файл успешно создан!")
    print()
    print("Файл находится в папке: dist/ComputerAlgebra.exe")
else:
    print()
    print("Ошибка при создании exe файла")
    print()
    sys.exit(1)
