from state.state import CodeGenState
from utils.llm import llm

def generate_code(state: CodeGenState) -> CodeGenState:

    prompt = f"""
    You are a highly skilled and experienced Software Engineer.
    Your task:
    - Carefully read the following Software Requirements Document (SRD).
    - Generate a clean, modular, production-ready codebase based on the SRD.
    - Follow industry best practices, including proper structure, naming conventions, error handling, and security.
    - Prioritize code readability, scalability, and maintainability.
    - If necessary, create multiple files/modules logically.
    - Use modern standards and frameworks where appropriate.

    Software Requirements Document (SRD):
    {state.srt_text}

    Respond only with the complete code. Do not add any extra explanation.
    """

    response = llm.invoke(prompt)
    return state.model_copy(update={"generate_code": response.content})