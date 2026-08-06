# write a code to print the sum of a given number .
n= int(input("enter a number : "))
sum = 0
while n!=0:
    d= n%10
    sum+=d
    n//=10
print("Sum of digits ", sum)


#write a code to print reverse of a given number .
n= int(input("enter a number : "))
rev=0
while n>0:
    d= n%10
    rev= rev*10+d
    n//=10
print("reverse number",rev)


#write a code to print the count of even digits and odd digits of a given number .
num= int(input("enter a number: "))
even=0
odd=0
while num!=0:
    d= num%10
    if d%2==0:
        even+=1
    else:
        odd+=1
    num//=10
print("even count",even)
print("odd count",odd)


#tom-riddle anagram
#anagram
#write a code to check whether the given 2 strings are sorted are not
# Anagram Program

str1 = input()
str2 = input()

# Remove spaces and convert to lowercase
s1 = sorted(str1.replace(" ", "").lower())
s2 = sorted(str2.replace(" ", "").lower())

if s1 == s2:
    print("Anagram")
else:
    print("Not Anagram")

    