'''
elif statement
--------------
--> This statement gives more option to get result of that program
m=int(input("Enter your marks: "))
if m>=90:
    print("A+")
elif m>=80:
    print("A")
elif m>=70:
    print("b+")
elif m>=60:
    print("b")
elif m>=50:
    print("c+")
elif m>=35:
    print("c")
else:
    print("fail")
'''
'''#Nested if:
#if statement inside another if statement is called nested if statement.
s_pin={"atm pin":"2002"}
i=input("enter your atm pin:")
if len(i)==4:
    if i in s_pin['atm pin']:
        print("welcome to sbi atm")
    else:
        print("pls enter correct pin")
else:
    print("pls enter the a 4digit pin")'''
"""
#for looping statements:
#--> a for statement used to iterate over items like(string,list,tuple) with fixed number of iterations
any=[23,45,6,78]
for j in any:
    print(j)"""
'''#else statement in for:
#after completing all iteration this else will execute
any=[23,45,6,78]
for j in any:
    print(j)
else:
    print("loop finished")'''
'''##String reversing and palimdrome fuction:
st=input("ENTER A NAME: ")
ep=""
for j in st:
    ep=j+ep
print(ep)
if ep==st:
    print("its a palindrome")
else:
    print("not a palindrome")'''

