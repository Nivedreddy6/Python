# 🚀 OOP & Advanced Python Concepts

Reference guide for advanced techniques covered in `day_23.py` through `day_30.py`.

---

## 🎭 1. Polymorphism & Method Overloading (`day_23.py`)

Python achieves method overloading natively via default arguments or variable-length arguments (`*args`, `**kwargs`):

```python
class Calculator:
    def add(self, a, b, c=0, d=0):
        return a + b + c + d

calc = Calculator()
print(calc.add(10, 20))        # 30
print(calc.add(10, 20, 30))    # 60
```

---

## 🛡️ 2. Exception Handling (`day_24.py`)

Safeguarding application flow against unexpected runtime errors:

```python
try:
    num = int(input("Enter number: "))
    result = 100 / num
except ValueError:
    print("Invalid input! Please enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
```

---

## 📁 3. File Operations & Context Managers (`day_25.py`)

Using `with open()` guarantees that file streams are automatically closed even if exceptions occur:

```python
# Writing to a file
with open("output.txt", "w") as f:
    f.write("Hello from Python File Handling!\n")

# Reading from a file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## 🔍 4. Regular Expressions (`day_26.py`)

Pattern matching using the `re` standard library:

```python
import re

text = "Python is a language created in 1991"
# Find all matching letters
matches = re.findall(r"[0-9]+", text)
print(matches)  # ['1991']
```

---

## 📊 5. Data Visualization with Matplotlib (`day_30.py`)

Creating line charts and bar graphs with labeled axes and titles:

```python
import matplotlib.pyplot as plt

overs = [1, 2, 3, 4, 5, 6]
score = [3, 19, 7, 2, 15, 9]

plt.plot(overs, score, marker='o', color='b')
plt.xlabel('Overs')
plt.ylabel('Score')
plt.title('Team Score Progress')
plt.grid(True)
plt.show()
```
