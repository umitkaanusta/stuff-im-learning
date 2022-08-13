def get_primes_upto(n: int):
    # n between 2 and 1000
    primes = []
    limit = max(min(1000, n), 2)
    for num in range(2, limit + 1):
        # is prime?
        for divisor in range(num, int(num ** 0.5) + 1):
            if num != divisor and num % divisor == 0:
                break
        primes.append(num)
    return primes
