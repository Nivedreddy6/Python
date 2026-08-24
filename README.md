<div align="center">

# 🐍 Python Mastery & Projects Repository

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/Nivedreddy6/Python?style=for-the-badge&color=orange)](https://github.com/Nivedreddy6/Python)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/Nivedreddy6/Python?style=for-the-badge&color=purple)](https://github.com/Nivedreddy6/Python)

**A comprehensive, production-grade Python repository featuring real-world applications, Object-Oriented Programming (OOP) architectures, daily programming modules, data structures, and data visualization.**

[Explore Projects](#-featured-projects) • [Tech Stack](#-technologies--tools-used) • [Curriculum Breakdown](#-daily-learning--topic-breakdown) • [Getting Started](#-getting-started) • [Author](#-author)

---

</div>

## 📖 Table of Contents

- [Overview](#-overview)
- [Technologies & Tools Used](#-technologies--tools-used)
- [Key Architectural Highlights](#-key-architectural-highlights)
- [Featured Projects](#-featured-projects)
  - [1. ATM Simulation System](#1-atm-simulation-system)
  - [2. University & Student Management System](#2-university--student-management-system)
- [Daily Learning & Topic Breakdown](#-daily-learning--topic-breakdown)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Code](#running-the-code)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🌟 Overview

This repository documents an end-to-end Python journey—spanning foundational programming concepts, data structures, control flow algorithms, advanced Object-Oriented Programming (OOP), file manipulation, regular expressions, and data visualization.

Whether you are exploring core language mechanics, referencing OOP design patterns in Python, or looking for algorithm implementations, this repository serves as a modular, hands-on reference codebase.

---

## 💻 Technologies & Tools Used

### 🛠️ Technology Stack Breakdown

| Category | Technologies & Tools | Description / Use Case in Project |
| :--- | :--- | :--- |
| **Core Language** | ![Python](https://img.shields.io/badge/Python_3.8+-3776AB?style=flat-square&logo=python&logoColor=white) | Primary language used across all projects, scripts, and algorithms |
| **Data Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white) | Used for line graphs, categorical bar charts, axis styling, and data rendering in [`day_30.py`](day_30.py) |
| **Standard Libraries** | ![RegEx](https://img.shields.io/badge/RegEx_(re)-Standard_Library-4B8BBE?style=flat-square) ![DateTime](https://img.shields.io/badge/DateTime-Standard_Library-306998?style=flat-square) | Built-in modules used for pattern matching ([`day_26.py`](day_26.py)) and date/time formatting with `strftime` ([`day_28.py`](day_28.py)) |
| **System & I/O** | ![File IO](https://img.shields.io/badge/File_I%2FO-Context_Managers-FFD43B?style=flat-square&logoColor=black) | File stream buffers and persistent storage operations using `open()` and `with open()` ([`day_25.py`](day_25.py)) |
| **Programming Paradigms** | ![OOP](https://img.shields.io/badge/OOP-Multiple_Inheritance-2b5b84?style=flat-square) ![Exception Handling](https://img.shields.io/badge/Defensive_Coding-try...except-e05d44?style=flat-square) | Object-oriented systems ([`ATM__Project.py`](ATM__Project.py), [`student_management_project.py`](student_management_project.py)) and robust exception handling ([`day_24.py`](day_24.py)) |
| **Version Control** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) | Source code management, semantic commits, and remote repository hosting |

---

## ✨ Key Architectural Highlights

- **Object-Oriented Design**: Clean class hierarchies, multiple inheritance, encapsulation, and polymorphism.
- **Defensive Error Handling**: Catching domain-specific exceptions (`TypeError`, `ValueError`, `ZeroDivisionError`, `NameError`).
- **Data Structures in Practice**: Deep indexing and manipulation across lists, dictionaries, tuples, and sets.
- **System & Stream Management**: Context managers (`with open`) ensuring safe file operations.
- **Statistical Visualization**: Data plotting, axis customization, and chart generation using `matplotlib`.

---

## 🚀 Featured Projects

### 1. ATM Simulation System
📁 **File**: [`ATM__Project.py`](ATM__Project.py)

An interactive, terminal-based banking system simulating real ATM workflows using object-oriented principles.

**Key Features:**
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

**Key Features:**
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
