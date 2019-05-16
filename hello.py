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

# checkBirthYear()

def stringManipulation():
    longstring = ''' 
    this
    is 
    to
    print
    on
    multiple
lines'''
    print (longstring)
    print (longstring[-10:-5])
    # this will print it exactly how it is in file ie with spacing included.
# stringManipulation()

def formatedString():
    first = 'david'
    last = 'friday'
    msg = f'{first} [{last}] can add text'
    print(msg)
    print(first.find('d'))
formatedString()

