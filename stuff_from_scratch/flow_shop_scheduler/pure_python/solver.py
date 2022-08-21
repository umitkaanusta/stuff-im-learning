"""
Logic on solving the flow shop scheduling problem

We will need two things to build a solver:
1) Neighborhood: Search space of possible solutions
2) Heuristic: Method of selecting a solution from the list of possible solutions (candidates)
"""
from flow_shop_scheduler.pure_python.solution_explainer import SolutionExplainer
from collections import namedtuple
from itertools import combinations, permutations, product
from functools import partial
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

    def __init__(self, problem: dict, num_iterations_limit=200):
        """
        :param problem: Problem in the dict format.
            Find examples in benchmark.json or tests/test_solution_explainer.py
        :param num_iterations_limit: When to decide the problem is "adequately solved"
        """
        self.problem = problem
        self.initial_solution = list(self.problem["processing_times"].keys())
        self.randomizer = random.Random(self.problem["initial_seed"])

        self.lns_max_num_subsets = 1000

        self.strategies = {}
        self.num_iterations = 0
        self.num_iterations_limit = num_iterations_limit

    def _neighborhood_remove_duplicate_permutations(self, neighborhood):
        neigh_dups_removed = list(set(tuple(perm) for perm in neighborhood))
        neigh_dups_removed = [list(perm_tuple) for perm_tuple in neigh_dups_removed]
        return neigh_dups_removed

    def neighborhood_random(self, max_num_permutations=120):
        """
        :param max_num_permutations: Number of permutations in the neighborhood
        :return: A list of possible permutations created by random.shuffle.
            Duplicates are removed.
        """
        num_perm = (max_num_permutations if self.problem["num_jobs"] >= 5
                    else math.factorial(self.problem["num_jobs"]))
        neighborhood = [self.initial_solution]
        for i in range(num_perm):
            candidate = self.initial_solution[:]  # copy list
            self.randomizer.shuffle(candidate)
            neighborhood.append(candidate)
        neighborhood = self._neighborhood_remove_duplicate_permutations(neighborhood)
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
        neighborhood = self._neighborhood_remove_duplicate_permutations(neighborhood)
        return neighborhood

    def neighborhood_swap_idle(self, top_k_idle_jobs=4):
        neighborhood = [self.initial_solution]
        exp = SolutionExplainer(self.problem, self.initial_solution)
        job_idle_times = exp.result["job_idle_times"]
        top_idle_jobs = sorted(job_idle_times,
                               key=lambda item: job_idle_times[item]["idle_time"],
                               reverse=True)[:top_k_idle_jobs]
        indices_top_idle_jobs = [self.initial_solution.index(job) for job in top_idle_jobs]
        for indices in permutations(indices_top_idle_jobs):
            candidate = self.initial_solution[:]
            for i in range(len(indices)):
                candidate[indices_top_idle_jobs[i]] = self.initial_solution[indices[i]]
            neighborhood.append(candidate)
        neighborhood = self._neighborhood_remove_duplicate_permutations(neighborhood)
        return neighborhood

    def neighborhood_large_neigh_search(self, subset_size=4):
        neighborhood = [self.initial_solution]
        subset_indices = list(combinations(range(len(self.initial_solution)), subset_size))
        self.randomizer.shuffle(subset_indices)
        # get best perm in each subset
        for subset in subset_indices[:self.lns_max_num_subsets]:
            exp_init = SolutionExplainer(self.problem, self.initial_solution)
            best_time = exp_init.result["performance"]["time_to_finish"]
            best_perm = self.initial_solution
            for indices in permutations(subset):
                candidate = self.initial_solution[:]
                for i in range(len(indices)):
                    candidate[subset[i]] = self.initial_solution[indices[i]]
                exp_curr = SolutionExplainer(self.problem, candidate)
                curr_time = exp_curr.result["performance"]["time_to_finish"]
                if curr_time < best_time:
                    best_perm = candidate
            neighborhood.append(best_perm)
        neighborhood = self._neighborhood_remove_duplicate_permutations(neighborhood)
        return neighborhood

    def heuristic_random_selection(self, candidates):
        return self.randomizer.choice(candidates)

    def heuristic_hill_climbing(self, candidates):
        cand_perf = {tuple(perm): SolutionExplainer(self.problem, perm).result["performance"]["time_to_finish"]
                     for perm in candidates}
        cand_sorted = sorted(cand_perf.keys(), key=lambda item: cand_perf[item])
        solution = list(cand_sorted[0])
        return solution

    def heuristic_random_hill_climbing(self, candidates):
        cand_perf = {tuple(perm): SolutionExplainer(self.problem, perm).result["performance"]["time_to_finish"]
                     for perm in candidates}
        cand_sorted = sorted(cand_perf.keys(), key=lambda item: cand_perf[item])
        soln_index = 0
        # at each step, 50% chance of going to next best solution, 50% chance of accepting current one
        while self.randomizer.random() < 0.5 and soln_index < len(cand_sorted) - 1:
            soln_index += 1
        solution = list(cand_sorted[soln_index])
        return solution

    def build_strategies(self):
        neighbourhoods = [
            # partialmethod helps freeze some parameter choices
            ('Random Permutation', partial(self.neighborhood_random, max_num_permutations=100)),
            ('Swap Pairs', self.neighborhood_swap_pairs),
            ('Swap Idle (3)', partial(self.neighborhood_swap_idle, top_k_idle_jobs=3)),
            ('Swap Idle (4)', partial(self.neighborhood_swap_idle, top_k_idle_jobs=4)),
            ('Swap Idle (5)', partial(self.neighborhood_swap_idle, top_k_idle_jobs=5)),
            ('Large Neighborhood Search (2)', partial(self.neighborhood_large_neigh_search, subset_size=2)),
            ('Large Neighborhood Search (3)', partial(self.neighborhood_large_neigh_search, subset_size=3))
        ]
        heuristics = [
            ("Random Selection", self.heuristic_random_selection),
            ("Hill Climbing", self.heuristic_hill_climbing),
            ("Random Hill Climbing", self.heuristic_random_hill_climbing)
        ]
        # combine these two, build strategies
        for (neigh, heur) in product(neighbourhoods, heuristics):
            strat = Strategy(f"{neigh[0]} & {heur[0]}", neigh[1], heur[1])
            self.strategies[strat] = {"improvement": 0, "weight": 1, "usage": 0}

    def pick_strategy(self):
        weights = [self.strategies[strat]["weight"] for strat in self.strategies]
        strat = self.randomizer.choices(list(self.strategies.keys()), weights=weights, k=1)[0]
        return strat

    def solve(self):
        self.build_strategies()  # initialize strategies
        best_soln = self.initial_solution
        best_res = SolutionExplainer(self.problem, best_soln).result["performance"]["time_to_finish"]
        while self.num_iterations < self.num_iterations_limit:
            # pick strategy and solve
            strategy = self.pick_strategy()
            candidates = strategy.neighborhood()
            solution = strategy.heuristic(candidates)
            res = SolutionExplainer(self.problem, solution).result["performance"]["time_to_finish"]
            # record that strat's results
            self.strategies[strategy]["improvement"] += best_res - res  # 200 if best_res = 400 and res = 200
            self.strategies[strategy]["usage"] += 1
            # print status
            print(f"Iteration: {self.num_iterations} - Strategy: {strategy.name} - "
                  f"Current time to finish: {res} - Best: {best_res}")
            # if strat better than the best so far, update
            if res < best_res:
                best_res = res
                best_soln = solution[:]
            # at each 100 iteration, switch strategy weights,
            # dynamically shifting to recently more effective strategies.
            if self.num_iterations > 0 and self.num_iterations % 100 == 0:
                strat_sorted_by_improvement = sorted(self.strategies.keys(),
                                                     key=lambda item: self.strategies[item]["improvement"],
                                                     reverse=True)
                # boost weight for successful strategies
                for idx, strat in enumerate(strat_sorted_by_improvement):
                    self.strategies[strat]["weight"] += len(self.strategies) - idx
                    # to avoid starvation, additional boost for unused strategies
                    if self.strategies[strat]["usage"] == 0:
                        self.strategies[strat]["weight"] += len(self.strategies)
                # reset improvements and usage
                for strat in self.strategies:
                    self.strategies[strat]["improvement"] = 0
                    self.strategies[strat]["usage"] = 0
            # rinse and repeat
            self.num_iterations += 1
        print(f"Solution: {best_soln}")
        print(f"Time to completion: {best_res}")
        return best_soln
