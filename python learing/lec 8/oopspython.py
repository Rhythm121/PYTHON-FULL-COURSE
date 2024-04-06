# 1. Oops in Python 
# To map with real world Scenarios ,We statred using Objects in the code
# This is called Object Oriented Programming.

# Class And Object in python
"""Class is the blue Print for creating objects."""

#Creating Class
"""
Class Student:
    name="karan kumar"
    
    #creating  onject(instances)
    s1=Student() ->class name 
    print(s1.name)
    """
class Student:
    name="rhythm rohatgi"
    
    
S1=Student()
print(S1.name)
print(S1)

class car:
    color="blue"
    brand="mercedes"
    
car1=car()
print(car1.color)
print(car1.brand)

""" __init__ Function 

Constructor
All classes have a function called __init__(),which is always executed when class is being initiated

"""
class database:
    def __init__(self,name1,fullname):
        self.name=fullname
        self.n1= name1
        print("adding new to the databases..")
        print(self)    
    
S2=database("rhythm","kiran")
print(S2.name,S2.n1)

S3=database("rhythm","kiran")
print(S3.n1)

# Types of constructor

"""
1) Default Constructor
def __init__(self): donot have the arguments

2) parameterized constructor:   having arguments
 def __init__(self ,name1,marks):
 
        """
# CLASS AND INSTANCE ATTRIBUTES
""" Class.attr
    obj.attr
"""
# Methods
"""methods are the functions that belongs to objects

class student:
    def __init__(self,fullname):
        self.name=fullname
    
    def hello(self):
        print("hello",self.name)
        
        
s1=student("karan")
s1.hello()
"""
class student:
    def __init__(self,fullname):
        self.name=fullname
    
    def hello(self):
        print("hello",self.name)
        
        
s1=student("karan")
s1.hello()
#
# Q1) Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

#sol1
"""
class student:
    def __init__(self):
        self.name1="rohan"
        self.name2="rhythm"
        self.name3="roshan"
        self.marks1=50
        self.marks2=49
        self.marks3=46

s1=student()
print(s1.name1,s1.marks1)
print(s1.name2,s1.marks2)
print(s1.name3,s1.marks3)
"""
#alternative
"""
class studentnew:
    def __init__(self,n1,n2,n3,m1,m2,m3):
        self.name1=n1
        self.marks1=m1
        self.name2=n2
        self.marks2=m2
        self.name3=n3
        self.marks3=m3
        
s4=studentnew("rhythm","sarthak","priya",45,60,75)
print(s4.name1,s4.marks1,s4.name2,s4.marks2,s4.name3,s4.marks3)

"""
class student:
    def __init__(self,name,marks):
        self.name1=name
        self.mark=marks
        
    def avg(self):
        sum=0
        for i in self.mark:
            sum+=i
        print(sum/3)
        
            
        
S4=student("rhythm rohatgi",[98,93,95])

print(S4.name1,S4.mark)
S4.avg()

# STATIC METHODS
"""
methods that don't use th self parameter (work at class level)
class student:
    @staticmethod
    def college():
        print("hello")   

"""
class student:
    @staticmethod #decorator  wrap a whole fuction in 1 unit and gives the wrap function as output by chainging its behaviour
    def college():
        print("hello") 
        
s5=student()
s5.college()


