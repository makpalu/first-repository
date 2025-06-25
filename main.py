from todolistBSC import Todo, Todolist

# # todo_name = input("Enter a todo: ")
# todo1 = Todo(todo_name, 1, 1, 20, False, True)
# todolist1 = Todolist("School work", "For keeping school stuff")
# for i in range(1, 6):
#     todolist1.add_todo(Todo(input(f"Enter todo {i}"), i, i, 23, False, True))
# todolist1.add_todo(todo1)
# print(todolist1.get_todo_names())

#Write a program that allows you to create multiple todolist and multiple todos and be able to store the todos and the todolist
def create_todolists():
    todolist = Todolist(input("Enter the name of the todolist: "), input("Enter the description: "))
    todolists.append(todolist)

def create_todo(selected_todolist):
    todo_name = input("Enter your task: ")
    todo_id = input("Enter the id: ")
    todo_level = input("Enter the priority level: ")
    todo_deadline = input("Enter the deadline: ")
    todo = Todo(todo_name, todo_id, todo_level, todo_deadline, False, True)
    selected_todolist.add_todo(todo)

def select_todolist():
    print("Select the todolist to add it to: ")
    for index, element in enumerate(todolists, 1):
        print(f"{index}. {element.get_name()}")

    user_input = 0

    while user_input < 1 or user_input > len(todolists):
        user_input = int(input(("Enter your option: ")))
    return todolists[user_input - 1]


def view_todos():
    
    view_selected_todos = select_todolist()

    for index, a_todo in enumerate(view_selected_todos.get_todos(), 1):
        print(f"{index}. {a_todo.get_name()}")




is_running = True
todolists = []
selected_todolist = None
view_selected_todos = None

while is_running:
    print("Enter 1 to create a todolist\nEnter 2 to create a todo\nEnter 3 to view todos\nEnter 4 to quit")
    x = input("x: ")
    if x == "1":
        create_todolists()

    elif x == "2":
        if not todolists:
            print("Todolist not available. Create one first.")
            continue
        
        selected_todolist = select_todolist()

        create_todo(selected_todolist)
        
    elif x == "3":
        view_todos()
    
    elif x == "4":
        is_running = False
    
    else:
        print("Enter a valid input.")



