'''In an object oriented python program, you can restrict access to methods and variables.
This can prevent the data from being modified by accident and is known as encapsulation.'''

#Example 1.1 : Private Methods (https://pythonspot.com/encapsulation/)

class BikeA:
    
    def __init__(self):
        self.__Accelerate()
        
    def drive(self):
        print('Driving!')
        
    def __Accelerate(self):
        print('Accelerating...')

Bluebike =  BikeA()
Bluebike.drive()
#Bluebike.__Accelerate()  not accesible from object. ***AttributeError: 'BikeA' object has no attribute '__Accelerate'***
'''Encapsulation prevents from accessing accidentally, but not intentionally.
The private attributes and methods are not really hidden, they’re renamed adding _Bike” in the beginning of their name.
The method can actually be called using "Bluebike._Bike__Accelerate()" '''

#Example 1.2 : Private Variables (https://pythonspot.com/encapsulation/)
'''Variables can be private which can be useful on many occasions.
A private variable can only be changed within a class method and not outside of the class.
Objects can hold crucial data for your application and you do not want that data to be changeable from anywhere in the code.
'''
class BikeB():
    
    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 220
        self.__name = "Pulsar"
        
    def drive(self):
        print('Driving...! Maxspeed ' + str(self.__maxspeed))

Redbike = BikeB()
Redbike.drive()
Redbike.__maxspeed = 150 #will not change the variable, beacuse it is private
Redbike.drive()










