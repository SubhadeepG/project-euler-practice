# Problem 2: Even Fibonacci Numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
# Author: Subhadeep Pal Date: 6/10/2026

a = 1
b = 2
c = 3
sum = 2
while c < 4000000:
    c = a + b
    if c % 2 == 0:
        sum = sum + c
    a = b
    b = c
    print(c)

print(f"Sum = {sum}")