from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil

# Initialize FastAPI app
app = FastAPI(
    title="SRD Upload API",
    description="Upload Software Requirements Document (SRD) to the server.",
    version="1.0.0"
)

# Create upload folder if it doesn't exist
UPLOAD_FOLDER = "upload"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(content={
            "message": "✅ File uploaded successfully!",
            "filename": file.filename
        }, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ File upload failed. Error: {str(e)}")

@app.get("/")
def hello_world():
    return {"message": "hello world"}

# uvicorn server:app --reload










