from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="Hayvancılık AI Sohbet Robotu - Test")

@app.get("/")
async def root():
    return {
        "message": "🐄 Hayvancılık AI Sohbet Robotu",
        "status": "Çalışıyor!",
        "version": "1.0.0"
    }

@app.get("/test", response_class=HTMLResponse)
async def test_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hayvancılık AI Sohbet Robotu - Test</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 20px;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #4CAF50;
                margin-bottom: 20px;
            }
            .status {
                background: #e8f5e8;
                color: #2e7d32;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
            }
            .info {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: left;
            }
            .btn {
                background: #4CAF50;
                color: white;
                padding: 12px 24px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                margin: 10px;
                text-decoration: none;
                display: inline-block;
            }
            .btn:hover {
                background: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐄 Hayvancılık AI Sohbet Robotu</h1>
            <div class="status">
                ✅ Uygulama başarıyla çalışıyor!
            </div>
            <div class="info">
                <h3>🎯 Proje Özellikleri:</h3>
                <ul>
                    <li>🤖 LangChain ve RAG teknolojileri</li>
                    <li>💬 Hayvancılık konularında uzman AI asistanı</li>
                    <li>👥 Kullanıcı yönetim sistemi</li>
                    <li>🔧 Admin paneli</li>
                    <li>📚 Kapsamlı bilgi bankası</li>
                    <li>🎨 Modern web arayüzü</li>
                </ul>
            </div>
            <div class="info">
                <h3>📊 Hayvancılık Konuları:</h3>
                <ul>
                    <li>🐄 Sığır yetiştiriciliği</li>
                    <li>🐔 Kümes hayvanları</li>
                    <li>🐑 Koyun ve keçi</li>
                    <li>🏠 Barınak yönetimi</li>
                    <li>💊 Sağlık ve aşılama</li>
                    <li>💰 Ekonomik analiz</li>
                </ul>
            </div>
            <a href="/docs" class="btn">📚 API Dokümantasyonu</a>
            <a href="/" class="btn">🏠 Ana Sayfa</a>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    print("=" * 60)
    print("🐄 Hayvancılık AI Sohbet Robotu - Test Uygulaması")
    print("=" * 60)
    print("🚀 Uygulama başlatılıyor...")
    print("📱 Test Sayfası: http://localhost:8000/test")
    print("📚 API Dokümantasyonu: http://localhost:8000/docs")
    print("🏠 Ana Sayfa: http://localhost:8000")
    print("=" * 60)
    
    uvicorn.run(app, host="0.0.0.0", port=8000)

