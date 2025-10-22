import csv


def create_grades_file():
    """Creates a CSV file with student names and three exam grades."""

    # Ask the user how many students to enter
    num_students = int(input("Enter the number of students: "))

    # Open the file for writing using the csv module
    with open("grades.csv", mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop for each student
        for i in range(num_students):
            print(f"\nEntering data for student {i + 1}:")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            # Get exam grades as integers
            exam1 = int(input("Enter grade for Exam 1: "))
            exam2 = int(input("Enter grade for Exam 2: "))
            exam3 = int(input("Enter grade for Exam 3: "))

            # Write each student record to the file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\n✅ grades.csv has been created successfully!")


# Run the function
if __name__ == "__main__":
    create_grades_file()
