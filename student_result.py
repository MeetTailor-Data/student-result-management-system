students = []

def add_st():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    num_subjects = int(input("Enter number of subjects: "))
    marks = []
    for i in range(num_subjects):
        m = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    student = {
        "Roll": roll,
        "Name": name,
        "Marks": marks
    }
    students.append(student)
    print("Student Added Successfully")

def cal_result():
    if not students:
        print("No Students to Calculate Result")
        return

    for s in students:
        total = sum(s["Marks"])
        per = total / len(s["Marks"])

        status = "PASS" if per >= 40 else "FAIL"

        if per >= 75:
            grade = "Distinction"
        elif per >= 60:
            grade = "First Class"
        elif per >= 40:
            grade = "Second Class"
        else:
            grade = "No Grade"

        s["Total"] = total
        s["Percentage"] = per
        s["Grade"] = grade
        s["Status"] = status

    print("Result Calculated Successfully")

def show_result():
    if not students:
        print("No Students to Show Result")
        return

    for s in students:
        print("\n----- Student Result -----")
        print("Roll No:", s["Roll"])
        print("Name:", s["Name"])
        print("Total Marks:", s["Total"])
        print("Percentage:", round(s["Percentage"], 2))
        print("Grade:", s["Grade"])
        print("Result:", s["Status"])
while True:
    print("\n===== Student Result Management System =====")
    print("1. Add Student")
    print("2. Calculate Result")
    print("3. Show Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_st()
    elif choice == "2":
        cal_result()
    elif choice == "3":
        show_result()
    elif choice == "4":
        print("Exiting Student Result Management System...")
        break
