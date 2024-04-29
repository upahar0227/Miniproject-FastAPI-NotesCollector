from fastapi import FastAPI
from routes.notes import notes

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(notes)

#
# @app.get("/items/{item_id}")
# async def get_data(item_id:int):
#     return {"item_id": item_id}