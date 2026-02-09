# Converts letter grade to GPA
def gradeToNumber(grade):
    grade = grade.upper().strip()
    
    base = 0
    if grade.startswith('A'):
        base = 4.0
    elif grade.startswith('B'):
        base = 3.0
    elif grade.startswith('C'):
        base = 2.0
    elif grade.startswith('D'):
        base = 1.0
    elif grade.startswith('F'):
        base = 0.0
    else:
        return None  # invalid

    # Handles the + or -
    if len(grade) > 1:
        if grade[1] == '+':
            base += 0.3
        elif grade[1] == '-':
            base -= 0.3

    # Sets max GPA at 4.0
    if base > 4.0:
        base = 4.0
    if base < 0:
        base = 0
    return base

# Converts numeric GPA to letter grade
def numberToGrade(num):
    if num >= 4.0:
        return 'A'
    elif num >= 3.7:
        return 'A-'
    elif num >= 3.3:
        return 'B+'
    elif num >= 3.0:
        return 'B'
    elif num >= 2.7:
        return 'B-'
    elif num >= 2.3:
        return 'C+'
    elif num >= 2.0:
        return 'C'
    elif num >= 1.7:
        return 'C-'
    elif num >= 1.3:
        return 'D+'
    elif num >= 1.0:
        return 'D'
    elif num >= 0.7:
        return 'D-'
    else:
        return 'F'

# Validates a single grade input
def validateGrade(grade):
    grade = grade.upper().strip()
    valid_letters = ['A', 'B', 'C', 'D', 'F']
    if len(grade) == 1:
        return grade in valid_letters
    elif len(grade) == 2:
        return grade[0] in valid_letters and grade[1] in ['+', '-']
    else:
        return False

# Processes input
def processLine(input_line):
    grades = [g.strip() for g in input_line.split('$')]
    if len(grades) != 4:
        return None  # must have 4 inputted grades
    for g in grades:
        if not validateGrade(g):
            return None
    return grades

# Calculates average after removing lowest grade
def calculateAverage(grades):
    numeric_grades = [gradeToNumber(g) for g in grades]
    lowest = min(numeric_grades)
    numeric_grades.remove(lowest)
    avg = sum(numeric_grades) / len(numeric_grades)

    # Curve in a bonus if all remaining grades are B- or lower than 2.7
    if all(g <= 2.7 for g in numeric_grades):
        avg += 0.25
        if avg > 4.0:
            avg = 4.0

    return lowest, avg
