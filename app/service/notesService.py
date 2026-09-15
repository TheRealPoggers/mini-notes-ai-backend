from app.schemas.notes import CreateNotesRequest
from app.repository.notes_repository import handle_create_notes,handle_get_notes,handle_get_note_by_id,handle_update_note_description,handle_disable_note

def service_get_notes():

    result = handle_get_notes()
    return result.data

def service_get_note_by_id(id: str):
    result = handle_get_note_by_id(id)
    return result.data

def service_update_note_description(note_id: str,description: str):
    result = handle_update_note_description(note_id,description)
    return result.data

def service_disable_note(note_id: str):
    result = handle_disable_note(note_id)
    return result.data


def service_create_notes(newNotes: CreateNotesRequest):

    # handle buniess Logic or verify idk maybe scaleable thing 

    return handle_create_notes(newNotes)