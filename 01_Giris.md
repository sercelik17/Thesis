# 1. GİRİŞ

## 1.1 Problem Tanımı

Hayvancılık sektörü, dünya genelinde gıda güvenliği ve ekonomik kalkınma açısından kritik öneme sahip bir sektördür. Türkiye'de de hayvancılık, tarım sektörünün önemli bir bileşeni olarak hem ekonomik hem de sosyal açıdan büyük değer taşımaktadır. Ancak, bu sektörde çalışan üreticiler ve uzmanlar, sürekli değişen teknolojiler, yeni hastalık türleri, beslenme programları ve üretim teknikleri hakkında güncel bilgilere ihtiyaç duymaktadır.

Geleneksel bilgi edinme yöntemleri olan kitaplar, dergiler ve uzman danışmanlıkları, günümüzün hızlı tempolu dünyasında yetersiz kalmaktadır. Özellikle acil durumlarda veya anlık sorulara ihtiyaç duyulduğunda, bu kaynaklara erişim sınırlı olmaktadır. Ayrıca, hayvancılık konularında uzman bilgiye sahip kişilerin sayısı sınırlı olduğundan, tüm üreticilerin bu uzmanlara erişimi mümkün değildir.

Son yıllarda yapay zeka teknolojilerindeki gelişmeler, özellikle büyük dil modelleri (LLM) ve doğal dil işleme (NLP) alanlarındaki ilerlemeler, bu sorunlara çözüm sunma potansiyeli taşımaktadır. Ancak, genel amaçlı yapay zeka sistemleri, hayvancılık gibi özelleşmiş alanlarda yeterli doğruluk ve güvenilirlik sağlayamamaktadır.

Bu bağlamda, hayvancılık sektörüne özel olarak tasarlanmış, güvenilir bilgi kaynaklarına dayalı ve sürekli güncellenebilen bir yapay zeka destekli sohbet robotu ihtiyacı ortaya çıkmaktadır.

## 1.2 Amaç ve Kapsam

### 1.2.1 Araştırmanın Amacı

Bu tez çalışmasının temel amacı, hayvancılık sektöründe kullanılmak üzere yapay zeka destekli bir sohbet robotu geliştirmektir. Geliştirilen sistem, aşağıdaki özelliklere sahip olacaktır:

1. **Uzman Bilgi Sağlama**: Sığır, kümes hayvanları, koyun ve keçi yetiştiriciliği konularında doğru ve güncel bilgiler sunma
2. **Kullanıcı Dostu Arayüz**: Teknik bilgi gerektirmeyen, kolay kullanılabilir web tabanlı arayüz
3. **Sürekli Öğrenme**: Yeni bilgilerin sisteme eklenebilmesi ve mevcut bilgilerin güncellenebilmesi
4. **Güvenilir Kaynaklar**: Akademik ve uzman kaynaklara dayalı bilgi sağlama
5. **Hızlı Yanıt**: Kullanıcı sorularına anında ve doğru yanıtlar verme

### 1.2.2 Araştırmanın Kapsamı

Bu çalışma aşağıdaki konuları kapsamaktadır:

**Teknik Kapsam:**
- LangChain framework'ü kullanarak RAG (Retrieval-Augmented Generation) sistemi geliştirme
- FastAPI ile modern web API'si oluşturma
- SQLAlchemy ile veritabanı yönetimi
- ChromaDB ile vektör veritabanı entegrasyonu
- OpenAI GPT modelleri ile doğal dil işleme

**İçerik Kapsamı:**
- Sığır yetiştiriciliği (beslenme, sağlık, üretim)
- Kümes hayvanları yetiştiriciliği (tavuk, hindi)
- Koyun ve keçi yetiştiriciliği
- Barınak tasarımı ve yönetimi
- Sağlık ve aşılama programları
- Ekonomik analiz ve verimlilik

**Kullanıcı Kapsamı:**
- Hayvancılık üreticileri
- Veteriner hekimler
- Tarım danışmanları
- Öğrenciler ve araştırmacılar
- Hayvancılık sektörü profesyonelleri

### 1.2.3 Araştırmanın Sınırlılıkları

Bu çalışma aşağıdaki sınırlılıklara sahiptir:

1. **Dil Sınırlılığı**: Sistem şu anda sadece Türkçe dil desteği sunmaktadır
2. **İçerik Sınırlılığı**: Hayvancılık konuları ile sınırlıdır, diğer tarım alanlarını kapsamamaktadır
3. **Teknoloji Sınırlılığı**: OpenAI GPT modelleri kullanılmaktadır, diğer LLM'ler test edilmemiştir
4. **Test Sınırlılığı**: Sistem testleri sınırlı sayıda kullanıcı ile gerçekleştirilmiştir

