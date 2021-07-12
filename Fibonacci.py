#Write a program to print the fibonacci series
terms = int(input("Enter number of terms: "))

n1, n2 = 0, 1
count = 0
#Checking the validity of the number of terms
if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)
# generating fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(n1)
       nth = n1 + n2
       # update
       n1 = n2
       n2 = nth
       count= count+1
"""
Spyder Editor

This is a temporary script file.
"""

