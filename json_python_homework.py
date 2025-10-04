import json
data = {"Model" :"Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

json_data = json.dumps(data)
print("Mashina JSON:", json_data)

talaba_json = """{"ism":"shohruza","familiya":"otanzarova","tyil":2007}"""


talaba = json.loads(talaba_json)

print("Talaba ismi:", talaba["ism"])
print("Talaba familiyasi:", talaba["familiya"])

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("talaba.json", "w") as f:
    json.dump(talaba, f, indent=4)

print("\n Fayllar muvaffaqiyatli saqlandi: data.json va talaba.json")
