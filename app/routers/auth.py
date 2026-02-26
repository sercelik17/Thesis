from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db, SessionLocal
from app import crud, schemas, auth
from app.config import settings

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    try:
        db_user = crud.get_user_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
        
        db_user = crud.get_user_by_username(db, username=user.username)
        if db_user:
            raise HTTPException(
                status_code=400,
                detail="Username already taken"
            )
        
        return crud.create_user(db=db, user=user)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Register error: {type(e).__name__}: {str(e)}",
        )

@router.post("/login")
def login(body: dict = Body(...)):
    """Login user and return access token. Body: { email, password }."""
    email = (body.get("email") or "").strip()
    password = body.get("password") or ""
    if not email or not password:
        return JSONResponse(
            status_code=422,
            content={"detail": "email ve password gerekli"},
        )
    db = SessionLocal()
    try:
        user = auth.authenticate_user(db, email, password)
        if not user:
            return JSONResponse(
                status_code=401,
                content={"detail": "Incorrect email or password"},
            )
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = auth.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        # JWT'yi JSON ile frontend'e veriyoruz; ayrıca basit bir oturum çerezi de ayarlıyoruz
        response = JSONResponse(
            status_code=200,
            content={"access_token": access_token, "token_type": "bearer"},
        )
        # Giriş yapıldığını gösteren hafif bir cookie (sunucu tarafı HTML sayfaları için)
        response.set_cookie(
            key="sf_logged_in",
            value="1",
            max_age=int(access_token_expires.total_seconds()),
            httponly=False,
            secure=False,  # prod'da True + HTTPS
            samesite="lax",
        )
        return response
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"detail": f"{type(e).__name__}: {str(e)}"},
        )
    finally:
        db.close()


@router.post("/logout")
def logout():
    """Çıkış yap: sf_logged_in cookie'sini siler. Frontend token'ı kendi temizler."""
    response = JSONResponse(status_code=200, content={"detail": "Çıkış yapıldı"})
    response.delete_cookie(key="sf_logged_in")
    return response


@router.get("/me", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(auth.get_current_active_user)):
    """Get current user information"""
    return current_user

@router.put("/me", response_model=schemas.User)
def update_user_me(
    user_update: schemas.UserUpdate,
    current_user: schemas.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update current user information"""
    return crud.update_user(db=db, user_id=current_user.id, user_update=user_update)

