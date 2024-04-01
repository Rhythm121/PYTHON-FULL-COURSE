print("rhythm is my name.","my age is 23")
print(23*25)
## print is fuction to give or return some value

# 1 VARIABLES
## variables is the name given to  memory location of the program
name="rhythm"
age=28
AGE2=age
price=63.54
print(name,age,price) 

#2 rules for Identifiers 
# 1) Identifiers can be the combination of uppercase and lower case letter ,digits or 
# or (_)underscore
# 2) Identifiers cannot start with the digits eg 1variable (invalid)
# 3) We cannot use special symbols like !,#,@ % $ etc
# 4) Identifier can be of any length 
# type() fuction used inside th print help to etetct what type of data type is that variable

print(type(name))
print(type(age))
print(type(price))

#3 DATA TYPE
# 1 INT eg: +ve ,-ve ,0
# 2 String eg: "rhythm",'hello','''hello''';
# 3 Float  eg: decimal 62.23
# 4 Boolean eg : True or False T AND F CAPITAL in python
# 5 None eg: a=None

age3=23
old=False
a=None
print(type(age3))
print(type(old))
print(type(a))

# 4 KEYWORDS -RESERVED WORDS IN PYTHON
#eg: and ,else,as,is,return,lambda,pass,del,def,break,class,or,import,not,none,continue,elif,del,while,try,else,global ,if,in,with,yeild,for,finally.

#PYTHON IS CASE sensative i.e a and A is different.

#print sum code
a=1500
b=1000
sum=a+b
print(sum)

""" 
    hello 
    """
#5 Types of operator in python 
"""
1.) Airthemethic Operator(+,-,*,/,%,**)
2.) Relational/comparision operator (==,!=,>,<.>=.<=)
3.) Assignment Operator (=,+=,-+,*=,/=,%=,**=)
4.) Logical operator(not ,and ,or)    
    """
# 6 TYPE CONVERSION
# python automatically do the type conversion 
"""
eg: a,b=1,2.3
    sum=a+b
    print(sum)

invalid eg : a,b=2,"hello"
             sum=a+b
             print(sum)//error  can only concatinate string and cannot be conversion   
"""
#to overcome the above string problem 

# 7 TYPE CASTING IS DONE or manual forcing to change dharm 

a1=int("2")
b=2.3
sum=a1+b
print(sum)
   
   # HOW TO TAKE INPUT IN PYTHON 
N=int(input())
P=float(input())
Q=str(input()) 
print(N,P,Q)
