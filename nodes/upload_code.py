from state.state import CodeGenState
import os

def upload_code(state: CodeGenState) -> CodeGenState:
    """
    Write the generated code into files, creating any missing folders or files as needed.
    """

    base_dir = "generated_project"
    generated_code = state.generate_code  # {file_path: code}

    for file_path, code in generated_code.items():
        if not isinstance(code, str):
            continue

        full_path = os.path.join(base_dir, file_path)
        dir_path = os.path.dirname(full_path)
        os.makedirs(dir_path, exist_ok=True)  # Ensure directory exists

        with open(full_path, "w") as f:
            f.write(code)

    print("PROJECT CREATED AND UPLOADED SUCCESSFULLY")
    return state.model_copy(update={"uploaded_code": generated_code})