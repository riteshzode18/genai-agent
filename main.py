from state.state import CodeGenState
from utils.llm import llm


# response = llm.invoke("Hey GroqAI, Good Morning!")
# print(response.content)


from langgraph.graph import END, StateGraph, START
from nodes.generate_code import generate_code
from nodes.review_code import review_code
from nodes.test_code import test_code
from nodes.zip_code import zip_code
from nodes.read_srd import read_srd


workflow = StateGraph(CodeGenState)


# Add the nodes

workflow.add_node("ReadSRD", read_srd)
workflow.add_node("GenerateCode", generate_code)
workflow.add_node("ReviewCode", review_code)
workflow.add_node("TestCode", test_code)
workflow.add_node("ZipCode", zip_code)


workflow.set_entry_point("ReadSRD")
workflow.add_edge("ReadSRD", "GenerateCode")
workflow.add_edge("GenerateCode", "ReviewCode")
workflow.add_edge("ReviewCode", "TestCode")
workflow.add_edge("TestCode", "ZipCode")
workflow.add_edge("ZipCode", END)

app = workflow.compile()

print("completed")


