# En Fazla Su Kapasitesi Problemi (Container with Most Water)

## Problem Tanımı

Bir tamsayı dizisi olan `height` verilmektedir. Bu dizi, uzunluğu `n` olan bir dizi olup, her bir elemanı bir dikey çizgiyi temsil eder. Bu çizgilerin uç noktaları şu şekildedir:

- Birinci uç noktası: `(i, 0)`
- İkinci uç noktası: `(i, height[i])`

Bu çizgilerle birlikte, x ekseni ile bir kap oluşturmak için iki çizgi seçilir. Bu kap, en fazla suyu tutacak şekilde seçilmelidir.

![Problem görseli](./question_11.jpg)

### İstenilen:
Kap içerisinde tutulan maksimum su miktarını döndüren bir fonksiyon yazınız. Kap eğik olmamalıdır.

---

## Çözüm Yöntemleri

### Brute Force (Kaba Kuvvet) Yaklaşımı

1. Her bir eleman diğer tüm elemanlarla kombinlenerek alan hesaplanır.
2. Alanlar arasında maksimum olanı bulunur.
3. Ancak bu yaklaşımda zaman karmaşıklığı `O(n*(n+1)/2)` olur, çünkü tüm elemanlar birbiriyle karşılaştırılır.

Bu yöntem büyük veri setlerinde zaman aşımı sorunlarına yol açabilir. Bu nedenle daha verimli bir çözüm için farklı bir algoritma geliştirilmiştir.

---

### Çift Pivot Algoritması
Bu algoritma, listenin başı ve sonundan başlayarak iki pivot kullanır ve şu şekilde çalışır:

#### Adımlar:
1. **Başlangıç Pivots**:
   - İlk pivot `i`, listenin başlangıç indeksine eşitlenir.
   - İkinci pivot `j`, listenin son indeksine eşitlenir.

2. **Alan Hesaplama**:
   - Pivotlar arasındaki alan hesaplanır: `alan = min(height[i], height[j]) * (j - i)`.

3. **Pivotları Güncelleme**:
   - Daha küçük olan pivotun değeri artırılır ya da azaltılır:
     - Eğer `height[i] < height[j]`, `i` pivotu bir ileri taşınır.
     - Eğer `height[i] > height[j]`, `j` pivotu bir geri taşınır.

4. **Döngü Kontrolü**:
   - `i < j` olduğu sürece işlem devam eder. Pivotlar birbirini geçtiğinde döngü sonlanır ve maksimum alan döndürülür.

---

## Python Kodlama

Aşağıdaki kod, çift pivot algoritması ile maksimum su miktarını hesaplar:

```python
# Çift Pivot Algoritması ile Maksimum Alan Hesaplama

def maxArea(height):
    # Maksimum alanı saklamak için bir değişken
    max_val = 0
    # Geçici olarak alanı hesaplamak için bir değişken
    current = 0

    # Pivotlar için başlangıç değerleri
    p_j = 0
    p_i = 0
    # Dizinin son indeksine işaret eden pivot
    j = len(height) - 1
    # Dizinin başlangıç indeksine işaret eden pivot
    i = 0

    # Pivotlar kesişene kadar döngü devam eder
    while (i < j and i >= 0 and j < len(height)):
        # Sol pivotun yüksekliği sağ pivotun yüksekliğinden küçükse
        if (height[i] < height[j]):
            # Sol pivotu kaydet
            p_i = i

            # Alanı hesapla ve maksimum değeri güncelle
            current = height[i] * (j - i)
            if (current > max_val):
                max_val = current

            # Daha büyük bir sol pivot bulmak için ilerle
            while (p_i < j and height[p_i] <= height[i]):
                p_i += 1
            i = p_i
            
        # Sağ pivotun yüksekliği sol pivotun yüksekliğinden küçükse
        elif (height[j] < height[i]):
            # Sağ pivotu kaydet
            p_j = j

            # Alanı hesapla ve maksimum değeri güncelle
            current = height[j] * (j - i)
            if (current > max_val):
                max_val = current
            
            # Daha büyük bir sağ pivot bulmak için gerile
            while (i < j and height[p_j] <= height[j]):
                p_j -= 1
            j = p_j
        
        # Eğer sol ve sağ pivotlar eşit yüksekliğe sahipse
        elif (height[i] == height[j]):
            # Sol ve sağ pivotları kaydet
            p_i = i
            p_j = j

            # Alanı hesapla ve maksimum değeri güncelle
            current = height[i] * (j - i)
            if (current > max_val):
                max_val = current

            # Sol ve sağ pivotları ilerleterek kontrol et
            while (p_i < p_j):
                if (height[p_i] > height[p_j]):
                    p_j = j
                    break
                if (height[p_j] > height[p_i]):
                    p_i = i
                    break
                if (height[p_i] == height[p_j] and height[p_j] != height[j]):
                    break

                p_i += 1
                p_j -= 1
            
            # Pivotları güncelle
            i = p_i
            j = p_j

    # Maksimum alanı döndür
    return max_val


```

---

## Çalışma Mantığı ve Açıklama

1. **Başlangıç Durumu**:
   - `i = 0`, `j = n-1` olacak şekilde pivotlar başlatılır.
   - Tüm alanlar hesaplanır ve maksimum değer kaydedilir.

2. **Pivotların Güncellenmesi**:
   - Küçük pivot değeri, daha büyük bir pivot bulmak amacıyla güncellenir.
   - Bu işlem daha küçük alanlar hesaplamayı engeller ve algoritmayı optimize eder.

3. **Sonuç Döndürme**:
   - Tüm pivot kombinasyonları kontrol edildikten sonra, kaydedilen maksimum değer döndürülür.

---

## Test Örnekleri ve Çıktılar

### Test 1:
#### Giriş:
```python
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
```
#### Çıkış:
```python
49
```

### Test 2:
#### Giriş:
```python
height = [1,1]
print(maxArea(height))
```
#### Çıkış:
```python
1
```

### Test 3:
#### Giriş:
```python
height = [4,3,2,1,4]
print(maxArea(height))
```
#### Çıkış:
```python
16
```

---

## Sonuç

Bu algoritma, çift pivot yaklaşımı kullanarak `O(n)` zaman karmaşıklığı ile maksimum alanı hesaplar. Bu, özellikle büyük veri setlerinde, kaba kuvvet yöntemine kıyasla ciddi performans artışı sağlar.

![Çalışma zamanı](./image.png)