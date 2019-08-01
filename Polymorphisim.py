'''
Sometimes an object comes in many types or forms.
If we have a button, there are many different draw outputs (round button, check button, square button, button with image)
but they do share the same logic: onClick().
We access them using the same method . This idea is called Polymorphism.
******
Polymorphism is based on the greek words POLY (many) and MORPHISM (forms).
We will create a structure that can take or use many forms of objects.
(https://pythonspot.com/polymorphism/comment-page-1/)
'''

#Example 1.1 : 

class Bear(object):
    def sound(self):
        print("Groarrr")
    
class Dog(object):
    def sound(self):
        print("Woof woof!")
    
    def makeSound(animalType):
        animalType.sound()
    

bearObj = Bear()
dogObj = Dog()
    
makeSound(bearObj)
makeSound(dogObj)
