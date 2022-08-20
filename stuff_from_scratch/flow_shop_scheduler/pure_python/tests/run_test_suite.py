from flow_shop_scheduler.pure_python.tests import test_solution_explainer

from typing import Callable

TEST_SUITE = [
    test_solution_explainer.test_is_permutation_valid_unique,
    test_solution_explainer.test_is_permutation_valid_not_unique,
    test_solution_explainer.test_is_permutation_valid_include_all_jobs_in_problem,
    test_solution_explainer.test_is_permutation_valid_not_include_all_jobs_in_problem,
    test_solution_explainer.test_schedule_creation,
    test_solution_explainer.test_performance_calculation,
    test_solution_explainer.test_job_idle_times_creation_optimal_case,
    test_solution_explainer.test_job_idle_times_creation_suboptimal_case,
    test_solution_explainer.test_machine_idle_times_creation_optimal_case,
    test_solution_explainer.test_machine_idle_times_creation_suboptimal_case
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
