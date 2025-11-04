import attempt_quiz
logged_user = ''
logged = False

def register():
    pass
def login():
    pass
def show_profile():
    pass
def update_profile():
    pass
def logout():
    pass
def close():
    print("Thanks for visiting our site")
    exit()

def main():
    print(" #*# " *10)
    print("Welcome in LNCT")
    print(" #*# " *10)
    response = input("""
    Choose option to perform operation:
        1. Registration
        2. Login
        3. Show Profile
        4. Update Profile
        8. attempt quiz
        5. Logout
        6. Main Menu
        7. Exit
            Select your option 1/2/3/4/5/6/7:     """)
    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        main()
    elif response == '7':
        close()
    elif response == '8':
        attempt_quiz()
    else:
        print("Invalid Choice, please choose correct option")
        main()

main()

'''
    1. attempt quiz
        a. Python
            
        b. DSA
        c. DBMS
    2. Show result
        username    quiz_topic    Marks/outof     datetime
    


'''









