def puzzle(s):
    return {ch: s.count(ch) for ch in set(s)}
#print(puzzle("banana")) #{'b':1,'a':3, 'n':2}

def mystery(x, y):
    return [x**i for i in range(1, y)]
#print(mystery(2, 5)) #[2,4,8,16]

def func(a, b=None):
    if b == None:
        b = []
    b.append(a)
    return b
#print(func(1)) #[1]
#print(func(2)) #[1,2]
#print(func(3)) #[1,2,3]

# kywor argumnts

def two(a,b,c):
    s = a + b + c
    print(s)
# two(a=1,2,3) # no
x = 50
y = 100
z = 20
two(z,x,y)
two(b=x,c=y,a=z) # ys
# two(a=1,b=2,3) # no
two(1,2,c=3) # ys
two(1,b=2,c=3) # ys
two(1,2,3) # ys

# function(rquir/positional, kywor, *args, **kwargs)

def func(s1, s2,*,pra=10):
    marks = s1 + s2 + pra
    print(marks)
#func(20,10,,50)

def two(a,b,c):
    a = 1
    b = 2
    c = 3
    s = a + b + c
    print(s)

two(10,20,30)


# variabl scop: global, local
a = 100
b = 200
c = 300
def th(a):
    global b
    b1 = 2
    c1 = 3
    s = a + b1 + c1 + b
    print(s)
    b = 745
th(50)
print(b)

marks = 0
def xm1():
    global marks

def xm2():
    global marks

'''
variabl lngth argumnts
*args: comma, list, tuple -> tuple
**kwargs: key = value -> dictionary
'''
def xm2(a,b,c=20):
    rs = a + b+ c
xm2(5,6)
xm2(b=10,c=10,a=20)


def xm4(z,*ar,**kwargs):
    sum = z
    if len(ar) > 1:
        for i in ar:
            sum += i
    else:
        for i in ar:
            for j in i:
                sum += j
    print(sum,kwargs)
xm4(5,1,4,na = "john",rs = 500)
xm4(5)
xm4(5,[2,8])
    













