from pydantic import BaseModel

class CreateNotesRequest(BaseModel):
    title: str
    description: str