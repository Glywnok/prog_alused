#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))

#See on lihtsalt copy paste, nüüd on vaja kirjutada koodi!


date_of_born = input(str("Sisestage kuupäeva. \nP.S. Kirjutage ainult numbritega:\n"))

print(elutee(date_of_born))

#ummmm, kas see on cheating või mitte?

number = elutee(date_of_born)

f = open("eluteenumber" + str(number) + ".txt", "w")

f.write(date_of_born + "\n")
f.close()