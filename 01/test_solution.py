from pathlib import Path

from .sol import process_rotations, process_rotations_part2

EXAMPLE_ROTATIONS = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


def load_input() -> list[str]:
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        return [line.strip() for line in f if line.strip()]


def test_part1_example():
    """Test part 1 with the example from PART-1.md."""
    assert process_rotations(EXAMPLE_ROTATIONS) == 3


def test_part2_example():
    """Test part 2 with the example from PART-2.md."""
    # Part 2 counts times dial points at 0 during rotations, not just at the end
    # Expected: 6 (3 at end + 3 during rotations)
    assert process_rotations_part2(EXAMPLE_ROTATIONS) == 6


def test_part1_input():
    """Test part 1 with actual input."""
    rotations = load_input()
    assert process_rotations(rotations) == 1055


def test_part2_input():
    """Test part 2 with actual input."""
    rotations = load_input()
    assert process_rotations_part2(rotations) == 6386
