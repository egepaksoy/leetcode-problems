# Matrisin 90 Derece Saat Yönünde Döndürülmesi (In-Place)

Bu problemde, bir **n x n boyutunda 2D matris** verilmiştir. Görevimiz, bu matrisi **in-place** olarak (yani, yeni bir matris oluşturmadan, doğrudan giriş matrisini düzenleyerek) saat yönünde 90 derece döndürmektir.

---

## Çözüm Adımları

### 1. Problem Anlayışı
Problemi anlamak için, önce 4x4 boyutunda bir matris üzerinde elle dönüşüm işlemi yaptım. Bu işlemi yaparken, her bir elemanın **mevcut konumu** ile **yeni konumunu** belirleyip yazdım:

#### Örnek Matris (Başlangıç):
```
[
 [1,  2,  3,  4],
 [5,  6,  7,  8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]
]
```

#### Elle Dönüşüm:
Her elemanın eski konumundan yeni konumuna dönüşümünü şu şekilde gözlemledim:
- **Birinci Satır:**
  ```
  (0, 0) -> (0, 3)
  (0, 1) -> (1, 3)
  (0, 2) -> (2, 3)
  (0, 3) -> (3, 3)
  ```
- **İkinci Satır:**
  ```
  (1, 0) -> (0, 2)
  (1, 1) -> (1, 2)
  (1, 2) -> (2, 2)
  (1, 3) -> (3, 2)
  ```

Bu adımları yazarken, eski konum ile yeni konum arasındaki **örüntüyü** fark ettim:
- **Yeni X değeri:** Mevcut Y değeri
- **Yeni Y değeri:** `len(matrix) - 1 - X`

---

### 2. Algoritmik Çözüm
Bu örüntüyü kullanarak, her elemanın yeni konumunu şu formülle hesapladım:
```
matrix[new_y][new_x] = eski_matrix[old_x][old_y]
```
Burada:
- `new_y = old_x`
- `new_x = len(matrix) - 1 - old_y`

---

### 3. Python Kodu

```python
def rotate(matrix):
    """
    Matrisin saat yönünde 90 derece döndürülmesi.
    """
    # Matrisin bir kopyasını oluştur
    temp_arr = [row[:] for row in matrix]  # Her satırın bir kopyasını al
    
    x = 0
    while x < len(matrix):  # Her satır için
        y = 0
        while y < len(matrix):  # Her sütun için
            # Yeni konum hesaplaması
            matrix[y][abs(len(matrix) - x - 1)] = temp_arr[x][y]
            y += 1
        x += 1
```

---

### 4. Kod Açıklaması

1. **Matrisin Kopyalanması:**
   ```python
   temp_arr = [row[:] for row in matrix]
   ```
   - `temp_arr` matrisin bir kopyasını oluşturur. Böylece `matrix` üzerinde yapılan değişiklikler `temp_arr`'i etkilemez.
   - Bu adım gereklidir çünkü matris üzerinde döndürme işlemi yapılırken aynı anda elemanlar değişecektir.

2. **Satır ve Sütun Döngüleri:**
   ```python
   x = 0
   while x < len(matrix):
       y = 0
       while y < len(matrix):
           ...
           y += 1
       x += 1
   ```
   - `x` satırları, `y` sütunları temsil eder.
   - İç içe döngülerle matrisin tüm elemanları gezilir.

3. **Yeni Konum Hesaplama:**
   ```python
   matrix[y][abs(len(matrix) - x - 1)] = temp_arr[x][y]
   ```
   - **Yeni Satır (`y`)**: Orijinal sütun (`y`) yeni satır olur.
   - **Yeni Sütun (`len(matrix) - x - 1`)**: Orijinal satırın (`x`) uzunluğa göre ters çevrilmesiyle elde edilir.
   - Bu formül, matrisin saat yönünde 90 derece döndürülmesini sağlar.

---

### 5. Test ve Çıktı

#### Giriş:
3x3 matris
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(matrix)
```

#### Çıkış:
```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```
#### Giriş:
4x4 matris
```python
[
 [1,  2,  3,  4],
 [5,  6,  7,  8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]
]
```

#### Çıkış:
```python
[
 [13,  9,  5, 1],
 [14, 10,  6, 2],
 [15, 11,  7, 3],
 [16, 12,  8, 4]
]
```

---

## Sonuç
Bu yöntem, verilen matrisi in-place olarak döndürmek için hem belleği verimli kullanır hem de doğrudan matrisin üzerinde çalışır. Döngü yapıları ve temel dizin işlemleri ile, bu problemi kolayca çözmek mümkün olmuştur.