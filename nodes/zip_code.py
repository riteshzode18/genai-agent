import os
import zipfile
from state.state import CodeGenState
import shutil

def zip_code(state: CodeGenState) -> CodeGenState:
    """
    Zip the 'generated_project' folder, save the zip in 'upload' folder, and delete the original folder.
    """
    base_dir = "generated_project"
    upload_dir = "output"
    zip_file_path = os.path.join(upload_dir, "generated_project.zip")

    # Ensure upload directory exists
    os.makedirs(upload_dir, exist_ok=True)

    # Create zip file
    with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, base_dir)
                zipf.write(file_path, arcname)

    # Delete the original folder
    shutil.rmtree(base_dir)

    return state.model_copy(update={"zip_code": zip_file_path})