from app.db.supabase import supabase
from app.schemas.notes import CreateNotesRequest

def handle_create_notes(newNotes: CreateNotesRequest):
    return supabase.table('notes').insert({
        "title":newNotes.title,
        "description":newNotes.description
    }).execute()