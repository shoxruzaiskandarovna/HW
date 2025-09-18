# Python Random seed() usuli tasodifiy sonlar generatorini ishga tushirish uchun ishlatiladi.
# Eslatma: Agar siz bir xil qiymatdan ikki marta foydalansangiz, bir xil tasodifiy raqamni ikki marta olasiz

import random
random.seed(10)       # Har safar bir xil ketma-ketlikni beradi
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


# Usul randint()belgilangan diapazondan tanlangan butun sonli elementni qaytaradi.
# Eslatma: Bu usul uchun taxallus randrange(start, stop+1).



