<div align="center">

# 🐍 Python Mastery & Projects Repository

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/Nivedreddy6/Python?style=for-the-badge&color=orange)](https://github.com/Nivedreddy6/Python)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Nivedreddy6/Python?style=for-the-badge&color=purple)](https://github.com/Nivedreddy6/Python)

**A structured, practical repository containing real-world Python projects, Object-Oriented Programming (OOP) architectures, daily learning modules, algorithms, and data visualizations.**

[Explore Projects](#-featured-projects) • [Curriculum Breakdown](#-daily-learning--topic-breakdown) • [Getting Started](#-getting-started) • [Author](#-author)

---

</div>

## 📖 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Featured Projects](#-featured-projects)
  - [1. ATM Simulation System](#1-atm-simulation-system)
  - [2. University & Student Management System](#2-university--student-management-system)
- [Daily Learning & Topic Breakdown](#-daily-learning--topic-breakdown)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Code](#running-the-code)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🌟 Overview

This repository documents an end-to-end Python journey—spanning foundational programming concepts, data structures, control flows, advanced Object-Oriented Programming (OOP), file manipulation, regex, and data visualization.

Whether you're exploring core language mechanics, looking for OOP design patterns in Python, or referencing common algorithm implementations, this repository serves as a modular, hands-on codebase.

---

## ✨ Key Features

- **Object-Oriented Design**: Clean class hierarchies, inheritance, encapsulation, and polymorphism.
- **Robust Exception Handling**: Real-world edge case validation and defensive programming.
- **Data Structures in Practice**: Practical implementations of lists, dictionaries, tuples, and sets.
- **File & System Automation**: Context managers, file streams, and datetime operations.
- **Data Visualization**: Charts and statistical plots using `matplotlib`.
- **Modular & Executable**: Every script is self-contained and ready to execute.

---

## 🚀 Featured Projects

### 1. ATM Simulation System
📁 **File**: [`ATM__Project.py`](ATM__Project.py)

An interactive, terminal-based banking system simulating real ATM workflows using object-oriented principles.

**Core Functionalities:**
- 🔒 **PIN Authentication**: Secure 4-digit PIN verification with a 3-attempt lockout system.
- 💵 **Deposit Operations**: Automated threshold checks (minimum ₹1,000 in multiples of 100).
- 🏧 **Cash Withdrawal**: Balance checks, multi-denomination validation, and instant account updates.
- 📜 **Transaction History**: Real-time logging of all deposits and withdrawals during the session.

```bash
# Run the ATM simulation
python ATM__Project.py
```

---

### 2. University & Student Management System
📁 **File**: [`student_management_project.py`](student_management_project.py)

A clean demonstration of Python **Multiple Inheritance** and OOP modular design modeling academic relationships between faculty members and students.

**Core Highlights:**
- Demonstrates `super()` and explicit multi-parent constructor invocation (`faculty.__init__`, `student.__init__`).
- Unified dashboard view displaying faculty qualifications and student academic records.

```bash
# Run the Student Management System
python student_management_project.py
```

---

## 📅 Daily Learning & Topic Breakdown

| Phase | File | Primary Concepts Covered | Highlights |
| :--- | :--- | :--- | :--- |
| **Foundations** | [`day1.py`](day1.py) | Python Intro & Syntax | Dynamic typing, interpreted model, basic I/O |
| **Foundations** | [`day2.py`](day2.py) | Variables & Identifiers | Naming rules, conventions, memory allocation |
| **Operators** | [`day3.py`](day3.py) | Python Operators | Arithmetic, comparison, assignment, logical, bitwise |
| **Data Types** | [`day4.py`](day4.py) | Mutable vs Immutable | Int, float, string slicing and indexing |
| **Data Structures** | [`day5.py`](day5.py) | Lists & Nested Lists | Deep indexing, `.append()`, `.extend()`, mutation |
| **Data Structures** | [`day6.py`](day6.py) | Tuples & Dictionaries | Immutability, key-value mappings, tuple concatenation |
| **Data Structures** | [`day7.py`](day7.py) | Sets & Uniqueness | Unordered sets, deduplication, set operations |
| **I/O Handling** | [`day8.py`](day8.py) | Advanced User Input | Multi-variable parsing, `map()`, type casting |
| **Control Flow** | [`day9.py`](day9.py) | Conditional Logic | `if` / `elif` / `else`, grading algorithms |
| **Algorithms** | [`day11.py`](day11.py) | Nested Loops & Patterns | Right-angle star patterns, triangle matrices |
| **Algorithms** | [`day12.py`](day12.py) | List Manipulation | Deduplication algorithms, finding 1st & 2nd max |
| **OOP** | [`day_23.py`](day_23.py) | Polymorphism | Method overloading patterns, default parameters |
| **Defensive Code** | [`day_24.py`](day_24.py) | Exception Handling | `try` / `except` blocks, catching specific errors |
| **System I/O** | [`day_25.py`](day_25.py) | File Handling | `open()`, context managers (`with open`), read/write |
| **Text Processing**| [`day_26.py`](day_26.py) | Regular Expressions | `re` module, pattern searching, meta-characters |
| **Utilities** | [`day_28.py`](day_28.py) | Date & Time Operations | `datetime`, timestamp formatting (`strftime`) |
| **Visualization** | [`day_30.py`](day_30.py) | Data Visualization | `matplotlib.pyplot` line graphs, bar charts, custom labels |

---

## 🛠️ Getting Started

### Prerequisites
Make sure you have **Python 3.8+** installed on your system. Verify with:
```bash
python --version
```

*(Optional)* If you wish to run the visualization scripts (e.g., [`day_30.py`](day_30.py)), install `matplotlib`:
```bash
pip install matplotlib
```

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Nivedreddy6/Python.git
   ```
2. Navigate into the repository directory:
   ```bash
   cd Python
   ```

### Running the Code

Execute any standalone script directly:
```bash
# Run any daily topic
python day5.py

# Run advanced OOP exercises
python day_23.py

# Run Data Visualization
python day_30.py
```

---

## 💻 Tech Stack

- **Language**: Python 3.8+
- **Libraries & Tools**: `matplotlib`, `re`, `datetime`, Git & GitHub

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewExercise`)
3. Commit your Changes (`git commit -m 'Add new Python exercise'`)
4. Push to the Branch (`git push origin feature/NewExercise`)
5. Open a Pull Request

---

## 👤 Author

**Nived Reddy**
- 🐙 GitHub: [@Nivedreddy6](https://github.com/Nivedreddy6)
- ✉️ Email: [nivedreddy6@gmail.com](mailto:nivedreddy6@gmail.com)

---

<div align="center">
⭐ If you found this repository helpful, consider giving it a star!
</div>
