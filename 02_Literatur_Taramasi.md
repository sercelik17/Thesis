# 2. LİTERATÜR TARAMASI

## 2.1 Yapay Zeka ve Sohbet Robotları

### 2.1.1 Yapay Zeka Tarihçesi ve Gelişimi

Yapay zeka (AI) kavramı, 1950'li yıllarda Alan Turing'in "Makineler Düşünebilir mi?" sorusu ile başlamıştır (Turing, 1950). İlk yapay zeka programları 1950'lerin sonunda geliştirilmiş, ancak gerçek anlamda pratik uygulamalar 1990'lardan sonra ortaya çıkmıştır (Russell & Norvig, 2020).

Son yıllarda, özellikle 2010'lardan itibaren derin öğrenme (deep learning) teknolojilerindeki gelişmeler, yapay zeka alanında devrim yaratmıştır. Büyük dil modelleri (LLM) olarak adlandırılan sistemler, doğal dil işleme alanında önemli başarılar elde etmiştir (Brown et al., 2020).

### 2.1.2 Sohbet Robotları (Chatbots)

Sohbet robotları, kullanıcılarla doğal dil aracılığıyla etkileşim kurabilen yazılım programlarıdır. İlk sohbet robotu olan ELIZA, 1966 yılında Joseph Weizenbaum tarafından geliştirilmiştir (Weizenbaum, 1966). O zamandan beri sohbet robotları, kural tabanlı sistemlerden makine öğrenmesi tabanlı sistemlere doğru evrim geçirmiştir.

Modern sohbet robotları, üç ana kategoride sınıflandırılabilir:

1. **Kural Tabanlı Sistemler**: Önceden tanımlanmış kurallar ve şablonlar kullanır
2. **Makine Öğrenmesi Tabanlı Sistemler**: Geçmiş verilerden öğrenerek yanıtlar üretir
3. **Hibrit Sistemler**: Her iki yaklaşımı birleştirir

### 2.1.3 Büyük Dil Modelleri (LLM)

Büyük dil modelleri, milyarlarca parametreye sahip derin öğrenme modelleridir. Bu modeller, büyük metin veri setleri üzerinde eğitilerek doğal dil anlama ve üretme yetenekleri kazanır (Vaswani et al., 2017).

Önemli LLM örnekleri:
- **GPT (Generative Pre-trained Transformer)**: OpenAI tarafından geliştirilen seri
- **BERT (Bidirectional Encoder Representations from Transformers)**: Google tarafından geliştirilen model
- **T5 (Text-to-Text Transfer Transformer)**: Google tarafından geliştirilen model

## 2.2 Hayvancılık Sektöründe Dijitalleşme

### 2.2.1 Dijital Tarım ve Hayvancılık

Dijital tarım, tarım ve hayvancılık sektöründe bilgi ve iletişim teknolojilerinin kullanımını ifade eder. Bu kavram, "Tarım 4.0" veya "Akıllı Tarım" olarak da adlandırılmaktadır (Wolfert et al., 2017).

Hayvancılık sektöründe dijitalleşme, aşağıdaki alanlarda kendini göstermektedir:

1. **Hassas Hayvancılık**: Sensörler ve IoT cihazları ile hayvan sağlığı ve performansının izlenmesi
2. **Otomatik Besleme Sistemleri**: Yapay zeka destekli beslenme programları
3. **Sağlık İzleme**: Görüntü işleme ve makine öğrenmesi ile hastalık tespiti
4. **Üretim Optimizasyonu**: Veri analizi ile üretim süreçlerinin iyileştirilmesi

### 2.2.2 Hayvancılıkta Bilgi Yönetimi

Hayvancılık sektöründe bilgi yönetimi, üreticilerin karar verme süreçlerinde kritik öneme sahiptir. Geleneksel bilgi kaynakları şunlardır:

- **Uzman Danışmanlığı**: Veteriner hekimler ve tarım danışmanları
- **Yayınlar**: Bilimsel dergiler, kitaplar ve raporlar
- **Eğitim Programları**: Kurslar ve seminerler
- **Deneyim Paylaşımı**: Üretici toplulukları ve kooperatifler

Ancak, bu kaynaklara erişimde çeşitli sınırlılıklar bulunmaktadır:
- Coğrafi uzaklık
- Maliyet yükü
- Zaman kısıtları
- Dil bariyerleri
- Güncellik sorunları

## 2.3 RAG Teknolojileri

### 2.3.1 RAG (Retrieval-Augmented Generation) Kavramı

RAG, büyük dil modellerinin bilgi tabanları ile birleştirilmesi yoluyla daha doğru ve güncel yanıtlar üretilmesini sağlayan bir yaklaşımdır (Lewis et al., 2020). Bu teknoloji, iki ana bileşenden oluşur:

