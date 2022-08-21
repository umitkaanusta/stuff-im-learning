"""
Logic on solving the flow shop scheduling problem

We will need two things to build a solver:
1) Neighborhood: Search space of possible solutions
2) Heuristic: Method of selecting a solution from the list of possible solutions (candidates)
"""
from flow_shop_scheduler.pure_python.solution_explainer import SolutionExplainer
from collections import namedtuple
from itertools import combinations
import random
import math

"""
A strategy is a combination of a neighborhood and a heuristic.
"""
Strategy = namedtuple("Strategy", ["name", "neighborhood", "heuristic"])


class DynamicStrategySolver:
    """
    Dynamic strategy solver is able to change strategies while solving the problem.

    How it changes strategies
    -------------------------
    Roulette wheel selection. We randomly select from the list of strategies,
    assigning the probabilities based on past performance of strategies.

    Neighborhood creation
    ---------------------
    - Random permutation: Randomly create a given number of possible permutations
    - Swapped pairs: Starting from an initial permutation, create permutations by swapping
    randomly chosen pairs in the initial permutation.
    - Swap idle pairs: Starting from an initial permutation, randomly swap top k jobs in terms
    of job idle time. (Suggested k <= 4)
    - Large neighborhood search (LNS): Starting from an initial permutation, locates best permutation
    of the subset of jobs. By repeating this for subsets of a particular size, we can increase
    the number of candidates in the neighborhood. (Suggested subset size <= 4)

    Selection heuristics
    --------------------
    - Random selection: Randomly selects a candidate in the neighborhood
    - Hill climbing: Selects the permutation with the best time to completion
    - Random hill climbing: Sort permutations based on their time to completion.
    At each step, with 50% chance, move on considering the next best solution.
    This way, we're able to smoothen our greedy heuristic.
    """
    def __init__(self, problem: dict):
        """
        :param problem: Problem in the dict format.
            Find examples in benchmark.json or tests/test_solution_explainer.py
        """
        self.problem = problem
        self.initial_solution = list(self.problem["processing_times"].keys())
        self.randomizer = random.Random(self.problem["initial_seed"])
        self.strategies = None

    def neighborhood_random(self, num_permutations=120):
        """
        :param num_permutations: Number of permutations in the neighborhood
        :return: A list of possible permutations created by random.shuffle
        """
        num_perm = (num_permutations if self.problem["num_jobs"] >= 5
                    else math.factorial(self.problem["num_jobs"]))
        neighborhood = [self.initial_solution]
        for i in range(num_perm):
            candidate = self.initial_solution[:]  # copy list
            self.randomizer.shuffle(candidate)
            neighborhood.append(candidate)
        return neighborhood

    def neighborhood_swap_pairs(self):
        """
        :return: List of possible permutations created by swapping every pair of the initial soln
        """
        neighborhood = [self.initial_solution]
        for pair_indices in combinations(range(len(self.initial_solution)), 2):
            i, j = pair_indices
            candidate = self.initial_solution[:]
            candidate[i], candidate[j] = candidate[j], candidate[i]  # swap pairs
            neighborhood.append(candidate)
        return neighborhood

    def neighborhood_swap_idle_pairs(self, top_k_idle_jobs=4):
        neighborhood = [self.initial_solution]
        exp = SolutionExplainer(self.problem, self.initial_solution)
        job_idle_times = exp.result["job_idle_times"]
        top_idle_jobs = sorted(job_idle_times,
                               key=lambda item: job_idle_times[item]["idle_time"],
                               reverse=True)[:top_k_idle_jobs]
        indices_top_idle_jobs = [self.initial_solution.index(job) for job in top_idle_jobs]
        for pair_indices in combinations(indices_top_idle_jobs, 2):
            i, j = pair_indices
            candidate = self.initial_solution[:]
            candidate[i], candidate[j] = candidate[j], candidate[i]  # swap pairs
            neighborhood.append(candidate)
        return neighborhood

    def neighborhood_large_neigh_search(self, subset_size=4):
        raise NotImplementedError

    def heuristic_random_selection(self):
        raise NotImplementedError

    def heuristic_hill_climbing(self):
        raise NotImplementedError

    def heuristic_random_hill_climbing(self):
        raise NotImplementedError
