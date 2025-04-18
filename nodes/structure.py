from state.state import CodeGenState
from utils.llm import llm

def project_structure(state: CodeGenState) -> CodeGenState:

    prompt = f"""
    You are a highly skilled Software Engineer and expert in craeting project structure.
    Your task:
    - Generate a good project structure as per discription 
    Code :
    {state.generate_code}
    """

    response = llm.invoke(prompt)
    return state.model_copy(update={"structure": response.content})