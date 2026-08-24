# 📘 Python Fundamentals Cheatsheet

A quick reference guide to core Python concepts based on our daily learning exercises (`day1.py` to `day12.py`).

---

## 🏷️ Variables & Identifiers (`day2.py`)

- **Valid Identifiers**: Start with letters (`a-z`, `A-Z`) or underscore (`_`).
- **Invalid Identifiers**: Starting with numbers (`1var`), special characters (`$var`), or containing spaces.
- **Convention**: Use lowercase with underscores (`snake_case`) for variable and function names.

---

## 🧱 Data Types & Mutability (`day4.py` - `day7.py`)

| Data Type | Syntax | Mutable? | Ordered? | Duplicates Allowed? |
| :--- | :--- | :--- | :--- | :--- |
| **Integer / Float** | `10`, `3.14` | ❌ No | N/A | N/A |
| **String** | `"Hello"` | ❌ No | ✅ Yes | ✅ Yes |
| **List** | `[1, 2, "a"]` | ✅ Yes | ✅ Yes | ✅ Yes |
| **Tuple** | `(1, 2, "a")` | ❌ No | ✅ Yes | ✅ Yes |
| **Set** | `{1, 2, 3}` | ✅ Yes | ❌ No | ❌ No |
| **Dictionary** | `{"key": "value"}` | ✅ Yes | ✅ (3.7+) | Keys: ❌ No, Values: ✅ Yes |

---

## 🧮 Operators Reference (`day3.py`)

- **Arithmetic**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponentiation)
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`
- **Identity & Membership**: `is`, `is not`, `in`, `not in`

---

## ✂️ Indexing & Slicing (`day4.py`, `day5.py`)

```python
text = "Python"
print(text[0])     # 'P'
print(text[-1])    # 'n'
print(text[0:4])   # 'Pyth' (slice: start:stop)
print(text[::-1])  # 'nohtyP' (reversed)
```
