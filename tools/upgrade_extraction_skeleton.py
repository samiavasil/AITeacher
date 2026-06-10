
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
import json
import fnmatch

# Конфигурирай кои файлове/папки да се изключват
EXCLUDE = [
    'tools/current_session.json',
    '*.mistakes*',
    '.git/*',
    '__pycache__/*',
]

# Кои файлове да се възстановят до темплейт (пример)
TEMPLATE_FILES = [
    'index.html',
    'assignment.md',
    'script.js',
    'style.css',
]

ALLOWED_SESSION_STATES = {'not_started', 'in_progress', 'completed'}


def load_manifest(manifest_path='tools/course_manifest.json'):
    if not os.path.exists(manifest_path):
        return None
    with open(manifest_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def default_course_from_manifest(manifest):
    if not manifest:
        return None

    courses = manifest.get('courses', [])
    if not courses:
        return None

    default_id = manifest.get('default_course_id')
    for course in courses:
        if course.get('id') == default_id:
            return course
    return courses[0]


def restore_session_template(session_path='tools/current_session.json', manifest=None):
    course = default_course_from_manifest(manifest)
    lesson_path = '01-html/01-intro'
    course_id = ''
    course_title = ''

    if course:
        steps = course.get('steps', [])
        lesson_path = course.get('entry_lesson_path') or (steps[0] if steps else lesson_path)
        course_id = course.get('id', '')
        course_title = course.get('title', '')

    template = {
        'schema_version': '2.0.0',
        'student_name': '',
        'current_branch': '',
        'current_course_id': course_id,
        'current_course_title': course_title,
        'last_update_utc': '',
        'current_step_index': 0,
        'current_lesson_path': lesson_path,
        'lesson_state': 'not_started',
        'next_step_action': 'load_theory',
        'completed_lessons': [],
        'mistakes_log': [],
        'teacher_internal_notes': ''
    }

    with open(session_path, 'w', encoding='utf-8') as f:
        json.dump(template, f, indent=4, ensure_ascii=False)
        f.write('\n')


def build_base_assignment(path):
    lesson_name = os.path.basename(os.path.dirname(path))
    return (
        '# ASSIGNMENT\n\n'
        f'## Задача: {lesson_name}\n\n'
        '- Прочети условието от учителя.\n'
        '- Реши задачата в съответния учебен файл.\n'
        '- Подготви кратко обяснение на решението.\n'
    )

def is_excluded(path):
    normalized = path.replace('\\', '/').lstrip('./')
    return any(fnmatch.fnmatch(normalized, pattern) for pattern in EXCLUDE)

def restore_template(file_path):
    # Възстановява index.html до работещ базов HTML темплейт
    if file_path.endswith('index.html'):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(
                '<!DOCTYPE html>\n'
                '<html lang="bg">\n'
                '<head>\n'
                '    <meta charset="UTF-8">\n'
                '    <title>HTML Урок</title>\n'
                '</head>\n'
                '<body>\n'
                '    <!-- Тук добави своето съдържание -->\n'
                '</body>\n'
                '</html>\n'
            )
    # Възстановява script.js до празен темплейт
    elif file_path.endswith('script.js'):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('// Празен темплейт за JavaScript\n')
    # Възстановява style.css до празен темплейт
    elif file_path.endswith('style.css'):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('/* Празен темплейт за CSS */\n')
    # assignment.md се връща до базово условие без лични отговори
    elif file_path.endswith('assignment.md'):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(build_base_assignment(file_path))


def should_restore(file_name):
    return file_name in TEMPLATE_FILES


def validate_manifest_shape(manifest):
    if not manifest:
        return
    if manifest.get('schema_version') != '2.0.0':
        print('[WARN] Manifest schema is not 2.0.0. Adjust script if needed.')
    courses = manifest.get('courses', [])
    for course in courses:
        steps = course.get('steps', [])
        if not steps:
            print(f"[WARN] Course without steps: {course.get('id', '<unknown>')}")


def validate_session_state(session_path='tools/current_session.json'):
    if not os.path.exists(session_path):
        return
    try:
        with open(session_path, 'r', encoding='utf-8') as f:
            session = json.load(f)
    except (ValueError, OSError):
        print(f'[WARN] Session file could not be parsed: {session_path}')
        return

    state = session.get('lesson_state')
    if state not in ALLOWED_SESSION_STATES:
        print(f"[WARN] Invalid lesson_state '{state}' in {session_path}")

def main():
    print("[TEMPLATE] Upgrade extraction стартиран...")
    manifest = load_manifest()
    validate_manifest_shape(manifest)

    if os.path.exists('tools/current_session.json'):
        print('Възстановявам tools/current_session.json до базов темплейт...')
        restore_session_template(manifest=manifest)

    # 1. Прегледай файловете в проекта
    for root, dirs, files in os.walk('.'):
        for file in files:
            path = os.path.join(root, file)
            if is_excluded(path):
                print(f"Изключен: {path}")
                continue
            if should_restore(file):
                print(f"Възстановявам темплейт: {path}")
                restore_template(path)
    validate_session_state()
    print("[TEMPLATE] Готово!\nПровери резултата и адаптирай според структурата си.")

if __name__ == "__main__":
    main()
