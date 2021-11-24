from tkinter import *
 
raam = Tk()
raam.title("Male")

tahvel = Canvas(raam, width=800, height = 800, background="white")
tahvel.grid()

#center
tahvel.create_rectangle(0,0,100,100, fill="black", outline="black")
tahvel.create_rectangle(100,100,200,200, fill="black", outline="black")
tahvel.create_rectangle(200,200,300,300, fill="black", outline="black")
tahvel.create_rectangle(300,300,400,400, fill="black", outline="black")
tahvel.create_rectangle(400,400,500,500, fill="black", outline="black")
tahvel.create_rectangle(500,500,600,600, fill="black", outline="black")
tahvel.create_rectangle(600,600,700,700, fill="black", outline="black")
tahvel.create_rectangle(700,700,800,800, fill="black", outline="black")

#line 1
tahvel.create_rectangle(200,000,300,100, fill="black", outline="black")
tahvel.create_rectangle(400,000,500,100, fill="black", outline="black")
tahvel.create_rectangle(600,000,700,100, fill="black", outline="black")

#line 2
tahvel.create_rectangle(300,100,400,200, fill="black", outline="black")
tahvel.create_rectangle(500,100,600,200, fill="black", outline="black")
tahvel.create_rectangle(700,100,800,200, fill="black", outline="black")

#line 3
tahvel.create_rectangle(000,200,100,300, fill="black", outline="black")
tahvel.create_rectangle(400,200,500,300, fill="black", outline="black")
tahvel.create_rectangle(600,200,700,300, fill="black", outline="black")

#line 4
tahvel.create_rectangle(100,300,200,400, fill="black", outline="black")
tahvel.create_rectangle(500,300,600,400, fill="black", outline="black")
tahvel.create_rectangle(700,300,800,400, fill="black", outline="black")

#line 5
tahvel.create_rectangle(000,400,100,500, fill="black", outline="black")
tahvel.create_rectangle(200,400,300,500, fill="black", outline="black")
tahvel.create_rectangle(600,400,700,500, fill="black", outline="black")

#line 6
tahvel.create_rectangle(100,500,200,600, fill="black", outline="black")
tahvel.create_rectangle(300,500,400,600, fill="black", outline="black")
tahvel.create_rectangle(700,500,800,600, fill="black", outline="black")

#line 7
tahvel.create_rectangle(000,600,100,700, fill="black", outline="black")
tahvel.create_rectangle(200,600,300,700, fill="black", outline="black")
tahvel.create_rectangle(400,600,500,700, fill="black", outline="black")

#line 8
tahvel.create_rectangle(100,700,200,800, fill="black", outline="black")
tahvel.create_rectangle(300,700,400,800, fill="black", outline="black")
tahvel.create_rectangle(500,700,600,800, fill="black", outline="black")

'''
i = 1
while i <= 8:
    line = 1
    if line % 2 == 0:
        kord = 1
        if kord % 2 == 0:
            time = 0
            tahvel.create_rectangle(0 + time * 100 , 0 + time * 100, 100 * time, 100 * time, fill = "black", outline="black")
            kord = kord + 1
            time = time + 2

'''
#Malenuppud
tahvel.create_oval(125,125,175,175, fill="black", outline="white")
tahvel.create_oval(75,75,25,25, fill="white", outline="black")

tahvel.create_oval(225,225,275,275, fill="black", outline="white")
tahvel.create_oval(375,375,325,325, fill="white", outline="black")

tahvel.create_oval(525,525,575,575, fill="black", outline="white")
tahvel.create_oval(475,475,425,425, fill="white", outline="black")

raam.mainloop()