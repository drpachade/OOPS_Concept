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



