#Loop
'''
    Repetition

    for: known number of iteration
        for variable in sequence:
            execution
    while: iteration depends on condition
        while (condition):
            execution
            incre/decre

range(): is used to return an iterable object with
sequence from the given integer intervals
    range(start, end, steps)
    start: default 0
    end: required
    steps: default 1, difference between each adjacent sequence



'''
# print numbers from 1 to 10
a  = range(100,2,2)
print(type(a))
print(type(iter(a)))
for num in range(1,11,1):
    print(num, end=" ")

# WAP to print numbers which are divisible by 5 and
#multiple of 7 b/w 5874 - 9851 (both included)
st = 5874
en = 9851
ls = []
for num in range(st, en+1):
    if num % 5 == 0 and num% 7 == 0:
        ls.append(num)

print(len(ls))

el = []
# wap to print all even numbers b/w 7854 - 9863
for num in range(7854,9864):
    if num % 2 == 0:
        el.append(num)

# iter(), next()
# iterate all elements of the list without using loop and
# indexing: ls = [10,20,30,40,50]

ls = [10,20,30,40,50] #iterable
lsi = iter(ls) 
print(lsi)
print(next(lsi)) #10


print("Hello")
print("bye")
for i in range(5):
    print("PYTHON")

print(next(lsi)) #
print(next(lsi))
print(next(lsi))
#print(next(lsi))
#print(next(lsi))
#print(next(lsi))

print("LNCT")

#control statements
'''
    break: terminate an iteration on specific condition
    continue: skip/jump iteration process on specific condition
    pass: Do nothing, None

'''
ls = ['bpl', 'sehore', 'pappu','astha', 'dewas','Indore']
for points in ls:
    if points == 'pappu':
        pass
    print(points)
else:
    print("REACHED")

#registeration, login

def reg():
    pass

def admin_reg():
    pass
for i in range(20):
    pass
ls = ['0103CS231212','0176CS231212','0157CS231212','0131CS231212']
inte = []

for std in ls:
    if std.startswith('0157') or std.startswith('0131'):
        continue
    inte.append(std)
print(inte)

print("##" * 10)

std = {'name':'john','college':'LNCT','branch':'CSE','city':'bhopal'}

for key,val in std.items():
    print(f"{key} = {val}")

#WAP to remove duplicates from the given array
ar = [10, 20, 30, 20,43,10,43,56]
new_ar = []
for i in ar: # ---> n
    if i not in new_ar: # ----> 1
        new_ar.append(i) #---> 1



# WAP to return original array
encoded = [8,5,6,11,9]
'''
    ar[i] = or_ar[i] + or_ar[i+1]
    last element remain same in both array
'''
original_array = [] #?

ls = [10,20,10,40,10,60]
for ind,val in enumerate(ls):
    print(f"{ind} = {val}")
    if val == 10:
        ls[ind] = 'John'
print(ls)

# While
i = 1
while i <=10:
    i += 1
    print(i)
else:
    pass

# comprehension, function
    
        





