from flow_shop_scheduler.pure_python.solver import DynamicStrategySolver
from flow_shop_scheduler.pure_python.solution_explainer import SolutionExplainer

from pprint import pprint

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
    assert len(neigh) == 24 + 1  # 4! + 1 (initial solution)
    # all shuffled solutions are valid
    assert all(SolutionExplainer(prob, perm) for perm in neigh)


def test_neighborhood_swap_pairs():
    dss = DynamicStrategySolver(prob)
    neigh = dss.neighborhood_swap_pairs()
    desired_neigh_swap_pairs = [
        ["Job0", "Job1", "Job2", "Job3"], ["Job1", "Job0", "Job2", "Job3"],
        ["Job2", "Job1", "Job0", "Job3"], ["Job3", "Job1", "Job2", "Job0"],
        ["Job0", "Job2", "Job1", "Job3"], ["Job0", "Job3", "Job2", "Job1"],
        ["Job0", "Job1", "Job3", "Job2"]
    ]
    assert neigh == desired_neigh_swap_pairs


def test_neighborhood_swap_idle_pairs():
    dss = DynamicStrategySolver(prob)
    neigh = dss.neighborhood_swap_idle_pairs(top_k_idle_jobs=3)
    desired_neigh_swap_idle_pairs = [
        ["Job0", "Job1", "Job2", "Job3"], ["Job0", "Job3", "Job2", "Job1"],
        ["Job0", "Job2", "Job1", "Job3"], ["Job0", "Job1", "Job3", "Job2"]
    ]
    assert neigh == desired_neigh_swap_idle_pairs
