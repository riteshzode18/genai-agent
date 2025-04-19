from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

## State class for tracking SRE input, generate code, review, test result, and zip file

class CodeGenState(BaseModel):
    srt_text: Optional[str] = None
    generate_code: Optional[str] = None
    add_code: Optional[str] = None
    test_code: Optional[str] = None
    zip_code: Optional[str] = None
    structure: Optional[str] = None
