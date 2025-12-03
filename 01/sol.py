def process_rotations(rotations: list[str]) -> int:
    """Process rotations and count how many times dial points at 0."""
    counter = 0
    number = 50
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == "L":
            number = (number - distance) % 100
        else:
            number = (number + distance) % 100
        if number == 0:
            counter += 1
    return counter


def count_zeros_crossed(start: int, end: int) -> int:
    """
    Count how many times we're at 0 when moving from start to end.

    On the dial, 0 appears at: ..., -200, -100, 0, 100, 200, ...
    We count each one we cross or land on (but not the starting point).
    """
    count = 0

    if end > start:
        # Moving right (R): check 100, 200, 300, ...
        # We cross a zero at each multiple of 100 that is > start and <= end
        boundary = 100
        while boundary <= end:
            if boundary > start:
                count += 1
            boundary += 100
    else:
        # Moving left (L): check 0, -100, -200, ...
        # We cross a zero at each multiple of 100 that is < start and >= end
        boundary = (start // 100) * 100  # Nearest multiple of 100 <= start
        if boundary == start:
            boundary -= 100  # Don't count where we start
        while boundary >= end:
            count += 1
            boundary -= 100

    return count


def process_rotations_part2(rotations: list[str]) -> int:
    """Part 2: Count how many times dial points at 0 during rotations."""
    pos = 50
    count = 0

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == "L":
            new_pos = pos - distance
        else:
            new_pos = pos + distance

        # Count how many zeros we crossed during this rotation
        count += count_zeros_crossed(pos, new_pos)

        # Wrap position back to 0-99
        pos = new_pos % 100

    return count


if __name__ == "__main__":
    from pathlib import Path

    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        rotations = [line.strip() for line in f if line.strip()]
    print(f"Password part 1: {process_rotations(rotations)}")
    print(f"Password part 2: {process_rotations_part2(rotations)}")
