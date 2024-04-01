# 1. FUNCTION
# It is a block of statement that performs a specific task.
""" def func_name(param1,param2...):
        
        #some work
        
        return val

func_name(arg1,arg2..)#function call


#reduces the redundancy of code i.e no repeated line reduces complexity and less number of lines
"""
def sum(a,b):
    c=a+b
    print(c) 

sum(3,5)
sum(1,5)
sum(2,2)
print(type(sum))

# or
print("\n")
print("\n")
print("\n")

def cal_sum(a,b):  #parameters
    return a+b

print(cal_sum(2,5)) #function calls

print("\n")
print("\n")

def print_hello():
    print("hello")
    
print_hello()

print("\n")
print("\n")

def avg(a,b,c):
    sum=(a+b+c)
    average=sum/3
    print(average)
    
avg(1,2,3)
avg(98,97,95)

print("\n")
print("\n")

# 2. FUNCTIONS IN PYTHON 
"""
1. Built-in Functions         2. Userdefined Function
 i) print()                    thoes written by user
 ii) len()                     eg: calc_sum
 iii) type()
 iv) range()
"""
# 3. Default Parameters
#assigning a default value to parameter,which is used when no argument is passed.

def prod_two(a=1,b=2):
    return a*b

print(prod_two())

# 3. practice questions
"""
1. WAF to print the length of a list. ( list is the parameter)
2. WAF to print the elements of a list in a single line. ( list is the parameter)
3. WAF to find the factorial of n. (n is the parameter)
4. WAF to convert USD to INR.
"""

#sol1
def leng_l(list=[1,2,3,4,5]):
    print(len(list))

leng_l()

print("\n")
print("\n")

#sol2

def p_line(list=[1,2,3]):
    for i in list:
        print(i,end="\n")
        
p_line()

#sol3
print("\n")
print("\n")

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))

#sol4
n=int(input("enter the american dollar ammount: $"))
ind=0
def conv(n):
    ind=83*n
    print(ind,"RS")

conv(n)

#check odd even 
n=int(input("enter your number to be checked"))
def checker(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
        
checker(n)
#__________________________________________________________________________________________________________________________________________________________________________________________________________________________
# 4. RECURSION

""" when a fuction call itself repeatedly
#print n to 1 backwards
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
"""
n=int(input("entr the number"))
def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)
    print("end"," ")

show(n)

#code of factorial using recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(6))



    