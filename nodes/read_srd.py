from state.state import CodeGenState
from utils.llm import llm

def read_srd(state: CodeGenState) -> CodeGenState:

    file_path = "../upload/PythonGenai.docx"

    with open(file_path, mode="r") as f:
        srd_text = f.read()

    prompt = f"""
        You are a highly experienced software Engineer.
        Based on the following Software Requirement Documents (SRD),
        Generate a clean, production-ready code base with all best practices
        SRD:
        {srd_text}"""

    response = llm.invoke(prompt)

    return state.model_copy(update={"srt_text": response.content})