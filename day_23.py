'''
Polymorphism
------------
-->Polymorphism mean "many forms", the same method, operator or a function  can perform different actions depending upon the objecg or datatype.

1.Method overloading
--> Method overloading is creating multiple methods with the same name with different parameter 
--------------------
class addition:
    def add(self,a,b=0,c=0):
        return a+b+c
o=addition()
print(o.add(23,45))
print(o.add(23,45,68))

class addition:
    def add(self,a,b,c=0,d=0):
        return a+b+c+d
o=addition()
print(o.add(2,3))
print(o.add(2,3,5))
print(o.add(2,3,4,6))

2.Method overriding
-------------------
class animal:
    def sound(self):
        print("Animal make sound")
class dog(animal):
    def sound(self):
        print("Dog barks bowwww")
any=dog()
any.sound()

3.operator overloading
----------------------
-->
class stu:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,an):
        return self.marks+an.marks
a=stu(55)
b=stu(60)
print(a+b)
'''
from abc import ABC, abstractmethod
class veh(ABC):
    @abstractmethod
    def start(self):
        pass
class car(veh):
    def start(self):
        print("car start with key")
who=car()
who.start()
