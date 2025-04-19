import os
import zipfile

def zip_code(base_dir, zip_file_path):
    """
    Create a zip file of the given directory.
    """
    with zipfile.ZipFile(zip_file_path, "w") as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, base_dir))