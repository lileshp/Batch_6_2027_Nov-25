'''
    Encapsulation:
        data binding in a single unit.
        data:
            attributes : public,private,protected
            methods: public,private,protected

    ACCESS MODIFIERS:
        Public: accessible within class, subclass, outside class
        Private: accessible only within class
        Protected: accessible within class and their childclass

        Public:
            a = 100
            def show(self):
                pass

        Priate:
            __a = 500
            def __result(self):
                pass
                
        Protected (convention):
            _a = 200
            def _exam(self):
                pass
'''
class EC:
    _college = "LNCT" #protected
    __fee = 123456 #private
    def _reg(self):
        print(f"Your Fee is: {EC.__fee}")
class ECA(EC):
    pass

obj = ECA()
obj._reg()
print(obj._college)
print(obj._EC__fee) #Name mangling

#ways to call private data members
# 1. Name mangling: _ClassName__DataMembers
# 2. via public/protected methods

'''
decorator
generator
destructor

'''






