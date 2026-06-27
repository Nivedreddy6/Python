'''
#li appending:
li=eval(input("enter a list"))
t=[]
for i in li:
    if i not in t:
        t.append(i)
print(t)'''
#printing max and scnd max number of list:-
li=eval(input("enter a list"))
max1=0
max2=0
for i in li:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2:
        max2=i    
print(f"{max1} is max number of {li}")
print(f"{max2} is 2nd max number of {li}")
