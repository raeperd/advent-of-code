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


if __name__ == "__main__":
    from pathlib import Path
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file) as f:
        rotations = [line.strip() for line in f if line.strip()]
    print(f"Password: {process_rotations(rotations)}")