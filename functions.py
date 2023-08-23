FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """ Reads a given file has default todos.txt."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILE_PATH):
    """ Writes a todo item """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_args)

# print("hello i am out ")
# print(__name__)
#
# if __name__ == "__main__":
#     print("hello i am in ")
