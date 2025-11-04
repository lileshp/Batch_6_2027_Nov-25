'''
Datatype:
    to choose operation
    to store in memory

    Number
        any input containing (0-9) digits, without quotes
        int()
        float()
        immutable object
        not iterable
        not subscriptable
        not indexable


      
    String
        sequence of characters (alphabets, digits, symbols)
        enclosed in ' ', " ", """ """, ''' '''

        str()
        immutable object
        iterable
        subscriptable
        indexable

        slicing operator [:]
        'a' + 'b' => "ab" -> concatenation
        'a'*3 => 'aaa' -> repetition

        
    List (Dynamic array)
        is a collection of ordered elements, elements
        could be different type, separated by comma,
        enclosed in [].
        Dynamic size
        list()
        []
        mutable object
        iterable
        suscriptable
        indexable
        slicing operator
        + -> add two list
        * -> repetition of elements
        
        
    Tuple
        immutable object
        tuple()
        ()

        iterable
        indexable
        
    Dictionary
        is a unordered collection of multiple elements
        in key:value pair.
        Key: unique, only immutable datatype
        Value: any data

        mutable object
        iterable
        not indexable
    Set
       collection unordered unique elements
       set()
       {}
       mutable
       iterable
       not indexable
    frozenset
        immutable object
    boolean
'''
'''
    program memory -> int 4 byte, string -> 8 byte
    files (Local storage) ->system user
    Cloud/Server -> every can access

OOPs:
    Class
    Object
    Attributes -> characterstics
    Methods -> behavior (exam, practical, midsem, result)
    Features:
        inheritance
        polymorphism
        encapsulation
        abstraction
'''
#a = int(input("Enter first number: ")) #5
#b = int(input("Enter second number: ")) #9
#c  = a + b #14

# WAP to count digits in given number
# e.g. 123456 -> output -> 6

'''
h = R"Hello\nWorld"
print(h)

inp1 = "abcdefgh" #8//2 = 4
inp2 = "stuvwxyz"
output = "abvwcxdeyz"

m1 = len(inp1)//2 # 5//2 = 2
m2 = len(inp2)//2 # 5//2 = 2
o1 = inp1[0:m1] #ab
o2 = inp2[0:m2] #vw
o3 = inp1[m1]
o4 = inp2[m2]
o5 = inp1[m1+1:]
o6 = inp2[m2+1:]

out = o1 + o2+o3+o4+o5+o6
print(out)
#slicing: [start:end:steps] [0:len(obj):1]

code = "1234-567-0002-abc-ZRH"
print(code.lower())

c1,c2,c3,c4,c5 = code.split("-") #unpacking
print(c1,c2,c3,c4,c5)

dob = "12-12-2000"
d,m,y = dob.split('-')

str1 = "Hello I am learning python"
print(str1.split('a'))

pwd = "123456"
enroll = "0157CS231224"
print(enroll.isalnum())

contact = "7896543216"
print(contact.isdigit())

name = "JOHN"
print(name.isalpha())


name = input("Enter your name: ")
name = name.strip()
print(len(name))

#leading and trailing spaces

str2 = "I am learning Python"
str3 = str2.split()
print(str3)
print(''.join(str3))
print(code)
nc = code.replace('-','/')
print(nc.replace('4/56','cvc'))

code = "1234-567-0002-abc-ZRH"
print(code.count('0'))
'''
#LIST
l1 = [1,2,3,4,5,6,7,8,9]
l2 = []
l3 = list()
l4 = ['a']*len(l1)

print(l1[0:8:3])
print(id(l1))
l1[0] = 100
print(l1)
print(id(l1))

std = ['john','cse','LNCT',[50,20,36,25,[78,98]]]
print(std[-1][4][0])

li = [10,35,90,50,40,20]
out = [10,35,90,50,110,20]
d = 40
ind = li.index(d)
res = li[ind] + li[ind-1] + li[ind+1]
li[ind] = res
print(li)


l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
l1.append(l2) #object
print(l1)
l2.extend(l3) #elements
print(l2)

st = [10,20,30]
st.append("John")
print(st)
st.extend("Bhopal")
print(st)

print(st.pop(2))
print(st.remove(20))

li = ['a','b','c']
li.append(li.append(li.remove('b'))) #['a','c',None,None]
print(li) #['a','c'], 

li.count('a')

ids = (123,456,876,346,236)
n_i = 200
li = list(ids)
li.append(n_i)
new_ids = tuple(li)
print(new_ids)

#LIST vs Tuple
import sys
lis = []
for i in range(1,1000000):
    lis.append(i)
tu = tuple(lis)
print(len(lis))
print(len(tu))
print(sys.getsizeof(lis))
print(sys.getsizeof(tu))

std = ['john','cse','LNCT',50, 26]

di = {0:1002,'name':'john', 'college':'LNCT'}
print(di.get(10,"Given Record is not found"))

di['city'] = "bhopal"
print(di)
print(di.popitem())
print(di.pop('name'))
print(di.keys())
print(di.values())
print(di.items())

li = [[568,'John',56],[120,'SAM',78],[52,'Peter',45],[10,'Zack',89]]
li1 = [23,43,12,54,3]
li1.sort(reverse=True)
#li1.reverse()
print(li1)

li.sort()
print(li)

#set

s1 = {1,2,3,2,1,3,4}
s2 = {4,3,6,1,6,7,8,9,1}
print(s1.union(s2))
print(s1)

print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)

print("Hello",end =" ",sep="")
print("World")
print("123")






