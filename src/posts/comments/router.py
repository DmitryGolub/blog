from src.posts.router import router


@router.post("/comments")
async def add_comment():
    ...
