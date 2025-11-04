def decor(func):
    def inner():
        x = func() #BHOPAL
        return len(x)
    return inner

@decor 
def f():
    u = 'bhopal'.upper()
    return u

print(f())


#generator

li = [2,3,4,5,1,6,7,8]
def cal():
    lis = []
    for i in li:
        lis.append(i**2)
    return lis
x = cal()
print(x)
