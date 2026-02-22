from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: str
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Authentication schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class LoginRequest(BaseModel):
    email: str
    password: str

# Conversation schemas
class ConversationBase(BaseModel):
    title: str

class ConversationCreate(ConversationBase):
    pass

class Conversation(ConversationBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Message schemas
class MessageBase(BaseModel):
    content: str
    is_user: bool

class MessageCreate(MessageBase):
    conversation_id: int

class Message(MessageBase):
    id: int
    conversation_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Chat schemas
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[int] = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: int
    message_id: int

# Knowledge base schemas
class LivestockKnowledgeBase(BaseModel):
    category: str
    subcategory: Optional[str] = None
    title: str
    content: str
    source: Optional[str] = None

class LivestockKnowledgeCreate(LivestockKnowledgeBase):
    pass

class LivestockKnowledge(LivestockKnowledgeBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Feedback schemas
class FeedbackBase(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    conversation_id: int

class Feedback(FeedbackBase):
    id: int
    user_id: int
    conversation_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Analytics schemas
class Analytics(BaseModel):
    id: int
    date: datetime
    total_conversations: int
    total_messages: int
    total_users: int
    avg_response_time: float
    popular_topics: Optional[str] = None

    class Config:
        from_attributes = True

# Çiftlik Yönetim Sistemi Şemaları
class FarmBase(BaseModel):
    name: str
    location: Optional[str] = None
    farm_type: Optional[str] = None  # "cattle", "poultry", "sheep", "mixed"
    total_area: Optional[float] = None  # hektar
    established_date: Optional[datetime] = None

class FarmCreate(FarmBase):
    pass

class FarmUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    farm_type: Optional[str] = None
    total_area: Optional[float] = None
    established_date: Optional[datetime] = None

class Farm(FarmBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class AnimalBase(BaseModel):
    tag_number: str
    name: Optional[str] = None
    species: str  # "cattle", "sheep", "goat", "chicken"
    breed: Optional[str] = None
    gender: Optional[str] = None  # "male", "female"
    birth_date: Optional[datetime] = None
    weight: Optional[float] = None  # kg
    status: str = "active"  # "active", "sold", "deceased"
    purchase_price: Optional[float] = None
    notes: Optional[str] = None

class AnimalCreate(AnimalBase):
    farm_id: int

class AnimalUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    breed: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[datetime] = None
    weight: Optional[float] = None
    status: Optional[str] = None
    purchase_price: Optional[float] = None
    notes: Optional[str] = None

class Animal(AnimalBase):
    id: int
    farm_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ProductionRecordBase(BaseModel):
    record_date: datetime
    production_type: str  # "milk", "meat", "eggs", "wool"
    quantity: float
    unit: str  # "litre", "kg", "piece"
    quality_grade: Optional[str] = None  # "A", "B", "C"
    price_per_unit: Optional[float] = None
    total_value: Optional[float] = None
    notes: Optional[str] = None

class ProductionRecordCreate(ProductionRecordBase):
    farm_id: int
    animal_id: Optional[int] = None

class ProductionRecord(ProductionRecordBase):
    id: int
    farm_id: int
    animal_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

class HealthRecordBase(BaseModel):
    record_date: datetime
    record_type: str  # "vaccination", "treatment", "checkup", "disease"
    description: str
    veterinarian: Optional[str] = None
    medication: Optional[str] = None
    dosage: Optional[str] = None
    cost: Optional[float] = None
    next_due_date: Optional[datetime] = None
    status: str = "completed"  # "completed", "pending", "overdue"
    notes: Optional[str] = None

class HealthRecordCreate(HealthRecordBase):
    farm_id: int
    animal_id: Optional[int] = None

class HealthRecord(HealthRecordBase):
    id: int
    farm_id: int
    animal_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

class FinancialRecordBase(BaseModel):
    record_date: datetime
    record_type: str  # "income", "expense"
    category: str  # "feed", "veterinary", "equipment", "sales"
    description: str
    amount: float
    payment_method: Optional[str] = None  # "cash", "bank_transfer", "credit_card"
    reference_number: Optional[str] = None
    notes: Optional[str] = None

class FinancialRecordCreate(FinancialRecordBase):
    farm_id: int

class FinancialRecord(FinancialRecordBase):
    id: int
    farm_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class FeedRecordBase(BaseModel):
    feed_date: datetime
    feed_type: str  # "hay", "grain", "supplement", "pasture"
    quantity: float  # kg
    unit_cost: Optional[float] = None  # kg başına maliyet
    total_cost: Optional[float] = None
    supplier: Optional[str] = None
    quality_notes: Optional[str] = None

class FeedRecordCreate(FeedRecordBase):
    farm_id: int
    animal_id: Optional[int] = None

class FeedRecord(FeedRecordBase):
    id: int
    farm_id: int
    animal_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

# Çiftlik Analitik Şemaları
class FarmAnalytics(BaseModel):
    total_animals: int
    total_production_this_month: float
    total_income_this_month: float
    total_expenses_this_month: float
    profit_this_month: float
    upcoming_vaccinations: int
    overdue_health_checks: int
    average_daily_milk_production: Optional[float] = None
    feed_cost_per_animal: Optional[float] = None

class ProductionSummary(BaseModel):
    period: str  # "daily", "weekly", "monthly", "yearly"
    total_quantity: float
    total_value: float
    average_per_animal: Optional[float] = None
    trend: str  # "increasing", "decreasing", "stable"

class HealthSummary(BaseModel):
    total_vaccinations: int
    pending_vaccinations: int
    overdue_vaccinations: int
    total_treatments: int
    active_health_issues: int
    next_due_dates: List[datetime]

class FinancialSummary(BaseModel):
    total_income: float
    total_expenses: float
    net_profit: float
    income_by_category: dict
    expenses_by_category: dict
    profit_margin: float
