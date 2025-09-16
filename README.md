# 🗂️ Obsidian Project Note Extractor

A one-time Python utility to recursively scan your `Node Projects` folder, extract each project's `README.md`, and convert it into an Obsidian-compatible note with metadata and safe naming.

## 📦 Features

- 🔍 Recursively finds all `README.md` files in nested project folders  
- 📝 Renames each file to match its parent folder name  
- 🛡️ Avoids overwriting by versioning duplicate filenames  
- 🧠 Adds Obsidian-friendly YAML frontmatter with tags and folder path  
- 📄 Logs skipped folders (missing README or errors) for audit trail

## 📁 Folder Structure Example

```
Node Projects/
├── game/
│   ├── offline games/
│   │   ├── chess/
│   │   │   └── README.md
│   │   ├── sudoku/
│   │   │   └── README.md
```

Each `README.md` becomes:

```
ObsidianVault/Projects/
├── chess.md
├── sudoku.md
```

## ⚙️ Usage

1. Update the paths in the script:
   ```python
   source_root = "/path/to/Node Projects"
   destination_root = "/path/to/ObsidianVault/Projects"
   ```

2. Run the script:
   ```bash
   python extract_notes.py
   ```

3. Check `skipped_folders.log` in the destination folder for any skipped entries.

## 🧩 Frontmatter Example

```yaml
---
title: "chess"
tags: [project, source:github]
folder_source: "game/offline games/chess"
created: 2025-09-16
---
```

## 🚀 Future Enhancements

- CLI flags for source/destination paths  
- Optional markdown cleanup (e.g., strip badges)  
- Auto-tagging based on folder hierarchy  
- Integration with Obsidian plugin workflows

## 🛠️ Author

Built by [Hridoy](https://github.com/your-profile), founder and systems architect at Varabit.  
Designed for modular reuse, clean onboarding, and frictionless knowledge capture.
