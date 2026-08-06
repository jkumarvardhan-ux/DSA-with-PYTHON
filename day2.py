#1D Data structure
n=int(input("Enter a value: "))
for i in range(n):
    print(i, end=' ')
    
#2D Data structure
n=int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        print(i,j,end=' ')
    print()

#Hollow square
n=int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or (i+j)=n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()


#Hour glass(note: n= even number)

n=int(input("Enter a value: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or (i+j)==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    


#butterfly
n=int(input("Enter a value:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or (i+j)==n-1:
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print()

#plus
n=int(input("Enter a value:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print()

#left increasing triangle
n=int(input("Enter a value:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j: 
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print()

#right increasing triangle
n=int(input("Enter a value:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i+j)==n-1:
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print()

# 2D Data Structure("*") pyramid
n=int(input("Enter a value:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for j in range(2*i-1):
        if i ==n or j==0 or j==2*i-2:
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print()


# 2D Data Structure("*") reverse pyramid

n=int(input("Enter a value:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=' ')
    for j in range(2*i-1):
        if i ==n or i== 1 or j==0 or j==2*i-2:
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print()

# dimond
n=int(input("Enter a value:"))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end=' ' )
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ", end=' ' )
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*", end=' ')
        else:
            print(' ',end=' ')
    print()