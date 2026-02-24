def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"


def main():
    print("=== Student Grade Calculator ===")

    name = input("Enter student name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    print("\n--- Result ---")
    print(f"Name: {name}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

    # Save result to file
    with open("result.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Total: {total}\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Grade: {grade}\n")

    print("\nResult saved to result.txt")


if __name__ == "__main__":
    main()