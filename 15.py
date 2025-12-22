# """find() usuli qidiruvning boshlang'ich indeksini qaytaradi"""
# student1 = 'shoxruza and shukurjon'
# student2 = student1.find('shukurjon')
# print(student2)
#
# """  Kod 'smart' so'zidan oxiridan boshlab har ikkinchi harfni olib, teskari tartibda 'tas' hosil qiladi."""
s = 'smart'
print(s[:-99:-2])
#
#
# """lst = [tup] - bu tuple'ni list ichiga bitta element sifatida qo'yadi
# lst.append(3) - oxiriga 3 raqami qo'shiladi, endi 2 ta element bor
# lst.pop(0) - birinchi elementni (ya'ni tuple'ni) o'chiradi
# Oxirida faqat [3] qoladi, uzunligi = 1  lst = [tup] deganda:
#
# Tuple butun holda listning bitta elementi bo'lib qo'yildi
# List shunday ko'rinadi: [(0, 1, 2)] - faqat 1 ta element
#
# Agar lst = [0, 1, 2] yoki lst = list(tup) yozilganda:
# Har bir raqam alohida element bo'lardi
# List shunday bo'lardi: [0, 1, 2] - 3 ta element
# """
#
#
# tup = 0, 1, 2
# lst = list(tup)
# lst.append(3)
# lst.pop(0)
# print(len(lst))
#
# """"""
# #
# # def swap():
# # b, a = a, b
# # a, b = 1, 2
# # swap()
# # print(a- b)
#
# """
# **`.find()` metodi nima qiladi?**
# - Berilgan belgini stringda qidiradi
# - Topsa - birinchi uchragan joyining **indeksini** qaytaradi
# - Topmasa - **-1** qaytaradi
#
# **Har bir qismni hisoblash:**
#
# 1. **`s.find('p')`**
#    - 'apple' da 'p' harfi bor
#    - Birinchi 'p' → **1-indeks**da (a=0, p=1)
#    - Natija: **1**
#
# 2. **`s.find('f')`**
#    - 'apple' da 'f' harfi **yo'q**
#    - Natija: **-1**
#
# 3. **`s.find('')`**
#    - Bo'sh string har doim topiladi
#    - Bo'sh string har doim **0-indeks**da hisoblanadi
#    - Natija: **0**
#
# **Hisoblash:**
# ```
# 1 + (-1) + 0 = 0"""
#
# s = 'apple'
# print(s.find('p') + s.find('f') + s.find(''))
#
#
# """ zip() metodi:
# Ikki listni juftlashtiradi - birinchi elementlarni, ikkinchi elementlarni...
# Qisqasi tugaguncha davom etadi p = ['abc'] → 1 ta element
# q = ['a', 'b', 'c'] → 3 ta element
# zip(p, q) → faqat 1 ta juft hosil qiladi: ('abc', 'a')
# Qolgan 'b' va 'c' ishlatilmaydi"""
#
# p = ['abc']
# q = ['a', 'b', 'c']
# zipped = list(zip(p, q))
# print(len(zipped))
#
# """ Qisqasi: i katta bo'lganda num oshadi, kichik bo'lganda o'zgarmaydi.
# ange(5, 0, -1) metodi:
# 5 dan boshlab 0 gacha (0 kirmaydi), -1 qadam bilan
# Natija: 5, 4, 3, 2, 1"""
#
# num = 0
# for i in range(5, 0,-1):
#         num += i > num
# print(num)
#
#
#
# """ t[-1:] = [4] slice assignment:
# Oxirgi elementdan boshlab hamma narsani almashtiradi
# [1, 2, 3] → [1, 2, 4]
#
# t[-1] = [5] oddiy assignment:
#
# Faqat oxirgi elementni almashtiradi
# [1, 2, 4] → [1, 2, [5]]
# [5] list sifatida qo'yildi (bitta element)
#
# Natija: 3
#
# Qisqasi:
#
# Birinchi: 3 ni 4 ga almashtirdi
# Ikkinchi: 4 ni [5] listiga almashtirdi
# Uzunlik o'zgarmadi: 3
# ."""
#
# t = [1, 2, 3]
# t[-1:] = [4]
# t[-1] = [5]
# print(len(t))
#
# """ t2 = t * 1 operatsiya:
# Listni 1 marta ko'paytiradi (ya'ni nusxa oladi)
# t2 = [0, 1, 2] (yangi list)
# t[0] = 100:
# Faqat t o'zgaradi → [100, 1, 2]
# t2 o'zgarmaydi, chunki u alohida list Natija: [0, 1, 2]
# Qisqasi: t2 mustaqil nusxa, t o'zgarganda t2 o'zgarmaydi.Claude is AI and can make mistakes. Please double-check responses."""
# t = [0, 1, 2]
# t2 = t * 1
# t[0] = 100
# print(t2)
#
# """ x o'zgaruvchi o'zgaradi
# Lekin dictionary ichidagi qiymatlar o'zgarmaydi
# Dictionary'da hali ham 10 turadi
# Dictionary yaratilganda qiymat ko'chiriladi, keyinchalik x o'zgarsa ta'sir qilmaydi."""
# x = 10
# d = {'Peter': x, 'Tom': x, 'Mary': x}
# x = 11
# print(d['Peter'])
#
#
#
# """t[2::-2] slice:
# 2-indeksdan boshlab, boshigacha, -2 qadam bilan
# Bu: indeks 2, indeks 0 → elementlar [3, 1]
# t[2::-2] = [10, 30]:
# t[2] → 10 ga almashadi
# t[0] → 30 ga almashadi
# List: [30, 2, 10, 4]  -qadam: t = [1, 2, 3, 4]
# Indekslar: 0, 1, 2, 3
# 2-qadam: t[2::-2] qaysi joylarni tanlaydi?
# 2-indeksdan boshla
# -2 qadam (orqaga 2 tadan sana)
# 2 → 0 (to'xtaydi)
# Faqat 2 ta joy: indeks 2 va indeks 0
# 3-qadam: t[2::-2] = [10, 30]
# Indeks 2 ga 10 qo'y
# Indeks 0 ga 30 qo'y """
# t = [1, 2, 3, 4]024
# t[2::-2] = [10, 30]
# print(t[0])
#
#
# """ ambda x: -abs(x) funksiya:
# abs(x) → sonning musbat qiymatini beradi
# -abs(x) → sonning manfiy musbat qiymatini beradi
# max(t, key=key) qanday ishlaydi:
# Har bir elementga key funksiyasini qo'llaydi
# Eng katta natija bergan elementni tanlaydi  key absolyut qiymati eng kichik sonni topadi
# Chunki manfiy qilinganda, kichik son katta bo'ladi
# Misol: 0 ning absolyuti 0, 9 ning 9 → -0 > -9"""
# t = [-2, 9, 0,-8]
# key = lambda x:-abs(x)
# print(max(t, key=key))
#
#
#
#
# """ ey = lambda x: -abs(x) funksiya: musbat qiladi, keyin manfiyga o'giradi
# 2. Har bir element uchun key hisoblash:
# -2 → -abs(-2) = -2
# 9 → -abs(9) = -9
# 0 → -abs(0) = 0
# -8 → -abs(-8) = -8
#
# 3. max() eng katta qiymatni tanlaydi:
# -2, -9, 0, -8 ichidan eng kattasi → 0
# 4. 0 ga mos kelgan asl element qaytariladi:Bu 0  Natija: 0
# Absolyut qiymati eng kichik son topildi - 0.Claude is AI and can make mistakes. Please double-check responses. Sonnet 4.5"""
# t = [0, 1, 2, 3]
# print(max(t, key=lambda x: x%2))
#
#
#
# """ append() metodi:
#
# Listning oxiriga element qo'shadi
# Misol: [1, 2].append(3) → [1, 2, 3]
#
# def f(): - funksiya yaratish:
#
# Kod blokini nomlaydi
# Chaqirilganda bajariladi
# Misol: f() deb yozilganda ichidagi kod ishlaydi
#
# Funksiya ichida tashqi o'zgaruvchi:
# t funksiyadan tashqarida yaratilgan
# Funksiya ichida t ga murojaat qilsa, tashqaridagi t ishlatiladi
# t.append(10) → tashqaridagi t listiga 10 qo'shadi
# Bu kodda:
# Funksiya yaratilganda t = [0] edi
# Lekin funksiya ishlaganda t = [1] edi
# Shuning uchun [1] ga 10 qo'shildi
# Natija: [1, 10]Claude is AI and can make mistakes. Please double-check responses. Sonnet 4.5"""
# t = [0]
# def f():
#         t.append(10)
# t = [1]
# f()
# print(t)t