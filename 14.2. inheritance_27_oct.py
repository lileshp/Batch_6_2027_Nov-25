'''
feature/pillar of oops
Inheritance:
    types:
        single
        multiple
        multilevel
        hybrid
        hierarichal
    


'''
li = [1,2,3,4]
for i in range(len(li)):
    pass

class GM:
    pass
class GF:
    pass
class F(GF,GM): #single/multiple
    pass
class C1(F):
    pass
class C2(C1): #multilevel/hybrid
    pass
class C3(F):
    pass

class LNCT:
    group = "LNCT" #class/static variable
    def __init__(self,x,y):
        print("Another constructor of LNCT")
    def __init__(self,a,b):
        self.name = a
        self.branch = b
        print("LNCT Constructor")
    #Constructor overloading: polymorphism (Compile time)
class LNCTE(LNCT):
    groups = "LNCT Group"
    def __init__(self,n1,n2):
        print("LNCTE Constructor")
    def exam(self,a):
        stream = "summer" #local
        self.sub = a #instance variable
        print(f"EXAM: Hello {self.name}")
#john = LNCTE("John","CSE") #john.name = "john", john.branch = "CSE",LNCT Constructor
#print(john.group)
#john.exam('M1')
#How to call parent class constructor in child class
#constructor:
        # 1. via class name: ClassName.__init__(self)
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x, b.y)
main()


# 1. via super(): super().__init__()
# super() invoke first inherited parent class constructor
class Test:
    def __init__(self):
        self.x = 0
class Test1:
    def __init__(self):
        self.z = 2
class Derived_Test(Test1,Test):
    def __init__(self):
        super().__init__()
        Test.__init__(self)
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x, b.y)
main()


class login:
    pass

class message(login):
    pass







