from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas, auth
from app.rag_system import rag_system
from typing import List

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/conversations", response_model=schemas.Conversation)
def create_conversation(
    conversation: schemas.ConversationCreate,
    current_user: schemas.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a new conversation"""
    return crud.create_conversation(db=db, conversation=conversation, user_id=current_user.id)

@router.get("/conversations", response_model=List[schemas.Conversation])
def get_conversations(
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get user's conversations"""
    return crud.get_user_conversations(db=db, user_id=current_user.id, skip=skip, limit=limit)

@router.get("/conversations/{conversation_id}", response_model=schemas.Conversation)
def get_conversation(
    conversation_id: int,
    current_user: schemas.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get a specific conversation"""
    conversation = crud.get_conversation(db=db, conversation_id=conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    if conversation.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return conversation

@router.get("/conversations/{conversation_id}/messages", response_model=List[schemas.Message])
def get_conversation_messages(
    conversation_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get messages from a conversation"""
    conversation = crud.get_conversation(db=db, conversation_id=conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    if conversation.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return crud.get_conversation_messages(db=db, conversation_id=conversation_id, skip=skip, limit=limit)

@router.post("/send", response_model=schemas.ChatResponse)
def send_message(
    chat_request: schemas.ChatRequest,
    current_user: schemas.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Send a message and get AI response"""
    import time
    start_time = time.time()
    
    # Create conversation if not provided
    if not chat_request.conversation_id:
        conversation = crud.create_conversation(
            db=db,
            conversation=schemas.ConversationCreate(title=chat_request.message[:50] + "..."),
            user_id=current_user.id
        )
        conversation_id = conversation.id
    else:
        conversation_id = chat_request.conversation_id
        # Verify conversation belongs to user
        conversation = crud.get_conversation(db=db, conversation_id=conversation_id)
        if not conversation or conversation.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Not enough permissions")
    
    # Save user message
    user_message = crud.create_message(
        db=db,
        message=schemas.MessageCreate(
            content=chat_request.message,
            is_user=True,
            conversation_id=conversation_id
        )
    )
    
    # Get AI response using RAG system
    try:
        rag_response = rag_system.query(chat_request.message)
        ai_response = rag_response["answer"]
    except Exception as e:
        ai_response = "Üzgünüm, şu anda bir teknik sorun yaşıyorum. Lütfen daha sonra tekrar deneyin."
    
    # Save AI response
    ai_message = crud.create_message(
        db=db,
        message=schemas.MessageCreate(
            content=ai_response,
            is_user=False,
            conversation_id=conversation_id
        )
    )
    
    # Update conversation title if it's the first message
    if len(crud.get_conversation_messages(db=db, conversation_id=conversation_id)) == 2:
        crud.update_conversation_title(db=db, conversation_id=conversation_id, title=chat_request.message[:50] + "...")
    
    response_time = time.time() - start_time
    
    return schemas.ChatResponse(
        response=ai_response,
        conversation_id=conversation_id,
        message_id=ai_message.id
    )

@router.delete("/conversations/{conversation_id}")
def delete_conversation(
    conversation_id: int,
    current_user: schemas.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Delete a conversation"""
    conversation = crud.get_conversation(db=db, conversation_id=conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    if conversation.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    success = crud.delete_conversation(db=db, conversation_id=conversation_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete conversation")
    
    return {"message": "Conversation deleted successfully"}

@router.post("/feedback")
def submit_feedback(
    feedback: schemas.FeedbackCreate,
    current_user: schemas.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    """Submit feedback for a conversation"""
    # Verify conversation exists and belongs to user
    conversation = crud.get_conversation(db=db, conversation_id=feedback.conversation_id)
    if not conversation or conversation.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return crud.create_feedback(db=db, feedback=feedback, user_id=current_user.id)

