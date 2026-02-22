from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./livestock_chatbot.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    title = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer)
    content = Column(Text, nullable=False)
    is_user = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="Hayvancılık AI Sohbet Robotu",
    description="LangChain ve RAG teknolojileriyle geliştirilmiş hayvancılık asistanı",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Sample livestock knowledge
LIVESTOCK_KNOWLEDGE = {
    "sığır": {
        "beslenme": "Sığır beslenmesinde kaba yem (ot, saman, silaj) ve kesif yem (arpa, mısır, soya) dengeli şekilde verilmelidir. Günde 50-100 litre temiz su sağlanmalıdır.",
        "sağlık": "Düzenli aşılama, temiz barınak, dengeli beslenme sığır sağlığı için önemlidir. Mastitis, ayak hastalıkları ve solunum yolu hastalıklarına dikkat edilmelidir.",
        "üretim": "Süt sığırı yetiştiriciliğinde Holstein, Simental gibi yüksek verimli ırklar tercih edilir. Düzenli sağım ve kayıt tutma önemlidir."
    },
    "kümes_hayvanları": {
        "beslenme": "Tavuk beslenmesinde yaş dönemine göre farklı yemler kullanılır: başlangıç yemi (0-6 hafta), büyütme yemi (6-18 hafta), yumurta yemi (18+ hafta).",
        "barınak": "Kümes tasarımında tavuk başına 0.1-0.15 m² alan, iyi havalandırma, 14-16 saat aydınlatma ve 18-22°C sıcaklık sağlanmalıdır.",
        "sağlık": "Kümes hijyeni, düzenli temizlik ve dezenfeksiyon hastalık kontrolü için kritiktir. Newcastle, Gumboro gibi hastalıklara karşı aşılama yapılmalıdır."
    },
    "koyun_keçi": {
        "beslenme": "Koyun ve keçi beslenmesinde mer'a en ekonomik besin kaynağıdır. Kaba yem (kuru ot, saman, silaj) ve kesif yem (tahıl, kepek) dengeli verilmelidir.",
        "üretim": "Koyun ve keçi üretiminde mevsimsel çiftleşme, 5 ay gebelik süresi, temiz doğum alanı ve kuzu/oğlak bakımı önemlidir.",
        "sağlık": "Mer'a döneminde parazit kontrolü, düzenli aşılama ve temiz su sağlanması sağlık için kritiktir."
    }
}

def get_ai_response(question: str) -> str:
    """Basit AI yanıt sistemi (OpenAI olmadan)"""
    question_lower = question.lower()
    
    # Kategori tespiti
    if any(word in question_lower for word in ["sığır", "inek", "dana", "buzağı"]):
        category = "sığır"
    elif any(word in question_lower for word in ["tavuk", "kümes", "yumurta", "horoz"]):
        category = "kümes_hayvanları"
    elif any(word in question_lower for word in ["koyun", "keçi", "kuzu", "oğlak"]):
        category = "koyun_keçi"
    else:
        category = "genel"
    
    # Alt kategori tespiti
    if any(word in question_lower for word in ["beslenme", "yem", "besin"]):
        subcategory = "beslenme"
    elif any(word in question_lower for word in ["sağlık", "hastalık", "aşı"]):
        subcategory = "sağlık"
    elif any(word in question_lower for word in ["üretim", "doğum", "yavru"]):
        subcategory = "üretim"
    elif any(word in question_lower for word in ["barınak", "kümes", "ahır"]):
        subcategory = "barınak"
    else:
        subcategory = "genel"
    
    # Yanıt oluşturma
    if category in LIVESTOCK_KNOWLEDGE and subcategory in LIVESTOCK_KNOWLEDGE[category]:
        response = LIVESTOCK_KNOWLEDGE[category][subcategory]
    else:
        response = "Hayvancılık konularında size yardımcı olmaya çalışıyorum. Daha spesifik bir soru sorabilir misiniz? Sığır, kümes hayvanları veya koyun/keçi konularında sorularınızı yöneltebilirsiniz."
    
    return f"Hayvancılık konusunda size yardımcı olmak için aşağıdaki bilgileri paylaşıyorum:\n\n{response}\n\nBaşka sorularınız varsa çekinmeden sorabilirsiniz!"

@app.get("/")
async def root():
    return {
        "message": "🐄 Hayvancılık AI Sohbet Robotu",
        "version": "1.0.0",
        "status": "Çalışıyor",
        "docs": "/docs"
    }

