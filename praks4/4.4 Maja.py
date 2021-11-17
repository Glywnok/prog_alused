from tkinter import *

raam = Tk()
raam.title("Liiklusmärk")

tahvel = Canvas(raam, width=750, height=700, background="cyan")
tahvel.grid()

tahvel.create_rectangle(0, 600, 750, 700, fill="yellow", outline="yellow")

tahvel.create_rectangle(450, 400, 750, 600, fill="brown", outline="brown")

tahvel.create_rectangle(700, 400, 670, 200, fill="black", outline="black")

tahvel.create_polygon(600, 200, 750, 400, 450, 400, fill="grey", outline="grey")

tahvel.create_rectangle(475, 425, 550, 600, fill="brown", outline="black")

tahvel.create_oval(525,525,540,540, fill="black", outline="green")

tahvel.create_rectangle(600, 450, 700, 550, fill="white", outline="black")

tahvel.create_rectangle(600, 498, 700, 502, fill="black")

tahvel.create_rectangle(648, 550, 652, 450, fill="black")

raam.mainloop()