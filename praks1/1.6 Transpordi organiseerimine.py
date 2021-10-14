x = int(input("Sisestage mitu inimest teil on: "))

y = int(input("Sisestage mitu bussi teil on: "))

z = int(input("Sisestage mitu inimest kokku võib istuda bussis: "))

#x on inimest
#y on bussi
#z on inimest ühes bussis võib istuda(ilma bussijuthti).
#mitu_kohhti on mitu on kokku kohti
#saab_sisse on mitu inimest saab bussi
#c on kokku mitu inimest jääb ära, võib teha if-iga asju...

#siin kirjutan arvutuse

mitu_kohti = ( y * z )
c = ( x - mitu_kohti )
saab_sisse = ( mitu_kohti - c )
#redaktuur 10:18 PM kodus 09.10: halvasti on...
#redaktuur 10:41 AM tunnis 14.10: hästi tuleb

#siin ma printid mitu inmest on kokku

if c > 0:
    print("Kokku on " + str(x) + " inimest ja " + str(y) + " bussi. Kokku ühes bussis võib istuda " + str(z) + " inimest. Kokku bussi saab " + str(saab_sisse) + " inimest,  ja " + str(c) + " inimest saab ära jääda.")
else:
    print("Kokku on " + str(x) + " inimest ja " + str(y) + " bussi. Kokku ühes bussis võib istuda " + str(z) + " inimest. Kokku bussi saab " + str(saab_sisse) + " inimest, ja mitte keegi ei jää ära!")