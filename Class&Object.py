'''
"Class" is a design for an object.
without design we cannot create anything.
'''

class Computer:
    #1 Attributes(Variables)
    #2 Behaviours(methods)
    def config(self):
        print("i5", "16gb", "1TB")

a = 'Shri'
x = 9
comp1 = Computer()
comp2 = Computer()

print(type(a)) #>>> <class 'str'>
print(type(x)) #>>> <class 'int'>
print(type(comp1)) #>>> <class '__main__.Computer'>

Computer.config(comp1) 
Computer.config(comp2)

comp1.config()
comp2.config()