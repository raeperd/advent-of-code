import pytest
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


def test_actual_input():
    """Test with the actual puzzle input."""
    from pathlib import Path
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        rotations = [line.strip() for line in f if line.strip()]
    
    result = process_rotations(rotations)
    print(f"\nPassword: {result}")
    assert result > 0  # Just verify it produces a positive result
