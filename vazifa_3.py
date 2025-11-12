#append  ro‘yxatning oxiriga yangi  element qo‘shadi.

colors = ["red", "green", "blue"]
colors.append("yellow")
print(colors)

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

#insert() — belgilangan joyga element qo‘shadi
colors = ["red", "blue"]
colors.insert(1, "green")
print(colors)

animals = ["cat", "dog"]
animals.insert(0, "bird")
print(animals)


#remove() — berilgan elementni o‘chiradi

names = ["Ali", "Vali", "Soli"]
names.remove("Vali")
print(names)


nums = [10, 20, 30]
nums.remove(20)
print(nums)

#pop() — oxirgi (yoki ko‘rsatilgan indeksdagi) elementni o‘chiradi
letters = ["a", "b", "c"]
letters.pop()
print(letters)

letters = ["a", "b", "c"]
letters.pop()
print(letters)

#clear() — ro‘yxatni tozalaydi

items = [1, 2, 3]
items.clear()
print(items)


words = ["hi", "hello"]
words.clear()
print(words)

# sort() — ro‘yxatni tartiblaydi
numbers = [3, 1, 2]
numbers.sort()
print(numbers)

names = ["Zara", "Ali", "Bob"]
names.sort()
print(names)

# reverse() — ro‘yxatni teskari qiladi
nums = [1, 2, 3]
nums.reverse()
print(nums)

letters = ["a", "b", "c"]
letters.reverse()
print(letters)

# count() — element nechta ekanligini sanaydi
nums = [1, 2, 2, 3]
print(nums.count(2))

letters = ["a", "b", "a", "a"]
print(letters.count("a"))

# index() — elementning indeksini topadi
nums = [10, 20, 30]
print(nums.index(20))

letters = ["x", "y", "z"]
print(letters.index("z"))
