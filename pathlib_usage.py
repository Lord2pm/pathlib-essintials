from pathlib import Path
import shutil

BASE_DIR = Path.cwd()
FILES_DIR = BASE_DIR / "files"
FILES_DIR.mkdir(exist_ok=True)

for path_object in FILES_DIR.iterdir():
    if path_object.is_file():
        new_folder = FILES_DIR / path_object.suffix.replace(".", "").upper()
        new_folder.mkdir(exist_ok=True)
        shutil.move(path_object, new_folder)
