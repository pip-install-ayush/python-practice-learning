# Dictonaries 

info = {'name':'ayush', 'age': 19, 'eligible': True }
print(info)
print(info.get('name'))
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The key are {key} , and the values is {info[key]}")

print(info.items())
for key, values in info.items():
    print(f"The corresponding key {key} item is {values}")

ep1 ={112:45, 123:67, 345:56, 654:97}
ep2 ={23:45, 3456:65, 678:76}

ep2.update(ep1)
ep1.clear()
# ep1.pop()
ep1.popitem()
del ep1[112]
print(ep1)

# Exeption handeling 
a = input("Enter the number you want the table :")
print(f"multiplication table of {a} is :")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a*i)} ")
except:
    print("somthing wnt wrong...")


# Squares of numbers

a = int(input("enter the number you want to be squre : "))
squr = a**2
print(f"the square is : {squr} ")


# Even numbers from list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    if(i%2==0):
        print(i)
    

# Length of each word

s= "Python is very easy"
words = s.split()

for word in words:
    print(word, ":", len(word))


# Uppercase strings
a = input("Enter the sentance : ")

print(a.lower())


# Flatten a list of list
lst = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [item for sublist in lst for item in sublist]
print(flat_list)

# Remove vowels from string
string = input("enter the string :")
vowels = "aeiouAEIOU"
result = ""

for ch in string:
    if ch not in vowels:
        result += ch

print(result)

# Filter numbers > 10

numbers = [3, 10, 15, 7, 22, 8]
result = []

for num in numbers:
    if num > 10:
        result.append(num)

print(result)

# frequency count
sentence = "python is easy and python is powerful"
words = sentence.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# character count
string = "python"
char_count = {}

for ch in string:
    char_count[ch] = char_count.get(ch, 0) + 1

print(char_count)

# square dict

n = 5
square_dict = {}

for i in range(1, n+1):
    square_dict[i] = (i*i) 

print(square_dict)

# filter keys with double values
data = {'a': 10, 'b': 15, 'c': 8, 'd': 7}
result = {}

for key,values in data.items():
    if values%2 == 0:
        result[key] = values

print(result)

# key value swap
data = {'a': 1, 'b': 2, 'c': 3}
swapped ={}
for key, values in data.items():
    swapped[values] = key

print(swapped)

# Count vowels

sen = "this is the sentance with vowel"
vowel ="aeiouAEIOU"
count = 0
for ch in sen:
    if ch in vowel:
        count += 1

print(count)

# Map words to length
sentence = "Python is very easy"
words = sentence.split()

word_length = {}
for word in words:
    word_length[word] = len(word)

print(word_length)

# grade system
students = {
    "Rahul": 85,
    "Aman": 72,
    "Neha": 91,
    "Pooja": 38
}

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(name, ":", grade)


