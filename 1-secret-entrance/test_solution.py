from solution import process_rotations, process_rotations_part2


def test_part1():
    """Test part 1 with the example from PART-1.md."""
    rotations = [
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

    assert process_rotations(rotations) == 3


def test_part2():
    """Test part 2 with the example from PART-2.md."""
    rotations = [
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

    # Part 2 counts times dial points at 0 during rotations, not just at the end
    # Expected: 6 (3 at end + 3 during rotations)
    assert process_rotations_part2(rotations) == 6
