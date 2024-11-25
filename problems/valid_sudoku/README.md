# Sudoku Doğrulama Problemi (Valid Sudoku)

Bu problemde, **9x9 boyutunda bir Sudoku tahtasının** kurallara uygun şekilde doldurulup doldurulmadığını kontrol etmek hedeflenmiştir.

---

## Çözüm Adımları

### 1. Problem Anlayışı
Sudoku tahtası şu kurallara göre doğrulanır:
- Aynı satırda bir sayı birden fazla kez bulunamaz.
- Aynı sütunda bir sayı birden fazla kez bulunamaz.
- Her 3x3 alt karede bir sayı birden fazla kez bulunamaz.

---

### 2. Algoritmik Çözüm
Bu problemi çözmek için şu adımları izledim:
1. **Bir Sayı Seçme:** Matrisin her elemanını kontrol ederek sayıları tek tek inceledim.
2. **Satır Doğrulama:** Seçilen sayı için bulunduğu satırda tekrar olup olmadığını kontrol ettim.
3. **Sütun Doğrulama:** Aynı şekilde, seçilen sayı için bulunduğu sütunda tekrar olup olmadığını kontrol ettim.
4. **3x3 Alt Kare Doğrulama:** Seçilen sayının içinde bulunduğu 3x3 alt karede tekrar olup olmadığını kontrol ettim.

---

### 3. Python Kodu

Kod, tüm bu doğrulama adımlarını gerçekleştiren bir algoritmayı içerir:

```python
def isValidSudoku(board: List[List[str]]):
    inspected_number = "0"

    y = 0
    while y < len(board):
        x = 0
        inspected_number = "0"
        while x < len(board[y]):
            if board[y][x] != ".":
                inspected_number = board[y][x]
                x2 = x + 1
                
                # satıra bakma
                while x2 < len(board[y]):
                    if board[y][x2] == inspected_number:
                        return False
                    x2 += 1

                # sutuna bakma
                y2 = y + 1
                while y2 < len(board):
                    if board[y2][x] == inspected_number:
                        return False
                    y2 += 1

                # kucuk kareye bakma
                min_x = x//3 * 3
                max_x = (x//3*3) + 2

                min_y = y//3 * 3
                max_y = (y//3*3) + 2

                y2 = min_y
                while y2 <= max_y:
                    x2 = min_x
                    while x2 <= max_x:
                        if board[y2][x2] == inspected_number and not (y2 == y and x2 == x):
                            return False
                        x2 += 1
                    y2 += 1
                
            x += 1
        y += 1
    return True
```

---

### 4. Kod Açıklaması

1. **Satır Kontrolü:**
   - Bir sayı seçildiğinde, o sayıdan sonraki sütunlar taranır.
   - Eğer aynı satırda tekrar eden bir sayı bulunursa `False` döndürülür.

2. **Sütun Kontrolü:**
   - Benzer şekilde, aynı sütunda tekrar eden bir sayı bulunursa `False` döndürülür.

3. **3x3 Alt Kare Kontrolü:**
   - İçinde bulunulan alt karenin başlangıç (min) ve bitiş (max) değerleri hesaplanır:
     - `min_x = x//3 * 3`, `max_x = min_x + 2`
     - `min_y = y//3 * 3`, `max_y = min_y + 2`
   - Alt kare bu aralıkta taranır ve tekrar eden bir sayı bulunursa `False` döndürülür.

---

### 5. Test ve Çıktı

#### Giriş:
```python
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
solution = Solution()
print(solution.isValidSudoku(board))  # Output: True
```

#### Çıkış:
```python
True
```

---

## Sonuç
Bu algoritma, Sudoku tahtasının doğruluğunu etkili bir şekilde kontrol eder. Satır, sütun ve 3x3 alt kare kontrolleri, algoritmanın kuralları eksiksiz şekilde uygulamasını sağlar.