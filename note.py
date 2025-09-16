import os
import shutil
from datetime import datetime

# === CONFIG ===
source_root = r"D:\Work\Node Projects"
destination_root = r"D:\Work\Node Projects\Project to Obsidian Note\ObsidianVault\Projects"
log_path = os.path.join(destination_root, "skipped_folders.log")

# === SETUP ===
os.makedirs(destination_root, exist_ok=True)
skipped = []

def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in "-_." else "_" for c in name)

def get_versioned_path(base_path):
    if not os.path.exists(base_path):
        return base_path
    name, ext = os.path.splitext(base_path)
    counter = 1
    while True:
        new_path = f"{name}_{counter}{ext}"
        if not os.path.exists(new_path):
            return new_path
        counter += 1

def build_frontmatter(project_name, relative_path):
    return f"""---
title: "{project_name}"
tags: [project, source:github]
folder_source: "{relative_path}"
created: {datetime.now().strftime('%Y-%m-%d')}
---

"""

# === MAIN ===
for dirpath, dirnames, filenames in os.walk(source_root):
    if "README.md" in filenames:
        readme_path = os.path.join(dirpath, "README.md")
        project_folder_name = os.path.basename(dirpath)
        relative_path = os.path.relpath(dirpath, source_root)
        sanitized_name = sanitize_filename(project_folder_name)
        destination_file = os.path.join(destination_root, f"{sanitized_name}.md")
        destination_file = get_versioned_path(destination_file)

        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()

            frontmatter = build_frontmatter(project_folder_name, relative_path)
            with open(destination_file, "w", encoding="utf-8") as f:
                f.write(frontmatter + content)

            print(f"✅ {project_folder_name}: saved as {os.path.basename(destination_file)}")
        except Exception as e:
            skipped.append(f"{dirpath} — ERROR: {str(e)}")
    else:
        skipped.append(f"{dirpath} — No README.md")

# === LOG SKIPPED ===
if skipped:
    with open(log_path, "w", encoding="utf-8") as log:
        log.write("\n".join(skipped))
    print(f"⚠️ Skipped folders logged to: {log_path}")