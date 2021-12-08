from easygui import *


number = integerbox("Sisestage esimest numbrit! \n     Number peab olla 1-10", lowerbound = 1, upperbound = 10)
number_1 = integerbox("Sisestage teist numbrit! \n     Number peab olla 1-10", lowerbound = 1, upperbound = 10)

nupud = ["Liitma", "Lahutada", "Korrutada", "Jagama"]
vajutati = buttonbox("Mida te tahate teha nende numbritega?", choices = nupud)
if vajutati == "Liitma":
    vastus = number + number_1
elif vajutati == "Jagama":
    vastus = number / number_1
elif vajutati == "Korrutada":
    vastus = number * number_1
elif vajutati == "Lahutamine":
    vastus = number - number_1
else:
    print("Kuidas sa seda tegid?")
    exit()
msgbox("Vastus on " + str(vastus) + "!")