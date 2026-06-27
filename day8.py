'''
User Input:
-----------
int:
any=int(input("Enter a number"))
print(type(any))
print(any)
c,d=map(int,input("Enter two numbers: ").split())
print(c,d)
print(type(c))
print(type(d))

string:
a=input("enter the word:")
print(type(a))
print(a)

list:
ls=list(map(int,input("enter the numbers: ").split()))

tuple:
ls=list(map(int,input("enter the numbers: ").split()))

formating string:f string and doc string---
-------------------------------------------
a=87
b=19
print(f"{a} + {b} : {a+b}")

if statement:
-------------
this is used to check condition is true or not

an=9
if an==9:
    print(f"an is equalto the {9}")
Else statement:
-->else is fall back statement, in case if statement, in case if ststement become false,it will enter into else.
a=10
b=22
if a>b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

eval():

a=eval(input())
print(a)
print(type(a))
m=int(input("enter marks"))
if m<35:
      print(f"{m} means fail")
else:
    print(f"{m} means pass")
'''
