from app.schemas.notes import CreateNotesRequest
from app.repository.notes_repository import handle_create_notes


def service_create_notes(newNotes: CreateNotesRequest):

    # handle buniess Logic or verify idk maybe scaleable thing 

    return handle_create_notes(newNotes)