@app.get("/chat", response_class=HTMLResponse)
async def chat_interface():
    try:
        with open("static/simple_chat.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Chat interface not found</h1>", status_code=404)

@app.post("/api/chat")
async def chat_endpoint(request: dict, db: Session = Depends(get_db)):
    """Basit chat endpoint"""
    message = request.get("message", "")
    user_id = request.get("user_id", 1)  # Basit kullanıcı ID
    
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")
    
    # AI yanıtı al
    ai_response = get_ai_response(message)
    
    # Konuşma oluştur (basit)
    conversation = Conversation(
        user_id=user_id,
        title=message[:50] + "..."
    )
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    
    # Mesajları kaydet
    user_message = Message(
        conversation_id=conversation.id,
        content=message,
        is_user=True
    )
    db.add(user_message)
    
    ai_message = Message(
        conversation_id=conversation.id,
        content=ai_response,
        is_user=False
    )
    db.add(ai_message)
    db.commit()
    
    return {
        "response": ai_response,
        "conversation_id": conversation.id
    }

@app.get("/admin", response_class=HTMLResponse)
async def admin_interface():
    return HTMLResponse(content="""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Admin Panel - Hayvancılık AI</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #4CAF50; text-align: center; margin-bottom: 30px; }
            .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px; }
            .stat-card { background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); color: white; padding: 20px; border-radius: 10px; text-align: center; }
            .stat-card h3 { font-size: 2em; margin-bottom: 5px; }
            .info { background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0; }
            .btn { background: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin: 5px; text-decoration: none; display: inline-block; }
            .btn:hover { background: #45a049; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔧 Admin Panel - Hayvancılık AI</h1>
            <div class="stats">
                <div class="stat-card">
                    <h3>✅</h3>
                    <p>Sistem Aktif</p>
                </div>
                <div class="stat-card">
                    <h3>🐄</h3>
                    <p>Hayvancılık AI</p>
                </div>
                <div class="stat-card">
                    <h3>💬</h3>
                    <p>Sohbet Sistemi</p>
                </div>
            </div>
            <div class="info">
                <h3>📊 Sistem Durumu</h3>
                <p>✅ Hayvancılık AI Sohbet Robotu başarıyla çalışıyor</p>
                <p>✅ Veritabanı bağlantısı aktif</p>
                <p>✅ API endpoint'leri hazır</p>
                <p>✅ Chat arayüzü erişilebilir</p>
            </div>
            <div class="info">
                <h3>🎯 Özellikler</h3>
                <ul>
                    <li>🤖 Basit AI yanıt sistemi</li>
                    <li>📚 Hayvancılık bilgi bankası</li>
                    <li>💾 Konuşma geçmişi kaydı</li>
                    <li>🎨 Modern web arayüzü</li>
                    <li>📱 Responsive tasarım</li>
                </ul>
            </div>
            <div style="text-align: center;">
                <a href="/chat" class="btn">💬 Chat Arayüzü</a>
                <a href="/docs" class="btn">📚 API Dokümantasyonu</a>
                <a href="/" class="btn">🏠 Ana Sayfa</a>
            </div>
        </div>
    </body>
    </html>
    """)

# Authentication endpoints (basit versiyon)
@app.post("/auth/register")
async def register(request: dict):
    return {"message": "Kayıt sistemi basit versiyonda aktif değil. Chat arayüzünü kullanabilirsiniz.", "status": "info"}

@app.post("/auth/login")
async def login(request: dict):
    return {"message": "Giriş sistemi basit versiyonda aktif değil. Chat arayüzünü kullanabilirsiniz.", "status": "info"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}

if __name__ == "__main__":
    import os
    
    # Port ayarı (Railway, Heroku gibi platformlar için)
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print("=" * 60)
    print("🐄 Hayvancılık AI Sohbet Robotu")
    print("=" * 60)
    print("🚀 Uygulama başlatılıyor...")
    print(f"📱 Kullanıcı Arayüzü: http://{host}:{port}/chat")
    print(f"🔧 Admin Paneli: http://{host}:{port}/admin")
    print(f"📚 API Dokümantasyonu: http://{host}:{port}/docs")
    print(f"🏠 Ana Sayfa: http://{host}:{port}")
    print("=" * 60)
    
    uvicorn.run(app, host=host, port=port)
