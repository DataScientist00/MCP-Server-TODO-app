from fastmcp import FastMCP
import json
import os

app = FastMCP("todo-server")

DATA_FILE = "todos.json"

# Ensure todos.json exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_todos():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

@app.tool()
def add_todo(item: str) -> str:
    """Add a new todo item."""
    todos = load_todos()
    todos.append(item)
    save_todos(todos)
    return f" Added todo: {item}"

@app.tool()
def list_todos() -> list[str]:
    """List all todo items."""
    todos = load_todos()
    if not todos:
        return ["No todos yet!"]
    return [f"{i+1}. {t}" for i, t in enumerate(todos)]

@app.tool()
def remove_todo(index: int) -> str:
    """Remove a todo item by its index (1-based)."""
    todos = load_todos()
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        save_todos(todos)
        return f" Removed todo: {removed}"
    else:
        return f" Invalid index. You have {len(todos)} todos."

if __name__ == "__main__":
    app.run()
