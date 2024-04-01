# 1. DICTIONARY IN PYTHON
""" Dictionary are used to store data values in key:value pairs
They are unordered,Mutable(changeable) and Donot allow duplicate key
eg:
dict={ "name":"rhythm",
"cgpa":9.0,
"marks":[98,97,95],
}

dict["name"],dict["cgpa"],dict["marks"]

dict["key"]="value ##To assign new or add new
"""
info = {
    "name": "Rhythm",
    "learning": "coding",
}
print(info)
print(info["name"])
info["age"]=23
print(info)

# 2. Nested DICTIONARY
""" syntax
student={
    "name": "rhythm",
    "score":{
        "chem":98,
        "phy": 97,
        "math": 95,
    }
}

student["score"]["math"]
"""
student={
    "name": "rhythm",
    "score":{
        "phy":87,
        "chem":98,
        "math":84,
    }
}
print("\n")
print(student)
print(student["name"])
print(student["score"]["math"])

# 3. DICTIONARY FUNCTION/METHODS
"""
1.)mydict.keys() #returns all the keys
2.)mydict.values() #returns all values
3.)mydict.items() #return all the (key,val) pairs as tuples
4.)mydict.get("key"") #return thre key according to value
5.)mydict.update(newdict) #insert the specified items to the dictionaries

    """
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("score"))
newdict={
    "class":12,
}
student.update(newdict)
print(student)
#______________________________________________________________________________________________________________________________________________________________________________________________________________

# 4.SET IN PYTHON
""" set is the collection of the unordered items.
Each element in the set must be unique & immutable.
but the set is (mutable)

nums={1,2,3,4}
set2={1,2,2,2}
#repeated elements stored only once,so it resolved to {1,2}
 
null_set=set() #empty set syntax

"""
c={1,2,3,4,"hello",(1,2,1),"hello"} #duplicate value is ignored while printing
print(c)     
print(type(c))
print(len(c)) #ignore the duplicate value during length count

#EMPTY SET SYNTAX
col=set()
print(col)
print(type(col))

# 5. SETS METHOD
"""
1. set.add(el) #add an element.
2. set.remove(el) #removes the element. 
3. set.clear() #empty entire set.
4. set.pop() #removes a random value.
""" 
c.add(9)
print(c)
c.remove("hello")
print(c)
c.clear()
print(c)
c.add(1)
c.add(3)
c.add(5)
c.add("hello")
print(c)
print(c.pop())

"""
5. set.union(set2)
6. set.intersection(set2)


"""
#eg:
set1={1,2,3}
set2={2,3,4}
newset=set1.union(set2)
newiset=set1.intersection(set2)
print(newset)
print(newiset)

#___________________________________________________________________________________________________________________________________________________________________________________________________________

# PRACTICE QUESTIONS

# Q1 store the word meanings in python 
""" word1="table
word2="cat"
"""
#sol1
dict={}
str1=input("enter the meaning1")
str2=input("enter the meaning 2")
str3=input("enetr meaning of word 2")
dict["table"]=[str1,str2]
dict["cat"]=str3
print(dict)

#Q2) you are given a list of subjects for the students,assume one classroom is required for 1 subject .
# how may classrooms are needed
"""
"python","java","c++","python","javascript","java","python","java","c++","c"


        """
collection={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(collection))

# q3 WAP enter marks of 3 students in a dictionary .starts
# with empty dictionary & add one by one.use subject name as key and marks as value
#sol3
score={}
marks1=input("enter the marks of phy: ")
marks2=input("enter the marks of chem: ")
marks3=input("enter the marks of math: ")
score["phy"]=marks1
score["chem"]=marks2
score["math"]=marks3
print(score)

# Q4 figure out a way to store 9,9.0 as seperate value in the set.
#sol4 
tup=(9,9.0)
val={tup}
print(val)
