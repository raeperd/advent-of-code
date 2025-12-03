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


if __name__ == "__main__":
    from pathlib import Path

    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text()
    print(f"Total joltage part 1: {total_max_joltage(input_text)}")
