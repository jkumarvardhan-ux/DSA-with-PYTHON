'''functions
1. arg pass return value
2. arg pass no return value
3.no arg return value
4.no arg no return'''

# args pass return value
def summate(a,b):
    return a+b
num1 = int(input("enter a first value:"))
num2 = int(input("enter a second value:"))
result = summate(num1,num2)
print("Sum:", result)

# args pass no return value
def summate(n1,n2):
    print("Sum:",n1+n2)
n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
summate(n1,n2)

# no args pass return value

def summate():
    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))
    return n1+n2
result=summate()
print("Sum:",result)

# no args pass no return value
def summate():
    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))
    print("Sum:",n1+n2)
summate()

'''RECURSIONS(base , recursion)
1. Direct
2. Indirect
3. Tail
4. Head --Backtracking
5. Tree
6. Nested --Backtracking'''

#1.Direct Recursion
#code to print n natural numberes using Direct Recursion
def numbers(n):
    if n==0:
        return
    print(n,end=" ")
    numbers(n-1)
n= int(input("Enter a number:"))
numbers(n)

#2.Indirect recursion
#code to check the given number is even or odd using In-Direct Recursion
def even(n):
    if n==0:
        print("Even")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print("Odd")
        return
    even(n-1)
n= int(input("Enter a number:"))
even(n)


#4.Tree Recursion - fibonacci number
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

n = int(input("Enter a number:"))
print("fibonacci",fib(n))













