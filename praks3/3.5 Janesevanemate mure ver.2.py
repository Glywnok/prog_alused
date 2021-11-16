korda = int(input("Siseta mitu ringi peab jänes jooksma? "))
i = 1
toit = 0
kokku = 0

while i <= korda:
    toit = toit + i
    i = i + 1
    kokku = kokku + toit
    
print("Jänes jooksis " + str(korda) + " ringi ja sai " + str(kokku) + " porgandi")