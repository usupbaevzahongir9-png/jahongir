
with open('file1.txt', encoding='UTF-8') as f1:
    t1 = f1.read().lower()
alf = 'абвгдеёжзийклмнопрстуфхцъыбэюя'
numeral = [i for i in range(len(alf))]
key = 'привет это ключ'
key1 = 'ключится'
symbl = [a for a in t1 if a in alf]
t_numb = [numeral[i] for a in symbl for i in range(len(alf)) if a == alf[i]]
k_numb = [numeral[i] for a in key for i in range(len(alf)) if a == alf[i]]
k1_numb = [numeral[i] for a in key1 for i in range(len(alf)) if a == alf[i]]
res = []
i = 0
j = 0
while i < len(t_numb):
    a = t_numb[i]
    b = k_numb[j]
    c = (a + b) % len(alf)
    res.append(alf[c])
    i += 1
    j += 1
    if j == len(k_numb):
        j = 0
res1 = []
i = 0
j = 0
while i < len(t_numb):
    a = t_numb[i]
    b = k1_numb[j]
    c = (a + b) % len(alf)
    res1.append(alf[c])
    i += 1
    j += 1
    if j == len(k1_numb):
        j = 0
chastota = []
i = 0
while i < len(alf):
    chastota.append(res.count(alf[i]) / len(res))
    i += 1
chastota1 = []
i = 0
while i < len(alf):
    chastota1.append(res1.count(alf[i]) / len(res1))
    i += 1
i = 0
while i < len(alf):
    print(alf[i], round(chastota[i], 4), round(chastota1[i], 4))
    i += 1
