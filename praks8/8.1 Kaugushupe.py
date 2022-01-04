def parandatud_tulemus(counted, change):
    return counted + change

print("Palun teid sisestada mõõteparanduses ja normatiivis meetrites")


filename = input("Sisestage failinimet: ")
mõõteparandus = float(input("Sisestage mõõteparandus: "))
normatiiv = float(input("Sisestage meistrivõistluste normatiiv: "))


kaugus = []
f = open(filename, encoding="UTF-8")
for rida in f:
    kaugus += [float(rida)]
    
f.close()

new_kaugus = []

print("Tegelikud tulemused")
for tulemus in kaugus:
    new_kaugus.append(round(parandatud_tulemus(tulemus, mõõteparandus), 2))
    #print(round(new_kaugus, 2))
    #new_kaugus += [float(kaugus)]


täitis = 0
people = 0
box = 0
for result in new_kaugus:
    if result >= normatiiv:
        täitis += 1
    elif result > 0:
        people += 1
    elif result == " ":
        break
    box = box + result
if people == 0:
    print("Mitte keegi ei tahtnud teha ülesannet... On väga halb")
    exit()
print("Normatiivi täitsid " + str(täitis) + ". inimest.")
print("Kokku kaugushüppe ülesannet tegi " + str(people) + ". inimest.\n Nende keskmine resultaat oli " + str(round(box/people, 2)) + " meetrit.")
#print("Kokku kaugushüppe ülesannet tegi " + str(people) + ". \nTäitnute keskmine on " + str(round(summa/arv, 2)) + ".")