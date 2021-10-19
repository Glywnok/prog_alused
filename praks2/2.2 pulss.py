vanus = int(input("Sisestage oma vanus "))
sugu = input("Sisestage oma sugu ")
Trenningtype = input("Sisestage oma trenningu tüüp: 1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening. ")
if sugu == "M" or sugu == "m":
    puls = 220 - vanus
if sugu == "N" or sugu == "n":
    puls = 206 - vanus * 0.88
pulssmadal = 0
pulsskorg = 0
if Trenningtype == 1:
    pulssmadal = 0.5 * puls
    pulsskorg = 0.7 * puls
elif Trenningtype == 2:
    pulssmadal = 0.7 * puls
    pulsskorg = 0.8 * puls
elif Trenningtype == 3:
    pulssmadal = 0.8 * puls
    pulsskorg = 0.87 * puls
print("Pulsisagedus peaks olema vahemikus " + str(pulssmadal) + " ja " + str(pulsskorg) + ".")
