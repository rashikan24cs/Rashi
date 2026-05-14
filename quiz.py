print("Welcome to the world of Quiz")
score=0
Answer1=input("What is the capital of India: ")
if Answer1.lower()=="delhi":
    print("yahh!! you'r right")
    score=score+1
else:
    print("Sorry, it's delhi")
Answer2=input("What is 2*2: ")
if Answer2=="4":
    print("yahh!! you'r right")
    score=score+1
else:
     print("Sorry, it's 4")
Answer3=input("Which language are you using now: ")
if Answer3.lower()=="python":
    print("yahh!! you'r right")
    score=score+1
else:
     print("Sorry, it's python")
 
print("your score is -"+str(score)+ "out of 3")