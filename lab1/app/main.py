from fastapi import FastAPI
from starlette.responses import FileResponse 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/landing")
def landing_page():
    return FileResponse("static/page1.html")