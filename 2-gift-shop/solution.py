def sum_invalid_ids(input_text: str) -> int:
    """Sum all invalid IDs across all ranges."""
    result = 0
    id_ranges = input_text.split(",")
    for id_range in id_ranges:
        start, end = id_range.split("-")
        for i in range(int(start), int(end) + 1):
            length = len(str(i))
            if length % 2 == 1:
                continue
            if str(i)[: length // 2] == str(i)[length // 2 :]:
                result += i
    return result


def sum_invalid_ids_part_2(input_text: str) -> int:
    """Sum all invalid IDs across all ranges."""
    result = 0
    id_ranges = input_text.split(",")
    for id_range in id_ranges:
        start, end = id_range.split("-")
        for number in range(int(start), int(end) + 1):
            number_length = len(str(number))
            invalid = False
            for length in range(1, number_length // 2 + 1):
                if invalid:
                    break
                if number_length % length != 0:
                    continue
                for i in range(0, number_length // length - 1):
                    if str(number)[i * length : (i + 1) * length] != str(number)[(i + 1) * length : (i + 2) * length]:
                        break
                else:
                    invalid = True
            if invalid:
                result += number

    return result


if __name__ == "__main__":
    from pathlib import Path

    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text()
    result = sum_invalid_ids(input_text)
    result_part_2 = sum_invalid_ids_part_2(input_text)
    print(f"Result: {result}")
    print(f"Result Part2: {result_part_2}")
