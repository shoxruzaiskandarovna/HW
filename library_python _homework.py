import re
emails = [
    "ali@gmail.com",            #Togri
    "test.user@yahoo.uz",       #Togri
    "invalid@",                 #notog`ri
    "@example.com",             #notog`ri
    "user@domain"               #notog`ri
]

email_pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$'

print(" Email tekshirish natijalari")
for email in emails:
    if re.match(email_pattern, email):
        print(f"{email}  To‘g‘ri email")
    else:
        print(f"{email}  Noto‘g‘ri email")

# masala2
text = """
Aloqa: +998901234567
Raqam: 998971234567
Tel: 901234567 (noto'g'ri)
"""

phone_pattern = r'(?:\+?998)(\d{2})(\d{3})(\d{2})(\d{2})'
numbers = re.findall(phone_pattern, text)
print("\n Telefon raqam formatlash natijalari ")
for n in numbers:
    formatted = f"+998 {n[0]} {n[1]} {n[2]} {n[3]}"
    print("Topildi:", formatted)
