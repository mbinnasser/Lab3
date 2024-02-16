emp = {} #0
def saveNames():
    name = input("please enter your name:")
    salary = input("please enter your salary:")
    if name == "no" or salary == "no":
        return False
    else:
        emp[name]=salary
        return True
while saveNames()!= False :
    print(emp)