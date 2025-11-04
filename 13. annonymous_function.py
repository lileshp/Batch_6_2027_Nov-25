#Annonymous function
'''
without name
single line
lambda keyword use to create
    lambda parameters:expression
lambda takes more than 1 argument, but return only
one expression
normal function has return statement but lambda no return statement
'''
#WAF to return square of any given digit
def sq(n):
    return n ** 2

sqr = lambda x:x**2
print(sqr(79))
'''
WAF to return square and addition of given  2 digit
n and m, so square will be n**m and addition: n+m
'''
def sq(n,m):
    s = n ** m
    a = n + m 
    return s, a
print(sq(79,4))
sqr1 = lambda x,y:x**y
print(sqr1(79,4))




