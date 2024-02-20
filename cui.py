# tasks list app for practice

from modules import functions

while True:
    user_input = input("Enter Add, Delete, Show, Exit or Edit : ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        task = user_input[4:] + "\n"
        tasks = functions.get_data()
        tasks.append(task)

        print("Your task has been added successfully!.. Type 'show' to see the changes")

        functions.write_data(tasks)

    elif user_input.startswith("exit"):
        break

    elif user_input.startswith("show"):
        tasks = functions.get_data()
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.title().strip("\n")} ")

    elif user_input.startswith("delete"):
        try:
            del_num = int(user_input[6:])
            tasks = functions.get_data()
            tasks.pop(del_num - 1)
            functions.write_data(tasks)

            print("Your task has been delete successfully!.. Type 'show' to see the changes")

        except ValueError:
            print("Please enter a integer after delete ")
            continue

    elif user_input.startswith("edit"):
        try:
            edit_no = int(user_input[5:])
            tasks = functions.get_data()
            new_task = input("Enter new tasks: ")
            tasks[edit_no - 1] = new_task + "\n"

            print("Your task has been edited successfully!.. Type 'show' to see the changes")
            functions.write_data(tasks)

        except ValueError:
            print("please enter a integer after edit")
            continue

    else:
        print("invalid command")
        continue
