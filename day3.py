'''Operators
-------------------------------------------
1.arithmetic operator  
2.assignment operator
3.comparision operator
4.logical operator
5.indentity operator
6.membership operator
7.bitwise operator.
-------------------------------------------'''
#1.arithmetic operator:+,-,%,*,**,...
#>>addition(+)
num1=143
num2=234
num3=133
print(num1+num2+num3)#>>o/p:510
#>>sub(-)
sub1=187
sub2=125
print(sub1-sub2)#>>o/p:62
#>>per(%)
per1=14
per2=5
print(per1%per2)#>>o/p:4=rem
#>>mul(*)
mul1=13
mul2=2
print(mul1*mul2)#>>o/p:26
#>>pow(**)
pow1=13
pow2=2
print(pow1**pow2)#>>o/p:169
#NOte:floor division is used to return decimal round up value
fl1=15.55
fl2=3
print(fl1//fl2)#o/p:5.0
#-------------------------------------------------
#2)assignment operator:=,+=,-=,*=,//=...
#>>(=):assign value to varibles
#a'='55
#>>(+=)
aso1=9
aso1+=4
print(aso1)#op:13
#>>(-=)
ao2=9
ao2-=4
print(ao2)#op:5
#>>(*=)
ao3=9
ao3*=4
print(ao3)#op:36
#>>(**=)
ao4=9
ao4**=4
print(ao4)#op:6561
##>>(//=)
ao5=9
ao5//=4
print(ao5)#op:6561
#--------------------------------------
#3)comparision operator:==,!=,>,<,<=,>=
#>>(==):
co1=15
co2=55
print(co1==co2)#o/p:f
#>>(!=):
co1=15
co2=55
print(co1!=co2)#o/p:t
#>>(>):
co1=15
co2=55
print(co1>co2)#o/p:f
#>>(<):
co1=15
co2=55
print(co1<co2)#o/p:t
#>>(<=):
co1=15
co2=55
print(co1<=co2)#o/p:t
#>>(==):
co1=15
co2=55
print(co1>=co2)#o/p:f
#---------------------------------
#4)logical operator:and,or,not
#>>and--> 2 conditions should be
lo1=15
lo2=30
print(lo1<20 and lo2>20)#o/p:true
#>>or-->atleast one conditions should be true
lo1=15
lo2=30
print(lo1>20 or lo2>20)#o/p:true
#>>not--> reverse the output
lo1=15
lo2=30
print (not(lo1<20 and lo2>20))#o/p:false
#------------------------------------------
#5)Identity operator:is,isnot
#>>is --> this operator is used to check the object
i1=15
i2=15
print(i1 is i2)#o/p:true
print(id(i1))
print(id(i2))
l1=[1,2]
l2=[1,2]
l3=l1
print(l1 is l2)#o/p:false
#>>Note: == checks the both sides of values and is finds the id values and compares
print(l1 == l2)
print(l1 is l3)#o/p:true
print(id(l1))
print(id(l3))
print(id(l2))
#>>is not--> this operator is used to check the object not same
i1=15
i2=15
print(i1 is not i2)#o/p:false
#--------------------------------------------------------
#5)membership operator:in,not in
#>>in-->to check if it is inside
l1=[1,2]
l2=[1,2]
l3=l1
print(l1 in l2)#o/p: False
#>>not in-->to check if it is not inside
l1=[1,2]
l2=[1,2]
l3=l1
print(l1 not in l2)#o/p: True
#-------------------------------------------------------------
#6)Bitwise operator:&,|,^,~,<<,>>
#(&):-->bitwise AND
#5--> 0101
#3--> 0011
#----------
#1-->  0001
print(5&3)#o/p:1
print(6&4)#o/p:4
#(^):-->bitwise xor
#5--> 0101
#3--> 0011
#----------
#6--> 0110
print(5^3)
#(|):-->bitwise or
#5--> 0101
#3--> 0011
#----------
#7--> 0111
print(5|3)







    
    





