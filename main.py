from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import csv
from Functions.process_json import *
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/download", response_class=HTMLResponse)
async def read_download(request: Request):
    return templates.TemplateResponse("download.html", {"request": request})

@app.post("/submit")
async def handle_form(jsonFile: UploadFile = File(...), directoryPath: str = Form(...)):
    json_path = f"json files/{jsonFile.filename}"
    
    # Save the uploaded JSON file
    with open(json_path, "wb") as buffer:
        buffer.write(await jsonFile.read())

    # Call the main function with the obtained JSON file path and directory path
    os.makedirs(directoryPath, exist_ok=True)

    main(json_path, directoryPath)

    return {"message": "Data processed successfully"}

