'''
map, filter


Write a function to indicate/mark values which is
less than 40 in given list/array

ls = [23,43,54,65,78,45,23,12,74,53,2]
out = [True, False, False, False, False, False,
True, True, False, False, True]
'''
ls = [23,43,54,65,78,45,23,12,74,53,2]
def is_greater(ls):
    out = [False] * len(ls)
    for key,val in enumerate(ls):
        if val <= 40:
            out[key] = True
    return out

print(is_greater(ls))

#map(function,list)
#res1 = list(map(is_greater,ls))
res = list(map(lambda n:n<=40,ls))
print(res)

'''
map, filter


Write a function to separate values which is
less than 40 in given list/array

ls = [23,43,54,65,78,45,23,12,74,53,2]
out = [23,23,12,2]
'''

ls = [23,43,54,65,78,45,23,12,74,53,2]
def is_greater_filter(ls):
    out = []
    for i in ls:
        if i <= 40:
            out.append(i)
    return out

#print(is_greater_filter(ls))
#filter(function,list)
res2 = list(filter(lambda x:x<=40,ls))
#print(res2)



#return and yield

ls = [23,43,54,65,78,45,23,12,74,53,2]
def is_greater_filter(ls):
    out = []
    for i in ls:
        if i <= 40:
            out.append(i)
    yield out
    
res = is_greater_filter(ls)
print(res)

#nested function: nonlocal










