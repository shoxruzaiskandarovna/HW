# 1Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya
def tug_ilgan_yil():
    ism = input("Ismingizni kiriting:")
    yosh = int(input("Yoshingizni kiriting:"))
    yil = 2025 - yosh
    print(f"{ism}, siz {yil}-yilda tug'ilgansiz")
print("1-masala: Tug'ilgan yilni hisoblash")
tug_ilgan_yil()



# 2Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya
def kvadrat_va_kub():
    son = float(input("Son kiriting:"))
    kvadrat = son ** 2
    kub = son ** 3
    print(f"Kvadrati: {kvadrat}")
    print(f"Kubi: {kub}")
kvadrat_va_kub()


# 3Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya
def juft_toq():
    son = int(input("Son kiriting:"))
    if son % 2 == 0:
        print(f"{son} - juft son")
    else:
        print(f"{son} - toq son")
juft_toq()


# 4Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya
def kattasini_top():
    son1 = float(input("Birinchi sonni kiriting:"))
    son2 = float(input("Ikkinchi sonni kiriting:"))
    if son1 > son2:
        print(f"Katta son: {son1}")
    elif son2 > son1:
        print(f"Katta son: {son2}")
    else:
        print("Sonlar teng")
kattasini_top()

# 5Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya
def darajaga_oshirish():
    x = float(input("X sonini kiriting:"))
    y = float(input("Y sonini kiriting:"))
    natija = x ** y
    print(f"{x}^{y} = {natija}")
print("5-masala: Darajaga oshirish")
darajaga_oshirish()

# 6Yuqoridagi funksiyada y uchun 2 standart qiymatini bering
def darajaga_oshirish_standart(x, y=2):
    natija = x ** y
    print(f"{x}^{y} = {natija}")
x_qiymat = float(input("X sonini kiriting:"))
darajaga_oshirish_standart(x_qiymat)
