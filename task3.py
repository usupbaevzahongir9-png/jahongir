# 1)найти книги 2шт чтобы по прохождению найти автора
# 2)сделать все символы маленькими
# 3) дать алфавит
# 4) конкатанация пар
# 5) найти каждого частату автора вхожений пар  4/len()-1
# 5) list1 = [конкатанация пар /len(file1)-1]
# 6) так же с лист 2
# 7)и что дальше?
alf = 'абвгдеёжзийклмнопрстуфхчщшъыьэюя'
with open('file1.txt',encoding = 'utf-8') as f1:
    t1 = f1.read().lower()
with open('file2.txt',encoding = 'utf-8') as f2:
    t2 = f2.read().lower()
big = []
for a in alf:
    for b in alf:
        big.append(a+b)

f_1 = []
f_2 = []
for bg in big:
    f_1.append(t1.count(bg)/(len(t1)-1))
    f_2.append(t2.count(bg)/(len(t2)-1))
i = 0
total = 0
while i<len(big):
    diff = abs(f_1[i]-f_2[i])
    total += diff
    i += 1
print(total)
