"""Grade Calculator"""


def read_grades(file_path: str) -> list[tuple[str, list[int]]]:
    """Read student grades from a text file."""

    students: list[tuple[str, list[int]]] = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Each line: "name,grade1,grade2,grade3"
                parts = line.strip().split(",")
                if len(parts) != 4:
                    print(f"Skipping invalid line format: {line.strip()}")
                    continue
                name: str = parts[0]
                valid_grades: list[int] = []
                for grade in parts[1:]:
                    try:
                        valid_grades.append(int(grade))
                    except ValueError:
                        print(f"Skipping invalid grade '{grade}' for {name}")
                        continue
                if valid_grades:
                    students.append((name, valid_grades))
                else:
                    print(f"No valid grades for {name}, skipping")
        return students
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []


def calculate_average(grades: list[int]) -> float:
    """Calculate the average of a list of grades."""
    return sum(grades) / len(grades) if grades else 0


def write_passing_students(students: list[tuple[str, list[int]]], output_file: str):
    """Write students with a passing average to a file"""
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for name, grades in students:
                avg = calculate_average(grades)
                if avg >= 60:
                    file.write(f"{name}: {avg:.2f}\n")
        print(f"Passing students written to {output_file}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")


def main():
    """Main function to read grades, calculate averages, and write passing students."""
    input_file = "grades.txt"
    output_file = "passing_students.txt"
    students = read_grades(input_file)

    if students:
        print("Student Averages:")
        for name, grades in students:
            avg = calculate_average(grades)
            print(f"{name}: {avg:.2f}")
        write_passing_students(students, output_file)
    else:
        print("No valid student data to process.")


if __name__ == "__main__":
    main()
