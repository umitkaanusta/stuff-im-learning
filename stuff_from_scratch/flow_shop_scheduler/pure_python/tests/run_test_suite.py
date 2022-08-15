from flow_shop_scheduler.pure_python.tests import test_problem_definition

from typing import Callable

TEST_SUITE = [
    test_problem_definition.test_build_processing_times,
    test_problem_definition.test_permutation_unique,
    test_problem_definition.test_permutation_not_unique,
    test_problem_definition.test_permutation_set_include_all_jobs_in_problem,
    test_problem_definition.test_permutation_set_not_include_all_jobs_in_problem
]


def run_test_func(testfunc: Callable):
    try:
        testfunc()
        return "Pass"
    except AssertionError:
        return "FAIL"


def run_test_suite():
    num_pass = 0
    num_fail = 0
    print("Running test suite:")
    for idx, testfunc in enumerate(TEST_SUITE):
        status = run_test_func(testfunc)
        print(f"Test {idx + 1}/{len(TEST_SUITE)} [{status}] - {testfunc.__name__}")
        if status == "Pass":
            num_pass += 1
        else:
            num_fail += 1
    print(f"Pass: {num_pass}/{len(TEST_SUITE)} FAIL: {num_fail}/{len(TEST_SUITE)}")


if __name__ == '__main__':
    run_test_suite()
