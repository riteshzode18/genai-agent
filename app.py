from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
from main import run_workflow

app = FastAPI(
    title="LangGraph SRD Processor",
    description="Upload SRD .docx file → Generates project using LangGraph",
    version="1.0.0"
)

# Ensure upload directory exists
os.makedirs("upload", exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Hello World 🌟"}


@app.post("/upload/")
async def upload_srd(file: UploadFile = File(...)):
    try:
        # Save uploaded file into 'upload' folder
        file_location = os.path.join("upload", file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run the LangGraph workflow
        result = run_workflow(uploaded_filename=file.filename)

        return JSONResponse(
            content={
                "message": "✅ File uploaded and workflow executed successfully.",
                "final_state_summary": result["final_state"],
                "generated_zip_file": result["generated_zip"],
                "log_file_path": result["log_file"]
            },
            status_code=200
        )

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
