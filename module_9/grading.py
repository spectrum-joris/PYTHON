from grading_student_scores import student_scores

for student in student_scores:
    if student_scores[student] > 90:
        print(f"{student} behaalde {student_scores[student]}. \nGraad: 'Uitmuntend'.\n")
    elif student_scores[student] > 80:
        print(f"{student} behaalde {student_scores[student]}.\nGraad 'Boven de Verwachtingen'.\n")
    elif student_scores[student] > 70:
        print(f"{student} behaalde {student_scores[student]}.\nGraad 'Voldoende'.\n")
    else: 
        print(f"{student} behaalde {student_scores[student]}.\nGraad 'Onvoldoende'.\n")


# bonus: voeg de grades toe aan de dictionary
def grade(score):
    if score > 90: return "Uitmuntend"
    elif score > 80: return "Boven de Verwachtingen"
    elif score > 70: return "Voldoende"
    else: return "Onvoldoende"

for name, score in list(student_scores.items()):
    student_scores[name] = {"score": score, "grade": grade(score)}

print(student_scores)





