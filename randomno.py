import random
secret = random.randint(1,10)
attempts = 0
print("Hellooo!! I am computer thinking of nmber btw 0 to 10")
while True:
    guess=int(input("Enter your guess: "))
    attempts = attempts+1
    if guess<secret:
        print("Too low!!")
    elif guess>secret:
        print("Too high!!")
    else:
        print("Hurrryyy youu got itt!")
        break

