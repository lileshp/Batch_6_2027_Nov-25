#import random
class Instagram:
    city = "bhopal" #class variable
    branch_code = "LN20100"

    #constructor
    '''
        is type of MEthod
        automatically call/invoke
        use: initialize class member variables

        python has __init__ which behave like constructor
    '''

    
    def account(self,a, b, amount = 0):
        self.name = a
        self.contact = b
        self.amount = amount
        ra1 = random.randint(1111,9999)
        ra2 = random.randint(2456,9658)
        ra3 = random.randint(9659,12530)

        acc = str(ra1) + str(ra2) + str(ra3)
        self.account_number = acc
        
        print(f"Hello {self.name} \nAccount Opened Successfuly, \naccount no. {acc}")
    def credit(self, amount):
        self.amount += amount #john.credit(5000)
        print(f"Current Balance: {self.amount}")
    def debit(self,amount):
        self.amount -= amount
        print(f"Current Balance: {self.amount}")
#john = Bank()
#john.account('john','9874563210')
#john.credit(5000)

class TnP:
    
    def __init__(self, na, en, branch, year):
        self.name = na
        self.enr = en
        self.branch = branch
        self.year = year

    def training(self, stream = "ap"):
        self.stream = stream
        print(f"Hello {self.name} you opt for {self.stream} training")
john = TnP("john","0103EC231524","EC","2027")
john.training("Python")


def areaR(l: int[],b: int) -> int[]:
    #Write your code here
    pass







