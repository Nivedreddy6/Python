'''
Set datatype
------------
-->Set is collection of unordered element or unique elements unlike list or tuple set is not permit duplicate in side.
-->set is mutable

Methods
-------
add()
-----
>this method is used to add new item into the set
syn:var_name.add(item)
s={1,2,3,2}
print(s)#2 is not printing
s.add(4)
print(s)

remove()
--------
-->This method is used to delete an item in thee set.
syn:va_name.remove(val)
s={1,2,3,4}
s.remove(4)
print(s)

pop()
-----
-->This is also used to delete elements in the set, but we can not specify the element.
syn:var_name.pop(no_arguements)
s={1,2,3,4}
s.pop()
print(s)#{2, 3, 4}

clear()
------
-->This method is used to delete all the elements in the set
syn:var_name.clear()
s={1,2,3,4}
s.clear()
print(s)#set()

update()
--------
-->same like add but this method will add more than one element.
syn:var_name.update([elements])
s={1,2,3,4}
s.update([6,7,8])
print(s)#{1, 2, 3, 4, 6, 7, 8}

union()
-------
-->This method will return a set all elements from both sets , but  not duplicates
syn:set1.union(s2) or s1 | s2
s={1,2,3,4,5}
u={2,4,6}
print(s.union(u))#{1, 2, 3, 4, 5, 6} ignores duplicates.

intersection():
---------------
-->This method will give only the common elements from both sets.
syn:s1.intersection(s2) or s1&s2
s1={1,2,3,4,5,6,7,8,9,10}
s2={2,4,6,8,10}
print(s1.intersection(s2))#{2, 4, 6, 8, 10}
print(s1&s2)#{2, 4, 6, 8, 10}

difference()
-->This method will give only the different elements from both sets:
s1={1,2,3,4,5,6,7,8,9,10}
s2={2,4,6,8,10}
print(s1.difference(s2))
print(s1-s2)#{1, 3, 5, 7, 9}
'''
#type coversion:
#----------------
'''
--> converting one data type into another datatype:

a=8
print(a)
print(type(a))
b=str(a)
print(b)
print(type(b))
c=float(a)
print(c)
print(type(c))

String--> int,float,list,tuple
'''
r=eval(input())
print(r)


