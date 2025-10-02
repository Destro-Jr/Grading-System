# print("Good morning")

name = input("Type in your name: ")
score = int(input("Type in your score: "))

if score >= 80 and score <= 100:
    print(name+" You got an A")
elif score>= 70 and score <= 79:
    print(name+" You got a B")
elif score >= 60 and score <= 69:
    print(name + "You got a C")
elif score >= 45 and score <= 59:
    print(name + " You got a D")
elif score >= 35 and score <= 44:
    print(name + " You got an E")
elif score >=0 and score <= 34:
    print (name + " You got a F")
else:
    print("oga u did not write this exam")