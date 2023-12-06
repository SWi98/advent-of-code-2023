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
    lines = read_lines("6_1/input.txt", rstrip=True)
    # lines = read_lines("6_1/test_input.txt", rstrip=True)
    times: list[int] = []
    distances: list[int] = []
    for line in lines:
        if "Time" in line:
            line = line.split(":")[1].strip().split(" ")
            times = [int(symbol) for symbol in line if symbol.isnumeric()]
        elif "Distance" in line:
            line = line.split(":")[1].strip().split(" ")
            distances = [int(symbol) for symbol in line if symbol.isnumeric()]
    n = len(times)
    res = 0
    for i in range(n):
        time, dist = times[i], distances[i]
        ways_to_win = 0
        for speed in range(1, dist):
            moved_distance = speed * (time - speed)
            if moved_distance > dist:
                ways_to_win += 1
        if ways_to_win > 0:
            if res == 0:
                res = ways_to_win
            else:
                res *= ways_to_win
    print(res)

if __name__ == "__main__":
    main()
