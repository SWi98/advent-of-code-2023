from utils.file_operations import read_lines


def main():
    input = read_lines("1_1/input.txt", rstrip=True)
    # input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    result = 0

    for line in input:
        first_digit: int | None = None
        last_digit: int | None = None
        for sign in line:
            if sign.isdigit():
                if first_digit is None:
                    first_digit = sign
                    last_digit = sign
                else:
                    last_digit = sign
        result += int(first_digit + last_digit)
    print(result)


if __name__ == "__main__":
    main()
