from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models, schemas, crud
from app.config import settings
from app.routers import auth, chat, admin, farm
from app.auth import get_password_hash, get_current_active_user

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="Hayvancılık sektöründe yapay zeka destekli sohbet robotu",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(admin.router)
app.include_router(farm.router)

@app.on_event("startup")
async def startup_event():
    """Initialize admin user on startup"""
    db = next(get_db())
    try:
        # Check if admin user exists
        admin_user = crud.get_user_by_email(db, settings.ADMIN_EMAIL)
        if not admin_user:
            # Create admin user
            admin_user_data = {
                "email": settings.ADMIN_EMAIL,
                "username": "admin",
                "password": settings.ADMIN_PASSWORD,
                "full_name": "System Administrator"
            }
            admin_user = crud.create_user(db, schemas.UserCreate(**admin_user_data))
            # Make user admin
            admin_user.is_admin = True
            db.commit()
            print(f"Admin user created: {settings.ADMIN_EMAIL}")
        else:
            print(f"Admin user already exists: {settings.ADMIN_EMAIL}")
    except Exception as e:
        print(f"Error creating admin user: {e}")
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def root():
    """Ana sayfa - HTML arayüzü"""
    try:
        with open("static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        # Eğer index.html yoksa basit bir HTML döndür
        html_content = """
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Akıllı Çiftlik Yönetim Sistemi</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
                .container { text-align: center; background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; backdrop-filter: blur(10px); }
                h1 { font-size: 3em; margin-bottom: 20px; }
                .btn { display: inline-block; padding: 15px 30px; margin: 10px; background: #4CAF50; color: white; text-decoration: none; border-radius: 25px; font-size: 1.2em; transition: transform 0.3s; }
                .btn:hover { transform: translateY(-3px); }
                .features { margin-top: 30px; }
                .feature { margin: 10px 0; font-size: 1.1em; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🏡 Akıllı Çiftlik Yönetim Sistemi</h1>
                <p style="font-size: 1.3em; margin-bottom: 30px;">Yapay zeka destekli çiftlik yönetimi</p>
                
                <a href="/login" class="btn">🔐 Giriş Yap</a>
                <a href="/register" class="btn">📝 Kayıt Ol</a>
                <a href="/smart-farm" class="btn">🚀 Çiftlik Yönetimi</a>
                <a href="/docs" class="btn">📚 API Dokümantasyonu</a>
                
                <div class="features">
                    <h3>Özellikler:</h3>
                    <div class="feature">🐄 Hayvan Takibi</div>
                    <div class="feature">📊 Üretim Analizi</div>
                    <div class="feature">💉 Sağlık Kontrolü</div>
                    <div class="feature">💰 Finansal Raporlama</div>
                    <div class="feature">🤖 AI Asistan</div>
                </div>
            </div>
        </body>
        </html>
        """
        return HTMLResponse(content=html_content)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Serve static files (for frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/chat", response_class=HTMLResponse)
async def chat_interface():
    """Serve chat interface"""
    try:
        with open("static/chat.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Chat interface not found</h1>", status_code=404)

@app.get("/admin", response_class=HTMLResponse)
async def admin_interface():
    """Serve admin interface"""
    try:
        with open("static/admin.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Admin interface not found</h1>", status_code=404)

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    """Giriş sayfası"""
    html_content = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Giriş Yap - Akıllı Çiftlik</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
            .container { background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; backdrop-filter: blur(10px); width: 100%; max-width: 400px; }
            h1 { text-align: center; margin-bottom: 30px; }
            .form-group { margin-bottom: 20px; }
            label { display: block; margin-bottom: 5px; }
            input { width: 100%; padding: 12px; border: none; border-radius: 8px; font-size: 16px; box-sizing: border-box; }
            button { width: 100%; padding: 15px; background: #4CAF50; color: white; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; margin-top: 10px; }
            button:hover { background: #45a049; }
            .links { text-align: center; margin-top: 20px; }
            .links a { color: white; text-decoration: none; margin: 0 10px; }
            .error { color: #ff6b6b; margin-top: 10px; text-align: center; }
            .success { color: #51cf66; margin-top: 10px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔐 Giriş Yap</h1>
            <form id="loginForm">
                <div class="form-group">
                    <label for="email">E-posta:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="password">Şifre:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <button type="submit">Giriş Yap</button>
            </form>
            <div id="message"></div>
            <div class="links">
                <a href="/">🏠 Ana Sayfa</a>
                <a href="/register">📝 Kayıt Ol</a>
            </div>
        </div>
        
        <script>
            document.getElementById('loginForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const email = document.getElementById('email').value;
                const password = document.getElementById('password').value;
                const messageDiv = document.getElementById('message');
                
                try {
                    const response = await fetch('/auth/login', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ email, password })
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        localStorage.setItem('token', data.access_token);
                        messageDiv.innerHTML = '<div class="success">Giriş başarılı! Yönlendiriliyorsunuz...</div>';
                        setTimeout(() => {
                            window.location.href = '/smart-farm';
                        }, 1500);
                    } else {
                        messageDiv.innerHTML = '<div class="error">Giriş başarısız: ' + (data.detail || 'Bilinmeyen hata') + '</div>';
                    }
                } catch (error) {
                    messageDiv.innerHTML = '<div class="error">Bağlantı hatası: ' + error.message + '</div>';
                }
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/register", response_class=HTMLResponse)
async def register_page():
    """Kayıt sayfası"""
    html_content = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kayıt Ol - Akıllı Çiftlik</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
            .container { background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; backdrop-filter: blur(10px); width: 100%; max-width: 400px; }
            h1 { text-align: center; margin-bottom: 30px; }
            .form-group { margin-bottom: 20px; }
            label { display: block; margin-bottom: 5px; }
            input { width: 100%; padding: 12px; border: none; border-radius: 8px; font-size: 16px; box-sizing: border-box; }
            button { width: 100%; padding: 15px; background: #4CAF50; color: white; border: none; border-radius: 8px; font-size: 16px; cursor: pointer; margin-top: 10px; }
            button:hover { background: #45a049; }
            .links { text-align: center; margin-top: 20px; }
            .links a { color: white; text-decoration: none; margin: 0 10px; }
            .error { color: #ff6b6b; margin-top: 10px; text-align: center; }
            .success { color: #51cf66; margin-top: 10px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📝 Kayıt Ol</h1>
            <form id="registerForm">
                <div class="form-group">
                    <label for="email">E-posta:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="username">Kullanıcı Adı:</label>
                    <input type="text" id="username" name="username" required>
                </div>
                <div class="form-group">
                    <label for="full_name">Ad Soyad:</label>
                    <input type="text" id="full_name" name="full_name" required>
                </div>
                <div class="form-group">
                    <label for="password">Şifre:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <button type="submit">Kayıt Ol</button>
            </form>
            <div id="message"></div>
            <div class="links">
                <a href="/">🏠 Ana Sayfa</a>
                <a href="/login">🔐 Giriş Yap</a>
            </div>
        </div>
        
        <script>
            document.getElementById('registerForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const email = document.getElementById('email').value;
                const username = document.getElementById('username').value;
                const full_name = document.getElementById('full_name').value;
                const password = document.getElementById('password').value;
                const messageDiv = document.getElementById('message');
                
                try {
                    const response = await fetch('/auth/register', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ email, username, full_name, password })
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        messageDiv.innerHTML = '<div class="success">Kayıt başarılı! Giriş sayfasına yönlendiriliyorsunuz...</div>';
                        setTimeout(() => {
                            window.location.href = '/login';
                        }, 1500);
                    } else {
                        messageDiv.innerHTML = '<div class="error">Kayıt başarısız: ' + (data.detail || 'Bilinmeyen hata') + '</div>';
                    }
                } catch (error) {
                    messageDiv.innerHTML = '<div class="error">Bağlantı hatası: ' + error.message + '</div>';
                }
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/smart-farm", response_class=HTMLResponse)
async def smart_farm_interface():
    """Serve smart farm interface - authentication handled by frontend"""
    try:
        with open("static/smart_farm.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Smart farm interface not found</h1>", status_code=404)

@app.get("/cprot-edr-test", response_class=HTMLResponse)
async def cprot_edr_test():
    """C-Prot EDR test sonuçları sayfası"""
    try:
        with open("static/cprot_edr_test.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>C-Prot EDR test sayfası bulunamadı</h1>", status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
