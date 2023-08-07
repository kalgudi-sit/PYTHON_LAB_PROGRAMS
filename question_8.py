# Cell 1:

import numpy as np
import pandas as pd
# write the contents on to the text file

f1 = open("file1.txt", 'w')
f1.write('----------------------------------------------------------------------------------------------'+'\n')
f1.write('Course Title'+'\t'+'Course Code'+'\t'+'Faculty Incharge'+'\t'+'Contact Hours'+ '\t'+'Credits'+'\n')
f1.write('----------------------------------------------------------------------------------------------'+'\n')

while 1:
    CT = input("\nEnter Course Title : ")
    CC = input("\nEnter Course Code  : ")
    FI = input("\nEnter Faculty Incharge : ")
    CH = input("\nEnter Contact Hours : ")
    CR = input("\nEnter Credits : ")
    
    f1.write(CT+'\t\t'+CC+'\t\t'+FI+'\t\t\t'+CH+'\t\t'+CR+'\n')
    
    choice = input("do you want to add more records (Y/N): ")
    
    if choice == 'N':
        print("\nEnd of input\n")
        break

f1.close()

# Cell 2:

print("Add a course")

f1 = open('file1.txt', 'a')

while 1:
    CT = input("\nEnter Course Title : ")
    CC = input("\nEnter Course Code  : ")
    FI = input("\nEnter Faculty Incharge : ")
    CH = input("\nEnter Contact Hours : ")
    CR = input("\nEnter Credits : ")
    
    f1.write(CT+'\t\t'+CC+'\t\t'+FI+'\t\t\t'+CH+'\t\t'+CR+'\n')
    
    print("Course added Successfully")
    
    choice = input("do you want to add more courses (Y/N): ")
    
    if choice == 'N':
        print("\nEnd of input\n")
        break

f1.close()

# Cell 3:

print("Delete a course with a given course code")

CC = input("\nEnter the Course Code to be deleted : ")

f1 = open('file1.txt', 'r')

lines = f1.readlines()

flag =1

new_lines = []

for line in lines[3:]:
    col = line.split('\t')
    if col[2] == CC:
        flag = 0
    else:
        new_lines.append(line)

f1.close()

f1 = open("file1.txt", "w")
f1.write('----------------------------------------------------------------------------------------------'+'\n')
f1.write('Course Title'+'\t'+'Course Code'+'\t'+'Faculty Incharge'+'\t'+'Contact Hours'+ '\t'+'Credits'+'\n')
f1.write('----------------------------------------------------------------------------------------------'+'\n')
f1.writelines(new_lines)
f1.close()

if flag:
    print('\nCourse code NOT found')
else:
    print('File contents after deleting reecord with given course code\n')
    f1 = open('file1.txt', 'r')
    print(f1.read())
    print('----------------------------------------------------------------------------------------------')
    f1.close()

#Cell 4:

print("List all courses of given credits")

CR = input("\nEnter the credits of course to be displayed : ")

f1 = open('file1.txt', 'r')

lines = f1.readlines()

flag = 1

new_lines = []

for line in lines[3:]:
    col = line.split('\t')
    if col[9].strip() == CR:
        flag = 0
        print(line)
    
f1.close()

if flag:
    print("\nNO Records found with given credits\n")

#Cell 5:

print("Search a course by name /faculty_incharge/ccode")

ch =int(input("\nchoose the Criteria to be searched\n 1: C_name \n 2: faculty_incharge \n 3: ccode "))

f1 = open('file1.txt', 'r')

lines = f1.readlines()

flag =1

if ch==1:
    CC= input("Enter the Course Name")
    new_lines = []
    for line in lines[3:]:
        col = line.split('\t')
        if col[0] == CC:
            flag = 0
            print(line)
        else:
            new_lines.append(line)
elif ch==2:
    CC= input("Enter the Faculty Incharge")
    new_lines = []
    for line in lines[3:]:
        col = line.split('\t')
        if col[4] == CC:
            flag = 0
            print(line)
        else:
            new_lines.append(line)
elif ch==3:
    CC= input("Enter the Course Code")
    new_lines = []
    for line in lines[3:]:
        col = line.split('\t')
        if col[2] == CC:
            flag = 0
            print(line)
        else:
            new_lines.append(line)
            
if flag:
    print("\nNO Records found with given credits\n")

f1.close()

#Cell 6:


print(" Read and disply the file contents")

f1 = open('file1.txt', 'r')
print(f1.read())
print('----------------------------------------------------------------------------------------------')

f1.close()
