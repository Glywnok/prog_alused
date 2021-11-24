failinimi = str(input(" Palun sisestage millise faili te tahate. \n Te võidte vailida nende vahel: \n 1. 80ndad.txt \n 2. jukebox.txt \n 3. edm.txt \n 4. eesti_muusika.txt \n Valige! \n P.S. kirjutage ainult numbrit \n "))

if failinimi == "1":
    failinimi = ("80ndad.txt")
elif failinimi == "2":
    failinimi = ("jukebox.txt")
elif failinimi == "3":
    failinimi = ("edm.txt")
elif failinimi == "4":
    failinimi = ("eesti_muusika")
else:
    print("Sisestatud number ei nõusta proovi uuesti.")

print(str(failinimi))

open = (failinimi, encoding="UTF-8")