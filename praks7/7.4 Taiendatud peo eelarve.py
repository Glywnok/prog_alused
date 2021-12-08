def eelarve(inimenemax, inimenemin):
    print(inimenemax * 10 + 55)
<    return inimenemin * 10 + 55

failinimi = (input("Sisestage failinimet: "))

f = open (failinimi, encoding="UTF-8")

sisu = f.read()

tuleb = 0
line_count = 0

for rida in f:
    kes = rida.split()
    for t in kes:
        if t == "+":
            tuleb =+ 1
        if line != "\n":
            line_count += 1

f.close()


print(eelarve(line_count, tuleb))