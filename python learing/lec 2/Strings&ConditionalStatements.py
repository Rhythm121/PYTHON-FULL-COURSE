# 1 STRINGS 
""" 
String is a datatype that stores sequence of charecters.
    """
""" Basics Operations
"""
#___________________________________________________________________________________________________________________________________
# 2 concatenation
""" "hello"+"world"->"helloworld"
+ here is operator to do so.
"""
str2="rhythm"
str3="rohatgi"
fstr=str2+" "+str3
print(fstr)
#_____________________________________________________________________________________________________________________________________
#3 length of str
"""   
lenstr()

"""
str2="rhythm"
len1=len(str2)
str3="rohatgi"
len2=len(str3)
fstr=str2+" "+str3
print(fstr)
print(len(fstr))
print(len1)
print(len2)
#str2="rhythmcse"
#str3=""" this is a string also"""
#_________________________________________________________________________________________________________________________________________________
# 4 escapesequence charecter is specialized charecter for formaating like space and line change.
# eg: \n->line change   \ ->tab escape sequence char
str1 = "this is a string.\nwe are creating in python"
print(str1)

# 5 INDEXING 
"""Rhythm_rohatgi
str[0]='R'
str[1]='h'
str[2]='y'

we cannont modify charecter using indexing but can only access. 
"""
str="Rhythm Rohatgi"
print(str[0])
print(str[3])
print(str[5])
print(str[6])
print(str[7])
#___________________________________________________________________________________________________________________________________________
# 6 SLICING 
# Accessing parts of string
"""str="apnacollege
str[1:4] is "pna" -> (1->left limit 4->end limit )
str[ :4] is same as str[0:4]
str[1: ] is same as str[1:len(str)]
"""
str4="apnacollege"
print(str4[1:4])
print(str4[ :4])
print(str4[4: ])
print(str4[4:len(str4)])

# 7 Negative Index
""" A   p   p   l   e
  [-5][-4][-3][-2][-1]  
  
  str="Apple"
  print(str[-3:-1]) 
  output="pl"
  #last e i.e [-1] not included  
"""
str5="apple"
print(str5[-3:-1])
#_____________________________________________________________________________________________________________________________________
# 8 VIMP STRING FUNCTIONS
"""str= "I am a Coder"
1)str.endwith("er") #returns true if string end with substr(here it is "er").
2)str.capitalize() #capitalizes 1st char.
3)str.replace() #replace a old value of sting to new value of the string.
4)str.find(word) #retuns 1st index of 1st occourer
5)str.count("am") #count the occurence of the substr in the string (here it is "am")
"""
str6="i am studying python from apnacollege"
print(str6.endswith("app"))#1
print(str6.endswith("ege")) #1
str6=str6.capitalize()#2  chnaging original string 
print(str6.capitalize()) #2 creating new but not changes original string 
print(str6)#2
print(str6.replace("o","a")) #3
print(str6.replace("python","javascript")) #3
print(str6.find("am")) #4 return the 1st index of the word where it starts at first occurence
print(str6.count('o')) #5 

# 9 PRACTICE QUESTIONS
# 1 write a program to take user name as input and give length of name as output
name=input()
print(len(name))

# 2 wap to find occurence of $ in the string?
string=input()
cnt=string.count('$')
print(cnt)
#____________________________________________________________________________________________________________________________________________________________________________________________

# 10 CONDITIONAL STATEMENTS

""" if-elif-else(SYNTAX)
if(condition):
     Statement1
elif(condition):
     Statement2
else:
     StatementN 
"""
"""
eg:

age=int(input())
if(age>=18):
    print("eligible") #indentation
elif(age<18 and age>0):
    print("not eligible")
else:
    print("dont know")
"""
"""
marks=int(input())
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")
   """ 
#__________________________________________________________________________________________________________________________________________________________________________________________________
#PRACTICE QUESTIONS
# 1 WAP to check isf the number is even or odd
"""number=int(input())
if(number%2==0 or number==0):
    print("The number is even")
else:
    print("The number entered is odd")
"""

# 2 WAP  print the greatest number between 3 numbers entered byv the users

a=int(input())
b=int(input())
c=int(input())
if(a>=b and a>=c):
    print("a is greatest")
elif(a<b and b>=c):
    print("b is greatest")
else:
    print("c i greatest")
    
# check if the number is multiple of 7 or not 
Mt=int(input())
if(Mt%7==0):
    print("Multiple")
else:
    print("not the multiple")
    