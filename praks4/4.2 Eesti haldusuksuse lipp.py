from tkinter import *
 
raam = Tk()
raam.title("Maardu lipp")
tahvel = Canvas(raam, width=750, height = 500)
kõrgus = 100
i = 0
while i < 5:
    if i == 0 or i == 4:
        tahvel.create_rectangle(0, i * kõrgus, 750, (i + 1) * kõrgus, fill="cyan", outline="cyan")
    else:
        tahvel.create_rectangle(0, i * kõrgus, 750, (i + 1) * kõrgus, fill="white", outline="white")
    i += 1
tahvel.pack()
raam.mainloop()