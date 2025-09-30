# with open('py.txt') as fayl:
#     py = fayl.read()
# print(py)

#
# fayl = open('py.txt')
# py = fayl.read()
# print(py)
# print(type(py))
# fayl.close()
#
# py = py.rstrip()
# py = py.replace('\n',"")
# py = float(py)
# print(type(py))
# print
#
#
# filename='data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(f"Assalomu aleykum {line}")
#
# with open(filename) as file:
#     talabalar=file.readlines()
#
# print(talabalar)
# talabalar=[talaba.rstrip() for talaba in talabalar]
# print(talabalar)

#
# faylnomi = 'developer.txt'
# with open(faylnomi, 'w') as fayl:
#     fayl.write('Shoxruza iskandarovna')
#
# faylnomi = 'new_file.txt'
# ism = 'Atabekova Sevinch'
# tyil = 2006
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism)
#     fayl.write(str(tyil))












import pickle

talaba1 = {'ism':'shohruza','familiya': 'otanazarova','tyil':2007,'kurs':1}
talaba2 = {'ism':'sevinch','familiya': 'Atabekova','tyil':2006,'kurs':2}

with open ('info', 'wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)