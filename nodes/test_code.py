from state.state import CodeGenState
from utils.llm import llm


def test_code(state: CodeGenState) -> CodeGenState:
    prompt = f"""
    You are a highly experienced software Engineer and code tester.
    Give the following code, generate a few unit test cases using pytest framework.
    Also mention any potential bugs or issue you find
    Code:
    {state.generate_code}"""

    response = llm.invoke(prompt)
    return state.model_copy(update={"test_result": response.content})