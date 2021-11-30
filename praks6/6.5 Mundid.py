#max 16 . mündid.txt encoding= UTF-8

def pronksikarva_summa(mündid):
    summa = 0
    for münt in mündid:
        if münt == 1 or münt == 2 or münt == 5:
            summa = summa + münt
    return summa
failinimi = input("Sisestage failinimi ")
fail = open(failinimi, encoding="UTF-8")
mündid = []
for rida in fail:
    mündid.append(int(rida.strip()))                                
fail.close()

print(mündid)

print(pronksikarva_summa(mündid))

