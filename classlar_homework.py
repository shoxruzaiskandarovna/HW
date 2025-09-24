class User:
    def __init__(self, full_name, username, email, age, address):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.age = age
        self.address = address


    def get_info(self):
        return (f"Foydalanuvchi: {self.username}, "
                f"Ismi: {self.full_name}, "
                f"Email: {self.email}, "
                f"Yoshi: {self.age}, "
                f"Manzili: {self.address}")

    def increment_age(self):
        self.age += 1

    def update_email(self, new_email):
        self.email = new_email

user1 = User("Otanazarova Shoxruza", "shoxruza07", "shaxrzuaotanazrova@gmail.com", 17, "Xiva")

print(user1.get_info())
user1.increment_age()
print("Yoshi oshgandan keyin:", user1.get_info())

###########################################################

class Avto:
    def __init__(self, model, rang, korobka, narh, yil, km=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = yil
        self.km = km

    def get_info(self):
        return (f"Model: {self.model}, Rang: {self.rang}, "
                f"Korobka: {self.korobka}, Narh: {self.narh}$, "
                f"Yil: {self.yil}, Yurgan: {self.km} km")

    def update_km(self, km):
        if km >= 0:
            self.km += km
        else:
            print(" 0")

# avto1 = Avto("Gentra", "Oq", "Mexanik", 12000, 2022)
# print(avto1.get_info())
#
# avto1.update_km(1500)
# print("Yangilangan ma’lumot:", avto1.get_info())
#




class Avtosalon:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avtos(self):
        return [avto.get_info() for avto in self.avtolar]

avto1 = Avto("Gentra", "Oq", "Mexanik", 12000, 2022)
avto2 = Avto("Cobalt", "Qora", "Avtomat", 13500, 2023, km=5000)

salon = Avtosalon("Xiva Motors", "Xiva sh.")
salon.add_avto(avto1)
salon.add_avto(avto2)

for info in salon.get_avtos():
    print(info)

print( avto1.get_info())


print(dir(Avto))
print(dir(str))
