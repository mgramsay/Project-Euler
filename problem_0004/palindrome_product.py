"""
Calculates the largest palindrome resulting from the product of two 3-digit
numbers.
"""

def check_palindrome(instring):
    for ichar in xrange(len(instring) // 2):
        if instring[ichar] != instring[-(ichar+1)]:
            return False
    return True

def largest_palindrome_product(n_digits=2):
    i = 10**(n_digits-1)
    while i < 10**n_digits:
        j = i + 1
        while j < 10**n_digits:
            prod = str(i * j)
            is_palindrome = check_palindrome(prod)
            if is_palindrome:
                largest_palindrome = prod
            j += 1
        i += 1
    print largest_palindrome

if __name__ == '__main__':
    largest_palindrome_product(n_digits=3)
