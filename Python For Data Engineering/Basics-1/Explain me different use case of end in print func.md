# Python `print()` `end` Parameter & Line Continuation — Revision Notes

> **Purpose:** Quick yet thorough revision with **clear explanations, detailed comments, and examples** — all in **one Markdown file**.

---

## 1️⃣ `print()` Function — The `end` Parameter

### What `end` Does

* `end` controls **what is printed after the current `print()` output**.
* Default value is a newline (`"\n"`), which moves output to the next line.
* By changing `end`, you can keep output on the **same line** or add **custom separators**.

```python
# Default behavior (end='\n')
print("Hello")
print("World")
# Output:
# Hello
# World
```

---

## 2️⃣ Common & Practical Use Cases of `end`

### Use Case 1: Same Line with Space

```python
# end=" " replaces the newline with a space
print("Hello", end=" ")
print("World")
# Output: Hello World
```

**Why:** Useful when splitting output across multiple statements.

---

### Use Case 2: No Separator (Concatenation)

```python
# end="" prints without adding anything
print("H", end="")
print("e", end="")
print("l", end="")
print("l", end="")
print("o")
# Output: Hello
```

**Why:** Character-by-character or streaming-style output.

---

### Use Case 3: Loop Output with Custom Separator

```python
# Print numbers on one line separated by commas
for i in range(5):
    print(i, end=", ")
# Output: 0, 1, 2, 3, 4,
```

**Note:** This leaves a trailing comma — handled later.

---

### Use Case 4: Custom Characters as `end`

```python
# Using a dash as a visual separator
print("Item 1", end=" - ")
print("Item 2", end=" - ")
print("Item 3")
# Output: Item 1 - Item 2 - Item 3
```

**Why:** Improves readability of chained outputs.

---

### Use Case 5: Tab (`\t`) for Column Alignment

```python
# Tab-separated output
print("Name", end="\t")
print("Age", end="\t")
print("City")
# Output:
# Name    Age     City
```

**Why:** Simple column formatting without extra libraries.

---

### Use Case 6: Progress / Status Simulation

```python
# Simulating steps in a process
for i in range(1, 6):
    print(f"Step {i}", end=" >>> ")
print("Done!")
```

**Why:** Visual feedback during execution.

---

### Use Case 7: CSV-like Output

```python
# Printing rows in CSV format
data = [[1, 2, 3], [4, 5, 6]]

for row in data:
    for item in row:
        print(item, end=",")
    print()  # Newline after each row
```

**Why:** Useful for exporting or viewing tabular data.

---

### Use Case 8: Avoid Trailing Separator (Best Practice)

```python
# Conditional end to avoid last comma
numbers = [1, 2, 3, 4, 5]

for i, num in enumerate(numbers):
    end_char = ", " if i < len(numbers) - 1 else "\n"
    print(num, end=end_char)
# Output: 1, 2, 3, 4, 5
```

**Why:** Clean, professional output formatting.

---

### Use Case 9: Real-Time Output (`flush=True`)

```python
# Prints dots without buffering
for _ in range(10):
    print(".", end="", flush=True)
```

**Why:** Loading indicators, progress bars.

---

### Use Case 10: Matrix / Table Display

```python
# Displaying a matrix in table form
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(f"{item:2d}", end=" | ")
    print()  # Move to next row
```

---

## 3️⃣ Line Continuation in Python

Line continuation allows breaking **long logical lines** into multiple **physical lines**.

### Two Types

1. **Explicit continuation** using backslash (`\`)
2. **Implicit continuation** using brackets — **recommended**

---

## 4️⃣ Explicit Line Continuation (`\`)

```python
# Using backslash to continue expression
result = 10 + \
         20 + \
         30 + \
         40

print(result)  # Output: 100
```

### ⚠ Problems with Explicit Continuation

* Trailing space after `\` → **SyntaxError**
* Hard to spot visually
* Not PEP 8 recommended

---

## 5️⃣ Implicit Line Continuation (Best Practice ✅)

Python automatically continues lines inside:

* Parentheses `()`
* Brackets `[]`
* Braces `{}`

---

### Example 1: Mathematical Expression

```python
# Cleaner and safer than backslash
result = (
    100 +
    200 +
    300 -
    50
)
```

---

### Example 2: Function Call

```python
print(
    "Name:", "Rajan",
    "Age:", 22,
    "City:", "Bangalore",
    sep=" | "
)
```

---

### Example 3: List Declaration

```python
numbers = [
    1,
    2,
    3,
    4,
    5
]
```

---

### Example 4: Dictionary Declaration

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

---

### Example 5: Implicit String Concatenation

```python
message = (
    "This is a long message "
    "split across multiple lines "
    "without using backslashes"
)
```

---

## 6️⃣ Combining `end` with Implicit Continuation

```python
print(
    "Name:", "Rajan",
    "Age:", 22,
    "City:", "Bangalore",
    sep=" | ",
    end="\n"
)
```

---

## 7️⃣ Revision Checklist (Quick Recall)

* `end` controls **what comes after print output**
* Default: `end='\n'`
* `end=''` → no separator
* `end=' '` → same line with space
* Use `flush=True` for real-time output
* Prefer **implicit line continuation**
* Avoid backslash unless unavoidable

---

## 8️⃣ Best Practices

* Keep output formatting readable
* Avoid trailing separators
* Follow PEP 8 line length guidelines
* Prefer clarity over cleverness

---

## References (for further reading)

* Python Official Documentation
* PEP 8 — Style Guide for Python Code
* GeeksForGeeks — Python `print()` Function

---

> ✅ **This file is optimized for revision, interviews, and daily practice.**
