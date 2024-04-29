from fastapi import APIRouter, Request
from models.notes import Notes
from config.db import conn
from schemas.notes import noteEntity, notesEntity

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

notes = APIRouter()

templates = Jinja2Templates(directory="templates")

@notes.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    docs = conn.Notes.Notes.find({})
    new_docs= []
    for doc in docs:
        new_docs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "description": doc["description"],
            "important": doc["important"],
            "File": docs["File"],
        })
    return templates.TemplateResponse("index.html", {"request": request, "new_docs": new_docs})

@notes.post("/")
async def create_content(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"]= True if formDict.get("important") == "on" else False
    notes = conn.Notes.Notes.insert_one(formDict)
    return {"success": True}