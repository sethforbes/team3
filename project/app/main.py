from fastapi import FastAPI
from starlette.responses import FileResponse 
import os

script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/landing")
def landing_page():
    return FileResponse(st_abs_file_path + "page1.html")