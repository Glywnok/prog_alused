korda = int(input("Sisesta täisarv: "))
arv = 1
i = 1

while i < korda:
    arv = arv * 2
    i = i + 1
    print(str(arv))
    print(str(i))
print("Nisuteri " + str(korda) + ". ruudu eest: " + str(arv))