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

filename='talabalar.txt'
with open(filename) as file:
    for line in file:
        print(f"Assalomu aleykum {line}")

with open(filename) as file:
    talabalar=file.readlines()

print(talabalar)
talabalar=[talaba.rstrip() for talaba in talabalar]
print(talabalar)