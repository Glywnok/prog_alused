print("Kui suur on fail? ")
suurus = float(input())
print("Kas failil on pealkiri? Kui on kirjuta missugune. ")
nimi = input()
print("Kas kirjale on kaasas fail? ")
fail = input()
if suurus > 1:
    first = True
    if fail == "jah" or "Jah":
        second = True
    else:
        second = False
else:
    first = False
    if nimi == "":
        third = True
    else:
        third = False
if (first == True and second == True) or third == True:
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")
