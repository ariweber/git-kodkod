def create_grades_file(filename):
    """Create a grades file with sample student data."""
    students = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68]),
    ]
    
    with open(filename, "w", encoding="utf-8") as f:
        for name, grades in students:
            grades_str = ",".join(map(str, grades))
            f.write(f"{name},{grades_str}\n")

def calculate_averages(filename):
    """Read a grades file and return a dict of {name: average}."""
    averages = {}
 
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")

            student_name = parts[0]
            grades = [int(grade) for grade in parts[1:]]
            average = sum(grades) / len(grades)

            averages[student_name] = average

    return averages


def save_results(averages, output_filename):
    """Save sorted averages and class statistics to a file."""
    sorted_averages = sorted(averages.items(), key=lambda item: item[1], reverse=True)

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("Name,Average\n")

        for student_name, average in sorted_averages:
            f.write(f"{student_name},{average:.1f}\n")

        class_average = sum(averages.values()) / len(averages)
        highest_name, highest_avg = sorted_averages[0]
        lowest_name, lowest_avg = sorted_averages[-1]
        passing_count = sum(1 for avg in averages.values() if avg >= 60)

        f.write("\n=== Statistics ===\n")
        f.write(f"Class average: {class_average:.1f}\n")
        f.write(f"Highest: {highest_name} ({highest_avg:.1f})\n")
        f.write(f"Lowest: {lowest_name} ({lowest_avg:.1f})\n")
        f.write(f"Passing (>=60): {passing_count}/{len(averages)}\n")


averages = calculate_averages('grades.txt')
save_results(averages, 'results.txt')









create_grades_file("grades.txt")

results = calculate_averages('grades.txt')
for name, avg in results.items():
    print(f'{name}: {avg:.1f}')
