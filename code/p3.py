# Problem 3: Largest Prime Factor
# What is the largest prime factor of the number 600,851,475,143?
# Author: Subhadeep Pal Date: 7/10/2026

# first generate prime numbers
def isPrime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag


# Load prime numbers upto 10000 from the text file prime_numbers.txt
file = open("prime_numbers.txt", "r")
prime_numbers_str = file.read().split("\n")
prime_numbers = list(map(int, prime_numbers_str[:-1]))
file.close()

num = 600851475143
prime_factors = []
# divide the number with primes to find the prime factors
for prime in prime_numbers:
    if num % prime == 0:
        num = num / prime
        prime_factors.append(prime)
        print(f"Prime factor = {prime}")