from state.state import CodeGenState
import docx  # install: pip install python-docx
import os

def read_srd(state: CodeGenState) -> CodeGenState:
    # Path to your SRD file
    # srd_file_path = "PythonGenai.docx"
    srd_file_path = os.path.join("upload", "PythonGenAI.docx")

    # Check if the file exists
    if not os.path.exists(srd_file_path):
        raise FileNotFoundError(f"The file at {srd_file_path} does not exist.")
    
    # Read the DOCX file
    doc = docx.Document(srd_file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    # Join all paragraphs into one text
    srd_text = "\n".join(full_text)

    # Update the state with the extracted text
    return state.model_copy(update={"srt_text": srd_text})
