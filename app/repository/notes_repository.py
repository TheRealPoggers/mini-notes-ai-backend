from app.db.supabase import supabase
from app.schemas.notes import CreateNotesRequest

def handle_create_notes(newNotes: CreateNotesRequest):
    return supabase.table('notes').insert({
        "title":newNotes.title,
        "description":newNotes.description
    }).execute()

def handle_get_notes():
    return supabase.table('notes').select('*').eq('is_active',True).execute()

def handle_update_note_description(note_id: str,description: str):
    return supabase.table('notes').update({'description':description}).eq('id',note_id).execute()

def handle_get_note_by_id(note_id: str):
    return supabase.table('notes').select('*').eq('is_active',True).eq('id',note_id).single().execute()

def handle_disable_note(note_id: str):
    return supabase.table('notes').update({'is_active':False}).eq('id',note_id).execute()