import json
import os
from state.state import CodeGenState
from utils.llm import llm
from langgraph.graph import END, StateGraph
from nodes.read_srd import read_srd
from nodes.generate_code import generate_code
from nodes.review_code import review_code
from nodes.test_code import test_code
from nodes.zip_code import zip_code
from datetime import datetime

# Create the logs & output folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")
if not os.path.exists("output"):
    os.makedirs("output")


# Create the StateGraph
workflow = StateGraph(CodeGenState)

# Add all nodes
workflow.add_node("ReadSRD", read_srd)
workflow.add_node("GenerateCode", generate_code)
workflow.add_node("ReviewCode", review_code)
workflow.add_node("TestCode", test_code)
workflow.add_node("ZipCode", zip_code)

# Define the flow
workflow.set_entry_point("ReadSRD")
workflow.add_edge("ReadSRD", "GenerateCode")
workflow.add_edge("GenerateCode", "ReviewCode")
workflow.add_edge("ReviewCode", "TestCode")
workflow.add_edge("TestCode", "ZipCode")
workflow.add_edge("ZipCode", END)

# After compiling
app = workflow.compile()

print("✅ Workflow compilation completed successfully.")

# RUN the workflow
initial_state = CodeGenState()  # <-- Empty state
final_state = app.invoke(initial_state)

print("✅ Workflow execution completed.")
print(f"🔍 Final State:\n{final_state}")

# Prepare the log data (convert the state to JSON format for readability)
final_state_dict = final_state.__dict__  # Convert the final state to a dictionary
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"logs/final_state_{timestamp}.json"

# Log the final state to a JSON file in the 'logs' folder
with open(log_filename, "w") as log_file:
    json.dump(final_state_dict, log_file, indent=4)

print(f"📜 Final state has been logged to {log_filename}")
