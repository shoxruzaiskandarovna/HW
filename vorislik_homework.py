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
