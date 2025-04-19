# # from state.state import CodeGenState
# # from utils.llm import llm
# # import json
# # import re

# # def clean_and_parse_generated_code(response_content: str) -> dict:
# #     """
# #     Extract and parse the JSON part of the response content using a regular expression.
# #     """
# #     try:
# #         # Remove ```json and ``` if present
# #         response_content = response_content.replace("```json", "").replace("```", "").strip()

# #         # Use a regular expression to extract the JSON part
# #         json_match = re.search(r"\{.*\}", response_content, re.DOTALL)
# #         if not json_match:
# #             raise ValueError("Failed to extract JSON from the response content.")

# #         # Extract the JSON string
# #         json_string = json_match.group()

# #         # Replace escaped newlines, tabs, and single quotes
# #         json_string = json_string.replace("\\n", "\n").replace("\\t", "\t").replace("\\'", "'")

# #         # Replace single quotes with double quotes (JSON requires double quotes)
# #         json_string = json_string.replace("'", "\"")

# #         # Remove invalid control characters
# #         json_string = re.sub(r'[\x00-\x1F]+', '', json_string)

# #          # Replace escaped forward slashes
# #         json_string = json_string.replace("\\/", "/")

# #         # Attempt to parse the extracted JSON
# #         parsed_json = json.loads(json_string)
# #         return parsed_json
# #     except json.JSONDecodeError as e:
# #         print(f"Failed to parse JSON: {e}")
# #         print(f"Failing JSON String: {json_string}")  # Print the string that failed to parse
# #         raise ValueError(f"Failed to parse extracted JSON: {e}")

# # def generate_code(state: CodeGenState) -> CodeGenState:
# #     """
# #     Generate a clean, modular, and production-ready FastAPI codebase based on the provided project structure and Software Requirements Document (SRD).
# #     """

# #     prompt = f"""
# #     You are a highly skilled Software Engineer and an expert in FastAPI development.
# #     Your task is to generate a clean, modular, and production-ready FastAPI codebase based on the provided project structure and Software Requirements Document (SRD).

# #     **Software Requirements Document (SRD):**
# #     {state.srt_text}

# #     **Instructions:**
# #     1. **Understand the Project Structure**:
# #        - Carefully review the provided project structure.
# #        - Understand the purpose of each file and folder in the structure.

# #     2. **Generate Code**:
# #        - Generate code for each file in the structure based on its purpose.
# #        - Ensure the code adheres to FastAPI best practices, including:
# #          - Proper error handling with meaningful error messages.
# #          - Input validation using Pydantic models.
# #          - Security best practices (e.g., authentication, authorization, and data validation).
# #          - Scalability and maintainability with modular and reusable components.
# #        - Add boilerplate code where necessary (e.g., `__init__.py` files).
# #        - For API route files:
# #          - Define endpoints with example request/response models.
# #          - Include proper HTTP methods (GET, POST, PUT, DELETE) where applicable.
# #        - For model files:
# #          - Define Pydantic models for request/response validation.
# #          - Use SQLAlchemy ORM models for database integration where needed.
# #        - For service files:
# #          - Implement business logic functions.
# #        - For `main.py`:
# #          - Set up the FastAPI application.
# #          - Include routers and configure middleware (e.g., CORS, logging).
# #        - For `database.py`:
# #          - Configure the database connection and ORM setup.
# #          - Include connection pooling and migrations using Alembic.
# #        - For `tests/`:
# #          - Generate example unit tests using `pytest`.
# #          - Cover critical paths, edge cases, and error handling.

# #     3. **Output Requirements**:
# #        - Return the generated code for the entire project in JSON format.
# #        - The JSON structure must strictly match the provided project structure.
# #        - Each key in the JSON should represent a file path, and the value should be the corresponding code for that file.

# #     **Project Structure:**
# #     {state.structure}

# #     **Example Output Format**:
# #     json
    
# #         "app/api/routes/user.py": "from fastapi import APIRouter\\n\\nrouter = APIRouter()\\n\\n@router.get('/users')\\ndef get_users():\\n    return {{'message': 'List of users'}}",
# #         "app/models/user.py": "from pydantic import BaseModel\\n\\nclass User(BaseModel):\\n    id: int\\n    name: str\\n    email: str",
# #         "app/main.py": "from fastapi import FastAPI\\nfrom app.api.routes.user import router as user_router\\n\\napp = FastAPI()\\n\\napp.include_router(user_router, prefix='/users')",
# #         "app/database.py": "from sqlalchemy import create_engine\\nfrom sqlalchemy.orm import sessionmaker\\n\\nDATABASE_URL = 'postgresql://user:password@localhost/db'\\nengine = create_engine(DATABASE_URL)\\nSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)",
# #         "tests/test_user_routes.py": "import pytest\\nfrom fastapi.testclient import TestClient\\nfrom app.main import app\\n\\nclient = TestClient(app)\\n\\ndef test_get_users():\\n    response = client.get('/users')\\n    assert response.status_code == 200\\n    assert response.json() == {{'message': 'List of users'}}"
    

