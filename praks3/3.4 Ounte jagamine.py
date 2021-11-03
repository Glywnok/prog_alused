from random import randint

korda = int(input("Mitu pöialpoissi tahab õunu? "))
i = 1
kokku = 14
while i <= korda:
    õunad = randint(1,2)
    print(str(õunad))
    # anname need õunad ära
    kokku = kokku - õunad
    i = i + 1 # järgmine tsükli samm
'''
if õunad > 14:
    print("Väga palju pöialpoissi tahab õunu.")
else:
    if õunad == 14:
        print("Õunu pole, sest kõik õunu on juba ära võtnud(ehk neid pole sest kõik on kasutanud")
    else:
        print("Õunu tahab " + str(korda) + " pöiapoissi ja on antud " + str(kokku) + " õunu, ja veel on " + str())
'''
print("Lumivalgekesele jäi " + str(kokku) + " õunu ")