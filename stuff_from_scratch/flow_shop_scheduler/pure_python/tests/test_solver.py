from flow_shop_scheduler.pure_python.solver import DynamicStrategySolver
from flow_shop_scheduler.pure_python.solution_explainer import SolutionExplainer

from pprint import pprint
import json

# using this problem for all kinds of functions here
prob = {
    "num_jobs": 4,
    "num_machines": 2,
    "num_tasks": 2,
    "initial_seed": 42,
    "upper_bound": 99999,
    "lower_bound": 11111,
    "processing_times": {
        "Job0": {"Task0": 1, "Task1": 200},
        "Job1": {"Task0": 20, "Task1": 10},
        "Job2": {"Task0": 150, "Task1": 2},
        "Job3": {"Task0": 65, "Task1": 35}
    }
}


def test_neighborhood_random():
    dss = DynamicStrategySolver(prob)
    neigh = dss.neighborhood_random()
    # all shuffled solutions are valid
    assert all(SolutionExplainer(prob, perm) for perm in neigh)


def test_neighborhood_swap_pairs():
    dss = DynamicStrategySolver(prob)
    neigh = dss.neighborhood_swap_pairs()
    desired_neigh = [
        ["Job0", "Job1", "Job2", "Job3"], ["Job1", "Job0", "Job2", "Job3"],
        ["Job2", "Job1", "Job0", "Job3"], ["Job3", "Job1", "Job2", "Job0"],
        ["Job0", "Job2", "Job1", "Job3"], ["Job0", "Job3", "Job2", "Job1"],
        ["Job0", "Job1", "Job3", "Job2"]
    ]
    # order not guaranteed. use set equality
    assert all(perm in neigh for perm in desired_neigh)
    assert all(perm in desired_neigh for perm in neigh)


def test_neighborhood_swap_idle():
    # top 3 idle jobs: Job1, Job3
    dss = DynamicStrategySolver(prob)
    neigh = dss.neighborhood_swap_idle(top_k_idle_jobs=2)
    desired_neigh = [
        ["Job0", "Job1", "Job2", "Job3"], ["Job0", "Job3", "Job2", "Job1"]
    ]
    assert all(perm in neigh for perm in desired_neigh)
    assert all(perm in desired_neigh for perm in neigh)


def test_neighborhood_large_neigh_search():
    # subsets: [(Job0, Job1, Job2), (Job0, Job1, Job3), (Job0, Job2, Job3), (Job1, Job2, Job3)]
    dss = DynamicStrategySolver(prob)
    neigh = dss.neighborhood_large_neigh_search(subset_size=3)
    desired_neigh = [
        ["Job0", "Job1", "Job3", "Job2"], ["Job0", "Job3", "Job2", "Job1"],
        ["Job0", "Job1", "Job2", "Job3"],
    ]
    # since there's random shuffle - we check equality with set equality
    assert all(perm in neigh for perm in desired_neigh)
    assert all(perm in desired_neigh for perm in neigh)


def test_heuristic_random_selection():
    dss = DynamicStrategySolver(prob)
    candidates = [["Job0", "Job1", "Job2", "Job3"], ["Job3", "Job2", "Job1", "Job0"]]
    solution = dss.heuristic_random_selection(candidates)
    assert SolutionExplainer(prob, solution)  # solution is valid
    assert solution in candidates


def test_heuristic_hill_climbing():
    dss = DynamicStrategySolver(prob)
    candidates = [["Job0", "Job1", "Job2", "Job3"], ["Job3", "Job2", "Job1", "Job0"]]
    solution = dss.heuristic_hill_climbing(candidates)
    desired_solution = ["Job0", "Job1", "Job2", "Job3"]  # time to finish = 271. it's 445 for the other one
    assert solution == desired_solution


def test_heuristic_random_hill_climbing():
    dss = DynamicStrategySolver(prob)
    candidates = [["Job0", "Job1", "Job2", "Job3"], ["Job3", "Job2", "Job1", "Job0"]]
    solution = dss.heuristic_random_hill_climbing(candidates)
    assert SolutionExplainer(prob, solution)
    assert solution in candidates


def test_solve_real_problem():
    real_problem = {
        "num_jobs": 20,
        "num_machines": 5,
        "num_tasks": 5,
        "initial_seed": 88325120,
        "upper_bound": 1108,
        "lower_bound": 1082,
        "processing_times": {
            "Job0": {"Task0": 27, "Task1": 79, "Task2": 22, "Task3": 93, "Task4": 38},
            "Job1": {"Task0": 92, "Task1": 23, "Task2": 93, "Task3": 22, "Task4": 84},
            "Job2": {"Task0": 75, "Task1": 66, "Task2": 62, "Task3": 64, "Task4": 62},
            "Job3": {"Task0": 94, "Task1": 5, "Task2": 53, "Task3": 81, "Task4": 10},
            "Job4": {"Task0": 18, "Task1": 15, "Task2": 30, "Task3": 94, "Task4": 11},
            "Job5": {"Task0": 41, "Task1": 51, "Task2": 34, "Task3": 97, "Task4": 93},
            "Job6": {"Task0": 37, "Task1": 2, "Task2": 27, "Task3": 54, "Task4": 57},
            "Job7": {"Task0": 58, "Task1": 81, "Task2": 30, "Task3": 82, "Task4": 81},
            "Job8": {"Task0": 56, "Task1": 12, "Task2": 54, "Task3": 11, "Task4": 10},
            "Job9": {"Task0": 20, "Task1": 40, "Task2": 77, "Task3": 91, "Task4": 40},
            "Job10": {"Task0": 2, "Task1": 59, "Task2": 24, "Task3": 23, "Task4": 62},
            "Job11": {"Task0": 39, "Task1": 32, "Task2": 47, "Task3": 32, "Task4": 49},
            "Job12": {"Task0": 91, "Task1": 16, "Task2": 39, "Task3": 26, "Task4": 90},
            "Job13": {"Task0": 81, "Task1": 87, "Task2": 66, "Task3": 22, "Task4": 34},
            "Job14": {"Task0": 33, "Task1": 78, "Task2": 41, "Task3": 12, "Task4": 11},
            "Job15": {"Task0": 14, "Task1": 41, "Task2": 46, "Task3": 23, "Task4": 81},
            "Job16": {"Task0": 88, "Task1": 43, "Task2": 24, "Task3": 34, "Task4": 51},
            "Job17": {"Task0": 22, "Task1": 94, "Task2": 23, "Task3": 87, "Task4": 21},
            "Job18": {"Task0": 36, "Task1": 1, "Task2": 68, "Task3": 59, "Task4": 39},
            "Job19": {"Task0": 65, "Task1": 93, "Task2": 50, "Task3": 2, "Task4": 27}
        }
    }
    dss = DynamicStrategySolver(real_problem)
    solution = dss.solve()
    exp = SolutionExplainer(real_problem, solution)
    print(exp.result)
    assert True
