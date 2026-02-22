from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas, auth, models
from app.rag_system import rag_system

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/users", response_model=List[schemas.User])
def get_all_users(
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get all users (admin only)"""
    return crud.get_users(db=db, skip=skip, limit=limit)

@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(
    user_id: int,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get user by ID (admin only)"""
    user = crud.get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int,
    user_update: schemas.UserUpdate,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Update user (admin only)"""
    user = crud.update_user(db=db, user_id=user_id, user_update=user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Delete user (admin only)"""
    success = crud.delete_user(db=db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Knowledge Base Management
@router.get("/knowledge", response_model=List[schemas.LivestockKnowledge])
def get_all_knowledge(
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get all knowledge base entries (admin only)"""
    return crud.get_livestock_knowledge(db=db, skip=skip, limit=limit)

@router.post("/knowledge", response_model=schemas.LivestockKnowledge)
def create_knowledge(
    knowledge: schemas.LivestockKnowledgeCreate,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Create new knowledge base entry (admin only)"""
    # Create in database
    db_knowledge = crud.create_livestock_knowledge(db=db, knowledge=knowledge)
    
    # Add to RAG system
    try:
        rag_system.add_documents([{
            "title": knowledge.title,
            "content": knowledge.content,
            "category": knowledge.category,
            "subcategory": knowledge.subcategory,
            "source": knowledge.source
        }])
    except Exception as e:
        print(f"Error adding to RAG system: {e}")
    
    return db_knowledge

@router.put("/knowledge/{knowledge_id}", response_model=schemas.LivestockKnowledge)
def update_knowledge(
    knowledge_id: int,
    knowledge_update: schemas.LivestockKnowledgeCreate,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Update knowledge base entry (admin only)"""
    knowledge = crud.update_livestock_knowledge(db=db, knowledge_id=knowledge_id, knowledge_update=knowledge_update)
    if not knowledge:
        raise HTTPException(status_code=404, detail="Knowledge entry not found")
    
    # Note: RAG system update would require more complex logic
    # For now, we'll just update the database
    
    return knowledge

@router.delete("/knowledge/{knowledge_id}")
def delete_knowledge(
    knowledge_id: int,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Delete knowledge base entry (admin only)"""
    success = crud.delete_livestock_knowledge(db=db, knowledge_id=knowledge_id)
    if not success:
        raise HTTPException(status_code=404, detail="Knowledge entry not found")
    return {"message": "Knowledge entry deleted successfully"}

@router.get("/analytics", response_model=List[schemas.Analytics])
def get_analytics(
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get analytics data (admin only)"""
    return crud.get_analytics(db=db, skip=skip, limit=limit)

@router.post("/analytics")
def create_analytics(
    analytics_data: dict,
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Create analytics entry (admin only)"""
    return crud.create_analytics(db=db, analytics_data=analytics_data)

@router.get("/stats")
def get_system_stats(
    current_user: schemas.User = Depends(auth.get_current_admin_user),
    db: Session = Depends(get_db)
):
    """Get system statistics (admin only)"""
    from sqlalchemy import func
    
    total_users = db.query(func.count(models.User.id)).scalar()
    total_conversations = db.query(func.count(models.Conversation.id)).scalar()
    total_messages = db.query(func.count(models.Message.id)).scalar()
    total_knowledge = db.query(func.count(models.LivestockKnowledge.id)).scalar()
    
    return {
        "total_users": total_users,
        "total_conversations": total_conversations,
        "total_messages": total_messages,
        "total_knowledge_entries": total_knowledge
    }
