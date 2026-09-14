from fastapi import APIRouter,HTTPException,status
from app.schemas.auth import RegisterRequestModel
from app.db.supabase import supabase
router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/register')
def handle_register(registerRequest: RegisterRequestModel):
    try:
        data = supabase.auth.sign_up({
            'email':registerRequest.email,
            'password':registerRequest.password
        })
        return data
    except Exception as e:
        raise HTTPException(
            detail=f'Failed to create new user: {e}',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )