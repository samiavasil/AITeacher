import os
import json

def create_course_structure():
    # 1. Пълна финална структура на проекта с включени памет, манифест и предложения за нови теми
    structure = {
        ".github": ["AI_TEACHER_PROMPT.md"],
        ".vscode": ["settings.json"],
        "tools": [
            "generate_structure.py",
            "current_session.json",  # Паметта за сесиите (Локален контекст)
            "course_manifest.json"   # Динамичната пътна карта на курса
        ],
        "tools/proposed_topics": [], # Папката за AI предложения за Pull Requests към main
        "01-html/01-intro": ["theory.md", "assignment.md", "index.html"],
        "01-html/02-elements": ["theory.md", "assignment.md", "index.html"],
        "02-css/01-selectors": ["theory.md", "assignment.md", "index.html", "style.css"],
        "02-css/02-box-model": ["theory.md", "assignment.md", "index.html", "style.css"],
        "03-javascript/01-variables": ["theory.md", "assignment.md", "script.js"],
        "03-javascript/02-dom-manipulation": ["theory.md", "assignment.md", "index.html", "script.js"],
    }
    
    # 2. Прочитане на текущия код на самия скрипт за самокопиране в tools/
    current_script_path = os.path.abspath(__file__)
    with open(current_script_path, "r", encoding="utf-8") as current_file:
        script_content = current_file.read()

    # 3. Създаване на коренния README.md
    if not os.path.exists("README.md"):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write("# AI-Driven Web Development Course\n\nДобре дошли! Моля, прочетете инструкциите в `.github/AI_TEACHER_PROMPT.md`, за да стартирате с вашия AI учител.")
        print("📁 Създаден коренен файл: README.md")

    # 4. Изграждане на папките и файловете
    for folder, files in structure.items():
        os.makedirs(folder, exist_ok=True)
        print(f"📁 Създадена папка: {folder}")
        
        # Конфигуриране на специфичните файлове
        for file in files:
            file_path = os.path.join(folder, file)
            
            # Копиране на скрипта
            if folder == "tools" and file == "generate_structure.py":
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(script_content)
                print(f"  💾 Скриптът се самокопира в: {file_path}")
                continue
                
            # Инициализиране на празната памет за сесията на ученика
            if folder == "tools" and file == "current_session.json":
                if not os.path.exists(file_path):
                    initial_session = {
                        "student_name": "Unknown",
                        "current_branch": "main",
                        "last_update": "",
                        "current_module": "01-html",
                        "current_lesson": "01-intro",
                        "completed_lessons": [],
                        "teacher_notes": "Ученикът стартира курса сега. Провери бранча му и го покани да започне."
                    }
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(initial_session, f, indent=4, ensure_ascii=False)
                    print(f"  🧠 Създадена локална памет: {file}")
                continue

            # Инициализиране на Манифеста на курса
            if folder == "tools" and file == "course_manifest.json":
                if not os.path.exists(file_path):
                    manifest = {
                        "course_name": "Web Dev за Начинаещи",
                        "steps": [
                            "01-html/01-intro",
                            "01-html/02-elements",
                            "02-css/01-selectors",
                            "02-css/02-box-model",
                            "03-javascript/01-variables",
                            "03-javascript/02-dom-manipulation"
                        ]
                    }
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(manifest, f, indent=4, ensure_ascii=False)
                    print(f"  🗺️ Създаден манифест на курса: {file}")
                continue

            # Настройки за VS Code (насочване на AI да индексира инструкциите първо)
            if folder == ".vscode" and file == "settings.json":
                if not os.path.exists(file_path):
                    vscode_settings = {
                        "github.copilot.chat.scope": "workspace",
                        "files.exclude": {
                            "**/.git": True,
                            "**/generate_structure.py": False
                        }
                    }
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(vscode_settings, f, indent=4, ensure_ascii=False)
                    print(f"  ⚙️ Създадени VS Code настройки: {file}")
                continue

            # Създаване на стандартните празни шаблони за учене
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    if file.endswith(".md"):
                        f.write(f"# {file.split('.')[0].upper()}\n")
                    elif file.endswith(".html"):
                        f.write("<!-- Пиши своя HTML код тук -->\n")
                    elif file.endswith(".css"):
                        f.write("/* Пиши своя CSS код тук */\n")
                    elif file.endswith(".js"):
                        f.write("// Пиши своя JavaScript код тук\n")
                print(f"  📄 Създаден учебен файл: {file}")

if __name__ == "__main__":
    print("🚀 Стартиране на генерирането на финалната архитектура...")
    create_course_structure()
    print("✅ Системата е напълно готова и структурирана!")
