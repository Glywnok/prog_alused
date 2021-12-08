from urllib.request import urlopen

kuu = str(input("Sisestage kuu: \nP.S. sisestage kuupäeva väikese tähtedega \n"))
päev = (input("Sisestage päeva: \nP.S. sisestage päeva numbrit numbrina \n"))
print("Kuupäeval " + str(päev) + ". " + kuu + " on nimepäevad järgimsel inimestel: ")

failVeebis = urlopen("http://kodu.ut.ee/~eno/mooc/" + kuu)
baidid = failVeebis.read()
tekst = baidid.decode()            
ridadeKaupa = tekst.splitlines()  
failVeebis.close()
print(ridadeKaupa[4])             