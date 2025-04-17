from state.state import CodeGenState
from utils.llm import llm

def review_code(state: CodeGenState) -> CodeGenState:

    prompt = f"""
    You are a highly experienced software Engineer and code reviewer.
    Carefully review the following code based on:
    - Code correctness
    - Readability and structure
    - Performance optimization
    - security vulnerabilities
    - Adherence to best coding practices
    
    Provide:
    1. A summary of your feedback.
    2. A list of specific improvements or corrections
    3. A final improve version of the code (if possible)
    
    Code to review:
    {state.generate_code}"""

    response = llm.invoke(prompt)
    return state.model_copy(update={"reviewed_code": response.content})