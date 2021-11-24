#ok boomer
#Copy & paste is a good thing m8

circle_ask = int(input("Mitu ringe sa tahad et janes jooksis? "))
porgandid = 0
for circle in range(1 ,circle_ask+1):
    print(str(circle) + ". ring")
    if circle % 2 == 0:
        porgandid = circle + porgandid
print ("Kokku janes jooksis " + str(circle_ask) + " ringi, ja sai " + str(porgandid) + " porgande.")