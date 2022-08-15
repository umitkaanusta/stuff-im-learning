from flow_shop_scheduler.pure_python.problem_definition import Problem, Solution


def test_build_processing_times():
    prob_dict = {
        "num_jobs": 2,
        "num_machines": 2,
        "initial_seed": ...,
        "upper_bound": ...,
        "lower_bound": ...,
        "processing_times": [[1, 2], [2, 1]]
    }
    prob = Problem(prob_dict)
    desired_processing_times = {
        "Job0": {"Task0": 1, "Task1": 2},
        "Job1": {"Task0": 2, "Task1": 1}
    }
    assert prob.processing_times == desired_processing_times


def test_permutation_unique():
    prob_dict = {
        "num_jobs": 2,
        "num_machines": 2,
        "initial_seed": ...,
        "upper_bound": ...,
        "lower_bound": ...,
        "processing_times": [[1, 2], [2, 1]]
    }
    prob = Problem(prob_dict)
    test_pass = False
    # if unique, no assertion error
    try:
        _ = Solution(prob, permutation=["Job1", "Job0"])
        test_pass = True
    except ValueError:
        ...
    assert test_pass


def test_permutation_not_unique():
    prob_dict = {
        "num_jobs": 2,
        "num_machines": 2,
        "initial_seed": ...,
        "upper_bound": ...,
        "lower_bound": ...,
        "processing_times": [[1, 2], [2, 1]]
    }
    prob = Problem(prob_dict)
    test_pass = False
    # if not unique, assertion error
    try:
        _ = Solution(prob, permutation=["Job1", "Job1"])
    except ValueError:
        test_pass = True
    assert test_pass


def test_permutation_set_include_all_jobs_in_problem():
    prob_dict = {
        "num_jobs": 2,
        "num_machines": 2,
        "initial_seed": ...,
        "upper_bound": ...,
        "lower_bound": ...,
        "processing_times": [[1, 2], [2, 1]]
    }
    prob = Problem(prob_dict)
    test_pass = False
    # if sets equal, no assertion error
    try:
        _ = Solution(prob, permutation=["Job1", "Job0"])
        test_pass = True
    except KeyError:
        ...
    assert test_pass


def test_permutation_set_not_include_all_jobs_in_problem():
    prob_dict = {
        "num_jobs": 2,
        "num_machines": 2,
        "initial_seed": ...,
        "upper_bound": ...,
        "lower_bound": ...,
        "processing_times": [[1, 2], [2, 1]]
    }
    prob = Problem(prob_dict)
    test_pass = False
    # if sets equal, no assertion error
    try:
        _ = Solution(prob, permutation=["Job1", "Job99"])
    except KeyError:
        test_pass = True
    assert test_pass
