from tkinter import *

raam = Tk()
raam.title("Liiklusmärk")

tahvel = Canvas(raam, width=300, height=500, background="white")
tahvel.grid()

tahvel.create_rectangle(0,0,300,500, fill="blue")

tahvel.create_rectangle(100,125,200,400, fill="white", outline="white")

tahvel.create_polygon(250, 125, 50, 125, 150, 25, fill="white", outline="white")

raam.mainloop()