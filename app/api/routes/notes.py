from fastapi import APIRouter,Header,HTTPException,status
from app.db.supabase import supabase
from app.schemas.notes import CreateNotesRequest
from app.core.security import get_access_token,get_current_user
from app.service.notesService import service_create_notes
router = APIRouter(
    prefix='/notes',
    tags=['Notes']
)

# @router.get('/')
# def get_notes():
#     return {
#         'message':"Get Notes Successfully"
#     }

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
    