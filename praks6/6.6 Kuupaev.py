def kuu_nimi(kuu_nr):
    month = ''
    if kuu_nr == 1:
        month = "jaanuar"
    elif kuu_nr == 2:
        month = "veebruar"
    elif kuu_nr == 3:
        month = "märts"
    elif kuu_nr == 4:
        month = "aprill"
    elif kuu_nr == 5:
        month = "mai"
    elif kuu_nr == 6:
        month = "juuni"
    elif kuu_nr == 7:
        month = "juuli"
    elif kuu_nr == 8:
        month = "august"
    elif kuu_nr == 9:
        month = "september"
    elif kuu_nr == 10:
        month = "oktoober"
    elif kuu_nr == 11:
        month = "november"
    elif kuu_nr == 12:
        month = "detsember"
    return month

def kuupäev_sõnena(päev_sõnena):
    data = päev_sõnena.split('.')
    text = data[0] + ". " + kuu_nimi(int(data[1])) + " " + data[2] + ". a."
    return text
    

kuupäev = input("Sisestage kuupäeva: ")

print(kuupäev_sõnena(kuupäev))