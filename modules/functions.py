def get_data(filepath="main.txt"):
    with open(filepath, "r") as file:
        tasks = file.readlines()
        return tasks


def write_data(tasks_arg, filepath="main.txt"):
    with open(filepath, "w") as file:
        file.writelines(tasks_arg)
