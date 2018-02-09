class A:
    a=10
    def __init__(self,b):
        self.b=b

class B(A):
    c=19
    def __init__(self,b,d):
        self.d=d
        #super().__init__(b)
        A.__init__(self,b)

obj=B(30,40)
print(obj.a,obj.b,obj.c,obj.d)
