def main():

"""
Upgrade Extraction Template Script
==================================
Този скрипт е шаблон за извличане на универсалните подобрения от студентски бранч.

Използване:
  1. Клонирай/чекаутни student/<user> бранча.
  2. Стартирай този скрипт (python upgrade_extraction_skeleton.py).
  3. Следвай инструкциите за адаптация към твоята структура.

Какво прави (примерен workflow):
  - Открива и копира само theory.md, assignment.md (шаблон), manifest, prerequisites и др.
  - Изключва лични файлове (session state, mistakes, попълнени index.html и др.).
  - Възстановява темплейти (ако е нужно).
  - Създава нов feature/upgrade бранч (или дава инструкции).

Конфигурирай според нуждите си:
  - EXCLUDE: списък с файлове/папки за изключване
  - TEMPLATE_FILES: кои файлове да се възстановят до темплейт

Примерни функции са дадени по-долу. Замени ги с реална логика според твоята структура!
"""

import os
import shutil

# Конфигурирай кои файлове/папки да се изключват
EXCLUDE = [
    'tools/current_session.json',
    '*.mistakes*',
    '**/index.html',  # попълнените index.html се възстановяват до темплейт
]

# Кои файлове да се възстановят до темплейт (пример)
TEMPLATE_FILES = [
    'index.html',
    'assignment.md',
]

def is_excluded(path):
    # TODO: Имплементирай логика за изключване по pattern
    return any(e in path for e in EXCLUDE)

def restore_template(file_path):
    # TODO: Имплементирай възстановяване на темплейт (пример)
    if file_path.endswith('index.html'):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("<!-- Пиши своя HTML код тук -->\n")
    if file_path.endswith('assignment.md'):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("# Задача\n\n(Тук ще бъде условието на задачата)\n")

def main():
    print("[TEMPLATE] Upgrade extraction стартиран...")
    # 1. Прегледай файловете в проекта
    for root, dirs, files in os.walk('.'):
        for file in files:
            path = os.path.join(root, file)
            if is_excluded(path):
                print(f"Изключен: {path}")
                continue
            if file in TEMPLATE_FILES:
                print(f"Възстановявам темплейт: {path}")
                restore_template(path)
    print("[TEMPLATE] Готово!\nПровери резултата и адаптирай според структурата си.")

if __name__ == "__main__":
    main()
