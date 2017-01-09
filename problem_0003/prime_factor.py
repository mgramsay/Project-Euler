"""
Calculates the largest prime factor of a number
"""

import math

class Prime_list(object):
    """
    List of prime numbers
    """
    def __init__(self, max_prime):
        self.prime_list = [2, 3]
        if max_prime > 3:
            while self.prime_list[-1] < max_prime:
                self.get_next_prime()

    def get_next_prime(self):
        current_val = self.prime_list[-1]
        while True:
            current_val += 2
            is_prime = self.test_prime(current_val)
            if is_prime:
                self.prime_list.append(current_val)
                return current_val

    def test_prime(self, test_val):
        for prime in self.prime_list:
            if test_val % prime == 0:
                return False
        return True

def largest_prime_factor(in_val=600851475143):
    max_factor = math.sqrt(in_val)
    prime_list = Prime_list(max_factor)
    for prime in prime_list.prime_list:
        if in_val % prime == 0:
            print prime
            last_prime_factor = prime
    print last_prime_factor

if __name__ == '__main__':
    largest_prime_factor()
