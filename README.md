# Cloudbian_Helper

## Graphics Module

**Authors:** Cloudberry Pi Foundations

A simple Python library that makes data visualization easier using Matplotlib with a clean API and built-in 2D + 3D graphs.

### Table of Contents

- [Example Usage](#example-usage)
- [Installation](#installation)
- [Creating a Graph Object](#creating-a-graph-object)
- [2D Graphs](#2d-graphs)
- [Realtime Graph](#realtime-graph)
- [Save Graph](#save-graph)
- [3D Graphs (Value-Only API)](#3d-graphs-value-only-api)
- [Themes](#themes)
- [Full Example](#full-example)

### Example Usage

```python
from graphs import Graphs

g = Graphs(
    title="Animal Balance",
    theme="ggplot"
)

g.pie_chart(
    labels=["Humans", "Animals", "Insects"],
    values=[80, 50, 40]
)

g.bar_graph(
    labels=["Humans", "Animals", "Insects"],
    values=[80, 50, 40]
)

g.horizontal_bar_graph(
    labels=["Humans", "Animals", "Insects"],
    values=[80, 50, 40]
)
```
---

# Password Entry Module

A lightweight Tkinter-based password prompt utility that creates a simple GUI window for password input and validation.

## Example Usage

```python
from password_entry import start_password_entry

start_password_entry(
    required="mysecretpassword"
)
```

## Function Reference

### start_password_entry(required="abcd1234")

Creates a password entry window and validates user input against the required password.

#### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| required | str | The password that must be entered correctly |

#### Default Value

```python
required="abcd1234"
```

## Basic Usage

```python
from password_entry import start_password_entry

start_password_entry()
```

Uses the default password:

```text
abcd1234
```

## Custom Password

```python
from password_entry import start_password_entry

start_password_entry(
    required="admin123"
)
```

## How It Works

1. Creates a Tkinter window.
2. Displays a password input field.
3. Masks entered characters using `*`.
4. Waits for the user to press **Submit**.
5. Compares the entered password with the required password.

## Source Example

```python
from tkinter import *

def start_password_entry(required="abcd1234"):
    root = Tk()
    root.title("Enter your password")

    password = Entry(root, show="*")
    password.pack()

    def submit():
        passw = password.get()

        if passw == required:
            return True
        else:
            return False

    Button(root, text="Submit", command=submit).pack()

    root.mainloop()
```

## Notes

- Password characters are hidden while typing.
- Built using Python's standard Tkinter library.
- The current implementation validates the password but does not display success or failure messages.
- Can be extended with dialogs, callbacks, or custom UI elements.

---