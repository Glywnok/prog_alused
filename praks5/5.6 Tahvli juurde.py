from datetime import date
failinimi = input(str(" Sisestage palun failinimet. \n "))

fail = open(failinimi, encoding="UTF-8")

nimikiri = []

for rida in fail:
    
    nimikiri.append(str(rida.strip()))

if len(nimikiri) < 30 :
    print(" Nimekirjas on vähe nimet, valige uue faili! ")
    exit()

today = str(date.today())
print(nimikiri[int(today.split("-")[2]) - 1])
