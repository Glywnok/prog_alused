def Lõimede_pikkus(hundred, number):
    return ((hundred) * ((number) * 1.2 + 0.5))


file = input("Sisestage faili nimet: ")
pikk = int(input("Sisestage 5 meetriste ja pikemate vaipade lõimede arv: "))
lühike = int(input("Sisestage lühemate vaipede lõimete arv: "))

vaibid = []
f = open(file, encoding="UTF-8")
for rida in f:
    vaibid += [float(rida.strip())]

f.close()



for tulemus in vaibid:
    
    if tulemus < 5:
        #print("väike")
        print(round(Lõimede_pikkus(lühike, float(tulemus))))
    elif tulemus >= 5:
        #print("pikk")
        print(round(Lõimede_pikkus(pikk, float(tulemus))))
    elif tulemus == "":
        #print("break")
        break
    else:
        print("How and why?")
        exit()


