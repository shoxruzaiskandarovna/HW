# add() set (to‘plam) ichiga bitta yangi element qo‘shadi.
#
# fruits = {"olma", "anor", "uzum"}
# fruits.add("gilos")
# print(fruits)
#
# cars = {"BMW", "Mercedes", "Chevrolet"}
# cars.add("Tesla")
# print(cars)
#
#
# cars = {"BMW", "Mercedes", "Chevrolet"}
# cars.add("Tesla")
# print(cars)

 # clear() – to‘plamni butunlay bo‘shatadi.
# numbers = {1, 2, 3, 4, 5}
# numbers.clear()
# print(numbers)
#
#
# cities = {"Toshkent", "Xiva", "Buxoro", "Urganch"}
# cities.clear()
# print(cities)
#
#
# colors = {"qizil", "yashil", "ko‘k"}
# colors.clear()
# print(colors)


# difference() metodi ikkita setni taqqoslaydi va faqat birinchisida bor, ikkinchisida yo‘q elementlarni qaytaradi.
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7}
# print(a.difference(b))
#
#
# cities1 = {"Toshkent", "Xiva", "Buxoro"}
# cities2 = {"Xiva", "Samarqand"}
# print(cities1.difference(cities2))
#
#
# colors1 = {"qizil", "ko‘k", "yashil"}
# colors2 = {"qizil", "sariq"}
# print(colors1.difference(colors2))
#


# u to‘g‘ridan-to‘g‘ri birinchi setni o‘zgartiradi va ikkinchisida bor elementlarni o‘chiradi.
# # Yangi set yaratmaydi, balki birinchi setni yangilaydi.
# companies1 = {"Google", "Microsoft", "Apple", "Tesla"}
# companies2 = {"Apple", "Samsung", "Microsoft"}
# companies1.difference_update(companies2)
# print(companies1)
#
# sports1 = {"Futbol", "Basketbol", "Tennis", "Shaxmat"}
# sports2 = {"Futbol", "Hokkey", "Tennis"}
# sports1.difference_update(sports2)
# print(sports1)
#
# subjects1 = {"Matematika", "Fizika", "Tarix", "Kimyo"}
# subjects2 = {"Matematika", "Ingliz tili", "Kimyo"}
# subjects1.difference_update(subjects2)
# print(subjects1)


# # difference_update() → sports1 ichidan, sports2 da ham bor bo‘lgan sozlarni o‘chirib tashlaydi.
# sports1 = {"Futbol", "Basketbol", "Tennis", "Shaxmat"}
# sports2 = {"Futbol", "Hokkey", "Tennis"}
# sports1.difference_update(sports2)
# print(sports1)
#
# tech1 = {"Python", "Java", "C++", "HTML"}
# tech2 = {"Python", "JavaScript", "HTML"}
# tech1.difference_update(tech2)
# print(tech1)
#
# activities1 = {"Kitob o‘qish", "Sport zal", "Rasm chizish", "Kod yozish"}
# activities2 = {"Sport zal", "Sayr qilish", "Kitob o‘qish"}
# activities1.difference_update(activities2)
# print(activities1)


# intersection() ikkita (yoki undan ko‘p) setni taqqoslaydi.
# Natijada ikkalasida ham mavjud bo‘lgan elementlar qaytadi.
#  Ya’ni faqat umumiy qismini oladi

# subjects1 = {"Matematika", "Fizika", "Tarix", "Kimyo"}
# subjects2 = {"Matematika", "Ingliz tili", "Kimyo"}
# z = subjects1.intersection(subjects2)
# print(z)
#
# sports1 = {"Futbol", "Basketbol", "Tennis"}
# sports2 = {"Tennis", "Hokkey", "Futbol"}
# z = sports1.intersection(sports2)
# print(z)
#
# tech1 = {"Python", "Java", "C++", "HTML"}
# tech2 = {"Python", "JavaScript", "HTML"}
# z = tech1.intersection(tech2)
# print(z)


