Nimi = input("Palun sisestage oma nimet: ")
Nimi = str(Nimi)
Lubatud = input("Sisestage lubatud kiirus: ")
Lubatud = int(Lubatud)
Kiirus = input("Sisestage teie kiirus: ")
Kiirus = int(Kiirus)
MAX_INT = 180
Trahv = ((int(Kiirus)) - int(Lubatud)) * 3
Trahv = str(Trahv)
print( Nimi + ", kiiruse ületamise eest on teie trahv " + Trahv + " eurot.")