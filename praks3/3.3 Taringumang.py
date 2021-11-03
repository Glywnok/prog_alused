from random import randint

times = int(input("Täringute arv: "))
i = 1
while i <= times:
    number = randint(1,6)
    print(number)
    i = i + 1
    