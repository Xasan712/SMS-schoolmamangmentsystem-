from users import s,d,users,tusers,tech,cst

# data types for while

while 1:
    print(cst)
    tsc = str(input("choose (1-2): "))
    if tsc == "1":
        print(s)
        e = str(input("Num: "))
        if e == "1":
            ids = input("id: ")

            if ids in users["students"].keys():
                username = input("username: ")
                password = input("password: ")
                if username == users["students"][ids]['username'] and password == str(users["students"][ids]["password"]):
                    print(d)
                    option = input("Menudan tanlang(1-4): ")
                    if option == "1":

                        print(users["students"][ids])
                    elif option == "2":

                        x = users["students"][ids]['lesson']
                        print(f"Your lessons: {x}")
                    elif option == "3":
                        x3 = users["students"][ids]['class']
                        print(f"Your class: {x3}")
                    elif option == "4":
                        x4 = users["students"][ids]['homeTask']
                        print(f"Your home task: {x4}")
                    else:
                        print("Invalid option selected.")
        if e == "2":
            newId = str(len(users["students"]) + 1)
            fullname = input("Enter fullname: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            grade = input("Enter grade: ")
            lesson = input("Enter lessons (comma-separated): ")
            student_class = input("Enter class: ")
            home_task = input("Enter home task: ")
            new_student = {
                "fullname": fullname,
                "username": username,
                "password": password,
                "grade": int(grade),
                "lesson": lesson,
                "class": student_class,
                "homeTask": home_task
            }
            users["students"][newId] = new_student
            print(f"Student successfully add: {newId}")
    if tsc == "2":
        tid = str(input("Id: "))
        t_username = str(input("username:"))
        t_password = str(input("password:"))
        if t_username == tusers['Teachers'][tid]["username"] and t_password == str(tusers['Teachers'][tid]["password"]):
                print(tech)
                tech_p = str(input("choose (1-3): "))
                if tech_p == "1":  # Add grade to a student
                    student_id = input("Enter Student ID : ")
                    if student_id in users["students"]:
                        new_grade = input("New grade: ")
                        users["students"][student_id]["grade"] = int(new_grade)
                        print(f"Successfully changed {student_id}.")
                if tech_p == "2":
                    # Collect all unique classes
                    classes = set([users["students"][sid]["class"] for sid in users["students"]])
                    print("Available classes:")
                    for c in classes:
                        print(c)
                    cc = input("Choose class: ")
                    for k, v in users["students"].items():
                        if v["class"] == cc:
                            print(f"Student ID: {k}, Fullname: {v['fullname']}, Grade: {v['grade']}")
                if tech_p == "3":
                    ...


