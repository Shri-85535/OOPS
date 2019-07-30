'''In an object oriented python program, you can restrict access to methods and variables.
This can prevent the data from being modified by accident and is known as encapsulation.'''

#Example 1 : https://pythonspot.com/encapsulation/

class Car:
    
    def __init__(self):
        self.__updateSoftware()
        
    def drive(self):
        print('Driving!')
        
    def __updateSoftware(self):
        print('Updating Software...')

redcar =  Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object. ***AttributeError: 'Car' object has no attribute '__updateSoftware'***
