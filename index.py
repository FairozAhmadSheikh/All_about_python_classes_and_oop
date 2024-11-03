"""
Question 1 :  Define a class named Car with attributes make, model, and year. Create an object of
Car class and print each attribute."""

class Car:
    make="Honda"
    model="Civic"
    year=2016

c1=Car()
print(c1.make)
print(c1.year)
print(c1.model)

"""Question 2 
Write a class called Book with attributes title, author, and pages. Write a method to
display information about the book.
"""
class Book:
    title="Hobbs and Shaw"
    author="Dwayne Jhonson"
    page=312
    def get_info(cls):
        print(f"{cls.title} by {cls.author} with pages {cls.page}")
c1=Book()
c1.get_info()

"""Question 3 : 
Define a class Person with attributes name and age, and a method introduce() that
prints "Hi, I'm [name] and I'm [age] years old."
"""
class Person:
    name="john"
    age=21
    def introduce(cls):
        print(f"Hi , I'm {cls.name} and I'm  {cls.age} years old ")

# Object 
p1=Person()
# Object invoke a method
p1.introduce()
""" Question 4 
Create a class Rectangle with attributes length and width, and methods area() and
perimeter() to calculate and return the area and perimeter of the rectangle.
"""

class Rectangle:
    length=16
    width=42
    def area(cls):
        return f"{cls.length*cls.width} cm^2"
    def perimeter(cls):
        return f"{2*(cls.length+cls.width)} cm^2"

r1=Rectangle()
print(r1.area())
print(r1.perimeter())

"""Question 5 :
Define a class Student that initializes with the attributes name, roll_number, and grade.
Create a constructor to initialize these values when a Student object is created.
"""
class Student:
    
    def __init__(self,name,roll_number,grade):
        self.name=name
        self.roll_number=roll_number
        self.grade=grade

s5=Student("Sameer",30,"A+")
print(s5.name)
print(s5.roll_number)
print(s5.grade)

"""
Q6: Write a BankAccount class that takes account_number and balance as parameters in
the constructor. Add a method deposit(amount) that adds the amount to the balance.

"""
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance 
    def deposit(self,amount):
        return self.balance+amount

b1=BankAccount(15016,1000)
print(b1.deposit(5000),"Balance For Account Number : ",b1.account_number)
"""
Q7: Implement a class Employee with private attributes name and salary. Create getter
and setter methods for both attributes to ensure encapsulation.
"""
class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
    #GETTER METHODS : a property method that return some attribute or values  
    @property # Property is a Decorator  used to define a method as a property (it can be accessed as an attribute)
    def name(self):
        return self._name
    @property
    def salary(self):
        return self._salary
    # Setter Method 
    @salary.setter
    def salary(self,new_salary):
        self._salary=new_salary
        return self._salary
    @name.setter
    def name(self,new_name):
        self._name=new_name
        return self._name
    
e1=Employee("Rabia",7200)
e1.salary=600
e1.name="EESA"
print(e1.salary)
print(e1.name)

"""
Q8: Define a class Patient with private attributes _name and _age. Use property decorators
to make these attributes accessible but also protect them with encapsulation.
"""
class Patient:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @property
    def get_info(self):
        return f"Patient name : {self._name} , Age: {self._age} "

p1=Patient("Nafi",54)
print(p1.get_info)

"""
Q9: Create a class Animal with a method speak(). Then, create two subclasses, Dog and
Cat, each with its own version of speak().
"""
class Animal:
    def speak(self):
        print("This animal Speaks")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Dog(Animal):
    def speak(self):
        print("Woof")
        
class Horse(Animal):
    pass
        
d1=Dog()
d1.speak()
c1=Cat()
c1.speak()
h1=Horse()
h1.speak()

"""
Question10: Implement a class hierarchy with Vehicle as the base class, Car and Bike as
subclasses, and each subclass has its own method type() returning "Car" or "Bike".
"""
class Vehicle:
    pass 
class Car(Vehicle):
    def type(self):
        print("Car")
