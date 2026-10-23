from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    load_text = await file.read()

    content = []

    for text in load_text.decode("utf-8").splitlines():
        content.append(text)

    return content