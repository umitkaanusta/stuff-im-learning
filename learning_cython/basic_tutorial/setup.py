from distutils.extension import Extension
from distutils.core import setup

# Note: we can compile both .py and .pyx files. So we can compile pure python w/ Cython as well.

# first we should check if the user has Cython.
# having Cython is optional, only the contributors need to have it.
# others can just rely on the compiled code.
try:
    from Cython.Build import cythonize
except ImportError:
    USE_CYTHON = False
else:
    USE_CYTHON = True

# now specifying our package(s)
SRC_DIR = "hello_world_app"
PACKAGES = [SRC_DIR]

# using .pyx or .c based on having cython istalled
file_ext = ".pyx" if USE_CYTHON else ".c"
extensions = [
    Extension(SRC_DIR + ".helloworld", [SRC_DIR + "/helloworld" + file_ext]),
    Extension(SRC_DIR + ".primes", [SRC_DIR + "/primes" + file_ext]),
    Extension(SRC_DIR + ".primes_faster", [SRC_DIR + "/primes_faster" + file_ext])
]
if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions, language_level="3")

setup(
    name="first_cython_app",
    packages=PACKAGES,
    ext_modules=extensions,
)
