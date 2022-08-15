"""
Logic on formulating this problem to our solver
"""


class Problem:
    def __init__(self, problem_dict):
        self.num_jobs = problem_dict["num_jobs"]
        self.num_machines = problem_dict["num_machines"]
        self.num_tasks = self.num_machines
        self.initial_seed = problem_dict["initial_seed"]
        self.upper_bound = problem_dict["upper_bound"]
        self.lower_bound = problem_dict["lower_bound"]
        self._processing_times_raw = problem_dict["processing_times"]
        self.processing_times = self._build_processing_times()

    def _build_processing_times(self):
        """
        Assigns zero-indexed IDs to jobs and tasks for explainability of problem solutions
        """
        processing_times = {}
        for j in range(self.num_jobs):
            processing_times[f"Job{j}"] = {}
            for t in range(self.num_tasks):
                task_time = self._processing_times_raw[j][t]
                processing_times[f"Job{j}"][f"Task{t}"] = task_time
        return processing_times


class Solution:
    def __init__(self, problem: Problem, permutation):
        """
        :param problem:
        :param permutation: List of job ids
        """
        self.problem = problem
        self.permutation = permutation
        self._verify_solution()

    def _verify_solution(self):
        """
        Verifying basic properties of a proposed solution before evaluating it
        """
        # job ids in permutation should be unique
        if len(self.permutation) != len(set(self.permutation)):
            raise ValueError("Job ids in the permutation must be unique")
        # jobs in "problem" set and "solution" set should be equal
        if set(self.permutation) != set(list(self.problem.processing_times.keys())):
            raise KeyError("Permutation must include only the jobs given in problem")