## 1.3 Tezin Yapısı

Bu tez altı ana bölümden oluşmaktadır:

**1. Bölüm - Giriş**: Problem tanımı, araştırmanın amacı ve kapsamı, tezin yapısı
**2. Bölüm - Literatür Taraması**: Yapay zeka, sohbet robotları, RAG teknolojileri ve ilgili çalışmalar
**3. Bölüm - Yöntem ve Materyal**: Araştırma yöntemi, kullanılan teknolojiler ve sistem mimarisi
**4. Bölüm - Sistem Tasarımı ve Geliştirme**: Sistem gereksinimleri, veritabanı tasarımı, API geliştirme
**5. Bölüm - Uygulama ve Test Sonuçları**: Sistem kurulumu, testler ve sonuç analizi
**6. Bölüm - Sonuç ve Öneriler**: Elde edilen sonuçlar, katkılar ve gelecek çalışmalar

## 1.4 Araştırmanın Önemi

Bu araştırma, aşağıdaki nedenlerle önemlidir:

### 1.4.1 Bilimsel Önem
- Hayvancılık sektöründe yapay zeka teknolojilerinin uygulanması
- RAG teknolojilerinin özelleşmiş alanlarda kullanımı
- Doğal dil işleme tekniklerinin pratik uygulaması

### 1.4.2 Teknolojik Önem
- Modern web teknolojileri ile yapay zeka entegrasyonu
- Vektör veritabanları ve embedding tekniklerinin kullanımı
- API tabanlı sistem mimarisi geliştirme

### 1.4.3 Sosyal ve Ekonomik Önem
- Hayvancılık sektöründe dijitalleşme
- Bilgiye erişimde eşitlik sağlama
- Üretim verimliliğini artırma potansiyeli

### 1.4.4 Eğitim Önemi
- Hayvancılık eğitiminde teknoloji kullanımı
- Sürekli öğrenme ve güncelleme imkanı
- Uzaktan danışmanlık hizmeti

## 1.5 Araştırma Soruları

Bu tez çalışması aşağıdaki araştırma sorularına yanıt aramaktadır:

1. **Ana Araştırma Sorusu**: Hayvancılık sektöründe yapay zeka destekli sohbet robotu nasıl geliştirilebilir?

2. **Alt Araştırma Soruları**:
   - RAG teknolojileri hayvancılık konularında ne kadar etkili sonuçlar üretebilir?
   - LangChain framework'ü bu tür özelleşmiş sistemler için uygun mudur?
   - Geliştirilen sistem kullanıcı memnuniyeti açısından nasıl değerlendirilir?
   - Sistem performansı ve doğruluk oranları kabul edilebilir seviyede midir?
   - Hayvancılık sektöründe bu tür sistemlere olan ihtiyaç ve kabul düzeyi nedir?

## 1.6 Araştırma Hipotezleri

Bu çalışma aşağıdaki hipotezleri test etmektedir:

**H1**: RAG teknolojileri kullanılarak geliştirilen hayvancılık sohbet robotu, geleneksel bilgi kaynaklarına göre daha hızlı ve doğru yanıtlar sağlayabilir.

**H2**: LangChain framework'ü ile geliştirilen sistem, hayvancılık konularında %80 ve üzeri doğruluk oranına ulaşabilir.

**H3**: Geliştirilen sistem, kullanıcılar tarafından kullanışlı ve güvenilir olarak değerlendirilecektir.

**H4**: Sistem, hayvancılık sektöründe bilgiye erişimde eşitlik sağlama konusunda katkıda bulunacaktır.

## 1.7 Araştırmanın Katkıları

Bu araştırma aşağıdaki katkıları sağlamaktadır:

### 1.7.1 Teorik Katkılar
- Hayvancılık sektöründe yapay zeka uygulamaları literatürüne katkı
- RAG teknolojilerinin özelleşmiş alanlarda kullanım metodolojisi
- Doğal dil işleme tekniklerinin pratik uygulama örnekleri

### 1.7.2 Pratik Katkılar
- Hayvancılık sektörü için kullanıma hazır yapay zeka sistemi
- Açık kaynak kodlu, geliştirilebilir sistem mimarisi
- Diğer tarım alanları için uyarlanabilir teknoloji altyapısı

### 1.7.3 Metodolojik Katkılar
- Özelleşmiş alanlar için RAG sistemi geliştirme metodolojisi
- Yapay zeka sistemlerinin değerlendirme kriterleri
- Kullanıcı deneyimi test yöntemleri

Bu bölümde, araştırmanın temel problem tanımı, amacı, kapsamı ve önemi detaylı olarak açıklanmıştır. Bir sonraki bölümde, konuyla ilgili literatür taraması ve mevcut çalışmalar incelenecektir.

