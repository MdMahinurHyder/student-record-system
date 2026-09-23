import json

print("=" * 40)
print("     🎓 STUDENT RECORD SYSTEM 🎓")
print("=" * 40)

student_id = input("Enter your ID: ")
student_name = input("Enter your name: ")

try:
    with open("student.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    print("\nℹ️  No data was found. Hey, new student, go ahead!")
    data = []

existing = [s for s in data if s["id"] == student_id]

if existing:
    print("\n✅ Student already registered! Here's the info:")
    print("-" * 40)
    for subject, mark in existing[0].items():
        print(f"{subject.capitalize():<15}: {mark}")
    print("-" * 40)

else:
    print(f"\n👋 Welcome, {student_name}! Let's set up your record.\n")

    while True:
        try:
            n = int(input("How many subjects are there? "))
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    subject_names = []
    marks = []

    print("\n--- Enter Subject Details ---")
    for i in range(0, n):
        subject_names.append(input(f"Subject {i + 1} name: "))
        while True:
            try:
                mark = float(input(f"Subject {i + 1} mark: "))
                marks.append(mark)
                break
            except ValueError:
                print("❌ Invalid mark — please enter a number.")

    student_info = {"id": student_id, "name": student_name}
    student_info.update({subject: mark for subject, mark in zip(subject_names, marks)})

    data.append(student_info)

    with open("student.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\n" + "=" * 40)
    print("✅ Hey, new student. Your data is saved!")
    print("-" * 40)
    for subject, mark in student_info.items():
        print(f"{str(subject).capitalize():<15}: {mark}")
    print("=" * 40)