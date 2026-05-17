import os
import json

def create_course_structure():
    structure = {
        ".github": ["AI_TEACHER_PROMPT.md"],
        ".vscode": ["settings.json"],
        "tools": [
            "generate_structure.py",
            "current_session.json",
            "course_manifest.json"
        ],
        "tools/hooks": ["pre-push"],
        "tools/proposed_topics": [],
        "01-html/01-intro": ["theory.md", "assignment.md", "index.html"],
        "01-html/02-elements": ["theory.md", "assignment.md", "index.html"],
        "02-css/01-selectors": ["theory.md", "assignment.md", "index.html", "style.css"],
        "02-css/02-box-model": ["theory.md", "assignment.md", "index.html", "style.css"],
        "03-javascript/01-variables": ["theory.md", "assignment.md", "script.js"],
        "03-javascript/02-dom-manipulation": ["theory.md", "assignment.md", "index.html", "script.js"],
    }
    
    current_script_path = os.path.abspath(__file__)
    with open(current_script_path, "r", encoding="utf-8") as current_file:
        script_content = current_file.read()

    if not os.path.exists("README.md"):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write("# AI-Driven Web Development Course\n\nДобре дошли! Моля, прочетете инструкциите в `.github/AI_TEACHER_PROMPT.md`, за да стартирате с вашия AI учител.")
        print("📁 Създаден коренен файл: README.md")

    for folder, files in structure.items():
        os.makedirs(folder, exist_ok=True)
        print(f"📁 Създадена папка: {folder}")
        
        for file in files:
            file_path = os.path.join(folder, file)
            
            if folder == "tools" and file == "generate_structure.py":
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(script_content)
                print(f"  💾 Скриптът се самокопира в: {file_path}")
                continue

            if folder == "tools/hooks" and file == "pre-push":
                if not os.path.exists(file_path):
                    hook_content = (
                        "#!/bin/sh\n"
                        "# Защита от директен push в main бранча\n"
                        "while read local_ref local_sha remote_ref remote_sha\n"
                        "do\n"
                        "    if [ \"$remote_ref\" = \"refs/heads/main\" ]; then\n"
                        "        echo \"❌ [ГРЕШКА] Директният push към бранч 'main' е забранен!\"\n"
                        "        echo \"ℹ️ Превключете към вашия студентски бранч чрез командата от AI учителя.\"\n"
                        "        exit 1\n"
                        "    fi\n"
                        "done\n"
                        "exit 0\n"
                    )
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(hook_content)
                    try:
                        os.chmod(file_path, 0o755)
                    except:
                        pass
                    print(f"  🔒 Създаден защитен Git hook: {file}")
                continue
                
            if folder == "tools" and file == "current_session.json":
                if not os.path.exists(file_path):
                    initial_session = {
                        "schema_version": "1.0.0",
                        "student_name": "Unknown",
                        "current_branch": "main",
                        "last_update_utc": "2026-05-17T12:00:00Z",
                        "current_step_index": 0,
                        "current_lesson_path": "01-html/01-intro",
                        "lesson_state": "not_started",
                        "next_step_action": "prompt_student_for_name",
                        "completed_lessons": [],
                        "mistakes_log": [],
                        "teacher_internal_notes": "Ученикът стартира курса сега. Провери бранча му и го онбордни."
                    }
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(initial_session, f, indent=4, ensure_ascii=False)
                    print(f"  🧠 Създадена локална памет: {file}")
                continue

            if folder == "tools" and file == "course_manifest.json":
                if not os.path.exists(file_path):
                    manifest = {
                        "course_name": "Web Dev за Начинаещи",
                        "course_version": "1.0.0",
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

            if folder == ".vscode" and file == "settings.json":
                if not os.path.exists(file_path):
                    vscode_settings = {
                        "github.copilot.chat.scope": "workspace",
                        "files.exclude": {
                            "**/.git": True,
                            "**/generate_structure.py": False  # ФИКСИРАНО: от false на False
                        }
                    }
                    with open(file_path, "w", encoding="utf-8") as f:
                        json.dump(vscode_settings, f, indent=4, ensure_ascii=False)
                    print(f"  ⚙️ Създадени VS Code настройки: {file}")
                continue

            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    if file.endswith(".md"):
                        # ФИКСИРАНО: Премахнат грешния split().upper()
                        clean_title = folder.split('/')[-1].replace('-', ' ').upper()
                        f.write(f"# {clean_title}\n")
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
    print("✅ Системата е 100% стабилна и готова!")
