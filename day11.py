#pattern problems:--
#Right angle triangle:-----
'''num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print('*', end="")
    print()'''
'''
o/p:

*
**
***
****
*****
'''
#Reverse_Right angle triangle:-----
'''num=int(input("enter the no: "))
for a in range(num,0,-1):
    for b in range(1,a+1):
        print('#', end="")
    print()'''

'''
#####
####
###
##
#
'''
#pirmid
'''
num=int(input("enter:"))
for i in range(num):
    for j in range(num-i-1,0,-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()'''
# Basic calculator:--
n1=int(input("Enter The 1st Num:  "))
n2=int(input("Enter The 2nd Num:  "))
c=int(input("\n1.Add \n2.sub \n3.mul \n4.div \n5.pow \n Enter choice no: "))
if c==1:
    print(n1+2)
elif c==2:
    print(n1-n2)
elif c==3:
    print(n1*2)
elif c==4:
    print(n1%2)
elif c==5:
    print(n1**2)
else:
    print("Enter valid choice")







