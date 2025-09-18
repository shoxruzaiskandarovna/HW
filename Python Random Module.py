# Python Random seed() usuli tasodifiy sonlar generatorini ishga tushirish uchun ishlatiladi.
# Eslatma: Agar siz bir xil qiymatdan ikki marta foydalansangiz, bir xil tasodifiy raqamni ikki marta olasiz

import random
random.seed(10)
print(random.randint(1, 10))

import random
random.seed(5)
print(random.randint(5, 15))


# Usul getstate()tasodifiy sonlar generatorining joriy holatiga ega ob'ektni qaytaradi.
# Holatni qo'lga kiritish uchun ushbu usuldan foydalaning va holatni tiklash uchun olingan holat bilan usuldan foydalaning setstate()

import random

print(random.randint(1, 10))
state = random.getstate()

import random

print(random.randint(1, 100))
state = random.getstate()


# Usul setstate()tasodifiy sonlar generatorining holatini belgilangan holatga qaytarish uchun ishlatiladi
# getstate()Davlatni qo'lga olish uchun usuldan foydalaning
#
import random

print( random.randint(1, 10))
state = random.getstate()
print( random.randint(1, 10))
random.setstate(state)
print( random.randint(1, 10))

import random

print( random.randint(100, 200))
state = random.getstate()
print( random.randint(100, 200))
random.setstate(state)
print( random.randint(100, 200))
# getstate() = generator holatini saqlash
# setstate() = shu holatni tiklash


# Usul getrandbits()belgilangan o'lchamdagi (bitlarda) butun sonni qaytaradi.
import random
print(random.getrandbits(8))

import random
print(random.getrandbits(4))


# Usul randrange()belgilangan diapazondan tasodifiy tanlangan elementni qaytaradi.
import random
print(random.randrange(3, 9))

import random
print(random.randrange(10, 21))


# Usul randint() belgilangan diapazondan tanlangan butun sonli elementni qaytaradi.
# Eslatma: Bu usul uchun taxallus randrange(start, stop+1).
import random
print(random.randint(3, 9))

import random
print(random.randint(100, 200))  # 100 dan 200 gacha tasodifiy son


# Usul choice()belgilangan ketma-ketlikdan tasodifiy tanlangan elementni qaytaradi.
# Ketma-ketlik qator, diapazon, ro'yxat, kortej yoki boshqa turdagi ketma-ketlik bo'lishi mumkin.
import random
colors = ["red", "green", "blue", "yellow"]
print(random.choice(colors))

import random
numbers = [10, 20, 30, 40, 50]
print(random.choice(numbers))


# sul choices()belgilangan ketma-ketlikdan tasodifiy tanlangan element bilan ro'yxatni qaytaradi.
# # Har bir natijaning imkoniyatini vaznlar parametri yoki cum_weights parametri bilan tortishingiz mumkin.
# # Ketma-ketlik qator, diapazon, ro'yxat, kortej yoki boshqa turdagi ketma-ketlik bo'lishi mumkin.
import random
fruits = ["apple", "banana", "cherry"]
print(random.choices(fruits, weights=[10, 1, 1], k=10))


import random
colors = ["red", "green", "blue"]
print(random.choices(colors, weights=[1, 5, 1], k=8))



# Usul shuffle()ro'yxat kabi ketma-ketlikni oladi va elementlarning tartibini qayta tashkil qiladi.
# Eslatma: Bu usul asl ro'yxatni o'zgartiradi, yangi ro'yxatni qaytarmaydi.
import random
numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
print(numbers)

import random
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)
print(colors)



# Usul sample()ketma-ketlikdan tasodifiy tanlangan elementlarning belgilangan soni bilan ro'yxatni qaytaradi.
# Eslatma: Bu usul asl ketma-ketlikni o'zgartirmaydi.
# Eslatma: Belgilangan raqam ( k=2) asl ketma-ketlik uzunligidan uzun bo'lishi mumkin emas.
import random
fruits = ["apple", "banana", "cherry", "mango"]
print(random.sample(fruits, k=2))

import random
numbers = [1, 2, 3, 4, 5, 6]
print(random.sample(numbers, k=3))



# Usul uniform()ikkita belgilangan raqam (ikkalasi ham kiritilgan) o'rtasida tasodifiy suzuvchi raqamni qaytaradi.
import random
print(random.uniform(20, 60))

import random
print(random.uniform(-10, 10))



# Usul triangular()ikkita belgilangan raqam (ikkalasi ham kiritilgan) o'rtasida tasodifiy suzuvchi raqamni qaytaradi, lekin siz uchinchi parametrni, mode parametrni ham belgilashingiz mumkin.
# Parametr modesizga mumkin bo'lgan natijani boshqa ikkita parametr qiymatlaridan biriga yaqinroq tortish imkoniyatini beradi.
# Parametr modesukut bo'yicha boshqa ikkita parametr qiymatlari orasidagi o'rta nuqtaga o'rnatiladi, bu hech qanday yo'nalishda mumkin bo'lgan natijani tortmaydi.
import random
print(random.triangular(20, 60, 30))

import random
print(random.triangular(-10, 10, 0))



