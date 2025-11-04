#WAP to fetch all odd numbers from the list
ls = [32,43,65,60,98,101,32,37]
for i in ls:
    if i % 2 == 0:
        continue
    else:
        print(i)

# sequence -> process -> new sequence
#WAP to swap key and value in a new dictionary
di = {'one':1,'two':2,'three':3,'four':4}
sw = {}
for key,val in di.items():
    sw[val] = key


#comprehension
#type: list, set, dictionary, generator
#fetch all odd numbers
ls = [32,43,65,60,98,101,32,37]
od = [i for i in ls if i %2 != 1]
print(od)

#dictionary comprehension
di1 = {val:key for key,val in di.items()}
print(di1)

#Set
std = ['0103CS','0103EC','0157CS','0103EC','0157EC']
clg = []
for i in std:
    if i[:4] not in clg:
        clg.append(i[:4])
print(clg)

college = {i[:4] for i in std}
print(college)

ls = [32,43,65,60,98,101,32,37]
# all even numbers
even = (i for i in ls if i %2 == 0)
print(next(even))
print(next(even))

#function -> return yield