1. **Retrieval (Alma)**: İlgili bilgilerin veri tabanından çıkarılması
2. **Generation (Üretim)**: Çıkarılan bilgilerin kullanılarak yanıt üretilmesi

### 2.3.2 RAG Sistem Mimarisi

RAG sistemi genellikle şu bileşenlerden oluşur:

1. **Veri Hazırlama**: Kaynak belgelerin işlenmesi ve vektörleştirilmesi
2. **Vektör Veritabanı**: Embedding'lerin saklanması
3. **Retrieval Sistemi**: Benzerlik araması yapan sistem
4. **LLM Entegrasyonu**: Yanıt üretimi için büyük dil modeli

### 2.3.3 RAG'in Avantajları

RAG teknolojisinin temel avantajları şunlardır:

- **Güncellik**: Bilgi tabanı sürekli güncellenebilir
- **Doğruluk**: Güvenilir kaynaklara dayalı yanıtlar
- **Şeffaflık**: Yanıtların hangi kaynaklara dayandığı belirtilebilir
- **Maliyet Etkinliği**: LLM'lerin eğitimi yerine bilgi tabanı kullanımı
- **Özelleştirilebilirlik**: Belirli alanlara özel sistemler geliştirilebilir

### 2.3.4 RAG Uygulama Alanları

RAG teknolojisi çeşitli alanlarda uygulanmaktadır:

- **Müşteri Hizmetleri**: Şirket bilgilerine dayalı sohbet robotları
- **Eğitim**: Akademik içerik tabanlı öğrenme sistemleri
- **Sağlık**: Tıbbi bilgi tabanları ile entegre sistemler
- **Hukuk**: Yasal belgeler tabanlı danışmanlık sistemleri
- **Tarım**: Tarımsal bilgi tabanları ile uzman sistemler

## 2.4 LangChain Framework'ü

### 2.4.1 LangChain Tanımı ve Özellikleri

LangChain, büyük dil modelleri ile uygulamalar geliştirmek için tasarlanmış açık kaynaklı bir framework'tür (Chase, 2022). Bu framework, LLM'lerin gerçek dünya uygulamalarında kullanılmasını kolaylaştırmak amacıyla geliştirilmiştir.

LangChain'in temel özellikleri:

1. **Modüler Yapı**: Farklı bileşenlerin kolayca birleştirilmesi
2. **Çoklu LLM Desteği**: Farklı sağlayıcıların entegrasyonu
3. **Vektör Veritabanı Entegrasyonu**: ChromaDB, Pinecone gibi sistemler
4. **Araç Entegrasyonu**: Harici API'ler ve veri kaynakları
5. **Zincirleme (Chaining)**: Farklı işlemlerin sıralı olarak yürütülmesi

### 2.4.2 LangChain Bileşenleri

LangChain framework'ü şu ana bileşenlerden oluşur:

1. **LLMs**: Büyük dil modelleri için arayüzler
2. **Prompts**: Prompt şablonları ve yönetimi
3. **Chains**: İşlem zincirleri
4. **Agents**: Akıllı ajanlar
5. **Memory**: Konuşma hafızası
6. **Vector Stores**: Vektör veritabanları
7. **Document Loaders**: Belge yükleme araçları

### 2.4.3 LangChain ile RAG Geliştirme

LangChain, RAG sistemleri geliştirmek için özel araçlar sağlar:

- **Document Loaders**: PDF, Word, web sayfaları gibi kaynaklardan veri yükleme
- **Text Splitters**: Uzun metinleri parçalara bölme
- **Embeddings**: Metinleri vektörlere dönüştürme
- **Vector Stores**: Vektör veritabanları ile entegrasyon
- **Retrieval QA**: Soru-cevap sistemleri

## 2.5 İlgili Çalışmalar

### 2.5.1 Tarım ve Hayvancılıkta Yapay Zeka Uygulamaları

Literatürde tarım ve hayvancılık alanında yapay zeka uygulamalarına dair çeşitli çalışmalar bulunmaktadır:

**Hassas Tarım Uygulamaları:**
- Kamilaris & Prenafeta-Boldú (2018), hassas tarımda derin öğrenme uygulamalarını incelemiştir
- Liakos et al. (2018), tarımda makine öğrenmesi tekniklerini araştırmıştır

**Hayvan Sağlığı ve Davranış Analizi:**
- Neethirajan (2020), hayvancılıkta yapay zeka uygulamalarını kapsamlı olarak incelemiştir
- Taneja et al. (2020), süt sığırlarında sağlık izleme sistemleri geliştirmiştir

