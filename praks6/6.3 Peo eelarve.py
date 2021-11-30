def eelarve(inimenemax, inimenemin):
    print(inimenemax * 10 + 55)
    return inimenemin * 10 + 55

inimenemax = int(input("Mitu inimest võib tulla maksimalselt?"))
inimenemin = int(input("Mitu inimest tulevad?"))

print(eelarve(inimenemax, inimenemin))