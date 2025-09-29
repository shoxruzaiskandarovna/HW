
class Shaxs:
    odamlar_soni = 0   # Klassga oid xususiyat

    def __init__(self, ism, familiya, yosh):
        self.__ism = ism
        self.__familiya = familiya
        self.__yosh = yosh
        Shaxs.odamlar_soni += 1   # har yangi obyekt yaratilganda oshadi

    def get_ism(self):
        return self.__ism

    def get_familiya(self):
        return self.__familiya

    def get_yosh(self):
        return self.__yosh


    def set_ism(self, ism):
        self.__ism = ism

    def set_familiya(self, familiya):
        self.__familiya = familiya

    def set_yosh(self, yosh):
        self.__yosh = yosh

    def get_info(self):
        return f"{self.__ism} {self.__familiya}, {self.__yosh} yoshda"


    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni



class Talaba(Shaxs):
    talabalar_soni = 0

    def __init__(self, ism, familiya, yosh, id_raqam):
        super().__init__(ism, familiya, yosh)
        self.__id_raqam = id_raqam
        self.fanlar = []
        Talaba.talabalar_soni += 1


    def get_id_raqam(self):
        return self.__id_raqam

    def set_id_raqam(self, id_raqam):
        self.__id_raqam = id_raqam


    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        fanlar = ', '.join([str(fan) for fan in self.fanlar]) if self.fanlar else "Fan yo‘q"
        return f"Talaba: {self.get_ism()} {self.get_familiya()}, {self.get_yosh()} yoshda, ID:{self.__id_raqam}, Fanlar: {fanlar}"


    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def __repr__(self):
        return self.nomi




# Talabalar yaratamiz
talaba1 = Talaba("shoxruza", "otanzarova", 18, "T123")
talaba2 = Talaba("Aziza", "Rahimova", 19, "T124")

# Fanlar yaratamiz
matematika = Fan("Matematika")
informatika = Fan("Informatika")

# Fanlarga yozilish
talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(informatika)
talaba2.fanga_yozil(informatika)

print(talaba1.get_info())
print(talaba2.get_info())

print("Talabalar soni:", Talaba.get_talabalar_soni())
print("Odamlar soni:", Shaxs.get_odamlar_soni())