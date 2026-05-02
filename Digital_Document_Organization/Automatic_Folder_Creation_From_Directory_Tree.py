"""
📂 Auto Folder Architect 🚀
----------------------------------------

✨ PURPOSE:
This script reads a directory tree structure from a text file and
automatically creates the same folder hierarchy on your system.

It is especially useful for:
- 📑 Organizing official documents
- 🎓 Structuring academic files
- 💻 Managing project directories
- 🗂️ Recreating predefined folder systems quickly

----------------------------------------

📥 INPUT FORMAT (Text File Example):

01-Official_Documents
├── 01-Personal
│   ├── 01-Identity
│   │   ├── 01-Aadhar
│   │   ├── 02-Pan_Card

----------------------------------------

⚙️ HOW IT WORKS:

1. Reads each line of the file
2. Calculates indentation level based on tree symbols (│, ├──, └──)
3. Maintains a stack to track parent directories
4. Creates folders using os.makedirs()

----------------------------------------

📌 USAGE:

1. Save your folder structure in a text file (e.g., structure.txt)
2. Run:
   python 📂_AutoFolderArchitect.py structure.txt

3. Output will be created in the current directory

----------------------------------------

⚠️ NOTES:

- Only directories are created (no files)
- Existing folders are skipped safely
- Make sure indentation format is consistent

----------------------------------------

💡 TIP:
You can customize the base directory easily inside the script.

----------------------------------------

👩‍💻 Author: Madhurima Rawat
🌟 Keep building amazing systems!
"""

import os
import sys


def create_structure_from_file(file_path, base_dir="."):
    stack = []  # Keeps track of directory hierarchy

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # Clean line
            line = line.rstrip("\n")
            if not line.strip():
                continue

            # Count indentation level
            level = line.count("│   ")

            # Remove tree symbols to get folder name
            name = (
                line.replace("│   ", "").replace("├── ", "").replace("└── ", "").strip()
            )

            # Adjust stack to current level
            stack = stack[:level]
            stack.append(name)

            # Create full path
            path = os.path.join(base_dir, *stack)

            # Create directory
            os.makedirs(path, exist_ok=True)
            print(f"✅ Created: {path}")


if __name__ == "__main__":

    file_path = input("Enter Directory Tree Text File Path: ")
    create_structure_from_file(file_path)
