from state.state import CodeGenState
from utils.llm import llm

def generate_code(state: CodeGenState) -> CodeGenState:
    prompt = f"""
    You are a software Engineer.
    Based on the following Software Requirement Documents (SRD),
    Generate a clean, production-ready code base with all best practices
    SRD:
    {state.srt_text}"""

    response = llm.invoke(prompt)
    return state.copy(update={"generate_code": response.content})