# #     **Your Task**:
# #     - Populate the files in the project structure with appropriate code.
# #     - Ensure the generated code is clean, modular, and ready for deployment.
# #     - Return the entire generated code in JSON format as described above.
# #       only in json format
# #     """

# #     # Invoke the LLM to generate the code
# #     response = llm.invoke(prompt)
# #     print("Response Content:", str(response.content))
# #     generated_code = response.content

# #     # Clean and parse the generated code
# #     # try:
# #     #     generated_code = clean_and_parse_generated_code(generated_code)
# #     # except ValueError as e:
# #     #     raise ValueError(f"Error while processing the response: {e}")

# #     # print(json.dumps(generated_code, indent=2))    
# #     print("CODE GENARTED")
# #     # Update the state with the generated code
# #     return state.model_copy(update={"generate_code": generated_code})


# from state.state import CodeGenState
# from utils.llm import llm
# import json
# import re

# # def clean_and_parse_generated_code(response_content: str) -> dict:
# #     """
# #     Extract and parse the JSON part of the response content using a regular expression.
# #     """
# #     try:
# #         # Remove ```json and ``` if present
# #         response_content = response_content.replace("```json", "").replace("```", "").strip()

# #         # Use a regular expression to extract the JSON part
# #         json_match = re.search(r"\{.*\}", response_content, re.DOTALL)
# #         if not json_match:
# #             raise ValueError("Failed to extract JSON from the response content.")

# #         # Extract the JSON string
# #         json_string = json_match.group()

# #         # Replace escaped newlines, tabs, and single quotes
# #         json_string = json_string.replace("\\n", "\n").replace("\\t", "\t").replace("\\'", "'")

# #         # Replace single quotes with double quotes (JSON requires double quotes)
# #         json_string = json_string.replace("'", "\"")

# #         # Remove invalid control characters
# #         json_string = re.sub(r'[\x00-\x1F]+', '', json_string)

# #          # Replace escaped forward slashes
# #         json_string = json_string.replace("\\/", "/")

# #         # Attempt to parse the extracted JSON
# #         parsed_json = json.loads(json_string)
# #         return parsed_json
# #     except json.JSONDecodeError as e:
# #         print(f"Failed to parse JSON: {e}")
# #         print(f"Failing JSON String: {json_string}")  # Print the string that failed to parse
# #         raise ValueError(f"Failed to parse extracted JSON: {e}")

# # def generate_code(state: CodeGenState) -> CodeGenState:
# def generate_code(state: CodeGenState) -> CodeGenState:
#     """
#     Generate a clean, modular, and production-ready FastAPI codebase based on the provided project structure and Software Requirements Document (SRD).
#     """

#     # Define the prompt for the LLM
#     prompt = f"""
#     You are a highly skilled Software Engineer and an expert in FastAPI development.
#     Your task is to generate a clean, modular, and production-ready FastAPI codebase based on the provided project structure and Software Requirements Document (SRD).

#     **Software Requirements Document (SRD):**
#     {state.srt_text}

#     **Instructions:**
#     1. **Understand the Project Structure**:
#       - Carefully review the provided project structure.
#       - Understand the purpose of each file and folder in the structure.

#     2. **Generate Code**:
#       - Generate code for each file in the structure based on its purpose.
#       - Ensure the code adheres to FastAPI best practices, including:
#         - Proper error handling with meaningful error messages.
#         - Input validation using Pydantic models.
#         - Security best practices (e.g., authentication, authorization, and data validation).
#         - Scalability and maintainability with modular and reusable components.
#       - Add boilerplate code where necessary (e.g., `__init__.py` files).
#       - For API route files:
#         - Define endpoints with example request/response models.
#         - Include proper HTTP methods (GET, POST, PUT, DELETE) where applicable.
#       - For model files:
#         - Define Pydantic models for request/response validation.
#         - Use SQLAlchemy ORM models for database integration where needed.
#       - For service files:
#         - Implement business logic functions.
#       - For `main.py`:
#         - Set up the FastAPI application.
#         - Include routers and configure middleware (e.g., CORS, logging).
#       - For `database.py`:
#         - Configure the database connection and ORM setup.
#         - Include connection pooling and migrations using Alembic.
#       - For `tests/`:
#         - Generate example unit tests using `pytest`.
#         - Cover critical paths, edge cases, and error handling.

