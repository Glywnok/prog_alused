#a = input("sisestage ainepunkt arv ")
#b = input("sisestage nädalate arv ")
#c = (a * 26 / b)
#print (round(c, 0))
#See oli esimene kuidas tahtsin teha, vaatasin internetis kuidas oli vaja teha

ainepunkt_arv = input("sisestage ainepunkt arv ")
ainepunkt_arv = int(ainepunkt_arv)

nadalate_arv = input("sisestage nädalate arv ")
nadalate_arv = int(nadalate_arv)

Punktid = (ainepunkt_arv * 26 / nadalate_arv)

print(round(Punktid))