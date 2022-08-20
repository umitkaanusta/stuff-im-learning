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

    def _build_schedule(self):
        """
        Builds schedule using the problem and solution info.
        Steps
        1) Initialize machines, remember num_machines = num_tasks, machine index = tasks index
        2) Assign first job to first machine
        3) Assign first job to other machines
        4) Assign other jobs
            4.1) To first machine
            4.2) To other machines

        For (4.2), start time of a task is calculated differently.
        Intuition says start time must be the time where machine becomes available.
        This happens when either:
            i) previous task of job is completed,
            ii) machine completes task of previous job.
        Here the start time = whichever is greater.
        """
        # initialize machines. keep in mind that machine index = task index.
        schedule = {f"Machine{m}": [] for m in range(self.problem["num_machines"])}
        # assign first job to first machine
        start_time = 0
        task_time = self.problem["processing_times"][self.solution[0]]["Task0"]
        schedule["Machine0"].append(
            {"job": self.solution[0], "task": "Task0",
             "start_time": 0,
             "processing_time": task_time,
             "end_time": start_time + task_time}
        )
        # assign first job to other machines
        for m in range(1, self.problem["num_machines"]):
            start_time = schedule[f"Machine{m - 1}"][0]["end_time"]
            task_time = self.problem["processing_times"][self.solution[0]][f"Task{m}"]
            schedule[f"Machine{m}"].append(
                {"job": self.solution[0], "task": f"Task{m}",
                 "start_time": start_time,
                 "processing_time": task_time,
                 "end_time": start_time + task_time}
            )
        # assign other jobs
        for j in range(1, len(self.solution)):
            # first machine doesn't have idle time
            start_time = schedule["Machine0"][j - 1]["end_time"]
            task_time = self.problem["processing_times"][self.solution[j]]["Task0"]
            schedule["Machine0"].append(
                {"job": self.solution[j], "task": "Task0",
                 "start_time": start_time,
                 "processing_time": task_time,
                 "end_time": start_time + task_time}
            )
            # other machines
            for m in range(1, self.problem["num_machines"]):
                start_time = max(schedule[f"Machine{m - 1}"][j]["end_time"],
                                 schedule[f"Machine{m}"][j - 1]["end_time"])
                task_time = self.problem["processing_times"][self.solution[j]][f"Task{m}"]
                schedule[f"Machine{m}"].append(
                    {"job": self.solution[j], "task": f"Task{m}",
                     "start_time": start_time,
                     "processing_time": task_time,
                     "end_time": start_time + task_time}
                )
        return schedule

    def _calc_performance(self, schedule):
        perf = {
            "time_to_finish": max([val[-1]["end_time"] for key, val in schedule.items()]),
            "benchmark_upper_bound": self.problem["upper_bound"],
            "benchmark_lower_bound": self.problem["lower_bound"]
        }
        return perf

    def _build_job_idle_times(self, schedule):
        """
        Idle time of job = End time  - Total processing time

        Steps
        1) Add start time of each job
        2) Add end time of each job
        3) Add total processing time of each job
        4) Calculate idle time
        """
        job_idle_times = {}
        # add start time of each job
        for record in schedule["Machine0"]:
            job = record["job"]
            job_start_time = record["start_time"]
            job_idle_times[job] = {"start_time": job_start_time}
        # add end time of each job
        for record in schedule[f"Machine{self.problem['num_machines'] - 1}"]:
            job = record["job"]
            job_end_time = record["end_time"]
            job_idle_times[job]["end_time"] = job_end_time
        # add total processing time of each job
        for job in self.problem["processing_times"]:
            total_processing_time = sum(self.problem["processing_times"][job].values())
            job_idle_times[job]["total_processing_time"] = total_processing_time
        # calculate idle time
        for job in job_idle_times:
            start_time = job_idle_times[job]["start_time"]
            end_time = job_idle_times[job]["end_time"]
            total_processing_time = job_idle_times[job]["total_processing_time"]
            job_idle_times[job]["idle_time"] = end_time - total_processing_time
        return job_idle_times

    def _build_machine_idle_times(self, schedule):
        """
        Idle time of machine = End time - Total processing time

        Steps
        1) Add start and end time of each machine
        2) Add total processing time of each machine
        3) Calculate idle time
        """
        machine_idle_times = {}
        for machine in schedule:
            # add start and end time
            start_time = schedule[machine][0]["start_time"]
            end_time = schedule[machine][-1]["end_time"]
            # add total processing time
            total_processing_time = 0
            for j in range(self.problem["num_jobs"]):
                total_processing_time += schedule[machine][j]["processing_time"]
            # calculate idle time
            idle_time = end_time - total_processing_time
            machine_idle_times[machine] = {"start_time": start_time, "end_time": end_time,
                                           "total_processing_time": total_processing_time, "idle_time": idle_time}
        return machine_idle_times

    @property
    def result(self) -> dict:
        """
        Returns a dict showing:
        1) Performance: Time to finish, benchmark upper/lower bounds
        2) Schedule: Visualized schedule showing each machine's assignment status
        3) Job idle times: Idle time of each job
        """
        schedule = self._build_schedule()
        performance = self._calc_performance(schedule)
        job_idle_times = self._build_job_idle_times(schedule)
        machine_idle_times = self._build_machine_idle_times(schedule)
        res = {"performance": performance, "schedule": schedule,
               "job_idle_times": job_idle_times, "machine_idle_times": machine_idle_times}
        return res
