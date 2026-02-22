from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    conversations = relationship("Conversation", back_populates="user")
    feedback = relationship("Feedback", back_populates="user")
    farms = relationship("Farm", back_populates="user")

class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation")

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    content = Column(Text, nullable=False)
    is_user = Column(Boolean, nullable=False)  # True for user, False for bot
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    conversation = relationship("Conversation", back_populates="messages")

class LivestockKnowledge(Base):
    __tablename__ = "livestock_knowledge"
    
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)  # e.g., "cattle", "poultry", "sheep"
    subcategory = Column(String)  # e.g., "feeding", "health", "breeding"
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String)  # Reference source
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Feedback(Base):
    __tablename__ = "feedback"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    rating = Column(Integer)  # 1-5 scale
    comment = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="feedback")

class Analytics(Base):
    __tablename__ = "analytics"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    total_conversations = Column(Integer, default=0)
    total_messages = Column(Integer, default=0)
    total_users = Column(Integer, default=0)
    avg_response_time = Column(Float, default=0.0)
    popular_topics = Column(Text)  # JSON string of popular topics

# Çiftlik Yönetim Sistemi Modelleri
class Farm(Base):
    __tablename__ = "farms"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    location = Column(String)
    farm_type = Column(String)  # "cattle", "poultry", "sheep", "mixed"
    total_area = Column(Float)  # hektar
    established_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="farms")
    animals = relationship("Animal", back_populates="farm")
    production_records = relationship("ProductionRecord", back_populates="farm")
    health_records = relationship("HealthRecord", back_populates="farm")
    financial_records = relationship("FinancialRecord", back_populates="farm")

class Animal(Base):
    __tablename__ = "animals"
    
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    tag_number = Column(String, unique=True, nullable=False)  # Hayvan küpe numarası
    name = Column(String)
    species = Column(String, nullable=False)  # "cattle", "sheep", "goat", "chicken"
    breed = Column(String)  # Irk
    gender = Column(String)  # "male", "female"
    birth_date = Column(DateTime(timezone=True))
    weight = Column(Float)  # kg
    status = Column(String, default="active")  # "active", "sold", "deceased"
    purchase_price = Column(Float)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    farm = relationship("Farm", back_populates="animals")
    health_records = relationship("HealthRecord", back_populates="animal")
    production_records = relationship("ProductionRecord", back_populates="animal")

class ProductionRecord(Base):
    __tablename__ = "production_records"
    
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=True)  # Null for farm-level records
    record_date = Column(DateTime(timezone=True), nullable=False)
    production_type = Column(String, nullable=False)  # "milk", "meat", "eggs", "wool"
    quantity = Column(Float, nullable=False)  # litre, kg, adet
    unit = Column(String, nullable=False)  # "litre", "kg", "piece"
    quality_grade = Column(String)  # "A", "B", "C"
    price_per_unit = Column(Float)
    total_value = Column(Float)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    farm = relationship("Farm", back_populates="production_records")
    animal = relationship("Animal", back_populates="production_records")

class HealthRecord(Base):
    __tablename__ = "health_records"
    
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=True)  # Null for farm-level records
    record_date = Column(DateTime(timezone=True), nullable=False)
    record_type = Column(String, nullable=False)  # "vaccination", "treatment", "checkup", "disease"
    description = Column(Text, nullable=False)
    veterinarian = Column(String)
    medication = Column(String)
    dosage = Column(String)
    cost = Column(Float)
    next_due_date = Column(DateTime(timezone=True))  # Sonraki aşı/tedavi tarihi
    status = Column(String, default="completed")  # "completed", "pending", "overdue"
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    farm = relationship("Farm", back_populates="health_records")
    animal = relationship("Animal", back_populates="health_records")

class FinancialRecord(Base):
    __tablename__ = "financial_records"
    
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    record_date = Column(DateTime(timezone=True), nullable=False)
    record_type = Column(String, nullable=False)  # "income", "expense"
    category = Column(String, nullable=False)  # "feed", "veterinary", "equipment", "sales"
    description = Column(Text, nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String)  # "cash", "bank_transfer", "credit_card"
    reference_number = Column(String)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    farm = relationship("Farm", back_populates="financial_records")

class FeedRecord(Base):
    __tablename__ = "feed_records"
    
    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=True)
    feed_date = Column(DateTime(timezone=True), nullable=False)
    feed_type = Column(String, nullable=False)  # "hay", "grain", "supplement", "pasture"
    quantity = Column(Float, nullable=False)  # kg
    unit_cost = Column(Float)  # kg başına maliyet
    total_cost = Column(Float)
    supplier = Column(String)
    quality_notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    farm = relationship("Farm")
    animal = relationship("Animal")
