import argparse
import json
import os
import re
from typing import Dict, List


MANIFEST_PATH = "tools/course_manifest.json"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"[^a-z0-9-]", "", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "new-course"


def load_manifest(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_manifest(path: str, data: Dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write("\n")


def ensure_course_does_not_exist(courses: List[Dict], course_id: str) -> None:
    for course in courses:
        if course.get("id") == course_id:
            raise ValueError(f"Course id already exists: {course_id}")


def write_file_if_missing(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def lesson_templates(course_title: str, lesson_number: int, lesson_slug: str) -> Dict[str, str]:
    lesson_title = lesson_slug.replace("-", " ").title()
    lesson_header = f"{lesson_number:02d}-{lesson_slug}"
    base_dir = f"{course_title}/{lesson_header}"

    theory = (
        "# THEORY\n\n"
        f"Този урок е част от курса {course_title}.\n\n"
        "## Цели\n"
        "- Разбиране на основната концепция на урока.\n"
        "- Приложение с кратък пример.\n"
    )

    assignment = (
        "# ASSIGNMENT\n\n"
        f"## Задача: {lesson_title}\n\n"
        "- Опиши решението си стъпка по стъпка.\n"
        "- Изпълни практическата част в подходящия файл.\n"
        "- Подготви кратко обяснение какво научи.\n"
    )

    return {
        f"{base_dir}/theory.md": theory,
        f"{base_dir}/assignment.md": assignment,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new course skeleton and register it in course_manifest.json")
    parser.add_argument("--title", required=True, help="Course title")
    parser.add_argument("--course-id", help="Optional explicit course id")
    parser.add_argument(
        "--lessons",
        default="intro,basics",
        help="Comma-separated lesson slugs, e.g. intro,variables,functions",
    )
    parser.add_argument(
        "--path-prefix",
        help="Optional folder prefix (e.g. 05-dsp). If omitted, computed from course id.",
    )

    args = parser.parse_args()

    if not os.path.exists(MANIFEST_PATH):
        raise FileNotFoundError(f"Manifest not found: {MANIFEST_PATH}")

    manifest = load_manifest(MANIFEST_PATH)
    courses = manifest.get("courses", [])

    course_id = args.course_id or slugify(args.title)
    ensure_course_does_not_exist(courses, course_id)

    lessons = [slugify(x) for x in args.lessons.split(",") if x.strip()]
    if not lessons:
        raise ValueError("At least one lesson is required")

    prefix = args.path_prefix or f"99-{course_id}"
    steps = [f"{prefix}/{index + 1:02d}-{slug}" for index, slug in enumerate(lessons)]

    course_entry = {
        "id": course_id,
        "title": args.title,
        "description": f"Auto-generated course skeleton for {args.title}.",
        "tags": [slugify(args.title), "custom"],
        "entry_lesson_path": steps[0],
        "steps": steps,
    }

    courses.append(course_entry)
    manifest["courses"] = courses
    save_manifest(MANIFEST_PATH, manifest)

    for index, slug in enumerate(lessons, start=1):
        templates = lesson_templates(prefix, index, slug)
        for path, content in templates.items():
            write_file_if_missing(path, content)

    print(f"Created course: {course_id}")
    print(f"Entry lesson: {steps[0]}")


if __name__ == "__main__":
    main()
