import random
a= int(random.randint(1,100))
y = 0
def game():
    x = 1
    while x < 7:
                    userguess = int(input("Guess a number between 1 and 100"))
                    if userguess < a:
                                    print("Too Low")
                                    x = x+1
                    if userguess > a:
                                    print("Too High")
                                    x = x + 1
                    if userguess == a:
                                    print("You won in ",x," goes")
                                    print("Go again , you've won")
                                    y = 1
                    elif x == 6:
                                    quit()
game()
if y == 1:
    game()