class Bike(Vehicle):
    def type(self):
        print("Bike")
c1=Car()
c1.type()
b1=Bike()
b1.type()

"""
Q11: Add a __str__ method to the Student class that prints a string containing the student’s
name and roll_number whenever the object is printed.
"""

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.rollno=roll_no
    def __str__(self):
        return f"{self.name} {self.rollno}"
s1=Student("Sameer",16)
print(s1)

"""
Q12: Define a class Product with attributes name and price, and implement a __str__
method to display product details in a user-friendly format.
"""
class Product:
    name="Aashirvaad"
    price=1600
    def __str__(self):
        return f"Product Name : {Product.name} , Price : {Product.price} $ "
p1=Product()
print(p1)
"""
Q13: Create a class MathOperations with a static method add(a, b) that returns the sum of a
and b. Test this method without creating an instance of the class.
"""
class MathOperations:
    
    @staticmethod
    def add(a,b):
        return a+b
    
print(MathOperations.add(16,20))

"""
Q14: Implement a class Person with a class attribute population and a class method
get_population() to return the total number of people created.

"""
class Person:
    population=0
    def __init__(self,name):
        self.name=name
        Person.population+=1
    @classmethod
    def get_population(cls):
        return f"Total Population of Village is {cls.population}"

p1=Person("Ali")
p2=Person("MOha")
print(Person.get_population())

"""
Q15: Define a class Temperature with a private attribute _celsius. Use the @property
decorator to create a getter and setter for celsius, and add validation in the setter.

"""
class Temperature:
    def __init__(self,celsius):
        self._celsius=celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self,update_temp):
        self._celsius=update_temp
        return self._celsius

t1=Temperature(102)
t1.celsius=109
print(t1.celsius)

"""
Q16: Create a BankAccount class with a private attribute _balance. Use @property
decorator to create a property balance that allows reading and updating the balance.

"""
class BankAccount:
    def __init__(self,balance):
        self._balance=balance
    @property
    def balance(self):
        return f"Amount in Account : {self._balance} $ "
    @balance.setter
    def balance(self,new_balance):
        self._balance+=new_balance
        return self._balance
    
b1=BankAccount(16000)
b1.balance=4000
print(b1.balance)


""""
Q19: Create a single inheritance hierarchy using Employee as the base class and Manager
as the derived class.
"""

class Employee:  # Parent Class
    def greeting(self):
        print("HI From Parent or Employee Class")  
             
class Manager(Employee): # Child Class
    def intro(self):
        print("I am Manger ")   
m1=Manager()
m1.greeting()
m1.intro()

"""
Q20: Demonstrate multilevel inheritance by creating a class GrandParent, then Parent that
inherits from GrandParent, and finally Child that inherits from Parent.
"""

class Grandparent:
    def grandparent(self):
        print("I AM GRANDPARENT CLASS")

class Parent(Grandparent):
    def parent(self):
        print("I AM PARENT CLASS THAT INHERITS GRANDPARENT CLASS")
class Child(Parent):
    def child(self):
        print("I am Child Class that inherits Parent Class ")

c1=Child()
c1.child()
c1.parent()
c1.grandparent()

"""
Q21: Show multiple inheritance by creating a class Father and a class Mother, then creating
a class Child that inherits from both Father and Mother
"""

class Father:
    def father(self):
        print(" I am Father")
class Mother:
    def mother(self):
        print(" I am Mother")
class Child(Father,Mother):
    def child(self):
        print("I am child and inherit both Father and Mother ")
    
cx=Child()
cx.child()
cx.father()
cx.mother()

"""
Q22: Implement a hybrid inheritance example where a class Animal has subclasses Bird and
Mammal, and Bat inherits from both Bird and Mammal
"""
class Animal:
    class Bird:
        def intro(self):
            print("I AM Bird")
    class Mammal:
        def define(self):
            print("I Am Mammal")

class Bat(Animal.Bird,Animal.Mammal):
    pass

b1=Bat()
b1.define()
b1.intro()