# 1-misol
def user_data(first_name, last_name, age):
     print(f"Ism: {first_name}")
     print(f"Familiya: {last_name}")
     print(f"Yosh: {age}")
# # Input orqali olish
ism = input("Ismni kiriting: ")
familiya = input("Familiyani kiriting: ")
yosh = int(input("Yoshni kiriting: "))
# user_data(ism, familiya, yosh)
# 2-misol
def find_max(a, b, c):
    max_val = max(a, b, c)
    result = []
    if a == max_val:
        result.append("A")
    if b == max_val:
        result.append("B")
    if c == max_val:
        result.append("C")
    print(f"Eng katta son - {' va '.join(result)} = {max_val}")

# Input orqali
a = int(input("A ni kiriting: "))
b = int(input("B ni kiriting: "))
c = int(input("C ni kiriting: "))

find_max(a, b, c)

# 3-misol
def find_letter_count(word, letter):
    count = word.lower().count(letter.lower())
    print(f'"{word}" so‘zida "{letter}" dan {count} ta.')

# Input
word = input("So‘zni kiriting: ")
letter = input("Qidiriladigan harfni kiriting: ")

find_letter_count(word, letter)



# 4-misol
def find_letter_count(word, letter):
     count = word.lower().count(letter.lower())
     print(f'"{word}" so‘zida "{letter}" dan {count} ta.')

 # Input
word = input("So‘zni kiriting: ")
letter = input("Qidiriladigan harfni kiriting: ")
#
find_letter_count(word, letter)

def list_sum(myList):
     print("Listning elementlar yig‘indisi =", sum(myList))
#
numbers = [2, 5, 10, 15]
list_sum(numbers)
#
def daraja4(a, b, c, d):
    print(a ** b, a ** c, a ** d)

daraja4(2, 2, 3, 4)  # 4 8 16


def digit_count_and_sum(word):
    digits = [int(ch) for ch in word if ch.isdigit()]
    print(f"Raqamlar soni: {len(digits)}")
    print(f"Raqamlar yig‘indisi: {sum(digits)}")

digit_count_and_sum("salom12345")


def add_right(a, b):
    print(int(str(a) + str(b)))

add_right(12, 34)   # 1234


def work_with_list(a):
    min_val = min(a)
    new_list = [x * min_val for x in a]
    print(new_list)

work_with_list([5, 2, 8, 3])   # [10, 4, 16, 6]

