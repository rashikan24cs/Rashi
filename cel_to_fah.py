def cel_to_fah(c):
     formula = c*9/5+32
     return formula
     
     
c=int(input("Enter celsius: "))
print(cel_to_fah(c))