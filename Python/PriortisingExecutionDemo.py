def hello():
    print("Hi Akshay")
    a()

def a():
    print("Hi Salman")
    b()

def b():
    print("Hi Sharukh")
print("First Priority")
if __name__=="__main__":
    hello()
    print("Second Priority")
