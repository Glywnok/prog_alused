fail = open("konto.txt", encoding="UTF-8")

raha = []

for rida in fail:
    
    raha.append(float(rida.strip()))
    
fail.close()

#print(raha)


for element in raha:
    if element > 0:
        print(element)

'''for i in range(len(raha)):
    if raha[i] >= 0:
        print(raha[i])'''