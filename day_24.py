'''
Error Handeling
---------------
try:
---
--> The try block, that will test a block of code of errors
except:
------
-This block will handle the error, which are written in the try block.
'''
try:
    print("Python"+9)
    print(num)
except NameError:
    print("It is handling NameError : ")
except TypeError:
    print("It is handling TypeError : ")
except ValueError:
    print("It is handling Value Error : ")
except ZeroDivisionError:
    print("It is handling Value Error : ")

'''
else:
the else keyword to define a block which will run to be executed if no error were raised'''
'''#print(num)
except NameError:
    print("It is handling NameError : ")
else:
    print("No Error")
'''
#Finally:
#This block will execute it-self even if there is a error or not:
try:
    print("num")
except:
    print("it is handeling some error")
else:
    print("No Error")
finally:
    print("print finally Block")
