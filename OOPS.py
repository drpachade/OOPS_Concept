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


