from state.state import CodeGenState
from utils.llm import llm

def test_code(state: CodeGenState) -> CodeGenState:

    prompt = f"""
    You are a highly skilled Software Engineer and expert in writing unit tests.
    Your task:
    - Review the following code carefully.
    - Generate comprehensive unit tests using the pytest framework.
    - Ensure the tests cover critical paths, edge cases, and error handling.
    - If you identify any potential bugs, bad practices, or hidden issues, list them separately after the tests.

    Code to test:
    {state.generate_code}

    Respond only with the complete test code first, followed by any issues (if found).
    """

    response = llm.invoke(prompt)
    return state.model_copy(update={"test_code": response.content})