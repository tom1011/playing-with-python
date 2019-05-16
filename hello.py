def checkName(name):
    checkName = input("is your name " + name + "? ")
    if checkName.lower() == "yes":
        print('Hello ' , name)
    else:
        name = input("We're sorry about that. What is your name agian?")
        print("Welcome, " + name)
# checkName("David")

def checkBirthYear():
    checkYear = input('what year are you born?')
    print(type(checkYear))
    print ( 2019 - int(checkYear))

checkBirthYear()