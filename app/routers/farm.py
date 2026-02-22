from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.database import get_db
from app import models, schemas, crud, auth
from app.smart_farm_chat import SmartFarmChatService
from app.farm_analytics import FarmAnalyticsService

router = APIRouter(prefix="/farm", tags=["farm"])

# Dependency to get current user
def get_current_user(current_user: models.User = Depends(auth.get_current_active_user)):
    return current_user

# Farm Management Endpoints
@router.post("/", response_model=schemas.Farm)
def create_farm(
    farm: schemas.FarmCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yeni çiftlik oluştur"""
    return crud.create_farm(db=db, farm=farm, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Farm])
def get_user_farms(
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kullanıcının çiftliklerini listele"""
    return crud.get_user_farms(db=db, user_id=current_user.id, skip=skip, limit=limit)

@router.get("/{farm_id}", response_model=schemas.Farm)
def get_farm(
    farm_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Belirli bir çiftliği getir"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm:
        raise HTTPException(status_code=404, detail="Çiftlik bulunamadı")
    if farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    return farm

@router.put("/{farm_id}", response_model=schemas.Farm)
def update_farm(
    farm_id: int,
    farm_update: schemas.FarmUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftlik bilgilerini güncelle"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm:
        raise HTTPException(status_code=404, detail="Çiftlik bulunamadı")
    if farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    return crud.update_farm(db=db, farm_id=farm_id, farm_update=farm_update)

@router.delete("/{farm_id}")
def delete_farm(
    farm_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftliği sil"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm:
        raise HTTPException(status_code=404, detail="Çiftlik bulunamadı")
    if farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    success = crud.delete_farm(db=db, farm_id=farm_id)
    if success:
        return {"message": "Çiftlik başarıyla silindi"}
    else:
        raise HTTPException(status_code=500, detail="Çiftlik silinirken hata oluştu")

# Production Records Endpoints
@router.post("/{farm_id}/production-records", response_model=schemas.ProductionRecord)
def create_production_record(
    farm_id: int,
    record: schemas.ProductionRecordCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yeni üretim kaydı ekle"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.create_production_record(db=db, record=record)

@router.get("/{farm_id}/production-records", response_model=List[schemas.ProductionRecord])
def get_production_records(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftliğin üretim kayıtlarını listele"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_production_records(db=db, farm_id=farm_id, skip=skip, limit=limit)

# Financial Records Endpoints
@router.post("/{farm_id}/financial-records", response_model=schemas.FinancialRecord)
def create_financial_record(
    farm_id: int,
    record: schemas.FinancialRecordCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yeni finansal kayıt ekle"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.create_financial_record(db=db, record=record)

@router.get("/{farm_id}/financial-records", response_model=List[schemas.FinancialRecord])
def get_financial_records(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftliğin finansal kayıtlarını listele"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_financial_records(db=db, farm_id=farm_id, skip=skip, limit=limit)

# Health Records Endpoints
@router.post("/{farm_id}/health-records", response_model=schemas.HealthRecord)
def create_health_record(
    farm_id: int,
    record: schemas.HealthRecordCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yeni sağlık kaydı ekle"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.create_health_record(db=db, record=record)

@router.get("/{farm_id}/health-records", response_model=List[schemas.HealthRecord])
def get_health_records(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftliğin sağlık kayıtlarını listele"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_health_records(db=db, farm_id=farm_id, skip=skip, limit=limit)

# Feed Records Endpoints
@router.post("/{farm_id}/feed-records", response_model=schemas.FeedRecord)
def create_feed_record(
    farm_id: int,
    record: schemas.FeedRecordCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yeni yem kaydı ekle"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.create_feed_record(db=db, record=record)

@router.get("/{farm_id}/feed-records", response_model=List[schemas.FeedRecord])
def get_feed_records(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftliğin yem kayıtlarını listele"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_feed_records(db=db, farm_id=farm_id, skip=skip, limit=limit)

# Analytics Endpoints
@router.get("/{farm_id}/analytics/summary", response_model=schemas.FarmAnalytics)
def get_farm_analytics(
    farm_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftlik analitik özeti"""
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    analytics_service = FarmAnalyticsService(db)
    return analytics_service.get_farm_dashboard(farm_id)

# Animal Management Endpoints
@router.post("/{farm_id}/animals", response_model=schemas.Animal)
def create_animal(
    farm_id: int,
    animal: schemas.AnimalCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yeni hayvan ekle"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    # Küpe numarası benzersizliğini kontrol et
    existing_animal = crud.get_animal_by_tag(db=db, tag_number=animal.tag_number)
    if existing_animal:
        raise HTTPException(status_code=400, detail="Bu küpe numarası zaten kullanılıyor")
    
    animal.farm_id = farm_id
    return crud.create_animal(db=db, animal=animal)

@router.get("/{farm_id}/animals", response_model=List[schemas.Animal])
def get_farm_animals(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftlikteki hayvanları listele"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_farm_animals(db=db, farm_id=farm_id, skip=skip, limit=limit)

@router.get("/{farm_id}/animals/{animal_id}", response_model=schemas.Animal)
def get_animal(
    farm_id: int,
    animal_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Belirli bir hayvanı getir"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    animal = crud.get_animal(db=db, animal_id=animal_id)
    if not animal or animal.farm_id != farm_id:
        raise HTTPException(status_code=404, detail="Hayvan bulunamadı")
    
    return animal

@router.put("/{farm_id}/animals/{animal_id}", response_model=schemas.Animal)
def update_animal(
    farm_id: int,
    animal_id: int,
    animal_update: schemas.AnimalUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Hayvan bilgilerini güncelle"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    animal = crud.get_animal(db=db, animal_id=animal_id)
    if not animal or animal.farm_id != farm_id:
        raise HTTPException(status_code=404, detail="Hayvan bulunamadı")
    
    return crud.update_animal(db=db, animal_id=animal_id, animal_update=animal_update)

# Production Record Endpoints
@router.post("/{farm_id}/production", response_model=schemas.ProductionRecord)
def create_production_record(
    farm_id: int,
    record: schemas.ProductionRecordCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Üretim kaydı ekle"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    record.farm_id = farm_id
    return crud.create_production_record(db=db, record=record)

@router.get("/{farm_id}/production", response_model=List[schemas.ProductionRecord])
def get_production_records(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Üretim kayıtlarını listele"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_production_records(db=db, farm_id=farm_id, skip=skip, limit=limit)

# Health Record Endpoints
@router.post("/{farm_id}/health", response_model=schemas.HealthRecord)
def create_health_record(
    farm_id: int,
    record: schemas.HealthRecordCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Sağlık kaydı ekle"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    record.farm_id = farm_id
    return crud.create_health_record(db=db, record=record)

@router.get("/{farm_id}/health", response_model=List[schemas.HealthRecord])
def get_health_records(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Sağlık kayıtlarını listele"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_health_records(db=db, farm_id=farm_id, skip=skip, limit=limit)

@router.get("/{farm_id}/health/upcoming", response_model=List[schemas.HealthRecord])
def get_upcoming_vaccinations(
    farm_id: int,
    days_ahead: int = 30,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yaklaşan aşıları listele"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_upcoming_vaccinations(db=db, farm_id=farm_id, days_ahead=days_ahead)

# Financial Record Endpoints
@router.post("/{farm_id}/financial", response_model=schemas.FinancialRecord)
def create_financial_record(
    farm_id: int,
    record: schemas.FinancialRecordCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Finansal kayıt ekle"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    record.farm_id = farm_id
    return crud.create_financial_record(db=db, record=record)

@router.get("/{farm_id}/financial", response_model=List[schemas.FinancialRecord])
def get_financial_records(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Finansal kayıtları listele"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_financial_records(db=db, farm_id=farm_id, skip=skip, limit=limit)

# Feed Record Endpoints
@router.post("/{farm_id}/feed", response_model=schemas.FeedRecord)
def create_feed_record(
    farm_id: int,
    record: schemas.FeedRecordCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yem kaydı ekle"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    record.farm_id = farm_id
    return crud.create_feed_record(db=db, record=record)

@router.get("/{farm_id}/feed", response_model=List[schemas.FeedRecord])
def get_feed_records(
    farm_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Yem kayıtlarını listele"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    return crud.get_feed_records(db=db, farm_id=farm_id, skip=skip, limit=limit)

# Analytics Endpoints
@router.get("/{farm_id}/analytics/dashboard", response_model=schemas.FarmAnalytics)
def get_farm_dashboard(
    farm_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Çiftlik dashboard verilerini getir"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    analytics_service = FarmAnalyticsService(db)
    return analytics_service.get_farm_dashboard(farm_id)

@router.get("/{farm_id}/analytics/production", response_model=schemas.ProductionSummary)
def get_production_summary(
    farm_id: int,
    period: str = "monthly",
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Üretim özetini getir"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    analytics_service = FarmAnalyticsService(db)
    return analytics_service.get_production_summary(farm_id, period)

@router.get("/{farm_id}/analytics/health", response_model=schemas.HealthSummary)
def get_health_summary(
    farm_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Sağlık özetini getir"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    analytics_service = FarmAnalyticsService(db)
    return analytics_service.get_health_summary(farm_id)

@router.get("/{farm_id}/analytics/financial", response_model=schemas.FinancialSummary)
def get_financial_summary(
    farm_id: int,
    period_days: int = 30,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Finansal özeti getir"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    analytics_service = FarmAnalyticsService(db)
    return analytics_service.get_financial_summary(farm_id, period_days)

# Smart Chat Endpoint
@router.post("/{farm_id}/chat")
def farm_chat(
    farm_id: int,
    chat_request: schemas.ChatRequest,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Akıllı çiftlik sohbeti"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    chat_service = SmartFarmChatService(db)
    response = chat_service.process_farm_query(current_user.id, chat_request.message, farm_id)
    
    return response

@router.get("/{farm_id}/suggestions")
def get_smart_suggestions(
    farm_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Akıllı önerileri getir"""
    # Çiftlik sahipliğini kontrol et
    farm = crud.get_farm(db=db, farm_id=farm_id)
    if not farm or farm.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Bu çiftliğe erişim yetkiniz yok")
    
    chat_service = SmartFarmChatService(db)
    suggestions = chat_service.get_smart_suggestions(farm_id)
    
    return {"suggestions": suggestions}
