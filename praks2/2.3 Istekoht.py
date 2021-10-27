from random import randint

print("Kas te tahate ise valida oma koht või lossida? ")
inimene = input()
if inimene == "ise":
    print("Kus te tahate istuda kas akna juurde või mujale? ")
    koht = input()
    if koht == "akna":
        kirjeldus = "Aknajuurde"
    else:
        kirjeldus = "Vahekärigukoht"
    print("Valisite " + inimene + ". " + kirjeldus + ".")
else:
    koht = randint(1, 3) # on vaja genereerida 1, 2, või 3
    if koht == 1:
        kirjeldus = "Aknakoht"
    else:
        kirjeldus = "Vahekäigukoht"
    print("Istekoht loositi. " + kirjeldus + ".")