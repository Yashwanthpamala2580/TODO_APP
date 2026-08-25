import sys
sys.path.append('./src')
from app import add_todo, view_todos, delete_todo, todos

def test_add_todo():
    todos.clear()
    add_todo("Test task")
    assert len(todos) == 1
    assert todos[0]["task"] == "Test task"
    print("✅ test_add_todo passed")

def test_delete_todo():
    todos.clear()
    add_todo("Task 1")
    add_todo("Task 2")
    delete_todo(0)
    assert len(todos) == 1
    assert todos[0]["task"] == "Task 2"
    print("✅ test_delete_todo passed")

def test_delete_invalid():
    todos.clear()
    add_todo("Task 1")
    delete_todo(5)   # invalid index
    assert len(todos) == 1  # todo should still exist
    print("✅ test_delete_invalid passed")

if __name__ == "__main__":
    test_add_todo()
    test_delete_todo()
    test_delete_invalid()
    print("All tests passed!")
