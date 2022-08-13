# distutils: language = c++
# first line is a compiler directive.
# same function, in cython, using cpp

DEF UPPER_LIMIT = 1000
DEF LOWER_LIMIT = 2

from libcpp.vector cimport vector

cpdef list get_primes_upto_faster(unsigned int n):
    # n between 2 and 1000
    cdef int limit, num  # declare upper and lower limits
    cdef int primes_idx  # current idx of primes list
    cdef int divisor  # will be used in is prime test
    cdef int divisor_max  # will be used in is prime test. it's the sqrt of the current number
    # defining and allocating memory for our vector
    cdef vector[int] primes
    limit = max(min(UPPER_LIMIT, n), LOWER_LIMIT)
    primes.reserve(limit)
    for num in range(2, limit + 1):
        # is prime?
        divisor_max = int(num ** 0.5)
        for divisor in range(num, divisor_max + 1):
            if num != divisor and num % divisor == 0:
                break
        # if prime, append to primes list
        primes.push_back(num)
    # vectors are automatically converted to python lists
    return primes