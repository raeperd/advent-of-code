from pathlib import Path

from solution import sum_invalid_ids, sum_invalid_ids_part_2

EXAMPLE_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def load_input() -> str:
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        return f.read()


def test_part1_example():
    """Test part 1 with the example from README.md."""
    assert sum_invalid_ids(EXAMPLE_INPUT) == 1227775554


def test_part2_example():
    """Test part 2 with the example from README.md."""
    assert sum_invalid_ids_part_2(EXAMPLE_INPUT) == 4174379265
