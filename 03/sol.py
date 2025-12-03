def total_max_joltage(input_text: str) -> int:
    """Calculate total output joltage from all battery banks."""
    result = 0
    banks = input_text.strip().splitlines()
    for bank in banks:
        max_number = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                if max_number < int(bank[i] + bank[j]):
                    max_number = int(bank[i] + bank[j])
        result += max_number
    return result


def index_of_max_with_suffix(numbers: str, num_suffix: int) -> int:
    result = 0
    max_number = 0
    for i in range(len(numbers) - num_suffix):
        if int(numbers[i]) > max_number:
            result = i
            max_number = int(numbers[i])
    return result


def total_max_joltage_part2(input_text: str) -> int:
    """Calculate total output joltage with new rules for part 2."""
    result = 0
    banks = input_text.strip().splitlines()
    for bank in banks:
        str_numbers = bank
        str_max_number = ""
        num_suffix = 11
        while len(str_max_number) != 12:
            max_index = index_of_max_with_suffix(str_numbers, num_suffix)
            str_max_number += str_numbers[max_index]
            str_numbers = str_numbers[max_index + 1 :]
            num_suffix -= 1
        result += int(str_max_number)
    return result


if __name__ == "__main__":
    from pathlib import Path

    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text()
    print(f"Total joltage part 1: {total_max_joltage(input_text)}")
    print(f"Total joltage part 2: {total_max_joltage_part2(input_text)}")
