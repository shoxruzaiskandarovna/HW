import pickle
pi = 'pi_million_digits.txt'

with open('pi_million_digits.txt', 'r') as fayl:
    ozgaruvchi = million_digits = fayl.read()
check = ozgaruvchi.count('26082007')
if check > 0:
    print(".txt ichida 26.08.2007 tugilgan sanangiz mavjud")
else:
    print("tugilgan sanangiz mavjud emas")


pi_float = float(ozgaruvchi[:10])
with open('pi_million_digits.txt', 'wb') as fayl:
    pickle.dump(pi_float, fayl)
    print('pi son floatga otdi pickle formatda')