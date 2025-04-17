# zip_code.py

import os
import zipfile
from state.state import CodeGenState
import tempfile

def zip_code(state: CodeGenState) -> CodeGenState:
    # Make sure the output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Create a temporary directory to hold the code file
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Write the generated code into a Python file
        code_file_path = os.path.join(tmpdirname, "generated_code.py")
        with open(code_file_path, "w") as f:
            f.write(state.generate_code or "# No code generated")

        # Now create a zip file
        zip_file_path = os.path.join(output_dir, "generated_code_bundle.zip")
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(code_file_path, arcname="generated_code.py")

    print(f"✅ Zip file saved at: {zip_file_path}")

    # You can also update the state if needed (optional)
    return state.model_copy(update={"zip_code": zip_file_path})
