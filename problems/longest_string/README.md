# Karakter Tekrarını Kaldırma (lognestString)

Bu Python fonksiyonu, verilen bir kelimede (string) tekrarlanan karakterleri kaldırarak, sadece bir kez görünen karakterlerden oluşan yeni bir kelime döndürür.

---

## Çözüm Adımları

### 1. Problem Anlayışı
Bu fonksiyon, verilen bir kelimedeki her bir karakteri kontrol eder ve eğer karakter birden fazla kez tekrarlanıyorsa, o karakteri kelimeden çıkarır. Bu işlem, sadece bir kez görünen karakterlerin kaldığı sonuca ulaşana kadar tekrarlanır.

---

### 2. Algoritmik Çözüm
1. **Döngü Başlatma:**
   - Fonksiyon, kelimenin her bir karakterini kontrol eder.
   - Eğer bir karakter birden fazla kez bulunuyorsa, bu karakter kelimeden çıkarılır.
2. **Karakterin Çıkarılması:**
   - Tekrarlanan karakterler çıkarıldığında, döngü yeniden başlatılır ve kelimenin başından itibaren tekrar kontrol yapılır.
3. **Sonuç Kelimesi:**
   - Bu işlem devam ederken, sadece bir kez görünen karakterlerden oluşan bir kelime elde edilir ve bu kelime döndürülür.

---

### 3. Python Kodu

Kod, verilen kelimedeki tekrarlanan karakterleri kaldırarak sonucu döndüren bir algoritma içerir:

```python
def lognestString(word: str):
    i = 0
    while i < len(word):
        if word.count(word[i]) > 1:
            word = word[:i] + word[i+1:]
            i = 0
        else:
            i += 1
    return word
```

---

### 4. Kod Açıklaması

1. **Karakter Kontrolü:**
   - `word.count(word[i])` ifadesi, mevcut karakterin kelimede kaç kez tekrar ettiğini kontrol eder.
   - Eğer karakter birden fazla kez bulunuyorsa, `word = word[:i] + word[i+1:]` ile bu karakter kelimeden çıkarılır.

2. **Döngü Yeniden Başlatma:**
   - Eğer çıkarılan karakter kelimenin başında ise, döngü sıfırlanır (`i = 0`), böylece kelimenin başından başlanarak her bir karakter kontrol edilir.

3. **Sonuç:**
   - Tüm tekrarlanan karakterler çıkarıldıktan sonra, kalan kelime döndürülür.

---

### 5. Test ve Çıktı

#### Giriş:
```python
word = "abccba"
print(lognestString(word))  # Çıktı: "cba"
```

#### Çıkış:
```python
"cba"
```

#### Giriş:
```python
word = "pwwekw"
print(lognestString(word))  # Çıktı: "pekw"
```

#### Çıkış:
```python
"pekw"
```
---

## Sonuç
Bu fonksiyon, verilen bir kelimede tekrarlanan karakterleri çıkararak sadece bir kez görünen karakterlerden oluşan yeni bir kelime döndürür. Bu işlem, tekrarlanan karakterler kaldırılana kadar devam eder.