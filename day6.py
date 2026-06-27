'''
-->Tuple is a collection of different datatypes that represent by "()"
and the in tuple is seprated by comma(,)>
>>tuple is immutable
'''
so=(1,"python",[7,8],(5,0),1)
print(so[1])
s2=(1,2,3,4,5,6,7,8)
s1=(10,20,30,40,50)
print(s2)
print(s1)
print(s2+s1)
'''
Dictionary:
----------
>>dict is collection key : value pair where keys are unique and immutable data-types  (such as strings,int,tuple) and values are any datatype.
this is represented by "{}"
methods:
-------
keys()
------
this method is used to access only keys in the dictionary
syn:dict.keys()
my={"name":"koushikvarma_Jampana",
    "Age" : 23,
    "edu":"MCA ,BSc:CS" }
print(my)
print(my.keys())

values()
--------
this method is used to access only values in the dictionary
syn:dict.values()
my={"name":"koushikvarma_Jampana",
    "Age" : 23,
    "edu":"MCA ,BSc:CS" }
print(my.values())

items()
--------
this method is used to access key:value pair.
my={"name":"koushikvarma_Jampana",
    "Age" : 23,
    "edu":"MCA ,BSc:CS" }
print(my.items())

clear()
-------
>> this clear method is used to delete all the items in the dict:
syn:dict.clear()
update()
--------
>> this  method is used to add a new item to dict,
my.update({"role":"PFS Trainee"})
'''

my={"name":"koushikvarma_Jampana",
    "Age" : 23,
    "edu":"MCA ,BSc:CS" }
print(my)
print(my.keys())
print(my.values())
print(my.items())
my.update({"role":"PFS Trainee"})
print(my)
