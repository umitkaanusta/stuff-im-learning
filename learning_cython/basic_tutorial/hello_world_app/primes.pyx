# pure python implementation
# --------------------------------------------------------
# def get_primes_upto(n: int):
#     # n between 2 and 1000
#     primes = []
#     limit = max(min(1000, n), 2)
#     for num in range(2, limit + 1):
#         # is prime?
#         for divisor in range(num, int(num ** 0.5) + 1):
#             if num != divisor and num % divisor == 0:
#                 break
#         primes.append(num)
#     return primes
# --------------------------------------------------------

DEF UPPER_LIMIT = 1000
DEF LOWER_LIMIT = 2

cpdef list get_primes_upto_fast(unsigned int n):
    # n between 2 and 1000
    cdef int limit, num  # declare upper and lower limits
    cdef int primes_idx  # current idx of primes list
    cdef int divisor  # will be used in is prime test
    cdef int divisor_max  # will be used in is prime test. it's the sqrt of the current number
    cdef int primes[UPPER_LIMIT]
    primes_idx = 0
    limit = max(min(UPPER_LIMIT, n), LOWER_LIMIT)
    for num in range(2, limit + 1):  # cython recognizes and optimizes python for loops
        # is prime?
        divisor_max = int(num ** 0.5)
        for divisor in range(num, divisor_max + 1):
            if num != divisor and num % divisor == 0:
                break
        # if prime, append to primes list
        primes[primes_idx] = num
        primes_idx += 1
    # convert int array primes to python list
    primes_as_py_list = [prime for prime in primes[:primes_idx]]
    return primes_as_py_list
