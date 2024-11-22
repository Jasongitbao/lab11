import matplotlib.pyplot as plt
import os

def main():
    student_file = "data/students.txt"
    assignment_file = "data/assignments.txt"
    submission_dir = "data/submissions"
    students = {}
    assignments = {}
    submissions = {}
    with open(student_file, "r") as file:
        for line in file:
            id = line[:3]
            name = line[3:].strip()
            students[name] = id
    with open(assignment_file, "r") as file:
        for index, line in enumerate(file):
            if index % 3 == 0:
                assign_name = line.strip()
            elif index % 3 == 1:
                assign_id = line.strip()
            elif index % 3 == 2:
                assign_value = int(line.strip())
                assignments[assign_name] = [assign_id, assign_value]
    for filename in os.listdir(submission_dir):
        filepath = os.path.join(submission_dir, filename)
        with open(filepath, "r") as file:
            for line in file:
                st_id, assign_id, score = line.strip().split("|")
                if assign_id not in submissions:
                    submissions[assign_id] = {}
                submissions[assign_id][st_id] = int(score)
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    print()
    choice = int(input("Enter your selection: "))
    if choice == 1:
        name = input("What is the student's name: ")
        if name not in students:
            print('Student not found')
        else:
            student_id = students[name]
            score = 0
            for a,b in assignments.items():
                assign_id = b[0]
                assign_value = b[1]
                score += assign_value * submissions[assign_id][student_id] / 1000
            print(f"{round(score)}%")
    elif choice == 2:
        assignment = input("What is the assignment name: ")
        if assignment not in assignments:
            print("Assignment not found")
        else:
            assign_id = assignments[assignment][0]
            scores = []
            for key, value in submissions[assign_id].items():
                scores.append(value)
            min_score = min(scores)
            max_score = max(scores)
            ave_score = sum(scores)/ len(scores)
            print(f"Min: {round(min_score)}%")
            print(f"Avg: {int(ave_score)}%")
            print(f"Max: {round(max_score)}%")
    elif choice == 3:
        assignment = input("What is the assignment name: ")
        scores = []
        if assignment not in assignments:
            print("Assignment not found")
        else:
            assign_id = assignments[assignment][0]
            for key, value in submissions[assign_id].items():
                scores.append(value)
        min_bin = min(scores) // 10 * 10
        bin_ref = list(range(min_bin, 101, 5))
        plt.hist(scores, bins=bin_ref, edgecolor='black')
        plt.show()

if __name__ == "__main__":
    main()