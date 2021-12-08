from datetime import datetime
kuupäev_kellaeg = str(datetime.today())


f = open("Paevik.txt", "a", encoding="UTF-8")

tegin = input("Sisesta mida sa tahad lisada: ")

f.write(kuupäev_kellaeg + "\n")
f.write(tegin + "\n")
f.write("\n")
f.close()
