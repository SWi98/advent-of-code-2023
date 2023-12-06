from utils.file_operations import read_lines
import numpy as np
from tqdm import tqdm
import queue
import numpy as np


def read_input_line(line: str) -> list[str]:
    line = line.split(":")[1].strip().split(" ")
    return [symbol for symbol in line if symbol.isnumeric()]


def linear_time_solution(time: int, distance: int) -> int:
    res = 0
    started_winning = False
    first_speed, first_racing_time = -1, -1
    for speed in range(1, distance):
        if not started_winning:
            moved_distance = speed * (time - speed)
            if moved_distance > distance:
                print(f"Started wining for speed: {speed} and (time - speed): {(time - speed)}")
                res += 1
                started_winning = True
                first_speed, first_racing_time = speed, (time - speed)
        elif started_winning:
            res += 1
            if speed == first_racing_time and (time - speed) == first_speed:
                print(f"Stopped winning for speed: {speed} and (time - speed): {(time - speed)}")
                break
    return res


def constant_time_solution(time: int, distance: int) -> int:
    """
    Solving: [ distance = speed(time - speed) ] === [ -speed^2 * x + speed * time - distance = 0 ]
    """
    delta = (time ** 2) - (4 * (-1) * (-distance))
    s1 = ((-time) - np.sqrt(delta)) / (2 * -1)
    s2 = ((-time) + np.sqrt(delta)) / (2 * -1)
    start = np.floor(min(s1, s2))
    end = np.ceil(max(s1, s2))
    return int(end - start - 1)


def main():
    lines = read_lines("6_1/input.txt", rstrip=True)
    # lines = read_lines("6_1/test_input.txt", rstrip=True)
    times: list[int] = []
    distances: list[int] = []
    for line in lines:
        if "Time" in line:
            times = read_input_line(line)
        elif "Distance" in line:
            distances = read_input_line(line)
    time = int("".join(times))
    distance = int("".join(distances))
    print(time, distance)
    linear_res = linear_time_solution(time, distance)
    print(linear_res)
    constant_res = constant_time_solution(time, distance)
    print(constant_res)

if __name__ == "__main__":
    main()
