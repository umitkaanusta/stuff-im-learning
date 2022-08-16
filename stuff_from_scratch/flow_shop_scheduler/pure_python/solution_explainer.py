"""
Logic on formulating this problem to our solver
"""


class SolutionExplainer:
    def __init__(self, problem: dict, solution: list):
        """
        :param problem: Problem in the dict format.
            Find examples in benchmark.json or tests/test_solution_explainer.py
        :param solution: List of job ids - a permutation of the jobs in the problem.
            Id format must be consistent with problem dicts
        """
        self.problem = problem
        self.solution = solution
        self._is_permutation_valid()

    def _is_permutation_valid(self):
        """
        Validating basic properties of a proposed solution before explaining it
        """
        # job ids in permutation should be unique
        if len(self.solution) != len(set(self.solution)):
            raise ValueError("Job ids in the permutation must be unique")
        # jobs in "problem" set and "solution" set should be equal
        if set(self.solution) != set(list(self.problem["processing_times"].keys())):
            raise KeyError("Permutation must include only the jobs given in problem")

    @property
    def result(self) -> dict:
        # in a dict show: 1) total time taken and benchmark upper/lower bounds, 2) visualized schedule
        res = {"performance": ..., "schedule": ...}
        return res
