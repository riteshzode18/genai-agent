import os
import tempfile
import zipfile
from state.state import CodeGenState

def zip_code(state: CodeGenState) -> CodeGenState:
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Path to save the code file temporarily
        code_file_path = os.path.join(temp_dir, "main.py")

        # Write the generated code to a temporary file
        with open(code_file_path, "w") as f:
            f.write(state.generate_code or "# No code generated.")

        # Make sure 'output' folder exists
        os.makedirs("output", exist_ok=True)

        # Define final zip path inside the 'output' folder
        final_zip_path = os.path.join("output", "code_archive.zip")

        # Create the ZIP file inside 'output'
        with zipfile.ZipFile(final_zip_path, "w") as zipf:
            zipf.write(code_file_path, arcname="main.py")

    # Update the state with the path to the output zip file
    return state.model_copy(update={"zip_code": final_zip_path})
