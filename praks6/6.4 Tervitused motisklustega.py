def tutvustus(külaline):
    print(" Võõrustaja: """ "Tere! " "" "\n Täna """ + str(kord) + """. kord tervitada, mõtiskleb võõrustaja. \n Külaline: """ "Tere, suur tänu kutse eest! " "")
    return " "

times = int(input(" Sisestage külaliste arv "))

kord = 1
while kord <= times:
    tulemus = tutvustus(times)
    print(tulemus)
    kord = kord + 1