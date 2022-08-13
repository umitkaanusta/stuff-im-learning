from basic_tutorial.hello_world_app.helloworld import print_hello_world
from basic_tutorial.hello_world_app.primes_pure import get_primes_upto
from basic_tutorial.hello_world_app.primes import get_primes_upto_fast
from basic_tutorial.hello_world_app.primes_faster import get_primes_upto_faster

from timeit import timeit

if __name__ == '__main__':
    # Run hello world in both pure python and cython
    print("Hello world")
    print_hello_world()
    # it works, seems like we can get things done in cython.

    # 'get_primes_upto' in pure python and cython
    # Test run
    primes_py = get_primes_upto(1000)
    primes_cy = get_primes_upto_fast(1000)
    primes_cpp = get_primes_upto_faster(1000)
    print(primes_py)
    print(primes_cy)
    print(primes_cpp)
    assert primes_py == primes_cy == primes_cpp
    # Runtime comparison w/ timeit
    runtime_primes_py = timeit("get_primes_upto(1000)",
           setup="from basic_tutorial.hello_world_app.primes_pure import get_primes_upto",
           number=1000)
    runtime_primes_cy = timeit("get_primes_upto_fast(1000)",
           setup="from basic_tutorial.hello_world_app.primes import get_primes_upto_fast",
           number=1000)
    runtime_primes_cpp = timeit("get_primes_upto_faster(1000)",
           setup="from basic_tutorial.hello_world_app.primes_faster import get_primes_upto_faster",
           number=1000)
    print(f"primes_py: {runtime_primes_py} - primes_cy: {runtime_primes_cy} - primes_cpp: {runtime_primes_cpp}")
