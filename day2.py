'''
varible
------------------------------------------------------------------------------------
To define a varible, we have 2 rules:
1. good ways  to define a varible(no error)
>>using captial or small letters at the start'''
A=100
print(A)                                                                           
b=255
print(b)
#>>using underscore at the start.
_r=333
print(_r)
'''-------------------------------------------------------------------------------------
2. bad ways to define a varible(will get error)
5v=13
print(5v)
$f=55
print($f)
>>any where you using space 
 f=22
 print(f)
nu m=123
print(nu m)
>>keywords cannot be used for varibles names.
Note
----'''
#>>we are going to use meaningfull words or name for defining varibles 
num_1=155
num_2=1342
'''keywords
--------------------------------------------------------------------------------------
>>this keywords not gonna used as a varible:
Note: these are also called as identifiers/reserved words.
ex: if,else,for,elif.....
token
--------------------------------------------------------------------------------------
>>token is nothing but a small program/code in python to complete the task
a,b=15,11
print(a-b)
--------------------------------------------------------------------------------------'''
a,b,c=12,1,31
print(a,b,c)
print(f"\n {a} \n {b} \n {c}")
print(a)
print(b)
print(c)
'''comment lines:
--------------------------------------------------------------------------------------
>>there are two types of commentes lines
1. single line comment:
>>This is used to explain about particulaer line in the code,for this we can use "#" symbol.
ex: a,b=13,11 #In this line i assigned 2 varible in a single line.
2. multi line comment:
to comment more then single line we can use muliti-line comment""" """,''' '''
note:
-----
code or text written b/w the lines is not cosindered by cursor/interpreter
>>Boolean type:
----------------------------------------------------------------------------------------'''
#this is used to find out the statement is true or false
a=90
b=9
print(a==b)
print(a!=b)

#odd/even number program
num=7
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")





