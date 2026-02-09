from grade_compute import processLine, gradeToNumber, numberToGrade, calculateAverage
def printBox(grades, lowest, average, final_letter):
    print('-' * 40)
    print('|{:^38}|'.format("GRADE REPORT SUMMARY"))
    print('-' * 40)
    print('| Grades Entered: {:<23}|'.format(', '.join(grades)))
    print('| Lowest Grade Dropped: {:<19}|'.format(numberToGrade(lowest)))
    print('| Calculated Average: {:>13.2f} |'.format(average))
    print('| Final Letter Grade: {:>14} |'.format(final_letter))
    print('-' * 40)

def main():
    while True:
        user_input = input("Enter 4 grades separated by $ (or Q to quit): ").strip()
        if user_input.upper() == 'Q':
            print("Exiting program...")
            break
        grades = processLine(user_input)
        if not grades:
            print("Invalid input. Please enter 4 grades like A$B+ $ C $ D.")
            continue
        lowest, avg = calculateAverage(grades)
        final_letter = numberToGrade(avg)
        printBox(grades, lowest, avg, final_letter)

if __name__ == "__main__":
    main()
