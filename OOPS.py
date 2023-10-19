# Creating an Object and Class in python:
class employee():
    def __init__(self,name,age,id,salary):   #creating a function
        self.name = name  # self is an instance of a class
        self.age = age
        self.salary = salary
        self.id = id
 
emp1 = employee("harshit",22,1000,1234) #creating objects
emp2 = employee("arjun",23,2000,2234)
# print(emp1.__dict__) #Prints dictionary

#Object-Oriented Programming methodologies:
# Inheritance
# Polymorphism
# Encapsulation
# Abstraction

# Inheritance:
    # 1)Single Inheritance:
    # 2)Multilevel Inheritance:
    # 3)Hierarchical Inheritance:
    # 4)Multiple Inheritance:

# 1)Single Inheritance:
class employee1(): #This is a parent class
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee(employee1): #This is a child class
    def __init__(self, name, age, salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
emp1 = employee1('harshit',22,1000)
emp2 = childemployee('manomay',10,100000,1)    
print(emp1.age)
print(emp2.salary)

# 2)Multilevel Inheritance:
class employee(): #//Super class
    def __init__(self,name,age,salary):  
        self.name = name
        self.age = age
        self.salary = salary

class childemployee1(employee): #//First child class
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
class childemployee2(childemployee1): #//Second child class
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
emp1 = employee('harshit',22,1000)
emp2 = childemployee1('arjun',23,2000)
 
print(emp1.age,emp1.name)
print(emp2.age)

# 3)Hierarchical Inheritance:
class employee():
    def __init__(self, name, age, salary):   #  //Hierarchical Inheritance
        self.name = name
        self.age = age
        self.salary = salary
    
class childemployee1(employee):
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
class childemployee2(employee):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
emp1 = employee('harshit',22,1000)
emp2 = employee('arjun',23,2000)
 
print(emp1.age)
print(emp2.age,emp2.name)

# 4)Multiple Inheritance:
class employee1(): #//Parent class
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class employee2(): #//Parent class
    def __init__(self,name,age,salary,id):
     self.name = name
     self.age = age
     self.salary = salary
     self.id = id
 
class childemployee(employee1,employee2):
    def __init__(self, name, age, salary,id):
     self.name = name
     self.age = age
     self.salary = salary
     self.id = id
emp1 = employee1('harshit',22,1000)
emp2 = employee2('arjun',23,2000,1234)
 
print(emp1.age)
print(emp2.id)

# Polymorphism:
# Compile-time Polymorphism
# Run-time Polymorphism

# Compile-time Polymorphism:

''' A compile-time polymorphism also called as static polymorphism which gets resolved during 
the compilation time of the program. One common example is “method overloading”.
Let me show you a quick example of the same.'''

class employee1():
    def name(self):
        print("Harshit is his name")    
    def salary(self):
        print("3000 is his salary")
 
    def age(self):
        print("22 is his age")
 
class employee2():
    def name(self):
        print("Rahul is his name")
    
    def salary(self):
        print("4000 is his salary")
    
    def age(self):
        print("23 is his age")
 
def func(obj): #//Method Overloading
    obj.name()
    obj.salary()
    obj.age()
 
# obj_emp1 = employee1()
obj_emp2 = employee2()
 
# func(obj_emp1)
func(obj_emp2)

# Run-time Polymorphism:
'''A run-time Polymorphism is also, called as dynamic polymorphism where it gets resolved into the run time.
One common example of Run-time polymorphism is “method overriding”.'''
class employee():
   def __init__(self,name,age,id,salary):  
       self.name = name
       self.age = age
       self.salary = salary
       self.id = id
def earn(self):
        pass
 
class childemployee1(employee):
 
   def earn(self): #//Run-time polymorphism
      print("no money")
 
class childemployee2(employee):
 
   def earn(self):
       print("has money")
 
# c = childemployee1
# c.earn(employee)
# d = childemployee2
# d.earn(employee)

# Encapsulation:
'''In a raw form, encapsulation basically means binding up of data in a single class.
Python does not have any private keyword, unlike Java. A class shouldn’t be directly accessed 
but be prefixed in an underscore.'''

class employee(object):
    def __init__(self):   
        self.name = 1234
        self._age = 1234
        self.__salary = 1234
    
# object1 = employee()
# print(object1.name)
# print(object1._age)
# print(object1.__salary)

'''Explanation: You will get this question what is the underscore and error? 
Well, python class treats the private variables as(__salary) which can not be accessed directly.
So, I have made use of the setter method which provides indirect access to them in my next example.'''

class employee():
    def __init__(self):
        self.__maxearn = 1000000
    def earn(self):
        print("earning is:{}".format(self.__maxearn))
 
    def setmaxearn(self,earn): #//setter method used for accesing private class
        self.__maxearn = earn
 
emp1 = employee()
emp1.earn()
 
emp1.__maxearn = 10000
emp1.earn()
 
emp1.setmaxearn(1000000000)
emp1.earn()

# Abstraction:
'''An abstract class cannot be instantiated which simply means you cannot create objects for this type of class.
It can only be used for inheriting the functionalities.'''

from abc import ABC,abstractmethod
class employee(ABC):
    def emp_id(self,id,name,age,salary):   # //Abstraction
        pass
 
class childemployee1(employee):
    def emp_id(self,id):
        print("emp_id is 12345")
 
emp1 = childemployee1()
emp1.emp_id(id)