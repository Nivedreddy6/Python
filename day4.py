'''#Data-types:
>>two types
1)mutable datatype
------------------
>>i can modify directly on the varible,which the datatype have taken
eg:>> list,dictionary.
>> in list performing modification is possible

2)immutable datatype
------------------
>>i cannot  modify directly on the varible,which the datatype have taken
eg:>> int,string
>> in str performing modification on var is not possible

integer or int
--------------
>> storing number or digit in the varible is called int
num=90

float
--------------
>> storing decimal values in the varible is called float
num1=15.55'''

##indexing
#----------
'''>> this is used to get a particular substring, item from string,lis  and tuple by calling with index position.
>> syn: varr_name[index_position]'''
anyr='python is programming language'
print(anyr[9])#op: " ":space

'''string or str:
---------------
>> string is a colllection of character that are in closed in '',"",''' '''
>> it is immutable datatype'''
#>> eg: any="2@#,./"
#print(any)

#method:
#-------
#1)replace(): this method is used to change old sub string with a new string.
#>>syn: var_name.replace("old","new")
anyr='python is programming language'
print(anyr.replace('Python','java'))
print(anyr.replace('python','java'))
print(anyr.replace(' ','//'))
#2)concat():
#>> to add 2 strings:"+" acts as different ways,if adding 2 integers it acts as addition in other cases list,string,tuple it acts as concatination
s1="HI"
s2=", I AM KOUSHIKVARMA"
print(s1+s2)
#3)split():
#this method is used to sperate the string using a substring and it will split into list such as before the substring is one index and after the substring is another index.
#>>syn: var_name.split("substring")
print(anyr.split())
print(anyr.split("is"))
#4)strip():
#this method is used to remove from 1st index postion or last index position
print(anyr.strip("age"))
print(anyr.strip("t"))
print(anyr.strip("pyn"))
#5)join():
print("-".join(anyr))

'''6.capitalize()
7.casefold()
8.isalnum()
i9.isalpha()
10.isdigit()
11.isdecimal()
i2.islower()
13.isupper'''





