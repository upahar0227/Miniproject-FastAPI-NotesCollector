from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

from pymongo import MongoClient

con = MongoClient("mongodb+srv://upahar1923:Handsome1923@cluster0.ef1sf7a.mongodb.net")

@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    docs= con.Notes.Notes.find({})
    new_docs=[]
    for doc in docs:
        print(doc)
        new_docs.append({
            "id": doc["_id"],
            "title": doc["title"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "new_docs": new_docs})
