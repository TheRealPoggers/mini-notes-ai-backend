from fastapi import APIRouter,Header,HTTPException,status,Body
from app.db.supabase import supabase
from app.schemas.notes import CreateNotesRequest, UpdateDescriptionRequest
from app.core.security import get_access_token,get_current_user
from app.service.notesService import service_create_notes,service_get_notes,service_get_note_by_id,service_update_note_description,service_disable_note
router = APIRouter(
    prefix='/notes',
    tags=['Notes']
)

@router.get('/')
def get_notes(
    authorization: str | None = Header(default=None),
):
    access_token = get_access_token(authorization)
    user = get_current_user(access_token)

    supabase.postgrest.auth(access_token)

    try:
        data = service_get_notes()
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to get notes: {e}'
        )

@router.get('/{note_id}')
def get_note_by_id(
    note_id: str, 
    authorization: str | None = Header(default=None)
):
    access_token = get_access_token(authorization)
    user = get_current_user(access_token)

    supabase.postgrest.auth(access_token)

    try:
        data = service_get_note_by_id(note_id)
        ConnectionResetError
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to get notes by id: {e}'
        )

@router.post('/')
def create_notes(
    newNotes: CreateNotesRequest,
    authorization: str | None = Header(default=None),

):
    access_token = get_access_token(authorization)
    user = get_current_user(access_token) # verify User

    supabase.postgrest.auth(access_token)
    
    try:
        data = service_create_notes(newNotes)
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to create new notes: {e}'
        )

@router.put('/{note_id}')
def update_description(
    note_id: str,
    request: UpdateDescriptionRequest,
    authorization: str | None = Header(default=None),
):
    access_token = get_access_token(authorization)
    user = get_current_user(access_token) # verify User

    supabase.postgrest.auth(access_token)
    
    try:
        data = service_update_note_description(note_id,request.description)
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to update description for notes: {e}'
        )
    
@router.delete('/{note_id}')
def update_description(
    note_id: str,
    authorization: str | None = Header(default=None),
):
    access_token = get_access_token(authorization)
    user = get_current_user(access_token) # verify User

    supabase.postgrest.auth(access_token)
    
    try:
        data = service_disable_note(note_id)
        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to remove notes: {e}'
        )
    