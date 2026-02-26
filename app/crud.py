from sqlalchemy.orm import Session
from sqlalchemy import and_, desc
from typing import List, Optional
from app import models, schemas
from app.auth import get_password_hash

# User CRUD operations
def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate) -> Optional[models.User]:
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        update_data = user_update.dict(exclude_unset=True)
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
        
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> bool:
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

# Conversation CRUD operations
def get_conversation(db: Session, conversation_id: int) -> Optional[models.Conversation]:
    return db.query(models.Conversation).filter(models.Conversation.id == conversation_id).first()

def get_user_conversations(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[models.Conversation]:
    return db.query(models.Conversation).filter(
        models.Conversation.user_id == user_id
    ).order_by(desc(models.Conversation.updated_at)).offset(skip).limit(limit).all()

def create_conversation(db: Session, conversation: schemas.ConversationCreate, user_id: int) -> models.Conversation:
    db_conversation = models.Conversation(
        title=conversation.title,
        user_id=user_id
    )
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

def update_conversation_title(db: Session, conversation_id: int, title: str) -> Optional[models.Conversation]:
    db_conversation = db.query(models.Conversation).filter(models.Conversation.id == conversation_id).first()
    if db_conversation:
        db_conversation.title = title
        db.commit()
        db.refresh(db_conversation)
    return db_conversation

def delete_conversation(db: Session, conversation_id: int) -> bool:
    db_conversation = db.query(models.Conversation).filter(models.Conversation.id == conversation_id).first()
    if db_conversation:
        db.delete(db_conversation)
        db.commit()
        return True
    return False

# Message CRUD operations
def get_conversation_messages(db: Session, conversation_id: int, skip: int = 0, limit: int = 100) -> List[models.Message]:
    return db.query(models.Message).filter(
        models.Message.conversation_id == conversation_id
    ).order_by(models.Message.created_at).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.MessageCreate) -> models.Message:
    db_message = models.Message(
        content=message.content,
        is_user=message.is_user,
        conversation_id=message.conversation_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# Livestock Knowledge CRUD operations
def get_livestock_knowledge(db: Session, skip: int = 0, limit: int = 100) -> List[models.LivestockKnowledge]:
    return db.query(models.LivestockKnowledge).offset(skip).limit(limit).all()

def get_livestock_knowledge_by_category(db: Session, category: str) -> List[models.LivestockKnowledge]:
    return db.query(models.LivestockKnowledge).filter(
        models.LivestockKnowledge.category == category
    ).all()

def create_livestock_knowledge(db: Session, knowledge: schemas.LivestockKnowledgeCreate) -> models.LivestockKnowledge:
    db_knowledge = models.LivestockKnowledge(
        category=knowledge.category,
        subcategory=knowledge.subcategory,
        title=knowledge.title,
        content=knowledge.content,
        source=knowledge.source
    )
    db.add(db_knowledge)
    db.commit()
    db.refresh(db_knowledge)
    return db_knowledge

def update_livestock_knowledge(db: Session, knowledge_id: int, knowledge_update: schemas.LivestockKnowledgeCreate) -> Optional[models.LivestockKnowledge]:
    db_knowledge = db.query(models.LivestockKnowledge).filter(models.LivestockKnowledge.id == knowledge_id).first()
    if db_knowledge:
        for field, value in knowledge_update.dict().items():
            setattr(db_knowledge, field, value)
        db.commit()
        db.refresh(db_knowledge)
    return db_knowledge

def delete_livestock_knowledge(db: Session, knowledge_id: int) -> bool:
    db_knowledge = db.query(models.LivestockKnowledge).filter(models.LivestockKnowledge.id == knowledge_id).first()
    if db_knowledge:
        db.delete(db_knowledge)
        db.commit()
        return True
    return False

# Feedback CRUD operations
def create_feedback(db: Session, feedback: schemas.FeedbackCreate, user_id: int) -> models.Feedback:
    db_feedback = models.Feedback(
        user_id=user_id,
        conversation_id=feedback.conversation_id,
        rating=feedback.rating,
        comment=feedback.comment
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedback_by_conversation(db: Session, conversation_id: int) -> List[models.Feedback]:
    return db.query(models.Feedback).filter(models.Feedback.conversation_id == conversation_id).all()

# Analytics CRUD operations
def get_analytics(db: Session, skip: int = 0, limit: int = 100) -> List[models.Analytics]:
    return db.query(models.Analytics).order_by(desc(models.Analytics.date)).offset(skip).limit(limit).all()

def create_analytics(db: Session, analytics_data: dict) -> models.Analytics:
    db_analytics = models.Analytics(**analytics_data)
    db.add(db_analytics)
    db.commit()
    db.refresh(db_analytics)
    return db_analytics

# Çiftlik Yönetim Sistemi CRUD İşlemleri

# Farm CRUD operations
def get_farm(db: Session, farm_id: int) -> Optional[models.Farm]:
    return db.query(models.Farm).filter(models.Farm.id == farm_id).first()

def get_user_farms(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[models.Farm]:
    return db.query(models.Farm).filter(models.Farm.user_id == user_id).offset(skip).limit(limit).all()

def create_farm(db: Session, farm: schemas.FarmCreate, user_id: int) -> models.Farm:
    db_farm = models.Farm(
        name=farm.name,
        location=farm.location,
        farm_type=farm.farm_type,
        total_area=farm.total_area,
        established_date=farm.established_date,
        user_id=user_id
    )
    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)
    return db_farm

def update_farm(db: Session, farm_id: int, farm_update: schemas.FarmUpdate) -> Optional[models.Farm]:
    db_farm = db.query(models.Farm).filter(models.Farm.id == farm_id).first()
    if db_farm:
        update_data = farm_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_farm, field, value)
        db.commit()
        db.refresh(db_farm)
    return db_farm

def delete_farm(db: Session, farm_id: int) -> bool:
    db_farm = db.query(models.Farm).filter(models.Farm.id == farm_id).first()
    if db_farm:
        db.delete(db_farm)
        db.commit()
        return True
    return False

# Animal CRUD operations
def get_animal(db: Session, animal_id: int) -> Optional[models.Animal]:
    return db.query(models.Animal).filter(models.Animal.id == animal_id).first()

def get_farm_animals(db: Session, farm_id: int, skip: int = 0, limit: int = 100) -> List[models.Animal]:
    return db.query(models.Animal).filter(models.Animal.farm_id == farm_id).offset(skip).limit(limit).all()

def get_animal_by_tag(db: Session, tag_number: str) -> Optional[models.Animal]:
    return db.query(models.Animal).filter(models.Animal.tag_number == tag_number).first()

def create_animal(db: Session, animal: schemas.AnimalCreate) -> models.Animal:
    db_animal = models.Animal(
        farm_id=animal.farm_id,
        tag_number=animal.tag_number,
        name=animal.name,
        species=animal.species,
        breed=animal.breed,
        gender=animal.gender,
        birth_date=animal.birth_date,
        weight=animal.weight,
        status=animal.status,
        purchase_price=animal.purchase_price,
        notes=animal.notes
    )
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

def update_animal(db: Session, animal_id: int, animal_update: schemas.AnimalUpdate) -> Optional[models.Animal]:
    db_animal = db.query(models.Animal).filter(models.Animal.id == animal_id).first()
    if db_animal:
        update_data = animal_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_animal, field, value)
        db.commit()
        db.refresh(db_animal)
    return db_animal

