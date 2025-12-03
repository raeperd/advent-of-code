from pathlib import Path

from .sol import total_max_joltage

EXAMPLE_INPUT = """987654321111111
811111111111119
234234234234278
818181911112111"""


def load_input() -> str:
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text()


def test_part1_example():
    """Test part 1 with the example from README.md."""
    # 98 + 89 + 78 + 92 = 357
    assert total_max_joltage(EXAMPLE_INPUT) == 357
