'''
"Class" is a design for an object. Without design we cannot create anything.
A class is a collection of Objects

The Object is an entity that has a state and behavior associated with it. More specifically, any single integer or any single string is an object
'''

class Computer:
    #1 Attributes(Variables)
    #2 Behaviours(methods)
    def config(self):
        print("i5", "16gb", "1TB")

a = 'Shri'
x = 9
comp1 = Computer()  #comp1 is an object
comp2 = Computer()  #comp2 is an object

print(type(a)) #>>> <class 'str'>
print(type(x)) #>>> <class 'int'>
print(type(comp1)) #>>> <class '__main__.Computer'>

Computer.config(comp1) 
Computer.config(comp2)

comp1.config()
comp2.config()
