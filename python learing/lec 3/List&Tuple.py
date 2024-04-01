# 1 LIST in PYTHON
"""A built-in data type that stores set of Values
It can store elements of different types(integer,float,String etc.)
eg: marks=[87,64,33,95,76]
    student=["karan",85,"Delhi]
    
"""
marks=[80,32,11,"rhythm",3,21,10]
print(marks)
print(type(marks))
print(len(marks))
print(marks[3])

#list are mutable in python but strings cannot beacuase string are mutable  

marks[0]="karan" #here we can assign new value to list but not to the string in python 
print(marks)
#_______________________________________________________________________________________________________________________________________________
# 2 LIST SLICING
"""list_name[start_idx:end_idx] #ending not included
marks=[87,64,33,95]
marks[1:4]  output:87 64 33
marks[1:] or marks[1:len(marks)] same 
marks[:4] same like marks[0:4]

#negative index slicing is also possible
""" 
marks1=[87,94,33,23,29]
print(marks1[:4])
print(marks1[0:])
print(marks1[-3:-1])
#___________________________________________________________________________________________________________________________________________________________

# 3 LIST METHODS or FUNCTIONS
"""
list=[2,1,3]
1. list.append(4) #adds one elements at the end [2,1,3,4]
2. list.sort() #sort the list in accending order
3. list.sort(reverse=True) #sort the list in decending order
4. list.reverse() #reverse the list
5. list.insert(idx,el) #inser the element at particula index of list
6. list.remove(1) # remove the first occurence of that element 
   eg: [2,1,3,1]
   output : [2,3,1]
7. list.pop(idx) #remove the element at idx  
    """
list=[2,1,3]
print(list.append(4))
print(list.sort(reverse=True))
print(list.sort())
print(list.reverse())
print(list.insert(2,5))
print(list)
print(list.remove(5))
print(list)
print(list.pop(0))
print(list)

#__________________________________________________________________________________________________________________________________________________________

# 4 TUPLES
# A built- in data type that let us create immutable sequences of values.
"""
tup=(87,64,33,95,76) #tup[0],tup[1]..
tup[0]=43 #not allowed in python similar like in string
tup1=()
tup2=(1,) single tuple is always seperated by ","
tup3=(1,2,3)
"""
tuple=(2,1,3,4,5)
print(type(tuple))
print(tuple[0])
print(tuple[1])
print(tuple)
#tuple[0]=9 assignment not possible immutable not changable like list .
"""t=(4,)
print(type(t))"""

# 5 TUPLE FUNCTION/METHODS
""" 
1. tup.index(el) #return index of first occurence of that element . tup.index(1) is 1
2. tup.count(el) #return the number of time the element occured in the tuple tup.count(2) is 2
"""
tup=(2,1,3,1)
print(tup.index(2))
print(tup.count(1))

#________________________________________________________________________________________________________________________________________________________________

#practice questions
# 1.) WAP to ask user to enter manes of 3 favorite movies and store them in a list .
#sol
movie1=input("enter your first fav movie")
movie2=input("enter your second fav movie")
movie3=input("enter your third fav movie")
#list_mov=[movie1,movie2,movie3]
list_mov=[]
list_mov.append(movie1)
list_mov.append(movie2)
list_mov.append(movie3)
print(list_mov)

# 2.) WAP to check whether the string is palindrome or not 
pal_check1=[1,"abc","abc",1]
pal_checkcp=pal_check1.copy()
pal_checkcp.reverse()

if(pal_check1==pal_checkcp):
    print("palindrome")
else:
    print("not palindrome")

# 3 WAP to count the number of students with the "A" grade in following tuple.
#["C","D","A","A","B","B","A"]

tp_cnt=("C","D","A","A","B","B","A")
a=tp_cnt.count("A")
print(a)

# 4 store the above value in list and then sort in acending order

grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)


