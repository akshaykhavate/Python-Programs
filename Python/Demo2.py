class A:
    a=10
    b=29
    def __init__(self,x,y):
        self.c=x
        self.d=y
    def disp(self):
        print("Hello Akshay")
obj=A(40,20)
obj.a=59
print(A.disp(obj))
print(obj.__dict__)
