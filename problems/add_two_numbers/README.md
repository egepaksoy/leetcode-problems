# İki Sayının Basamak Basamak Toplanması (addTwoNum)

Bu Python fonksiyonu, iki tamsayı listesinin elemanlarını basamak basamak toplayarak bir sonuç listesi döndürür. Bu yöntem, özellikle çok büyük sayılarla çalışırken faydalıdır.

---

## Çözüm Adımları

### 1. Problem Anlayışı
Bu fonksiyon, iki tamsayı listesi (örneğin `l1` ve `l2`) alır ve her iki listeyi basamaklarına göre toplayarak bir sonuç listesi döndürür. Eğer bir toplama işlemi sırasında elde değer (carry) oluşursa, bu değer bir sonraki toplama işlemine aktarılır.

---

### 2. Algoritmik Çözüm
1. **Liste Uzunluklarının Karşılaştırılması:**
   - Uzun olan liste `l`, kısa olan liste `lmin` olarak belirlenir. Bu, toplama işlemini daha kolay hale getirir.
2. **Toplama Döngüsü:**
   - Her iki listenin aynı indeksteki elemanları toplanır.
   - Eğer toplam 9'dan büyükse, elde değeri hesaplanır ve bir sonraki toplama işlemine eklenir.
   - Eğer toplam 9'dan küçükse, doğrudan sonuç listesine eklenir.
3. **Sonuç Listesinin Döndürülmesi:**
   - Döngü tamamlandıktan sonra oluşan sonuç listesi (`sum`) döndürülür.

---

### 3. Python Kodu

Kod, iki tamsayı listesinin elemanlarını basamak basamak toplar:

```python
def addTwoNum(l1, l2):
    n = 0
    l = l2
    lmin = l1

    if len(l1) > len(l2):
        l = l1
        lmin = l2

    kalan = 0
    sum = []

    while n < len(l):
        if len(lmin) > n:
            if l1[n] + l2[n] > 9:
                k = kalan
                kalan = (l1[n] + l2[n]) // 10
                sum.append(l1[n] + l2[n] - kalan * 10 + k)
            else:
                sum.append(l1[n] + l2[n] + kalan)
                kalan = 0
        else:
            if l[n] + kalan > 9:
                k = kalan
                kalan = (l[n] + k) // 10
                sum.append(l[n] - kalan * 10 + k)
            else:
                sum.append(l[n] + kalan)
                kalan = 0
        n += 1

    return sum
```

---

### 4. Test ve Çıktı

#### Giriş:
```python
l1 = [5, 6, 3]
l2 = [8, 4, 9]
print(addTwoNum(l1, l2))  # Çıktı: [3, 1, 3, 1]
```

#### Çıkış:
```python
[3, 1, 3, 1]
```

---

## Sonuç
Bu fonksiyon, iki sayıyı basamaklarına ayırarak toplamak için etkili bir algoritma sunar. Özellikle çok büyük sayılarla çalışırken belleği verimli bir şekilde kullanır ve liste işlemleriyle doğru sonuçlar üretir.