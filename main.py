import json
import os
from datetime import datetime
from state.state import CodeGenState
from utils.llm import llm
from langgraph.graph import END, StateGraph
from nodes.read_srd import read_srd
from nodes.generate_code import generate_code
from nodes.review_code import review_code
from nodes.test_code import test_code
from nodes.zip_code import zip_code

# Create necessary folders
os.makedirs("logs", exist_ok=True)
os.makedirs("output", exist_ok=True)
os.makedirs("upload", exist_ok=True)

# Create the StateGraph
workflow = StateGraph(CodeGenState)
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

# Compile the workflow
compiled_app = workflow.compile()

print("✅ Workflow compilation completed successfully.")


def run_workflow(uploaded_filename: str):
    """
    Run the langgraph workflow with the uploaded SRD filename.
    """
    # Initialize state with uploaded filename
    initial_state = CodeGenState(uploaded_filename=uploaded_filename)

    # Run workflow
    final_state = compiled_app.invoke(initial_state)

    print("✅ Workflow execution completed.")
    print(f"🔍 Final State:\n{final_state}")

    # Save final state to logs
    final_state_dict = final_state.__dict__
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"logs/final_state_{timestamp}.json"

    with open(log_filename, "w") as log_file:
        json.dump(final_state_dict, log_file, indent=4)

    print(f"📜 Final state has been logged to {log_filename}")

    return {
        "final_state": final_state_dict,
        "generated_zip": final_state.zip_code,  # Assuming you save zip file path in state
        "log_file": log_filename
    }
