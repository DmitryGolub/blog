from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def home_page():
    return {"Hello": "World"}
