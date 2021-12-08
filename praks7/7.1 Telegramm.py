
filename =(input("Millist faili te tahate lugeda? "))

f = open(filename, encoding="UTF-8")
 
sisu = f.read().upper().replace("Õ", "OE").replace("Ü", "UE").replace("Ä", "AE").replace("Ö", "OE")

f.close()

print(sisu)