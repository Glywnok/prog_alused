fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    
    vastuvõetud.append(int(rida))
    
fail.close()

#print(vastuvõetud)

aasta = int(input("Siseta millest aastast sa tahda teada? \nP.S. saaba teada saada ainult aastatest 2011. kuni 2019. \n "))
    
aasta1 = aasta - 2011
    
print(str(aasta) + ". aastal võeti Ülikooli " + str(vastuvõetud[aasta1]) + " õilast.")