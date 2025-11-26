class Avto:
    def __init__(self, model, yil, yurgan_km, narx):
        self.model = model
        self.yil = yil
        self.yurgan_km = yurgan_km
        self.narx = narx

    def info(self):
        """Avtomobil haqida ma'lumot qaytaradi"""
        print(f"Model: {self.model}")
        print(f"Yil: {self.yil}")
        print(f"Yurgan masofa: {self.yurgan_km} km")
        print(f"Narx: ${self.narx}")
        print("-" * 30)

    def yurish(self, km):
        """Mashina yurgan masofasiga km qo'shadi"""
        if km < 0:
            print("Km manfiy bo'lishi mumkin emas")
        else:
            self.yurgan_km += km
            print(f"{self.model} {km} km yurdi. Jami masofa: {self.yurgan_km} km")

    def chegirma(self, foiz):
        """Berilgan foiz bo'yicha narxni kamaytiradi"""
        chegirma_summasi = self.narx * foiz / 100
        self.narx -= chegirma_summasi
        print(f"{self.model} uchun {foiz}% chegirma qo'llandi. Yangi narx: ${self.narx}")


# 3 ta obyekt yaratamiz
nexia = Avto("Nexia", 2015, 120000, 5500)
malibu = Avto("Malibu", 2020, 45000, 18000)
tracker = Avto("Tracker", 2022, 25000, 22000)
nexia.info()
malibu.info()
tracker.info()

malibu.yurish(500)
print()
tracker.chegirma(15)
print()

# Yana info() larini yangilangan holda chiqaramiz
nexia.info()
malibu.info()
tracker.info()
