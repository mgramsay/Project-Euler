"""
Calculates the sum of all of the multiples of 3 and 5 below 1000
"""

def sum_multiples():
    max_range = 1000
    sum_mults = 0
    for imult in xrange(max_range):
        if imult % 3 == 0 or imult % 5 == 0:
            sum_mults += imult
    print sum_mults

if __name__ == '__main__':
    sum_multiples()
