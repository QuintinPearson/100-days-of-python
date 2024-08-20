student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create a function to get each student's grades
def get_grades(score_object):
    student_grades = {}
    for key in score_object:
        if score_object[key] > 90:
            student_grades[key] = "Outstanding"
        elif score_object[key] > 80:
            student_grades[key] = "Exceeds Expectations"
        elif score_object[key] > 70:
            student_grades[key] = "Acceptable"
        elif score_object[key] < 70:
            student_grades[key] = "Fail"

    return student_grades



student_grades = get_grades(student_scores)
print(student_grades)