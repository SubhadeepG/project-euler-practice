# Problem 4: Largest Palindrome Product
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_num_palindrome(num):
    num_str = str(num)
    num_str_rev = num_str[::-1]
    return num_str == num_str_rev



highest_product = 100 * 101

for a in range(500, 999):
    for b in range(501, 999):
        product = a * b
        if is_num_palindrome(product):
            if product > highest_product:
                highest_product = product
                print(f"{product} is a palindrome")

print(f"The largest palindrome is: {highest_product}")
