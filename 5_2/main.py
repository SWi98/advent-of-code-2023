from utils.file_operations import read_lines
import numpy as np
from tqdm import tqdm
import queue


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
    lines = read_lines("5_1/input.txt", rstrip=True)
    # lines = read_lines("5_1/test_input.txt", rstrip=True)
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

    print(seeds_nums)
    seed_pairs = [seeds_nums[i:i+2] for i in range(0, len(seeds_nums), 2)]
    next_seeds = [(seed_start, seed_start + seed_range - 1)
                    for seed_start, seed_range in seed_pairs]
    current_queue = queue.Queue()
    next_queue = queue.Queue()
    for elem in next_seeds:
        next_queue.put(elem)
    for mapping_category in mappings:
        current_queue, next_queue = next_queue, current_queue
        while not current_queue.empty():
            seed_start, seed_end = current_queue.get()
            # print(f"Going strong with {seed_start}, {seed_end}")
            mapped_something = False
            for mapping in mapping_category:
                source, destination, range_size = mapping
                source_start = source
                source_end = source + range_size - 1
                destination_start = destination
                destination_end = destination + range_size - 1
                # print(f"Analyzing mapping with {seed_start}, {seed_end} for mapping: {source_start} - {source_end}")
                if seed_start >= source_start and seed_end <= source_end:
                    seed_start_step = seed_start - source_start
                    seed_end_step = seed_end - source_start
                    next_queue.put(
                        (destination + seed_start_step, destination + seed_end_step)
                    )
                    mapped_something = True
                    # print(f"TOTAL inside. Put: {(destination + seed_start_step, destination + seed_end_step)}")
                    break
                elif seed_start < source_start and seed_end > source_end:
                    next_queue.put(
                        (destination_start, destination_end)
                    )
                    current_queue.put(
                        (seed_start, source_start - 1)
                    )
                    current_queue.put(
                        (source_end + 1, seed_end)
                    )
                    # print(f"BIG Overlap. Put: { (destination_start, destination_end)}; {  (seed_start, source_start - 1)}, {(source_end + 1, seed_end)}")
                    mapped_something = True
                    break
                elif seed_start < source_start and seed_end > source_start and seed_end <= source_end:
                    seeds_range = seed_end - source_start
                    next_queue.put(
                        (destination_start, destination_start + seeds_range)
                    )
                    current_queue.put(
                        (seed_start, source_start - 1)
                    )
                    mapped_something = True
                    # print(f"LEFT Overlap. Put: {(destination_start, destination_start + seeds_range)}; {(seed_start, source_start - 1)}")
                    break
                elif seed_start >= source_start and seed_start < source_end and seed_end > source_end:
                    seeds_range = source_end - seed_start
                    next_queue.put(
                        (destination_end - seeds_range, destination_end)
                    )
                    current_queue.put(
                        (source_end + 1, seed_end)
                    )
                    mapped_something = True
                    # print(f"RIGHT Overlap. Put: {(destination_end - seeds_range, destination_end)}; {(source_end + 1, seed_end)}")
                    break
            if not mapped_something:
                next_queue.put((seed_start, seed_end))

    print("NEXT SEEDS:", next_queue.queue)
    print(min([x[0] for x in next_queue.queue]))

if __name__ == "__main__":
    main()
