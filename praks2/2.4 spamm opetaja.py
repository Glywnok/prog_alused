print("Sisestage kirja suurus")
suurus = float(input())
print("Sisestage kirja teema pealkiri")
pealkiri = input()
print("Kas kirjaga on kaasas fail?")
fail = input()
if pealkiri == "" or (suurus > 1.0 and fail == "jah"):
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")