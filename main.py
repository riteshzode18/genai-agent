from state.state import CodeGenState
from utils.llm import llm


response = llm.invoke("Hey GroqAI, Good Morning!")
print(response.content)

