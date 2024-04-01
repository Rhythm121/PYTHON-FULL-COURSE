# 1. LOOPS IN PYTHON

# Loops are used to repeat the instructions.

"""
while Loops

while condition:
   #some works

"""
"""
1. Print numbers from 1 to 100.

2. Print numbers from 100 to 1.

3. Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

4. Search for a number x in this tuple using loop:

[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

5. Print the multiplication table of a number n.
    """
#sol1
n=1
while n>=1 and n<=100:
    print(n)
    n+=1
print("\n")
#sol2
n=100
while n<=100 and n>=1:
    print(n)
    n-=1
print("\n")
#sol3
list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
n=len(list)
i=0
while i<n:
    print(list[i])
    i+=1

print("\n")

#sol4
x=int(input("enter the element to be found"))
tuple=(1,4,9,16,25,36,49,64,81,100)
i=0
n=len(tuple)
while i<n:
    if x==tuple[i]:
        print("the element is at:", i)
        break
    i=i+1
else:
    print("not found")
       
print("\n")  
#sol5 
n=3
i=1
while i<=10:
    print(n*i)
    i=i+1
    
# 2. BREAK AND CONTINUE

# 1. Break: used to terminate the loop when encountered
# 2. Continue: terminates execution in the current itteration & continues execution of the loop with next iteration
#eg of break:
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

print("end of loop")

#eg 2 of continue
i=0
while i<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1
    
print("skipping 3 ")
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# 3. for loops are used for sequential traversal list,strings,tuples etc.

#for loops
"""
1. for el in list:
      #some work

2. for-else loop

for el in list:
    #some work
else:
    #some work
    


"""
list=[1,2,3]
for i in list:
    print(i)

print("\n") 
print("\n") 
tup=(1,2,3,4,2,8,9)
for num in tup:
    print(num)
    
print("\n") 
print("\n") 

str="abcdfga"
for char in str:
    if char=="e":
        print("founded e")
        break
else: #since using break else can be used 
    print("End")

#practice

"""
q1)Print the elements of the following list using a loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

q2) Search for a number x in this tuple using loop:

[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

"""    
#sol1

list2=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for nums in list:
    print(nums)
    
#sol2

x=int(input("enter the number to be founded "))
tpl=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
i=1
for num in tpl:
    if(num==x):
        print("the number is founded at: ", i )
        break
    i+=1
else:
    print("not founded")
    
# 4. RANGE()
"""range function returns a sequence of numbers,starting from 0 bu default ,and increments by 1(by default), and stops before a specified number .

range(start?,stop,step?)

for el in range(5):
    print(el)
for el in range(1,5):
    print(el)
for el in range(1,5,2):
    print(el)

"""
print("\n")
print("\n")
seq=[1,2,3,4,5]
for i in seq:
    print(i)
print("\n")
print("\n")
for i in range(2,10,2):
    print(i)

print("\n")
print("\n")
"""
1. Print numbers from 1 to 100.

2. Print numbers from 100 to 1.

3. Print the multiplication table of a number n.
"""
#sol1
for i in range(1,101,1):
    print(i)
print("\n")
print("\n")

#sol2
for j in range(100,0,-1):
    print(j)
    
print("\n")
print("\n")

#sol3
n=int(input("enter the number"))
for i in range(1,11,1):
    print(i*n)
    
#_______________________________________________________________________________________________________________________________________________________________________________
# 5. PASS    
""" pass is a null statwment that does nothing . it is used as placeholder for future code

for el ijn range(10):
    pass
    
"""
#eg1:
print("\n")
print("\n")
for i in range(10):
    pass #cannot leave a for loop empty so write a pass as null statement.
print("hello world")

#practice question
#1 WAP to find the some of first n number(sing while)
#sol
n=int(input("enter the numbers range from 0"))
i=0
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)

# 2. WAT to find factorial of first n number.(using for)

#sol2
n1=5
fact=1
for i in range(1,n1+1):
    fact=fact*i
print(fact)