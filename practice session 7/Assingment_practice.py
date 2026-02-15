def greet_student(name):
    return "Hello, " + name + "!"

def analyze_scores(scores):
    total_subjects = len(scores)
    average_scores = sum(scores) / total_subjects
    return total_subjects, average_scores

def check_result(average):
    if average >= 50:
        return "pass"
    else:
        return "Fail"
    
def main():
    name = "Rahul"
    scores = [60, 45, 70, 55]

    greeting = greet_student(name)
    subjects, average = analyze_scores(scores)
    result = check_result(average)

    print(greeting)
    print("No of subjects : ", subjects)
    print("Average scores : ", average)
    print("Result : ", result)

main()



# Out of syllabus lag rha hai to be serious