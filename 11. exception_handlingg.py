# exception handling:
'''
try: (Required block)
    write program/code which you want to execute
    and there could an exception
    pass
except: (required)
    handle any type of exception.
    we can write except for each exception
    an empty except block can handle any type of exception
    pass
else: (optional)
    with no exception
    means, when a try block will execute successfully
    then else block will be execute
    pass
finally: (optional)
    will be execute always
    with and without exception
    pass
'''
print("$"*20)

try:
    #file
    #DB
    a = 10
    b = int('5')
    c = a/b
    print(c)
except ZeroDivisionError as msg:
    print(msg)
except TypeError as e:
    print(e)
except ValueError as msg:
    print(msg)
except:
    print("ANY TYpe of errro")
else:
    print("WITHOUT ERROR")
finally:
    print("ALWAYS")

print("WoW")










