'''
Function:
    built-in
    user-defined

    basis on arguments function has these types:
        1. required/positional argument
        2. keyword argument
        3. default argument
        4. variable length argument.
        
    

'''

'''
Registration
'''
'''
us = []
for i in range(5):
    fn = input()
    ln = input()
    con = input()
    mail = input()

    r = (fn, ln, con, mail)
    us.append(r)
'''

'''
LOGIN
'''
'''
uname = "John"
pwd = "12f"

if uname == "john" and pwd == '12f':
    print("Hello {uname}")
else:
    print("Invalid Credentials")

def show():
    show()

print(input("HB"))

st = 'abc'
st.upper()
'''
'''
print("HO","\t","\\n",end="\t")
print("ABC")

range(5)
range(5,50)
range(5,50,2)
'''
'''create a function to reverse a list'''
def one():
    print("ABC")

one()


def two():
    print("ABC")

print(two())

def three():
    return "ABC"
    print("XYZ")
print(three())

def four():
    return
print(four())

def five():
    return None
print(five())

def six():
    return "H"

out = six()
print(out)

def seven():
    return "H","I",456, [5,6,8],{'a':5,'b':9}

out = seven()
print(out)

''' enumerate()'''
ls = [1,2,4,5]
for i in enumerate(ls):
    print(i)



one()

'''arguments:
    1.positional
'''

def si(a,b,c):
    
    return (a * b * c)/100

pri = float(input())
rat = float(input())
ti = int(input())
out1 = si(pri,rat,ti)
print(out1)


print(range())









