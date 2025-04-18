from state.state import CodeGenState
import os

def upload_code(state: CodeGenState) -> CodeGenState:
    """
    Upload the generated code into the created project structure.
    """

    # Base directory for the project
    base_dir = "/workspaces/genai-agent/generated_project"

    # Use `state.generate_code` directly as it is already a dictionary
    generated_code = state.generate_code

    # Write the generated code to the corresponding file paths
    for file_path, code in generated_code.items():
        # Skip directories or invalid entries
        if not isinstance(code, str):
            continue

        # Create the full path for the file
        full_path = os.path.join(base_dir, file_path)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Write the code to the file
        with open(full_path, "w") as f:
            f.write(code)

    # Return the updated state
    return state.model_copy(update={"uploaded_code": generated_code})