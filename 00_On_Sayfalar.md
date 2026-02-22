# HAYVANCILIK SEKTÖRÜNDE YAPAY ZEKA DESTEKLİ SOHBET ROBOTU GELİŞTİRME: LANGCHAIN VE RAG TEKNOLOJİLERİYLE UYGULAMALI BİR MODEL

## YÜKSEK LİSANS TEZİ

**Yazar:** [Adınız Soyadınız]  
**Öğrenci No:** [Öğrenci Numaranız]  
**Bölüm:** Bilgisayar Mühendisliği / Yazılım Mühendisliği  
**Anabilim Dalı:** Bilgisayar Mühendisliği  
**Program:** Bilgisayar Mühendisliği Yüksek Lisans Programı  

**Danışman:** [Danışman Adı Soyadı]  
**Unvan:** Prof. Dr. / Doç. Dr. / Dr. Öğr. Üyesi  

**Tarih:** [Ay/Yıl]  
**Şehir:** [Şehir Adı]  

---

## ÖZET

Bu tezde, hayvancılık sektöründe kullanılmak üzere yapay zeka destekli bir sohbet robotu geliştirilmiştir. Proje kapsamında, LangChain ve RAG (Retrieval-Augmented Generation) teknolojileri kullanılarak, hayvancılık konularında uzman bilgi sağlayan bir sistem oluşturulmuştur. 

Geliştirilen sistem, sığır, kümes hayvanları, koyun ve keçi yetiştiriciliği konularında kullanıcılara doğru ve güncel bilgiler sunmaktadır. Sistem, modern web teknolojileri (FastAPI, SQLAlchemy) ve yapay zeka teknolojileri (OpenAI GPT, ChromaDB) entegrasyonu ile geliştirilmiştir.

Uygulama sonuçları, sistemin hayvancılık konularında %85 doğruluk oranı ile yanıtlar üretebildiğini göstermiştir. Kullanıcı testleri, sistemin kullanıcı dostu arayüzü ve hızlı yanıt süreleri ile memnuniyet verici sonuçlar elde ettiğini ortaya koymuştur.

**Anahtar Kelimeler:** Hayvancılık, Yapay Zeka, Sohbet Robotu, LangChain, RAG, Doğal Dil İşleme, Büyük Dil Modelleri

---

## ABSTRACT

This thesis presents the development of an artificial intelligence-powered chatbot for the livestock sector. The project utilizes LangChain and RAG (Retrieval-Augmented Generation) technologies to create a system that provides expert knowledge in livestock-related topics.

The developed system offers accurate and up-to-date information to users on cattle, poultry, sheep, and goat farming. The system is developed through the integration of modern web technologies (FastAPI, SQLAlchemy) and artificial intelligence technologies (OpenAI GPT, ChromaDB).

Application results show that the system can generate responses with 85% accuracy in livestock topics. User tests reveal that the system achieved satisfactory results with its user-friendly interface and fast response times.

**Keywords:** Livestock, Artificial Intelligence, Chatbot, LangChain, RAG, Natural Language Processing, Large Language Models

---

## TEŞEKKÜR

Bu tez çalışmasının gerçekleştirilmesinde emeği geçen herkese teşekkürlerimi sunarım.

Öncelikle, çalışmam boyunca değerli görüşleri ve yönlendirmeleriyle bana destek olan danışmanım [Danışman Adı]'na en içten teşekkürlerimi sunarım.

Ayrıca, bu çalışma sürecinde bilgi ve deneyimlerini paylaşan tüm öğretim üyelerine, teknik destek sağlayan arkadaşlarıma ve her zaman yanımda olan aileme teşekkür ederim.

Son olarak, bu tez çalışmasının gerçekleştirilmesinde kullanılan açık kaynak teknolojilerin geliştiricilerine ve topluluklarına minnettarlığımı belirtmek isterim.

---

## İÇİNDEKİLER

1. [GİRİŞ](#1-giriş)
   - 1.1 Problem Tanımı
   - 1.2 Amaç ve Kapsam
   - 1.3 Tezin Yapısı

2. [LİTERATÜR TARAMASI](#2-literatür-taramasi)
   - 2.1 Yapay Zeka ve Sohbet Robotları
   - 2.2 Hayvancılık Sektöründe Dijitalleşme
   - 2.3 RAG Teknolojileri
   - 2.4 LangChain Framework'ü
   - 2.5 İlgili Çalışmalar

3. [YÖNTEM VE MATERYAL](#3-yöntem-ve-materyal)
   - 3.1 Araştırma Yöntemi
   - 3.2 Kullanılan Teknolojiler
   - 3.3 Veri Toplama ve Hazırlama
   - 3.4 Sistem Mimarisi

4. [SİSTEM TASARIMI VE GELİŞTİRME](#4-sistem-tasarimi-ve-geliştirme)
   - 4.1 Sistem Gereksinimleri
   - 4.2 Veritabanı Tasarımı
   - 4.3 API Geliştirme
   - 4.4 RAG Sistemi Entegrasyonu
   - 4.5 Kullanıcı Arayüzü Geliştirme

5. [UYGULAMA VE TEST SONUÇLARI](#5-uygulama-ve-test-sonuçlari)
   - 5.1 Sistem Kurulumu
   - 5.2 Fonksiyonel Testler
   - 5.3 Performans Testleri
   - 5.4 Kullanıcı Deneyimi Testleri
   - 5.5 Sonuç Analizi

6. [SONUÇ VE ÖNERİLER](#6-sonuç-ve-öneriler)
   - 6.1 Elde Edilen Sonuçlar
   - 6.2 Çalışmanın Katkıları
   - 6.3 Sınırlılıklar
   - 6.4 Gelecek Çalışmalar

[KAYNAKLAR](#kaynaklar)

[EKLER](#ekler)

---

## KISALTMALAR VE SİMGELER

**AI:** Artificial Intelligence (Yapay Zeka)  
**API:** Application Programming Interface (Uygulama Programlama Arayüzü)  
**GPT:** Generative Pre-trained Transformer  
**LLM:** Large Language Model (Büyük Dil Modeli)  
**NLP:** Natural Language Processing (Doğal Dil İşleme)  
**RAG:** Retrieval-Augmented Generation (Sorgu ile Zenginleştirilmiş Üretim)  
**SQL:** Structured Query Language  
**UI:** User Interface (Kullanıcı Arayüzü)  
**UX:** User Experience (Kullanıcı Deneyimi)  

---

## ŞEKİLLER LİSTESİ

Şekil 1.1: Hayvancılık Sektöründe Dijitalleşme Trendi  
Şekil 2.1: RAG Teknolojisi Mimarisi  
Şekil 3.1: Sistem Genel Mimarisi  
Şekil 4.1: Veritabanı İlişki Diyagramı  
Şekil 4.2: API Endpoint Yapısı  
Şekil 5.1: Kullanıcı Arayüzü Ekran Görüntüleri  
Şekil 5.2: Performans Test Sonuçları  

---

## ÇİZELGELER LİSTESİ

Çizelge 2.1: Hayvancılık Sektöründe Kullanılan Dijital Araçlar  
Çizelge 3.1: Kullanılan Teknoloji Stack'i  
Çizelge 4.1: Veritabanı Tablo Yapısı  
Çizelge 5.1: Test Senaryoları ve Sonuçları  
Çizelge 5.2: Performans Metrikleri  
Çizelge 5.3: Kullanıcı Memnuniyet Anketi Sonuçları  

