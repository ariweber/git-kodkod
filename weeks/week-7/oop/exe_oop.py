class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof"

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        self.area * self.height


class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count +=1

    def value(self):
        return self.count

class  Point:
    def __init__(self, n1 = 1, n2 =2):
        self.n1 = n1
        self.n2 = n2

    def __str__(self):
        return f"{self.n1},{self.n2}"
    
print(Point(1,2))

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount 
        
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= amount


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def fahrenheit(self):
         (self.celsius * 9/5) + 32    

class Student:
    school = "kodkod"
    def __init__(self, name):
        self.name = name


class Player:
    count = 0
    def __init__(self):
        self.count += 1


class Mony:
    def __init__(self, amount):
        self.amount = amount

    def  is_more_than(self, other):
        print(self.amount > other)

a = Mony(3)   
b = Mony(5)
print(b.is_more_than(a.amount))
        

        




        

        