#Electricity bill calculation
'''
    First 100 units ₹5 per unit
    Next 100 units  ₹8 per unit
    Above 200 units ₹10 per unit
'''
'''
unit = int(input("enter units: "))
if unit <= 100:
    bill = unit *5
elif unit > 100 and unit <= 200:
    n_u = unit - 100
    bill = n_u * 8
    bill = bill + (100 * 5)
else:
    n_u = unit - 200
    bill = n_u * 10
    s_u = (100 *5) + (100*8)
    bill = unit * 10
    bill = bill + s_u
'''  
# Simple calculator (two numbers and an operator)
nu1 = 25
nu2 = 4
op = '+' # + - * /

if op == '+':
    res = nu1 + nu2
elif op == '-':
    res = nu1 - nu2
elif op == '*':
    res = nu1 * nu2
elif op == '/':
    if nu2 == 0:
        print("ZeroDivisionError")
    else:
        res = nu1/nu2
else:
    print("Invalid Operator")

#Check eligibility to vote
age = 40
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible")

#Find the greatest of three numbers
nu1 = 45
nu2 = 98
nu3 = 54

if nu1 > nu2 and nu1 > nu3:
    print(f"Bigger number is {nu1}")
elif nu2 > nu1 and nu2 >nu3:
    print(f"Bigger number is {nu2}")
else:
    print(f"Bigger number is {nu3}")








