class A:
    a=10
    def __init__(self,b=None,c=None):
        self.b=b
        self.c=c
obj1=A(10)
obj2=A(20,30)
print(obj1.__dict__)
print(obj2.__dict__)
