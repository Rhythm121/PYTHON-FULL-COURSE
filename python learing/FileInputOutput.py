#FILE I/O in python
"""
python can be used to perform operations on file(read and write data)

types of all files
1. Text files: .txt , .docs, .log etc
2. Binary Files: .mp4, .mov, .png, .jpeg etc

"""
# Open ,read and Close File
"""
we have to open a file before reading or writing
f=open("file_name,"mode")
file_name=sample.txt
mode= r:read
      w:write
data=f.read()
f.close()

"""
f=open("C:/Users/rhythm rohatgi/Desktop/python learing/lec 7/demo.txt","r")
data=f.read(5) #we can read a file one time while running 
line1=f.readline()
print(data)
print(line1)
print(type(data))
f.close()
"""   
Character                                Meaning

 1. 'r'                              open for reading (default)

2. 'w'                               open for writing, truncating the file first

3. 'x'                               create a new file and open it for writing

4. 'a'                               open for writing, appending to the end of the file if it exists

5. 'b'                               binary mode

6.'t'                                text mode (default)

7. '+'                               open a disk file for updating (reading and writing)
"""

#writting on a file

"""
f=open(".txt,"w")
f.write("hello world")//overritting of the data

f=open(".txt,"a")
f.write("hello world")//here we are appending adding new line at the end

"""
f=open("C:/Users/rhythm rohatgi/Desktop/python learing/lec 7/demo.txt","w")
f.write("hello world")
f.close()

f=open("C:/Users/rhythm rohatgi/Desktop/python learing/lec 7/demo.txt","a")
f.write("\nthis is rhythm")
f.close()