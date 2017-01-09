"""
Calculates the sum of the even terms in the Fibonacci series which are equal to or less than 4 million.
"""

def even_fib():
    previous_vals = [0, 1]
    current_val = sum(previous_vals)
    fib_sum = 0
    while current_val <= 4000000:
        if current_val % 2 == 0:
            fib_sum += current_val
        previous_vals[0] = previous_vals[1]
        previous_vals[1] = current_val
        current_val = sum(previous_vals)
    print fib_sum

if __name__ == '__main__':
    even_fib()