def delete_animal(db: Session, animal_id: int) -> bool:
    db_animal = db.query(models.Animal).filter(models.Animal.id == animal_id).first()
    if db_animal:
        db.delete(db_animal)
        db.commit()
        return True
    return False

# Production Record CRUD operations
def get_production_records(db: Session, farm_id: int, skip: int = 0, limit: int = 100) -> List[models.ProductionRecord]:
    return db.query(models.ProductionRecord).filter(
        models.ProductionRecord.farm_id == farm_id
    ).order_by(desc(models.ProductionRecord.record_date)).offset(skip).limit(limit).all()

def get_animal_production_records(db: Session, animal_id: int, skip: int = 0, limit: int = 100) -> List[models.ProductionRecord]:
    return db.query(models.ProductionRecord).filter(
        models.ProductionRecord.animal_id == animal_id
    ).order_by(desc(models.ProductionRecord.record_date)).offset(skip).limit(limit).all()

def create_production_record(db: Session, record: schemas.ProductionRecordCreate) -> models.ProductionRecord:
    db_record = models.ProductionRecord(
        farm_id=record.farm_id,
        animal_id=record.animal_id,
        record_date=record.record_date,
        production_type=record.production_type,
        quantity=record.quantity,
        unit=record.unit,
        quality_grade=record.quality_grade,
        price_per_unit=record.price_per_unit,
        total_value=record.total_value,
        notes=record.notes
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# Health Record CRUD operations
def get_health_records(db: Session, farm_id: int, skip: int = 0, limit: int = 100) -> List[models.HealthRecord]:
    return db.query(models.HealthRecord).filter(
        models.HealthRecord.farm_id == farm_id
    ).order_by(desc(models.HealthRecord.record_date)).offset(skip).limit(limit).all()

def get_animal_health_records(db: Session, animal_id: int, skip: int = 0, limit: int = 100) -> List[models.HealthRecord]:
    return db.query(models.HealthRecord).filter(
        models.HealthRecord.animal_id == animal_id
    ).order_by(desc(models.HealthRecord.record_date)).offset(skip).limit(limit).all()

def get_upcoming_vaccinations(db: Session, farm_id: int, days_ahead: int = 30) -> List[models.HealthRecord]:
    from datetime import datetime, timedelta
    future_date = datetime.utcnow() + timedelta(days=days_ahead)
    return db.query(models.HealthRecord).filter(
        and_(
            models.HealthRecord.farm_id == farm_id,
            models.HealthRecord.record_type == "vaccination",
            models.HealthRecord.next_due_date <= future_date,
            models.HealthRecord.status == "pending"
        )
    ).all()


def get_upcoming_health_appointments(db: Session, farm_id: int, days_ahead: int = 90) -> List[models.HealthRecord]:
    """Yaklaşan veteriner randevularını (next_due_date olan aşı/tedavi/kontrol) getirir."""
    from datetime import datetime, timedelta
    from sqlalchemy import asc
    now = datetime.utcnow()
    future_date = now + timedelta(days=days_ahead)
    return db.query(models.HealthRecord).filter(
        and_(
            models.HealthRecord.farm_id == farm_id,
            models.HealthRecord.next_due_date.isnot(None),
            models.HealthRecord.next_due_date >= now,
            models.HealthRecord.next_due_date <= future_date
        )
    ).order_by(asc(models.HealthRecord.next_due_date)).limit(30).all()


def create_health_record(db: Session, record: schemas.HealthRecordCreate) -> models.HealthRecord:
    db_record = models.HealthRecord(
        farm_id=record.farm_id,
        animal_id=record.animal_id,
        record_date=record.record_date,
        record_type=record.record_type,
        description=record.description,
        veterinarian=record.veterinarian,
        medication=record.medication,
        dosage=record.dosage,
        cost=record.cost,
        next_due_date=record.next_due_date,
        status=record.status,
        notes=record.notes
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# Financial Record CRUD operations
def get_financial_records(db: Session, farm_id: int, skip: int = 0, limit: int = 100) -> List[models.FinancialRecord]:
    return db.query(models.FinancialRecord).filter(
        models.FinancialRecord.farm_id == farm_id
    ).order_by(desc(models.FinancialRecord.record_date)).offset(skip).limit(limit).all()

def create_financial_record(db: Session, record: schemas.FinancialRecordCreate) -> models.FinancialRecord:
    db_record = models.FinancialRecord(
        farm_id=record.farm_id,
        record_date=record.record_date,
        record_type=record.record_type,
        category=record.category,
        description=record.description,
        amount=record.amount,
        payment_method=record.payment_method,
        reference_number=record.reference_number,
        notes=record.notes
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# Feed Record CRUD operations
def get_feed_records(db: Session, farm_id: int, skip: int = 0, limit: int = 100) -> List[models.FeedRecord]:
    return db.query(models.FeedRecord).filter(
        models.FeedRecord.farm_id == farm_id
    ).order_by(desc(models.FeedRecord.feed_date)).offset(skip).limit(limit).all()

def create_feed_record(db: Session, record: schemas.FeedRecordCreate) -> models.FeedRecord:
    db_record = models.FeedRecord(
        farm_id=record.farm_id,
        animal_id=record.animal_id,
        feed_date=record.feed_date,
        feed_type=record.feed_type,
        quantity=record.quantity,
        unit_cost=record.unit_cost,
        total_cost=record.total_cost,
        supplier=record.supplier,
        quality_notes=record.quality_notes
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
