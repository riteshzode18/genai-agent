from state.state import CodeGenState
from utils.llm import llm
import os
import json
import re

# Function to create the folder structure
def create_structure(base_path, structure):
    for key, value in structure.items():
        current_path = os.path.join(base_path, key)
        if isinstance(value, dict) and value:  # Non-empty dictionary -> Folder
            os.makedirs(current_path, exist_ok=True)
            create_structure(current_path, value)
        elif isinstance(value, dict) and not value:  # Empty dictionary -> File
            if key in ["Dockerfile", "README.md", "requirements.txt", ".env"] or key.endswith(".py"):
                # Treat as a file if it matches specific filenames or ends with .py
                with open(current_path, "w") as f:
                    f.write(f"# Boilerplate code for {key}")  # Add boilerplate code
            else:
                raise ValueError(f"Unexpected empty dictionary for key: {key}")
        else:
            raise ValueError(f"Unexpected structure format for key: {key}, value: {value}")

def project_structure(state: CodeGenState) -> CodeGenState:
    """
    Generate a modular FastAPI project structure, create the corresponding files and folders,
    and generate unit tests for the code.
    """

    prompt = f"""
    You are a highly skilled Software Engineer and an expert in FastAPI development.
    The project structure must be generated based on the following Software Requirements Document (SRD).

    Software Requirements Document (SRD):
    {state.srt_text}

    Your task:
    - Generate a modular project structure for a FastAPI application based on the SRD.
    - The structure should include folders for API routes, models, services, and tests.
    - Include essential files like Dockerfile, requirements.txt, .env, and README.md.
    - Ensure the structure adheres to best practices for FastAPI projects, including scalability, maintainability, and security.

    **Output Requirements:**
    - Provide the project structure in JSON format only, without any additional text or explanation.
    - The JSON structure must strictly match the folder and file hierarchy described below.

    
    **Sample Folder Structure:**
    project_root/
    │── app/
    │   ├── api/
    │   │   ├── routes/
    │   │   │   ├── user.py
    │   │   │   ├── item.py
    │   │   │   └── __init__.py
    │   ├── models/
    │   │   ├── user.py
    │   │   ├── item.py
    │   │   └── __init__.py
    │   ├── services/
    │   ├── database.py
    │   ├── main.py
    │── tests/
    │── Dockerfile
    │── requirements.txt
    │── .env
    │── README.md


    """

    # Invoke the LLM to get the project structure
    response = llm.invoke(prompt)

    # Use regular expression to extract the JSON part from the response
    json_match = re.search(r"\{.*\}", response.content, re.DOTALL)
    if not json_match:
        raise ValueError(f"Failed to extract JSON from LLM response: {response.content}")

    folder_structure = json.loads(json_match.group())  # Parse the extracted JSON
    print(folder_structure)  # Debugging: Print the folder structure
    # Base directory for the project


    # Example usage
    base_dir = "/workspaces/genai-agent/generated_project"

    # Create the folder structure
    create_structure(base_dir, folder_structure)
        # Update the state with the generated structure
    state = state.model_copy(update={"structure": folder_structure})

    return state