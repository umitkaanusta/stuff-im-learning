from setuptools import sandbox

# run setup.py w/o command line

# simulating command python setup.py build_ext --inplace
sandbox.run_setup("setup.py", ["build_ext", "--inplace"])