# intersection_update() — ikkita (yoki undan ko‘p) to‘plamni taqqoslaydi
# Faqat umumiy elementlarni saqlab qoladi, qolganlarini o‘chirib tashlaydi
# # Bu metod birinchi to‘plamni o‘zgartiradi (ya’ni yangi set qaytarmaydi)
#
# subjects1 = {"Matematika", "Fizika", "Tarix", "Kimyo"}
# subjects2 = {"Matematika", "Ingliz tili", "Kimyo"}
# subjects1.intersection_update(subjects2)
# print(subjects1)
#
# sports1 = {"Futbol", "Basketbol", "Tennis"}
# sports2 = {"Tennis", "Hokkey", "Futbol"}
# sports1.intersection_update(sports2)
# print(sports1)
#
# tech1 = {"Python", "Java", "C++", "HTML"}
# tech2 = {"Python", "JavaScript", "HTML"}
# tech1.intersection_update(tech2)
# print(tech1)
#
# isdisjoint() ikkita setni taqqoslaydi.
# Agar ikkalasida ham umumiy element bo‘lmasa → True qaytaradi.
# Agar kamida bitta umumiy element bo‘lsa → False qaytaradi.
# #
# subjects1 = {"Matematika", "Fizika", "Kimyo"}
# subjects2 = {"Tarix", "Geografiya"}
# print(subjects1.isdisjoint(subjects2))
#
#
# set1 = {"Detektiv", "Roman", "Fantastika"}
# set2 = {"She’riyat", "Dramma"}
# print(set1.isdisjoint(set2))
#
# set1 = {"O‘qituvchi", "Dasturchi", "Shifokor"}
# set2 = {"Muhandis", "Arxitektor"}
# print(set1.isdisjoint(set2))


#
# symmetric_difference() ikki setni taqqoslaydi.
# Faqat umumiy bo‘lmagan elementlarni qaytaradi.
# 👉 Ya’ni: ikkalasida turli bo‘lgan narsalarni oladi.
#
# activities1 = {"Kitob o‘qish", "Rasm chizish", "Musiqa tinglash"}
# activities2 = {"Sayr qilish", "Kitob o‘qish", "Pazandachilik"}
# z = activities1.symmetric_difference(activities2)
# print(z)
#
#
# jobs1 = {"O‘qituvchi", "Shifokor", "Dasturchi"}
# jobs2 = {"Shifokor", "Muhandis", "Arxitektor"}
# z = jobs1.symmetric_difference(jobs2)
# print(z)
#
#
# genres1 = {"Roman", "Detektiv", "Fantastika"}
# genres2 = {"Detektiv", "She’riyat", "Dramma"}
# z = genres1.symmetric_difference(genres2)
# print(z)
#
# # ISSUBset ikkinchisining ichida bormi tekshiradi.
# #  True → agar hammasi ichida bo‘lsa.
# a = {"Musiqa", "Sayr qilish"}
# b = {"Musiqa", "Sayr qilish", "Rasm chizish"}
# print(a.issubset(b))
#
#
# a = {"O‘qituvchi", "Shifokor"}
# b = {"O‘qituvchi", "Shifokor", "Muhandis"}
# print(a.issubset(b))
#
#
# a = {"Drama", "Komediya"}
# b = {"Drama", "Fantastika"}
# print(a.issubset(b))


#  REMOVE BEelgilangan elementni o‘chiradi.
#  Agar element mavjud bo‘lmasa — xato chiqaradi.
#
# a = {"Musiqa", "Sayr qilish", "Rasm chizish"}
# a.remove("Sayr qilish")
# print(a)
#
# a = {"Drama", "Komediya"}
# a.remove("Komediya")
# print(a)

# pop()Setdan tasodifiy elementni o‘chiradi va qaytaradi.
# a = {"Musiqa", "Sayr qilish", "Rasm chizish"}
# print(a.pop())
# print(a)
#
#
# a = {"O‘qituvchi", "Shifokor", "Muhandis"}
# print(a.pop())
# print(a)
#
# a = {"Drama", "Komediya", "She’riyat"}
# print(a.pop())
# print(a)

# # issuperset()Bir set boshqasini ichiga oladimi tekshiradi. True → agar ikkinchi set elementlari birinchida mavjud bo‘lsa.
# a = {"Musiqa", "Sayr qilish", "Rasm chizish"}
# b = {"Musiqa", "Sayr qilish"}
# print(a.issuperset(b))
#
#
# a = {"O‘qituvchi", "Shifokor", "Muhandis"}
# b = {"O‘qituvchi", "Shifokor"}
# print(a.issuperset(b))


#  # update()Birinchi setni o‘zgartirib, ikkinchi set elementlarini qo‘shib yuboradi.
# a = {"Rasm chizish", "Sport zal"}
# b = {"Sayr qilish", "Musiqa"}
# a.update(b)
# print(a)
#
#
# a = {"Tarjimon", "Shifokor"}
# b = {"Muhandis", "Arxitektor"}
# a.update(b)
# print(a)
#
#
# a = {"Drama", "Fantastika"}
# b = {"She’riyat", "Roman"}
# a.update(b)
# print(a)

