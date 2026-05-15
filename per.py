def find_percentage(marks,total):
    formula=(marks/total)*100
    return formula
marks=float(input("Enter a no: "))
total=float(input("Enter a no: "))
print(find_percentage(marks,total))