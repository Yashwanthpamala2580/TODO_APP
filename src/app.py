# Todo App - Version 1.0

todos = []

def add_todo(task):
    todos.append({"task": task, "done": False})
    print(f"Added: {task}")

def view_todos():
    if not todos:
        print("No todos yet!")
        return
    for i, todo in enumerate(todos):
        status = "✅" if todo["done"] else "❌"
        print(f"{i+1}. {status} {todo['task']}")

def main():
    print("=== Todo App v1.0 ===")
    add_todo("Buy groceries")
    add_todo("Read book")
    view_todos()

if __name__ == "__main__":
    main()
