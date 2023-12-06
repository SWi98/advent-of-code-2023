from utils.file_operations import read_lines
from dataclasses import dataclass

DIGITS_STOI = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

DIGITS_AS_STR = list(DIGITS_STOI.keys())


@dataclass
class FoundDigits:
    left_index: int
    left_digit: int
    right_index: int
    right_digit: int



def find_true_digits(text: str) -> FoundDigits | None:
    first_digit_index: int | None = None
    last_digit_index: int | None = None
    for index, sign in enumerate(text):
        if sign.isdigit():
            if first_digit_index is None:
                first_digit_index = index
                last_digit_index = index
            else:
                last_digit_index = index
    if first_digit_index is None:
        return None
    else:
        return FoundDigits(
            left_index=first_digit_index,
            left_digit=int(text[first_digit_index]),
            right_index=last_digit_index,
            right_digit=int(text[last_digit_index])
        )
    

def find_text_digits(text: str) -> FoundDigits | None:
    first_digit_index = len(text) + 1
    first_digit: int | None = None
    last_digit_index = -1
    last_digit: int | None = None
    for digit_str in DIGITS_AS_STR:
        found_digit_index = text.find(digit_str)
        if found_digit_index != -1:
            if found_digit_index < first_digit_index:
                first_digit_index = found_digit_index
                first_digit = DIGITS_STOI[digit_str]

        found_digit_index = text.rfind(digit_str)
        if found_digit_index != -1:
            if found_digit_index >= last_digit_index:
                last_digit_index = found_digit_index
                last_digit = DIGITS_STOI[digit_str]

    if first_digit is None:
        return None
    else:
        return FoundDigits(
            left_index=first_digit_index,
            left_digit=first_digit,
            right_index=last_digit_index,
            right_digit=last_digit
        )


def main():
    input = read_lines("1_2/input.txt", rstrip=True)
    # input = [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen"
    # ]
    result = 0

    for line in input:
        prev_result = result
        text_digits = find_text_digits(line)
        real_digits = find_true_digits(line)
        if text_digits is None:
            assert type(real_digits) is FoundDigits
            result += int(str(real_digits.left_digit) + str(real_digits.right_digit))
        elif real_digits is None:
            assert type(text_digits) is FoundDigits
            result += int(str(text_digits.left_digit) + str(text_digits.right_digit))
        else:
            if real_digits.left_index < text_digits.left_index:
                left_digit = str(real_digits.left_digit)
            else:
                left_digit = str(text_digits.left_digit)
            if real_digits.right_index > text_digits.right_index:
                right_digit = str(real_digits.right_digit)
            else:
                right_digit = str(text_digits.right_digit)
            result += int(left_digit + right_digit)
        # print(result - prev_result, "for", line)
    print(result)


if __name__ == "__main__":
    main()