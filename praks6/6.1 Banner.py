def banner(lause):
    return lause.upper()


kordamine = int(input(" Mitu korda sa tahd et reklaamlause korrutas? \n "))
reklaamlause = input(" Milline reklaamlause sa tahad? (P.S. Sa pead ise kirjutama selle reklaamlause) \n ")
kord = 1
while kord <= kordamine:
    tulemus = banner(reklaamlause)
    print(tulemus)
    kord = kord + 1