#     3. **Output Requirements**:
#       - Return the generated code for the entire project in JSON format.
#       - The JSON structure must strictly match the provided project structure.
#       - Each key in the JSON should represent a file path, and the value should be the corresponding code for that file.

#     **Project Structure:**
#     {state.structure}

#     **Example Output Format**:
#     json

#         "app/api/routes/user.py": "from fastapi import APIRouter\\n\\nrouter = APIRouter()\\n\\n@router.get('/users')\\ndef get_users():\\n    return {{'message': 'List of users'}}",
#         "app/models/user.py": "from pydantic import BaseModel\\n\\nclass User(BaseModel):\\n    id: int\\n    name: str\\n    email: str",
#         "app/main.py": "from fastapi import FastAPI\\nfrom app.api.routes.user import router as user_router\\n\\napp = FastAPI()\\n\\napp.include_router(user_router, prefix='/users')",
#         "app/database.py": "from sqlalchemy import create_engine\\nfrom sqlalchemy.orm import sessionmaker\\n\\nDATABASE_URL = 'postgresql://user:password@localhost/db'\\nengine = create_engine(DATABASE_URL)\\nSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)",
#         "tests/test_user_routes.py": "import pytest\\nfrom fastapi.testclient import TestClient\\nfrom app.main import app\\n\\nclient = TestClient(app)\\n\\ndef test_get_users():\\n    response = client.get('/users')\\n    assert response.status_code == 200\\n    assert response.json() == {{'message': 'List of users'}}"


#     **Your Task**:
#     - Populate the files in the project structure with appropriate code.
#     - Ensure the generated code is clean, modular, and ready for deployment.
#     - Return the entire generated code in JSON format as described above and parse it so i can use it in my code
#     parsing the json response is very important
#     """

#     # Invoke the LLM to generate the code
#     response = llm.invoke(prompt)
#     # print("Response Content:", str(response.content))
#     generated_code = response.content
#     print("Response Content:", str(generated_code))



#     # import json
#     # import re

#     # def clean_and_parse_llm_json(llm_response: str):
#     #     # Remove code block markers if present
#     #     cleaned = llm_response.strip()
#     #     if cleaned.startswith("```json"):
#     #         cleaned = cleaned[len("```json"):].strip()
#     #     if cleaned.startswith("```"):
#     #         cleaned = cleaned[len("```"):].strip()
#     #     if cleaned.endswith("```"):
#     #         cleaned = cleaned[:-3].strip()

#     #     # Extract the JSON part using regex (in case there is extra text)
#     #     match = re.search(r"\{.*\}", cleaned, re.DOTALL)
#     #     if match:
#     #         cleaned = match.group(0)

#     #     # Remove invalid control characters (ASCII 0-31 except \n, \r, \t)
#     #     cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', cleaned)

#     #     # Parse as JSON
#     #     return json.loads(cleaned)

#     # # Example usage:
#     # llm_response = f"""{str(generated_code)}"""  # Paste your LLM output string here
#     # parsed_json = clean_and_parse_llm_json(llm_response)
#     # print(json.dumps(parsed_json, indent=2))

#     # # Clean and parse the generated code
#     # # try:
#     # #     generated_code = clean_and_parse_generated_code(generated_code)
#     # # except ValueError as e:
#     # #     raise ValueError(f"Error while processing the response: {e}")

#     # print(json.dumps(generated_code, indent=2))    
#     print("CODE GENARTED SUCCESSFULLY")
#     # Update the state with the generated code
#     return state.model_copy(update={"generate_code": generated_code})
#   #     # Update the state with the generated code



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

    Return only JSON like:
    {{
      "app/main.py": "...",
      "app/api/routes/user.py": "...",
      "app/models/user.py": "..."
    }}
    """

    # Invoke the LLM to generate the code
    response = llm.invoke(prompt)

    # Extract the content from the response object
    input_string = response.content

    # clean_and_save_json(input_string)
    # print("file done")
    content = re.sub(r'^```json|```$', '', response.content.strip(), flags=re.MULTILINE)
    try:
        code = json.loads(content)
        # print(code)
    except:
        print("Failed to parse JSON. Attempting to clean and save.")
        # Attempt to clean and save the JSON
        code = clean_and_save_json(input_string)
        if code is None:
            raise ValueError("Failed to clean and parse the JSON response.")

    print(code)
    print("PROJECT CODE GENERATED")

    return state.model_copy(update={"generate_code": code})