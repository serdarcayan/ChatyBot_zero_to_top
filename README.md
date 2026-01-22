# 🤖 ChatyBot

**ChatyBot**, sıfırdan geliştirilen, internetten (özellikle Wikipedia) veri çekerek sorulara anlamlı yanıtlar üretmeyi hedefleyen bir **yapay zeka sohbet botu** projesidir.

Bu proje:

* **Hazır GPT / LLM kullanmaz**
* **Temel Python bilgisiyle** adım adım geliştirilebilir
* Gerçek dünyada AI sistemlerinin nasıl kurulduğunu öğretmeyi amaçlar

> 🎯 Nihai hedef:
> Kullanıcının sorduğu soruları anlayan, gerekirse internetten veri toplayan ve zamanla kendi bilgi temsilini oluşturan bir sohbet sistemi geliştirmek.

---

## 📌 Projenin Mevcut Durumu

✔ Wikipedia’dan sayfa indirme
✔ Türkçe karakter ve URL encoding desteği
✔ Temel proje mimarisi
⬜ HTML → temiz metin çıkarma
⬜ Soru türü tespiti
⬜ Bilgi çıkarımı
⬜ Diyalog hafızası
⬜ Basit öğrenme mekanizması

---

## 🧠 Temel Fikir

ChatyBot klasik bir chatbot değildir.

Sistem şu mantıkla çalışır:

1. Kullanıcı soru sorar
2. Soru analiz edilir
3. Gerekirse internetten veri çekilir
4. Ham HTML temizlenir
5. Bilgi çıkarılır
6. Anlamlı bir cevap oluşturulur

> ❗ Doğru cevap şart değildir
> Önemli olan **anlamlı bir cevap üretim sürecidir**

---

## 🗂️ Proje Yapısı

```
ChatyBot/
│
├── main.py                 # Uygulama girişi
│
├── config/
│   └── settings.py         # Genel ayarlar (URL'ler vs.)
│
├── search/
│   └── wikipedia_search.py # Wikipedia veri çekme
│
├── parser/
│   └── info_extractor.py   # HTML → metin (henüz yapılmadı)
│
├── brain/
│   ├── question_parser.py  # Soru analizi (planlanan)
│   └── memory.py           # Basit hafıza sistemi (planlanan)
│
├── venv/                   # Virtual environment (gitignore)
│
├── .gitignore
└── README.md
```

---

## ⚙️ Kurulum

### 1️⃣ Projeyi klonla

```bash
git clone <repo_url>
cd ChatyBot
```

### 2️⃣ Virtual environment oluştur

```bash
python3 -m venv venv
```

### 3️⃣ Ortamı aktif et

```bash
source venv/bin/activate
```

### 4️⃣ Gerekli paketleri yükle

```bash
python -m pip install requests beautifulsoup4
```

---

## ▶️ Çalıştırma

```bash
python main.py
```

Örnek çıktı:

```
Sayfa başarıyla indirildi!
<!DOCTYPE html>
<html class="client-nojs" lang="tr">
...
```

---

## 🌐 Kullanılan Teknolojiler

* Python 3.12
* requests
* beautifulsoup4
* Wikipedia (veri kaynağı)

---

## ❓ Neden Wikipedia?

* Açık kaynak
* Güvenilir
* Yapısal (HTML kolay ayrıştırılır)
* Yapay zeka projeleri için ideal

> ⚠️ ChatyBot Wikipedia’yı **kopyalamaz**,
> bilgiyi **ham veri olarak kullanır**

---

## 🚧 Bilinen Kısıtlar

* Cevaplar şu an ham ve düzensiz
* Öğrenme mekanizması yok
* Konuşma bağlamı tutulmuyor
* Bilgi doğrulama yapılmıyor

Bu kısıtlar **bilinçli** olarak vardır.
Amaç sistemi adım adım inşa etmektir.

---

## 🛣️ Yol Haritası

### Aşama 1 – Veri

* [x] İnternetten sayfa indirme
* [ ] Metin temizleme
* [ ] Ana bilgi çıkarımı

### Aşama 2 – Anlama

* [ ] Soru türü tespiti
* [ ] Anahtar kelime çıkarımı

### Aşama 3 – Zeka

* [ ] Basit hafıza
* [ ] Diyalog bağlamı
* [ ] Cümle üretimi

### Aşama 4 – Öğrenme

* [ ] Bilgiyi saklama
* [ ] Basit istatistiksel öğrenme
* [ ] Yanıt iyileştirme

---

## 👨‍💻 Geliştirici

**Serdar**
Python & AI öğrenme odaklı bireysel proje

---

## ⚠️ Not

Bu proje:

* Hızlı sonuç değil
* Kısa yol değil
* Hazır zeka değil

> **Gerçekten yapay zeka öğrenmek isteyenler içindir.**

---

## 🧭 Devam

Bir sonraki adım:
👉 **HTML’den anlamlı metin çıkarma**
