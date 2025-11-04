# Conditional statement
'''
    if
    else
    elif

    if - simple if
    if else
    if elif... else (Ladder if)
    if if ... else else (Nested if)

execution: appear in exam
cond1 : fees
    cond2: attendance
        cond3: registration
            appear in exam

if cond1 and cond2 and cond3:
    appear in exam

'''
# Scene 1
'''
uname = input("Enter username : ").strip().lower()
pwd = input("Enter password :")

user = "john"
pw = "j123"

if uname == user and pwd == pw:
    print(f"Welcome {uname}")
else:
    print("Wrong credentials")

'''

#scene 2
'''
uname = input("Enter username : ").strip().lower()

user = "john"
pw = "j123"

if uname == user:
    pwd = input("Enter password :")
    if pw == pwd:
        print(f"Welcome {uname}")
    else:
        print("Wrong password")
else:
    print("Wrong username")
'''

#scene 3
'''
uname = input("Enter username : ").strip().lower() #john

users = ["john",'mac','sam','peter','johny']
pws = {'john':"j123",'sam':'s123','mac':'m123','peter':'p123','johny':'jo123'}

if uname in users:
    pw = input("Enter password : ")
    if pw == pws[uname]:
        print(f"Welcome {uname} in Bhopal")
    else:
        pass
else:
    pass
'''

#scene 4
'''
uname = input("Enter username : ").strip().lower() #john

users = ["john",'mac','sam','peter','johny']
pws = {'john':"j123",'sam':'s123','mac':'m123','peter':'p123','johny':'jo123'}
branch = {"EC":['john','mac'],"CS":['sam','peter'],"AIML":['johny']}
if uname in users:
    pw = input("Enter password : ")
    if pw == pws[uname]:
        print(f"Welcome {uname} in Bhopal")
        br = input("Enter branch CS/EC/AIML : ").upper().strip()
        if uname in branch[br]:
            print(f"welcome {uname} in {br} branch")
        else:
            print("Select proper branch")
    else:
        pass
else:
    pass
'''

#Scene 5
uname = input("Enter username : ").strip().lower() #john
users = ["john",'mac','sam','peter','johny']
pws = {'john':"j123",'sam':'s123','mac':'m123','peter':'p123','johny':'jo123'}
#branch = {"EC":['john','mac'],"CS":['sam','peter'],"AIML":['johny']}
if uname in users:
    pw = input("Enter password : ")
    if pw == pws[uname]:
        print(f"Welcome {uname} in Bhopal")
        choice = input("Enter your choice A/I/: ").upper().strip()
        if choice == 'A':
            print("Today is practical")
        elif choice == "I":
            print("Today is holiday")
        else:
            print("Wrong choice")
    else:
        pass
else:
    pass









