
from fastapi import APIRouter, UploadFile, File
from hashlib import sha1

router = APIRouter(prefix="/api", tags=["school_vision"])

@router.post("/school/risk")
async def school_risk(file: UploadFile = File(...)):
    content = await file.read()
    h = int(sha1(content).hexdigest()[:6], 16)
    violations = []
    if h % 3 == 0: violations.append({"type":"double_parking","count":1})
    if h % 5 == 0: violations.append({"type":"u_turn","count":1})
    if h % 7 == 0: violations.append({"type":"unsafe_crossing","count":1})
    return {"filename": file.filename, "violations": violations, "note": "stub model — replace with real detector"}
