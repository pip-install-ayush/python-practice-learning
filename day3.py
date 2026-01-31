class person():
    name = "Ayush Mishra"
    occupation = "ai engineer"
    sallary = 400

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
# a.name = "Harsh Mishra"
a.occupation = "AI Engineer"


c = person()
c.name = "Vaibhav"
c.occupation = "Game Developer"
b = person()
b.name = "Shubhm"
b.occupation = "Tax Collector"


a.info()
c.info()
b.info()


class person():

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is an {self.occupation} in this firm")

a = person("Ayush Mishra", "AI Engineer")
a.info()        

# Decorator 

def greet(fx):
    def mfx(*args, **kwargs):
        print("Jai Hind")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def add(a,b):
    sum = a+b
    print("The addition of two number is :", sum )
add(6, 7)


# ---------random function---------- #
@greet
def hello():
    print("hello someone born with glorious perpose")
hello()






