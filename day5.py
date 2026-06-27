'''
list data-type
--------------
>>list is a collection of different dayatypes and it is represented by "[]".
>>data types are seperated by data-types.
any=[1,"python is a language",67,68,[23,["this is python class"],69],78,"i am looking for bat",[2,"this is 5th class",3],56]
print(any[4][1][0][14])

methods:
--------
1.append():
>> This method is used to add new item into list but it will add in the last index position.
--> syn: var_name.append(item)
als=[1,2,3,4,5]
als.append(7)
print(als)
als.append([7,8,9,0])
print(als)
--------------------------
2.extend()
--------------------------
>> this method is also used to add new items into list, but this extend add eaach position to each index in list.
>>extend only take itterables
syn:var.extend(item)#itterble items
any=[1,2]
any.append("python")
any.extend("python")
any.extend([3,4,5,6,7,8])
print(any)
--------------------------
3.pop()
this is used to delete an item from the list,this pop() removes the value based on the index index postion.
>>if nothing is mentioned the parameters it will remove last index postion
syn:var.pop(index_positition)
ap=[1,2,3,4,5,6,7]
print(ap)
ap.pop(3)#3 is index place
print(ap)
---------------------------
4.remove():
this is used to delete an item from the list.
syn:var.remove(value)
lr=[1,2,3,4,5,6]
lr.remove(4,5)
print(lr)

##slicing()
-----------
This is used to get particular part of list,string or tuple
--> this will worrk based on index postition
syn:-->var_name[s_index:e_index]

##len():
to find the length of list,string and tuple
>>method is used to find the no of items present in the list
syn --> len(var)
'''
any="python is a programming laguage"
print(len(any))
print(any[:15])
'''---------------------
count()
index()
insert()'''
