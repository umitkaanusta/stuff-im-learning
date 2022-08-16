"""
Parser script to convert flow shop scheduling problem benchmarks into json
"""
import requests
import json

URLS = [
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai20_5.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai20_10.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai20_20.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai50_5.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai50_10.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai50_20.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai100_5.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai100_10.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai100_20.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai200_10.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai200_20.txt",
    "http://mistic.heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai500_20.txt"
]


def get_raw_data_from_url(url):
    return requests.get(url).content.decode("UTF-8")


def make_list_of_lines(rawdata):
    lines = rawdata.split("\n")
    lines = [*map(str.strip, lines)]
    return lines


def construct_dicts(lines_list):
    # show processing times and other data in a dictionary format
    dicts = []
    curr_dict = {}
    for line in lines_list:
        starting_line_cond = "number of jobs" in line or line == ""
        processing_line_cond = "processing times" in line
        number_line_cond = not starting_line_cond and not processing_line_cond
        if starting_line_cond and curr_dict:  # starting line
            # checks dict so no empty dict is added to list
            dicts.append(curr_dict)
            continue
        if number_line_cond:
            number_line = [int(item) for item in line.strip().split(" ") if item != ""]
            if len(number_line) == 5:  # defining line
                curr_dict["num_jobs"] = number_line[0]
                curr_dict["num_machines"] = number_line[1]
                curr_dict["num_tasks"] = curr_dict["num_machines"]
                curr_dict["initial_seed"] = number_line[2]
                curr_dict["upper_bound"] = number_line[3]
                curr_dict["lower_bound"] = number_line[4]
                curr_dict["processing_times"] = [[] for _ in range(curr_dict["num_jobs"])]
            elif len(number_line) == curr_dict["num_jobs"]:  # line showing processing times
                for i in range(len(number_line)):
                    curr_dict["processing_times"][i].append(number_line[i])
    return dicts


def name_jobs_tasks(dicts):
    # give standardized names to jobs and tasks for easier identification instead of using index numbers
    dicts_named = []
    for D in dicts:
        processing_times_raw = D["processing_times"]
        processing_times = {}
        for j in range(D["num_jobs"]):
            processing_times[f"Job{j}"] = {}
            for t in range(D["num_tasks"]):
                task_time = processing_times_raw[j][t]
                processing_times[f"Job{j}"][f"Task{t}"] = task_time
        new_dict = {key: val for key, val in D.items()}  # copy D to not mutate it
        new_dict["processing_times"] = processing_times
        dicts_named.append(new_dict)
    return dicts_named


def name_problems(list_parsed_problems):
    # standardized names for each problem as well - will be useful for experiment tracking
    # names are 0-indexed
    return {f"Problem{i}": list_parsed_problems[i]
            for i in range(len(list_parsed_problems))}


def parse_all_urls():
    parsed_all = []
    for url in URLS:
        raw = get_raw_data_from_url(url)
        lines = make_list_of_lines(raw)
        parsed = name_jobs_tasks(construct_dicts(lines))
        parsed_all += parsed
    parsed_all_named = name_problems(parsed_all)
    with open("benchmark.json", "w") as f:
        json.dump(parsed_all_named, f, indent=2)


if __name__ == '__main__':
    parse_all_urls()
