import sys
sys.path.append('./src')
from app import add_todo, view_todos, todos

def test_add_todo():
    todos.clear()
    add_todo("Test task")
    assert len(todos) == 1
    assert todos[0]["task"] == "Test task"
    assert todos[0]["done"] == False
    print("✅ test_add_todo passed")

def test_view_todos():
    todos.clear()
    add_todo("Task 1")
    add_todo("Task 2")
    assert len(todos) == 2
    print("✅ test_view_todos passed")

if __name__ == "__main__":
    test_add_todo()
    test_view_todos()
    print("All tests passed!")
