from flow_shop_scheduler.pure_python.solution_explainer import SolutionExplainer

from pprint import pprint

# using this problem for all functions here
prob = {
    "num_jobs": 2,
    "num_machines": 2,
    "num_tasks": 2,
    "initial_seed": ...,
    "upper_bound": 99999,
    "lower_bound": 11111,
    "processing_times": {"Job0": {"Task0": 1, "Task1": 2}, "Job1": {"Task0": 2, "Task1": 1}}
}


def test_is_permutation_valid_unique():
    test_pass = False
    # if unique, no assertion error
    try:
        _ = SolutionExplainer(prob, solution=["Job1", "Job0"])
        test_pass = True
    except ValueError:
        ...
    assert test_pass


def test_is_permutation_valid_not_unique():
    test_pass = False
    # if not unique, assertion error
    try:
        _ = SolutionExplainer(prob, solution=["Job1", "Job1"])
    except ValueError:
        test_pass = True
    assert test_pass


def test_is_permutation_valid_include_all_jobs_in_problem():
    test_pass = False
    # if sets equal, no assertion error
    try:
        _ = SolutionExplainer(prob, solution=["Job1", "Job0"])
        test_pass = True
    except KeyError:
        ...
    assert test_pass


def test_is_permutation_valid_not_include_all_jobs_in_problem():
    test_pass = False
    # if sets equal, no assertion error
    try:
        _ = SolutionExplainer(prob, solution=["Job1", "Job99"])
    except KeyError:
        test_pass = True
    assert test_pass


def test_schedule_creation():
    exp = SolutionExplainer(prob, solution=["Job1", "Job0"])
    desired_schedule = {
        "Machine0": [{"job": "Job1", "task": "Task0", "start_time": 0, "processing_time": 2, "end_time": 2},
                     {"job": "Job0", "task": "Task0", "start_time": 2, "processing_time": 1, "end_time": 3}],
        "Machine1": [{"job": "Job1", "task": "Task1", "start_time": 2, "processing_time": 1, "end_time": 3},
                     {"job": "Job0", "task": "Task1", "start_time": 3, "processing_time": 2, "end_time": 5}]
    }
    schedule = exp.result["schedule"]
    assert schedule == desired_schedule


def test_performance_calculation():
    exp = SolutionExplainer(prob, solution=["Job1", "Job0"])
    desired_perf_dict = {
        "time_to_finish": 5,
        "benchmark_upper_bound": 99999,
        "benchmark_lower_bound": 11111
    }
    performance = exp.result["performance"]
    assert performance == desired_perf_dict


def test_job_idle_times_creation_optimal_case():
    exp = SolutionExplainer(prob, solution=["Job0", "Job1"])
    desired_job_idle_times = {
        "Job0": {"start_time": 0, "end_time": 3, "total_processing_time": 3, "idle_time": 0},
        "Job1": {"start_time": 1, "end_time": 4, "total_processing_time": 3, "idle_time": 1}
    }
    job_idle_times = exp.result["job_idle_times"]
    assert job_idle_times == desired_job_idle_times


def test_job_idle_times_creation_suboptimal_case():
    exp = SolutionExplainer(prob, solution=["Job1", "Job0"])
    desired_job_idle_times = {
        "Job0": {"start_time": 2, "end_time": 5, "total_processing_time": 3, "idle_time": 2},
        "Job1": {"start_time": 0, "end_time": 3, "total_processing_time": 3, "idle_time": 0}
    }
    job_idle_times = exp.result["job_idle_times"]
    assert job_idle_times == desired_job_idle_times


def test_machine_idle_times_creation_optimal_case():
    exp = SolutionExplainer(prob, solution=["Job0", "Job1"])
    desired_machine_idle_times = {
        "Machine0": {"start_time": 0, "end_time": 3, "total_processing_time": 3, "idle_time": 0},
        "Machine1": {"start_time": 1, "end_time": 4, "total_processing_time": 3, "idle_time": 1}
    }
    machine_idle_times = exp.result["machine_idle_times"]
    assert machine_idle_times == desired_machine_idle_times


def test_machine_idle_times_creation_suboptimal_case():
    exp = SolutionExplainer(prob, solution=["Job1", "Job0"])
    desired_machine_idle_times = {
        "Machine0": {"start_time": 0, "end_time": 3, "total_processing_time": 3, "idle_time": 0},
        "Machine1": {"start_time": 2, "end_time": 5, "total_processing_time": 3, "idle_time": 2}
    }
    machine_idle_times = exp.result["machine_idle_times"]
    assert machine_idle_times == desired_machine_idle_times
