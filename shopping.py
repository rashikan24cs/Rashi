print("Welcome to the world of shopping")
shopping=[]
while True:
    print("\n1.Add item")
    print("\n2.View")
    print("\n3.Quit")
    choice=(input("Enter yur choice"))
    if choice=="1":
        item=input("Enter the item")
        shopping.append(item)
        print(item+ "added!")
    elif choice=="2":
        if len(shopping)==0:
            print("List is empty")
        else:
            print("your list:")
            for item in shopping:
                print("-"+item)
    elif choice=="3":
        print("See you next tym!!")
        break
