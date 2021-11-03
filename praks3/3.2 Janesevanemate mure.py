circle_ask = int(input("Mitu ringe sa tahad et janes jooksis? "))
porgandid = 0
circle = 1
while circle <= circle_ask:
    print(str(circle) + ". ring")
    if circle % 2 == 0:
        porgandid = circle + porgandid
    circle = circle + 1
print ("Kokku janes jooksis " + str(circle_ask) + " ringi, ja sai " + str(porgandid) + " porgande.")