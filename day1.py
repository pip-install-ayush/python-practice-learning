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

# loops [for loop]

name ="Ayush Mishra"
for i in name:
    print(i)

colors =["red", "Brown", "yellow", "green"]
for colour in colors:
    print(colour)
    for i in colour:
        print(i)

for i in range(1,5):
    print(i)

# odd no 
print("odd no :")
for i in range(1,20,2):
    print(i)

#even no 
print("even no:")
for i in range(0,20,2):
    print(i)

# while loop
n = 5
while(n>0):
    print(n)
    n = n - 1
else:
    print("I am inside else")



# sum of the list 
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter number: ")))

print("Sum of list =", sum(lst))



# frequency of the element
lst = [1, 2, 2, 3, 1, 4, 2]
freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

# reverse of string
str = "ayush"

rev = str[::-1]
print(rev)

# maximum and minimum
lst = [1,2,4,5,7,3,8,4]
 
maximum =  minimum = lst[0]

for i in lst:
    if (i>maximum):
        maximum = i

    if(i<minimum):
        minimum = i
       
print("maximum:", maximum)
print("minimum:", minimum)

# palindrom
p ="madam"

if p == p[::-1]:
    print("palindrom")
else:
    print("not palindrom")

lst = [1, 2, 2, 3, 1, 4, 2]
unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)



# menu program calculation
while True:
    print("\nMENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting program...")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result =", a + b)

    elif choice == 2:
        print("Result =", a - b)

    elif choice == 3:
        print("Result =", a * b)

    elif choice == 4:
        if b != 0:
            print("Result =", a / b)
        else:
            print("Division by zero not allowed")

    else:
        print("Invalid choice")



# fibonacci program 
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

# prime numbers 
n = int(input("Enter a number: "))
flag = 1

if n <= 1:
    flag = 0
else:
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break

if flag == 1:
    print("Prime number")
else:
    print("Not a prime number")


# word count in sentence
sentence = "Python is very easy to learn"

words = sentence.split()
count = len(words)

print("Word count =", count)


