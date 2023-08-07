# Cell 1:

print("addition, subtraction, multiplication of 2 matrices")

import numpy as np
#accept order of m1 at once
R1, C1 =input('\nEnter the order of the matrix-1 : ').split()

#define matrix of order mXn
M1 = np.zeros((int(R1),int(C1)),dtype='int32')

#read matrix
for i in range(0,int(R1)):
    print('\nEnter ', C1, 'elements in row ', i+1, 'separated by space : ')
    M1[i] = input().split()
    
#accept order of m2 at once
R2,C2=input('\nEnter the order of the matrix-2 : ').split()

#define matrix of order mXn
M2 = np.zeros((int(R2),int(C2)),dtype='int32')

#read matrix
for i in range(0,int(R2)):
    print('\nEnter ', C2, 'elements in row ', i+1, 'separated by space : ')
    M2[i]=input().split()

#display matrices    
print('---------------------------------------------------')
print('\nThe matrix1 is\n ', M1)
print('---------------------------------------------------')
print('nThe matrix2 is \n ', M2)

#Display sum of them

try:
    print('---------------------------------------------------')
    print('\nSum of matrices is \n ',M1 + M2)
    
    print('---------------------------------------------------')
    print('Differen of the matrices is \n ', M1 - M2)
except:
    print('---------------------------------------------------')
    print('\nEXCEPTION: Addition and subtraction of matrices is NOT possible as matrix order mismatch!!!!! \n ')

# Multiply the matrices
try:
    print('---------------------------------------------------')
    print('\nProduct of the matrices is :\n',np.matmul(M1, M2))
except:
    print('---------------------------------------------------')
    print('\nEXCEPTION: Matrix multiplication is NOT possible as C1 != R2!!!!! \n')

# Cell 2:

print("addition, subtraction, multiplication and division of a matrix with a given value.")
#display matrix    
print('---------------------------------------------------')
ch=int(input("Choose the matrix 1 or 2"))
if ch==1:
    M=M1
else:
    M=M2
print('---------------------------------------------------')

# Read an integer value
value = int(input("\nEnter an integer : "))
        
print('---------------------------------------------------')
print('\nSum of matrix and the given integer is \n ',M + value)
    
print('---------------------------------------------------')
print('\nDifference of matrix and the given integer is \n ',M - value)

print('---------------------------------------------------')
print('\nDifference of matrix and the given integer is \n ', M* value)

try:
    print('---------------------------------------------------')
    print('\nDivision of matrix and the given integer is \n ', M / value)
    print('---------------------------------------------------')
except:
    print('---------------------------------------------------')
    print("EXCEPTION : Divide by zero error!!!!!")
    print('---------------------------------------------------')

# Cell 3:

print("Finding sum of secondary diagonal elements and trace of the matrix ") 
print('---------------------------------------------------')
ch=int(input("Choose the matrix 1 or 2"))
if ch==1:
    M=M1
else:
    M=M2
print('---------------------------------------------------')


SD2 = 0
if R1 != C1:
    print("\nUser defined EXCEPTION: Matrix must be square to have the diagonal\n")
else:    
    for i in range(int(R1)):
        for j in range(int(C1)):
                if i+j == int(R1)-1:
                    SD2 = SD2 + M1[i][j]
    print('---------------------------------------------------')
    print("\nSum of secondary diagonal : ", SD2)
    print('---------------------------------------------------')

    print('----------------------------------------')
    print("\nSum of primary diagonal (Trace of the matrix) : ",np.trace(M))
    print('----------------------------------------')
    

