"""
Скелет на скрипт за upgrade extraction:
- Сравнява student/<user> с main
- Изключва лични файлове (session, mistakes, попълнени index.html)
- Възстановява темплейти
- Създава feature/upgrade бранч с универсалните промени
"""

import os
import shutil
import subprocess

# Конфигурирай кои файлове/папки да се изключват
EXCLUDE = [
    'tools/current_session.json',
    'tools/mistakes_log.json',
    '*index.html',  # попълнените index.html се възстановяват до темплейт
]

# TODO: Имплементирай логика за сравнение, филтриране и създаване на нов бранч

def main():
    print("[СКЕЛЕТ] Upgrade extraction стартиран...")
    # 1. Сравни student/<user> с main
    # 2. Изключи личните файлове
    # 3. Възстанови темплейти
    # 4. Създай feature/upgrade бранч
    print("[СКЕЛЕТ] Готово!")

if __name__ == "__main__":
    main()