### 2.5.2 Sohbet Robotları ve Doğal Dil İşleme

**Genel Sohbet Robotları:**
- Adamopoulou & Moussiades (2020), sohbet robotları teknolojilerini kapsamlı olarak incelemiştir
- Abdul-Kader & Woods (2015), sohbet robotu performans değerlendirme yöntemlerini araştırmıştır

**Özelleşmiş Alan Sohbet Robotları:**
- Følstad et al. (2018), müşteri hizmetleri sohbet robotlarını incelemiştir
- Montenegro et al. (2019), eğitim alanında sohbet robotu uygulamalarını araştırmıştır

### 2.5.3 RAG Teknolojileri ve Uygulamaları

**RAG Temel Çalışmaları:**
- Lewis et al. (2020), RAG teknolojisinin temel makalesini yayınlamıştır
- Karpukhin et al. (2020), RAG sistemlerinin performansını değerlendirmiştir

**RAG Uygulama Örnekleri:**
- Petroni et al. (2019), bilgi tabanı tabanlı soru-cevap sistemleri geliştirmiştir
- Chen et al. (2017), açık alan soru-cevap sistemlerini araştırmıştır

### 2.5.4 Hayvancılıkta Bilgi Sistemleri

**Geleneksel Bilgi Sistemleri:**
- Sorensen et al. (2010), hayvancılıkta karar destek sistemlerini incelemiştir
- Banhazi et al. (2012), hayvancılıkta sensör teknolojilerini araştırmıştır

**Dijital Danışmanlık Sistemleri:**
- Wolfert et al. (2017), dijital tarım ekosistemlerini incelemiştir
- Eastwood et al. (2012), çiftçiler için bilgi sistemlerini araştırmıştır

## 2.6 Literatürdeki Boşluklar

Mevcut literatür incelendiğinde, aşağıdaki boşluklar tespit edilmiştir:

### 2.6.1 Hayvancılık Özelinde RAG Uygulamaları

- Hayvancılık sektörüne özel RAG sistemleri geliştiren çalışmalar sınırlıdır
- Türkçe hayvancılık bilgi tabanları ile RAG entegrasyonu bulunmamaktadır
- Hayvancılık uzmanları ile yapay zeka sistemlerinin etkileşimi yeterince araştırılmamıştır

### 2.6.2 Kullanıcı Deneyimi ve Kabul

- Hayvancılık sektöründe yapay zeka sistemlerine olan kabul düzeyi araştırılmamıştır
- Üreticilerin bu tür sistemleri kullanma eğilimleri bilinmemektedir
- Sistem kullanımına etki eden faktörler yeterince incelenmemiştir

### 2.6.3 Performans Değerlendirme

- Hayvancılık konularında yapay zeka sistemlerinin doğruluk oranları belirlenmemiştir
- Farklı hayvancılık alt alanlarında sistem performansı karşılaştırılmamıştır
- Kullanıcı memnuniyeti ölçüm kriterleri geliştirilmemiştir

## 2.7 Araştırmanın Literatüre Katkısı

Bu tez çalışması, yukarıda belirtilen boşlukları doldurmaya yönelik olarak aşağıdaki katkıları sağlamaktadır:

### 2.7.1 Teknik Katkılar

1. **Hayvancılık Özelinde RAG Sistemi**: İlk kez hayvancılık sektörüne özel RAG sistemi geliştirilmesi
2. **Türkçe Hayvancılık Bilgi Tabanı**: Kapsamlı Türkçe hayvancılık bilgi tabanı oluşturulması
3. **LangChain Uygulaması**: LangChain framework'ünün hayvancılık alanında pratik uygulaması

### 2.7.2 Metodolojik Katkılar

1. **Performans Değerlendirme**: Hayvancılık yapay zeka sistemleri için değerlendirme kriterleri
2. **Kullanıcı Deneyimi**: Hayvancılık sektörü için UX tasarım prensipleri
3. **Sistem Mimarisi**: Özelleşmiş alanlar için RAG sistemi geliştirme metodolojisi

### 2.7.3 Pratik Katkılar

1. **Kullanıma Hazır Sistem**: Hayvancılık sektörü için pratik kullanıma hazır yapay zeka sistemi
2. **Açık Kaynak Çözüm**: Geliştirilebilir ve uyarlanabilir açık kaynak sistem
3. **Eğitim Materyali**: Hayvancılık eğitimi için destekleyici teknoloji

Bu literatür taraması, araştırmanın teorik temelini oluşturmakta ve mevcut bilgi birikiminin üzerine nasıl katkı sağlanacağını göstermektedir. Bir sonraki bölümde, araştırma yöntemi ve kullanılan teknolojiler detaylı olarak açıklanacaktır.

