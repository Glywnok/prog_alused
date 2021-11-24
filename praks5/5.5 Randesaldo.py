fail1 = open("sisseranne.txt", encoding="UTF-8")

inimesisisse = []

for rida in fail1:
    
    inimesisisse.append(int(rida.strip()))
    
fail1.close()


fail = open("valjaranne.txt", encoding="UTF-8")

inimesivälja = []

for rida in fail:
    
    inimesivälja.append(int(rida.strip()))
    
fail.close()

'''
print(inimesisisse)
print(inimesivälja)
'''

vahe = []

for i in range(len(inimesisisse)):
    vahe.append(inimesisisse[i] - inimesivälja[i])
    
print(vahe)

