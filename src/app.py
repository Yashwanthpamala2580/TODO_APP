# Todo App - Version 1.1

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

def delete_todo(index):
    if index < 0 or index >= len(todos):
        print("Invalid todo number!")
        return
    removed = todos.pop(index)
    print(f"Deleted: {removed['task']}")

def main():
    print("=== Todo App v1.1 ===")
    add_todo("Buy groceries")
    add_todo("Read book")
    add_todo("Exercise")
    view_todos()
    print("\nDeleting second todo...")
    delete_todo(1)
    view_todos()

if __name__ == "__main__":
    main()
