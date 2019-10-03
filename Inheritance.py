'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
(https://www.w3schools.com/python/python_inheritance.asp)
'''

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(self.fname, self.lname)

p1 = Person('Akash', 'Kumar')
p1.printname()


class Student(Person):
    def __init__(self, fname, lname, year): #Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#        Person.__init__(self, fname, lname) # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        super().__init__(fname, lname) # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
        self.graduationyear = year
    
    def welcome(self):
        print(f" Welcome{self.fname} {self.lname} to the class of {self.graduationyear}")
        

s1 = Student('Shri', 'Ram', 2019)
s1.welcome()





'''Single Level Inheritence'''
class A:
    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")
        
class B(A): #B is a child/sub class of A
    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")

#a1 = A()
#b1 = B()
#b1.feature1() #class B inherits the features of class A


'''Multi Level Inheritence'''
class A:
    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")
        
class B(A): #B is a child/sub class of A
    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")

class C(B): #C inherits B and B inherits the class A
    def feature5(self):
        print("feature5 is working")

#c1 = C()
#c1.feature2()
#c1.feature4()


'''Multiple Inheritence'''


class A:
    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")
        
class B():
    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")

class C(A,B): #C inherits A and B
    def feature5(self):
        print("feature5 is working")

#c1 = C()
#c1.feature4()
