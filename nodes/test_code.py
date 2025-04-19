from state.state import CodeGenState
from utils.llm import llm
import json

def test_code(state: CodeGenState) -> CodeGenState:
    """
    Generate comprehensive unit tests for the provided FastAPI code, identify potential issues, and provide actionable feedback.
    """

    prompt = f"""
    You are a highly skilled Software Engineer and an expert in FastAPI development and testing.
    Your task is to carefully review the provided FastAPI code and project structure, write comprehensive unit tests, and identify any potential bugs or issues.

    **Project Structure:**
    {json.dumps(state.structure, indent=4)}

    **Code to Test:**
    {state.generate_code}

    **Instructions:**
    1. **Write Unit Tests**:
       - Use the `pytest` framework to write unit tests for the provided code.
       - Ensure the tests cover:
         - Critical paths
         - Edge cases
         - Error handling
         - Security-related scenarios (e.g., authentication, authorization)
       - Include setup and teardown methods where necessary.
       - Ensure the tests are modular, readable, and follow best practices.

    2. **Identify Bugs and Issues**:
       - While reviewing the code, identify any potential bugs, bad practices, or hidden issues.
       - List these issues separately after the test code, along with suggestions for fixing them.

    3. **Run the Tests**:
       - Simulate running the generated unit tests and provide the expected results.
       - If any tests fail, explain why and suggest fixes for the underlying issues.

    **Output Format**:
    - Respond with the complete test code first.
    - After the test code, provide a section titled "Identified Issues" with a list of any bugs or issues found.
    - Finally, provide a section titled "Test Results" with the simulated results of running the tests.

    **Example Output Format**:
    ```python
    # Test Code
    <unit test code here>

    # Identified Issues
    1. <Description of the issue>
       - Suggested Fix: <How to fix the issue>
    2. <Description of the issue>
       - Suggested Fix: <How to fix the issue>

    # Test Results
    - Test 1: Passed
    - Test 2: Failed
      - Reason: <Explanation of why the test failed>
      - Suggested Fix: <How to fix the issue>
    ```
    """

    # Invoke the LLM to generate unit tests and identify issues
    response = llm.invoke(prompt)

    # Update the state with the generated test code and feedback
    return state.model_copy(update={"test_code": response.content})