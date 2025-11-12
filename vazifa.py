 #capitaliza Converts the first character to upper case
animal="This is a cat"
x = animal.capitalize()
print(animal)

fruit = "The  apple tree has few apples"
x = fruit.capitalize()
print(fruit)

# casefold()Converts string into lower case
color = "This flower is yellow!"
x = color.casefold()
print(x)

color = "I like pink"
x = color.casefold()
print(x)

 #center()Returns a centered string
box = "beatiful"
x = box.center(30)
print(x)

box = "flower"
x = box.center(50)
print(x)

#count()	Returns the number of times a specified value occurs in a string
matn = "I love coding, because coding is fun "
soni = matn.count("coding")
print(soni)

mevalar =["olam","banan, olma", "gilos","olma"," anjir"]
soni =mevalar.count("olma")
print(soni)

#The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

book = "This book is about Märchen"
x = book.encode("utf-8")
print(x)

txt = "I love reading the book ‘Gödel, Escher, Bach’"
x = txt.encode("utf-8")
print(x)
#endswith nuqta bor yoqligini tekshiradi
matn = "I am reading a book"
x = matn.endswith(".")
print(x)

txt = "This is my favorite book"
x = txt.endswith("book")
print(x)

#Usul format()belgilangan qiymat(lar) ni formatlaydi va ularni satrning to'ldiruvchisiga kiritadi.
book_info = "This book costs {cost:.2f} USD."
print(book_info.format(cost = 15.5))

item = "One apple costs {price:.2f} dollars."
print(item.format(price = 0.75))

#Usul expandtabs()yorliq o'lchamini belgilangan bo'shliqlar soniga o'rnatadi.
sentence = "Py\tth\ton"
x = sentence.expandtabs(4)
print(x)

title = "Re\tad\ting\t is\t fun"
x = title.expandtabs(3)
print(x)
#Usul find()belgilangan qiymatning birinchi paydo bo'lishini topadi.
#find()Agar qiymat topilmasa, usul -1 ni qaytaradi .
txt = "apple"
x = txt.find("p")
print(x)

txt = "reading"
x = txt.find("ing")
print(x)

#isalnum()Agar barcha belgilar alfavit-raqamli bo'lsa, bu usul alifbo harfi (az) va raqamlarni (0-9) bildirsa, "True" qiymatini qaytaradi.
word = "Book123"
x = word.isalnum()
print(x)

code = "Python3"
x = code.isalnum()
print(x)
#Usul index()belgilangan qiymatning birinchi paydo bo'lishini topadi.
#index()Agar qiymat topilmasa, usul istisno keltiradi .
txt = "hello"
x = txt.index("e")
print(x)

txt = "python"
x = txt.index("t")
print(x)

#isalpha()Agar barcha belgilar alifbo harflari (az) bo'lsa, usul "True" ni qaytaradi .
#Alfavit harflari bo'lmagan belgilarga misol: (bo'shliq)!#%&? va hokazo.
name = "Book"
x = name.isalpha()
print(x)

title = "Python"
x = title.isalpha()
print(x)
#Usul isdigit(), agar barcha belgilar raqam bo'lsa, True, aks holda False qiymatini qaytaradi.
#² kabi ko'rsatkichlar ham raqam hisoblanadi.
number = "2025"
x = number.isdigit()
print(x)

code = "12a"
x = code.isdigit()
print(x)

#Usul islower()barcha belgilar kichik harfda bo'lsa True, aks holda False qiymatini qaytaradi.
#Raqamlar, belgilar va bo'shliqlar belgilanmaydi, faqat ali
word = "hello"
x = word.islower()
print(x)

name = "Book"
x = name.islower()
print(x)

#isspace()Agar satrdagi barcha belgilar bo'sh joy bo'lsa, usul "True", aks holda "False" ni qaytaradi .
text = "   "
x = text.isspace()
print(x)

word = " a "
x = word.isspace()
print(x)
# istitle()Agar matndagi barcha so'zlar katta harf bilan boshlansa, VA so'zning qolgan qismi kichik harflar bo'lsa, usul "True" qiymatini qaytaradi, aks holda "False" .
# Belgilar va raqamlar e'tiborga olinmaydi.
title = "My Book"
x = title.istitle()
print(x)

