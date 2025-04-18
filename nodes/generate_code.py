from state.state import CodeGenState
from utils.llm import llm
import json
import re

def clean_and_save_json(input_string, output_file="cleaned_data.json"):
    try:
        # Use a regular expression to extract the JSON content
        json_match = re.search(r'\{.*\}', input_string, re.DOTALL)
        if not json_match:
            raise ValueError("No valid JSON found in the input string.")

        # Extract the matched JSON string
        json_string = json_match.group(0)

        # Replace invalid escape sequences and fix common issues
        json_string = json_string.replace("\\n", "\n").replace("\\t", "\t").replace("\\'", "'").replace('"{', '{').replace('}"', '}')

        # Remove invalid control characters
        json_string = re.sub(r'[\x00-\x1F]+', '', json_string)

        # Attempt to parse the cleaned JSON string
        try:
            json_data = json.loads(json_string)
        except json.JSONDecodeError as e:
            # If direct parsing fails, try more aggressive cleaning
            json_string = re.sub(r'\\(?=[{}])', '', json_string)  # Remove backslashes before curly braces
            json_string = re.sub(r'"([^"]*)": "([^"]*)"', r'"\1": "\2"', json_string)  # Remove extra quotes
            json_data = json.loads(json_string)

        # Save the cleaned JSON to a file
        with open(output_file, "w") as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"JSON data cleaned and saved to '{output_file}'.")
        return json_data

    except (json.JSONDecodeError, ValueError, TypeError) as e:
        print(f"Failed to parse JSON: {e}")
        return None

def generate_code(state: CodeGenState) -> CodeGenState:
    """
    Generate a clean, modular, and production-ready FastAPI codebase based on the provided project structure and Software Requirements Document (SRD).
    """

    prompt = f"""
    You are an expert Software Engineer specializing in FastAPI. Your objective is to generate a complete, high-quality, and production-ready FastAPI codebase that adheres to the provided project structure and Software Requirements Document (SRD). The output MUST be a valid JSON.

    **Software Requirements Document (SRD):**
    {state.srt_text}

    **Project Structure:**
    {state.structure}

    **Instructions:**

    1.  **Code Generation**: Generate code for each file specified in the project structure. Ensure each file's code fulfills its intended purpose within the application.
    2.  **FastAPI Best Practices**: Adhere to FastAPI best practices, including:

        *   Comprehensive error handling with informative error messages.
        *   Strict input validation using Pydantic models.
        *   Robust security measures (authentication, authorization, data validation).
        *   Modular, scalable, and maintainable design.
    3.  **File-Specific Guidelines**:

        *   `__init__.py`: Add boilerplate code as needed.
        *   API Route Files:
            *   Define API endpoints with appropriate HTTP methods (GET, POST, PUT, DELETE).
            *   Include example request and response models.
        *   Model Files:
            *   Define Pydantic models for request and response validation.
            *   Use SQLAlchemy ORM models for database integration where necessary.
        *   Service Files: Implement business logic functions.
        *   `main.py`:
            *   Set up the FastAPI application instance.
            *   Include routers.
            *   Configure middleware (CORS, logging, etc.).
        *   `database.py`:
            *   Configure the database connection using SQLAlchemy.
            *   Implement connection pooling.
            *   Set up database migrations using Alembic.
        *   `tests/`:
            *   Generate comprehensive unit tests using pytest.
            *   Cover critical paths, edge cases, and error handling scenarios.
    4.  **Output Format**: Return the generated code as a single, valid JSON object. The JSON object's structure MUST strictly match the provided project structure. Each key in the JSON object represents a file path, and its corresponding value is the complete code for that file.

    **Example Output Format:**
    ```json
    {{
        "app/api/routes/user.py": "from fastapi import APIRouter\\n\\nrouter = APIRouter()\\n\\n@router.get('/users')\\ndef get_users():\\n    return {{\\'message\\': \\'List of users\\'}}",
        "app/models/user.py": "from pydantic import BaseModel\\n\\nclass User(BaseModel):\\n    id: int\\n    name: str\\n    email: str",
        "app/main.py": "from fastapi import FastAPI\\nfrom app.api.routes.user import router as user_router\\n\\napp = FastAPI()\\n\\napp.include_router(user_router, prefix='/users')",
        "app/database.py": "from sqlalchemy import create_engine\\nfrom sqlalchemy.orm import sessionmaker\\n\\nDATABASE_URL = \\'postgresql://user:password@localhost/db\\'\\nengine = create_engine(DATABASE_URL)\\nSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)",
        "tests/test_user_routes.py": "import pytest\\nfrom fastapi.testclient import TestClient\\nfrom app.main import app\\n\\nclient = TestClient(app)\\n\\ndef test_get_users():\\n    response = client.get('/users')\\n    assert response.status_code == 200\\n    assert response.json() == {{\\'message\\': \\'List of users\\'}}"
    }}
    ```

    **IMPORTANT: Your entire output MUST be a valid JSON object representing the complete codebase. Ensure that the JSON is well-formed and that all code strings are properly escaped.**
    """

    # Invoke the LLM to generate the code
    response = llm.invoke(prompt)

    # Extract the content from the response object
    input_string = response.content


    print(f"Response from LLM: {input_string}")
    # Update the state with the cleaned JSON
    return state.model_copy(update={"generate_code": input_string})