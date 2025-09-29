class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yoshda"


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi


class Talaba(Shaxs):
    def __init__(self, ism, familiya, yosh, id_raqam):
        super().__init__(ism, familiya, yosh)
        self.id_raqam = id_raqam
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        if self.fanlar:
            fanlar = ', '.join([fan.nomi for fan in self.fanlar])
        else:
            fanlar = "Fan yo‘q"
        return f"Talaba: {self.ism} {self.familiya}, {self.yosh} yoshda, ID:{self.id_raqam}, Fanlar: {fanlar}"

matematika = Fan("Matematika")
fizika = Fan("Fizika")
informatika = Fan("Informatika")

talaba1 = Talaba("Shoxruza", "Otanzarova", 18, "T123")

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(informatika)

print(talaba1.get_info())

talaba1.remove_fan(fizika)
talaba1.remove_fan(matematika)

print(talaba1.get_info())

print(matematika.nomi)
print(fizika.nomi)
print(informatika.nomi)



class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yoshda"



class Professor(Shaxs):
    def __init__(self, ism, familiya, yosh, kafedra):
        super().__init__(ism, familiya, yosh)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor {self.ism} {self.familiya}, {self.yosh} yoshda, Kafedra: {self.kafedra}"

class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, username):
        super().__init__(ism, familiya, yosh)
        self.username = username

    def get_info(self):
        return f"Foydalanuvchi: {self.username} ({self.ism} {self.familiya})"

class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, dokon):
        super().__init__(ism, familiya, yosh)
        self.dokon = dokon

    def get_info(self):
        return f"Sotuvchi {self.ism} {self.familiya}, Do‘kon: {self.dokon}"

class Mijoz(Shaxs):
    def __init__(self, ism, familiya, yosh, mijoz_id):
        super().__init__(ism, familiya, yosh)
        self.mijoz_id = mijoz_id

    def get_info(self):
        return f"Mijoz {self.ism} {self.familiya}, ID: {self.mijoz_id}"


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, yosh, username, daraja):
        super().__init__(ism, familiya, yosh, username)
        self.daraja = daraja

    def ban_user(self, foydalanuvchi):
        print(f"Foydalanuvchi {foydalanuvchi.username} bloklandi!")

    def get_info(self):
        return f"Admin: {self.username}, daraja: {self.daraja}"

prof = Professor("shoxruza", "otanazarova", 18, "Matematika")
print(prof.get_info())

user1 = Foydalanuvchi("sevinch", "otabekova", 19, "sevinch18")
print(user1.get_info())

sotuvchi1 = Sotuvchi("feruza", "otanazarova", 18, "ruzella")
print(sotuvchi1.get_info())

mijoz1 = Mijoz("shoxruza", "otanazarova", 18, "M001")
print(mijoz1.get_info())

admin1 = Admin("Abbos", "ahmedov", 23, "abbos_admin", "Super")
print(admin1.get_info())