heading = "Python Course"
x = heading.istitle()
print(x)
# Usul join()barcha elementlarni iteratsiyada oladi va ularni bitta satrga birlashtiradi.
# Ajratuvchi sifatida qator ko'rsatilishi kerak.
words = ["read", "the", "book"]
x = " ".join(words)
print(x)

numbers = ["one", "two", "three"]
x = ",".join(numbers)
print(x)

#Usul ljust()to'ldirish belgisi sifatida belgilangan belgidan (bo'sh joy sukut bo'yicha) foydalanib, satrni chapga tekislaydi.
word = "Book"
x = word.ljust(10, "-")
print(x)

text = "Hi"
x = text.ljust(5, "*")
print(x)
# Usul lower()barcha belgilar kichik harf bo'lgan qatorni qaytaradi.
#  Belgilar va raqamlar e'tiborga olinmaydi.
word = "HELLO"
x = word.lower()
print(x)

name = "BoOk"
x = name.lower()
print(x)
#Usul lstrip()har qanday bosh belgilarni olib tashlaydi (bo'sh joy olib tashlash uchun birlamchi asosiy belgidir)
word = "   book"
x = word.lstrip()
print(x)

text = "---book"
x = text.lstrip("-")
print(x)

#Usul replace()belgilangan iborani boshqa belgilangan ibora bilan almashtiradi.
sentence = "I like apples"
x = sentence.replace("apples", "books")
print(x)

text = "Hello world"
x = text.replace("world", "Python")
print(x)
# Usul rfind()belgilangan qiymatning oxirgi takrorlanishini topadi.
# rfind()Agar qiymat topilmasa, usul -1 ni qaytaradi .
# Usul rfind()deyarli usul bilan bir xil rindex() . Quyidagi misolga qarang.
word = "banana"
x = word.rfind("na")
print(x)

sentence = "hello hello"
x = sentence.rfind("hello")
print(x)

# usul rindex()belgilangan qiymatning oxirgi takrorlanishini topadi.
# rindex()Agar qiymat topilmasa, usul istisno keltiradi .
# Usul rindex()deyarli usul bilan bir xil rfind() . Quyidagi misolga qarang.
word = "banana"
x = word.rindex("a")
print(x)

text = "book"
x = text.rindex("b")
print(x)

#Usul rjust()to'ldirish belgisi sifatida belgilangan belgidan (bo'sh joy sukut bo'yicha) foydalanib, satrni to'g'ri tekislaydi.
word = "Hi"
x = word.rjust(5, "*")
print(x)

text = "Book"
x = text.rjust(10, "-")
print(x)


#Usul rstrip()har qanday keyingi belgilarni (satr oxiridagi belgilar) o'chiradi, bo'sh joy esa olib tashlash uchun birlamchi keyingi belgilar hisoblanadi.
word = "book   "
x = word.rstrip()
print(x)

text = "data----"
x = text.rstrip("-")
print(x)
#
# Usul split()qatorni ro'yxatga ajratadi.
# Siz ajratuvchini belgilashingiz mumkin, standart ajratuvchi har qanday bo'shliqdir.
sentence = "I love books"
x = sentence.split()
print(x)

fruits = "apple,banana,grape"
x = fruits.split(",")
print(x)


# Usul startswith(), agar satr belgilangan qiymatdan boshlansa, True qiymatini qaytaradi, aks holda False.
word = "Hello world"
x = word.startswith("Hello")
print(x)

text = "python"
x = text.startswith("p")
print(x)

# Usul upper()barcha belgilar katta harf bilan yozilgan qatorni qaytaradi.
text = "python"
x = text.upper()
print(x)

text = "book"
x = text.upper()
print(x)

# swapcase()barcha katta harflar kichik va aksincha bo'lgan qatorni qaytaradi.
word = "Hello"
x = word.swapcase()
print(x)

text = "Python Programming"
x = text.swapcase()
print(x)


# sul zfill()belgilangan uzunlikka yetguncha satr boshida nol (0) qo'shadi.
# Agar len parametrining qiymati satr uzunligidan kichik bo'lsa, hech qanday to'ldirish amalga oshirilmaydi.
number = "7"
x = number.zfill(3)
print(x)


pin = "123"
x = pin.zfill(6)
print(x)
