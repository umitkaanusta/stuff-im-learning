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
    dicts = []
    curr_dict = {}
    for line in lines_list:
        starting_line_cond = "number of jobs" in line or line == ""
        processing_line_cond = "processing times" in line
        number_line_cond = not starting_line_cond and not processing_line_cond
        if starting_line_cond:  # starting line
            dicts.append(curr_dict)
            curr_dict = {}
            continue
        if number_line_cond:
            number_line = [int(item) for item in line.strip().split(" ") if item != ""]
            if len(number_line) == 5:  # defining line
                curr_dict["num_jobs"] = number_line[0]
                curr_dict["num_machines"] = number_line[1]
                curr_dict["initial_seed"] = number_line[2]
                curr_dict["upper_bound"] = number_line[3]
                curr_dict["lower_bound"] = number_line[4]
                curr_dict["processing_times"] = [[] for _ in range(curr_dict["num_jobs"])]
            elif len(number_line) == curr_dict["num_jobs"]:  # line showing processing times
                for i in range(len(number_line)):
                    curr_dict["processing_times"][i].append(number_line[i])
    return dicts[1:]  # first dict is empty dict


def parse_all_urls():
    parsed_all = []
    for url in URLS:
        raw = get_raw_data_from_url(url)
        lines = make_list_of_lines(raw)
        parsed = construct_dicts(lines)
        parsed_all += parsed
    with open("benchmark.json", "w") as f:
        json.dump(parsed_all, f, indent=2)


if __name__ == '__main__':
    parse_all_urls()
