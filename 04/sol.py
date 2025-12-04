def count_accessible_rolls(input_text: str) -> int:
    """Count paper rolls accessible by forklifts (fewer than 4 neighbors)."""
    result = 0
    matrix: list[str] = input_text.splitlines()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "@":
                continue
            count = 0
            for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                r = i + di
                c = j + dj
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[i]):
                    if matrix[r][c] == "@":
                        count += 1
            if count < 4:
                result += 1
    return result


if __name__ == "__main__":
    from pathlib import Path

    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text()
    print(f"Accessible rolls: {count_accessible_rolls(input_text)}")
