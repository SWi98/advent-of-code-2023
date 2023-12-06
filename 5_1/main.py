from utils.file_operations import read_lines
import numpy as np
from tqdm import tqdm


MAPPING_TYPES = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:"
]


def main():
    # lines = read_lines("5_1/input.txt", rstrip=True)
    lines = read_lines("5_1/test_input.txt", rstrip=True)
    seeds_nums = []
    mappings = [[] for _ in range(7)]
    mapping_idx = -1
    for i, line in tqdm(enumerate(lines)):
        if i == 0:
            seeds_nums = line.split(":")[1].strip().split(" ")
            seeds_nums = [int(num) for num in seeds_nums if num.isnumeric()]
        if any(mapping_type_str in line for mapping_type_str in MAPPING_TYPES):
            mapping_idx += 1
        elif mapping_idx > -1 and line.strip() != "":
            mapping = line.strip().split(" ")
            mapping = (int(num) for num in mapping if num.isnumeric())
            destination, source, range_size = mapping
            mappings[mapping_idx].append((source, destination, range_size))
    
    locations = []
    print(seeds_nums)
    for number in tqdm(seeds_nums):
        for mappings_category in mappings:
            # print("-----------")
            # print(f"CURRENT NUMBER: {number}")
            for mapping in mappings_category:
                # print(mapping)
                source, destination, range_size = mapping
                if source + range_size > number >= source:
                    # print("Found good mapping")
                    range_step = number - source
                    # print(f"Mapped {number} to {destination + range_step}")
                    number = destination + range_step
                    break
        locations.append(number)
    print(min(locations))

if __name__ == "__main__":
    main()
