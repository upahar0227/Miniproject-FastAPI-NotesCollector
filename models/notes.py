from pydantic import BaseModel

class Notes(BaseModel):
    title: str
    description: str
    important: bool = None
    File: bytes