import os

FILEPATH = "todos.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as file:
        pass

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        # readlines() returns the list datatype and
        # it is referenced by todos
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    print('filePath',filepath)
    print('todos:',todos_arg)
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print("In Functions.py __name__: ", __name__)
if __name__ == "__main__":
    print ("hello from function.py")
    print (get_todos())