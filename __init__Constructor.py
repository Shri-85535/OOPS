'''
(*) Normally we use __init__ to initialize variables
(*) __init__ method will be called automatically
(*) self refers to the object
'''
class Computer:
    
    def __init__(self): 
        print("in init") 

    def config(self):
        print("i5", "16gb", "1TB")
        
#For every object the __init__ method will be called automatically
comp1 = Computer() #>>> in init
comp2 = Computer() #>>> in init

