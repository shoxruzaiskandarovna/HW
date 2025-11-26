class User:

    def __init__(self, ism, familiya, foydalanuvchi_ismi, email, telefon=None):
        self.ism = ism
        self.familiya = familiya
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.email = email
        self.telefon = telefon
        self.royxatdan_otgan = True

    def get_info(self):
        info = f"Foydalanuvchi: {self.foydalanuvchi_ismi}, "
        info = f"ismi: {self.ism} {self.familiya}, "
        info = f"email: {self.email}"

        if self.telefon:
            info += f", telefon: {self.telefon}"

        return info

    def get_full_name(self):
        """Foydalanuvchining to'liq ismini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def update_email(self, yangi_email):
        """Email manzilini yangilash"""
        self.email = yangi_email
        print(f"Email manzil yangilandi: {yangi_email}")

    def update_telefon(self, yangi_telefon):
        """Telefon raqamini yangilash"""
        self.telefon = yangi_telefon
        print(f"Telefon raqam yangilandi: {yangi_telefon}")


user1 = User("Alijon", "Valiyev", "alijon1994", "alijon1994@gmail.com", "+998901234567")
print("\n1. " + user1.get_info())
user2 = User("Madina", "Karimova", "madina_k", "madina.k@example.com")
print(user2.get_info())
user3 = User("Bekzod", "Toshmatov", "bekzod_t", "bekzod@mail.uz", "+998977654321")
print(user3.get_info())
user4 = User("Dilnoza", "Rahimova", "dilnoza2000", "dilnoza@gmail.com")
print(user4.get_info())
user5 = User("Sardor", "Abdullayev", "sardor_dev", "sardor.dev@example.uz", "+998909876543")
print(user5.get_info())

print(f"\nUser1 ning to'liq ismi: {user1.get_full_name()}")

print("\nUser2 ning email manzilini yangilash:")
user2.update_email("madina.karimova@newmail.com")

print("\nUser4 ga telefon raqam qo'shish:")
user4.update_telefon("+998931112233")

print("\nYangilangan ma'lumotlar:")
print(user2.get_info())
print(user4.get_info())
