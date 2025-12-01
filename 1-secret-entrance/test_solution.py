from solution import process_rotations


def test_example():
    """Test with the example from README."""
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
