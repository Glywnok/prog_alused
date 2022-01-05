def juurdekasv(pindala, aastanejuurdekasv):
    return (pindala) * 0.4047 * (aastanejuurdekasv)
    

file = input("Sisestage faili nimet: ")
aastanejuurdekasv = (float(input("Sisestage aastane juurdekasv hektari kohta tihumeetrites: ")))
many = (float(input("Sisestage piir, mitmes aakrist suuremad metsatükid arvesse võtta: ")))

aakrid = []
f = open(file, encoding="UTF-8")
for rida in f:
    aakrid += [float(rida.strip())]
f.close

ring = 0
while ring <= many - 1:
    #print("inside")
    pindala = aakrid[ring]
    print("Metsatükki aastane juurdekasv on " + str(round(juurdekasv(pindala, aastanejuurdekasv), 2)))
    ring += 1
    