from pathlib import Path

from .sol import count_accessible_rolls, count_total_removable_rolls

EXAMPLE_INPUT = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def load_input() -> str:
    input_file = Path(__file__).parent / "input.txt"
    return input_file.read_text()


def test_part1_example():
    """Test part 1 with the example from README.md."""
    assert count_accessible_rolls(EXAMPLE_INPUT) == 13


def test_part2_example():
    """Test part 2 with the example from README.md."""
    assert count_total_removable_rolls(EXAMPLE_INPUT) == 43
