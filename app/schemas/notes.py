from pydantic import BaseModel

class CreateNotesRequest(BaseModel):
    title: str
    description: str


class UpdateDescriptionRequest(BaseModel):
    description: str | None