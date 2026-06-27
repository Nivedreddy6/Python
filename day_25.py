'''
File Handling:
--------------
--> File handler is a object of a file to maintain several function of file like creating, reading, updating and deleting the files...
two ways to open
----------------
1.open()
eg
--
syntax---> file handler = open("filename.txt","mode")
            --------------------------------------
            --------------------------------------
            file handler.close()
any=open("demo.txt","r")

2.with open()
-------------
syn: with(keyword)open("filename","mode") as file handler:

eg:
--
with open("demo.txt","r") as so:
    print(so.read())
    
with keyword
------------
-->Using this with keyword no need to close the file in the lines, it will close the file automatically.

Modes:
------
r--> used to the and throught error if the file does not exist...
a--> used add the text at last, if the file does not exist it will create
w--> used to add new text as override the txt in the file, if the file does not exist it will create:
with open("dem.txt","w") as so:
    print(so.write("not feeling well: "))
x--> used to create the file and through error if the file exist
with open("ko.txt","x") as k:
    print(k.write("koushik"))
with open("ko.txt","a") as k:
    print(k.write("how are you:"))
    with open("sample.txt", "w+") as file:
    file.write("Python File Handling")
    
    file.seek(0)   # Move cursor to beginning
    
    print(file.read())'''
with open("sample.txt","r") as so:
    print(so.readline())



