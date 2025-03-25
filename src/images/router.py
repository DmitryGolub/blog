import shutil
from fastapi import APIRouter, UploadFile


router = APIRouter(
    prefix="/images",
    tags=["Download images"]
)


@router.post("/posts")
async def add_post_image(name: int, file: UploadFile):
    with open(f"src/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)