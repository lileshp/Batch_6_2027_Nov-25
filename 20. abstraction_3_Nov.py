'''
Abstraction (hiding details):
         1. python uses abc module to implement abstraction
            from abc import ABC, abstractmethod
        2. any class which is having 1 or more than 1 abstract method
            treated as abstract class
        3. @abstractmethod decorator is use to create abstract
            method
        4. abstract methods only declared in abstract class without
            implementation
        5. all abstract methods should be redeclared in child class
        6. we cannot create an object of abstract class.
'''
#decorator
def length(func):
    def inner():
        x = func()
        return len(x)
    return inner

def repeat(fun):
    def inner():
        x = fun()
        ls = []
        for i in range(x):
            ls.append("WoW")
        return ls
    return inner

@repeat
@length
def up():
    st = input("Enter a string: ")
    return st.upper()

#print(up())

#Abstraction
from abc import ABC, abstractmethod

class Account(ABC):
    def show(self):
        print("Show method of abstract class")

    @abstractmethod
    def fee_collection(self):
        pass

    @abstractmethod
    def rewards(self):
        pass

    @abstractmethod
    def salary(self):
        pass

class LNCT_std(Account):
    def fee_collection(self):
        pass

    def salary(self):
        pass

class LNCTE_std(Account):
    def fee_collection(self):
        pass
obj = LNCT_std()















