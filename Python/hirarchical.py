class A():
    a=10
    def __init__(self,b):
        self.b=b

class B(A):
    d=20
    def __init__(self,b,e):
        self.e=e
        super().__init__(b)
        #A.__init__(self,b)

obj1=B(100,200)
print(obj1.b,obj1.e)

class C(A):
    f=30
    def __init__(self,b,g):
        self.g=g
        super().__init__(b)
        #A.__init__(self,b)
obj2=C(99,98)
print(obj2.b,obj2.g)
