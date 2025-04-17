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
    """

    # prompt = f"""
    # You are a highly skilled and experienced Software Engineer tasked with generating a clean, modular, and production-ready codebase.
    #
    # **Your Goal:** Based on the following Software Requirements Document (SRD), produce well-structured, maintainable, and scalable code adhering to industry best practices.
    #
    # **Key Considerations:**
    #
    # - **Code Quality:** Ensure readability, proper naming conventions, comprehensive error handling, and security best practices.
    # - **Modularity:** Break down the codebase into logical modules or files for better organization.
    # - **Scalability:** Design the code with potential future growth and changes in mind.
    # - **Maintainability:** Write clear and well-documented code to facilitate future modifications and debugging.
    # - **Modern Standards:** Utilize contemporary programming paradigms and frameworks where appropriate to enhance efficiency and robustness.
    #
    # **Software Requirements Document (SRD):**
    # {state.srt_text}
    # """

    # prompt = f"""
    #     You are a highly experienced software Engineer to generate quality code.
    #     Based on the following Software Requirement Documents (SRD),
    #     Generate a clean, production-ready code base with all best practices
    #     SRD:
    #     {state.srt_text}"""

    response = llm.invoke(prompt)
    return state.model_copy(update={"generate_code": response.content})
