'''
Polymorphism
    poly: many
    morph: forms

    types:
        method overloading -> compile time
        method overriding -> run time polymorphism
        


'''
class A:
    city = "Bhopal"

    def show(self,a,b):
        c = a + b
obj = A()
#obj.show()


class B(A):
    city = "Indore"
    def show(self):
        pass
print(B.mro())
#obj = B()
#print(obj.city)
#obj.show()
#print(B.mro())
#print(A.__mro__)
#obj.con = 987645321
#print(obj.con)
#a = A()
#a.show(100)
#a.show(100,200)


from abc import ABC, abstractmethod

class A(ABC):
    def show(self):
        pass

    @abstractmethod
    def fees(self):
        pass

class B(A):
    def fees(self):
        pass

o = B()



