#function 

def Gmean(a,b):
    mean = (a*b)/(a+b)
    print("Gmean is :", mean)


def isGreater(a,b):
    if(a>b):
        print(f"{a} is Greater than {b}")
    elif(b>a):
        print(f"{b} is Greater than {a}")
    elif(a == b):
        print(f"Both {a} and {b} are equal ")
    else:
        print("numbers are invalid")


#arguments in functions

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

average(2,3,4,5,6,8)

