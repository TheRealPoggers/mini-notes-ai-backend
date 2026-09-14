from fastapi import APIRouter

router = APIRouter(
    prefix='/notes',
    tags=['Notes']
)

@router.get('/')
def get_notes():
    return {
        'message':"Get Notes Successfully"
    }