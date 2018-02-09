class A:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def swp(self):
        self.a,self.b=self.b,self.a
    @classmethod
    def swap(cls):
        cls.a,cls.b=cls.b,cls.a
obj=A(70,80)
print("Before Change")
print(obj.a,obj.b)
print(A.a,A.b)
print("After changing wrt obj")
obj.swp()
print(obj.a,obj.b)
print(A.a,A.b)
print("After changing wrt cls")
A.swap()
print(obj.a,obj.b)
print(A.a,A.b)
print("After changing wrt cls in method")
obj.swap()
print(obj.a,obj.b)
print(A.a,A.b)
