from flow_shop_scheduler.pure_python.solution_explainer import SolutionExplainer

# using this problem for all functions testing "is_permutation_valid"
prob_is_permutation_valid = {
    "num_jobs": 2,
    "num_machines": 2,
    "initial_seed": ...,
    "upper_bound": ...,
    "lower_bound": ...,
    "processing_times": {"Job0": {"Task0": 1, "Task1": 2}, "Job1": {"Task0": 2, "Task1": 1}}
}


def test_is_permutation_valid_unique():
    test_pass = False
    # if unique, no assertion error
    try:
        _ = SolutionExplainer(prob_is_permutation_valid, solution=["Job1", "Job0"])
        test_pass = True
    except ValueError:
        ...
    assert test_pass


def test_is_permutation_valid_not_unique():
    test_pass = False
    # if not unique, assertion error
    try:
        _ = SolutionExplainer(prob_is_permutation_valid, solution=["Job1", "Job1"])
    except ValueError:
        test_pass = True
    assert test_pass


def test_is_permutation_valid_include_all_jobs_in_problem():
    test_pass = False
    # if sets equal, no assertion error
    try:
        _ = SolutionExplainer(prob_is_permutation_valid, solution=["Job1", "Job0"])
        test_pass = True
    except KeyError:
        ...
    assert test_pass


def test_is_permutation_valid_not_include_all_jobs_in_problem():
    test_pass = False
    # if sets equal, no assertion error
    try:
        _ = SolutionExplainer(prob_is_permutation_valid, solution=["Job1", "Job99"])
    except KeyError:
        test_pass = True
    assert test_pass
