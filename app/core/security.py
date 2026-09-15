from fastapi import HTTPException,status
from app.db.supabase import supabase
def get_access_token(authorization: str | None):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header"
        )

    if not authorization.startswith('Bearer '):
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Authorization header'
        )

    return authorization.split(' ',1)[1]

def get_current_user(access_token: str):
    try: 
        response = supabase.auth.get_user(access_token)

        if not response.user:
            raise HTTPException (
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token'
            )

        return response.user 
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Invalid access token'
        )