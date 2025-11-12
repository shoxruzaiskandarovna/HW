rang = input("Svetafor qaysi rangda? (qizil, sariq ,yashil):").lower()
while rang not in ["qizil", "sariq", "yashil"]:
    print("Xato rang! Qayta kiriting.")
    rang = input("Svetafor qaysi rangda? (qizil/sariq/yashil):").lower()

print("Rahmat, to'g'ri keladi!")

#random o`yini
import random
tasodifiy_son = random.randint(1, 10)
taxmin = int(input("1 dan 10 gacha bo'lgan sonni toping:"))

while taxmin != tasodifiy_son:
    print("Noto'g'ri, qayta urinib ko'ring!")
    taxmin = int(input("Yana urinib ko'ring: "))
print("Tabriklaymiz, siz topdingiz!")

###############################3######
dostlar = []
while True:
    ism = input("Do'stingiz ismini kiriting (to'xtatish uchun 'stop' yozing):")
    if ism.lower() == "stop":
        break
    dostlar.append(ism)
print("Sizning do'stlaringiz ro'yxati:")
for dostlar in dostlar:
    print("dostlar")

