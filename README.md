# 🐍 Python Examples & Practice

[![Python Version](https://img.shields.io/badge/python-3.15+-blue.svg)](https://www.python.org/)
[![Package Manager](https://img.shields.io/badge/managed%20by-uv-purple.svg)](https://docs.astral.sh/uv/)
[![Course](https://img.shields.io/badge/Udemy-Course-EC5252.svg?logo=udemy&logoColor=white)](https://www.udemy.com/course/complete-python-with-ai-skills-to-get-your-dream-it-job/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A hands-on repository created to practice, experiment with, and master core concepts and practical projects from the Udemy course:

> **[Complete Python with AI Skills to Get Your Dream IT Job](https://www.udemy.com/course/complete-python-with-ai-skills-to-get-your-dream-it-job/)**

---

## 🎯 Purpose & Goals

- 💡 **Hands-on Practice**: Reinforce theory with real code samples and exercises.
- 🤖 **AI-Enhanced Workflows**: Learn how to leverage modern AI tools to accelerate development, debugging, and testing.
- 🚀 **Modern Tooling**: Managed with [`uv`](https://docs.astral.sh/uv/) for ultra-fast dependency resolution and virtual environment management.
- 💼 **Job-Ready Portfolio**: Build clean, well-documented code that reflects modern Python best practices.

---

## 📁 Project Structure

```text
Python_Examples/
├── .python-version          # Python target version (managed via uv)
├── pyproject.toml           # Project metadata and dependencies
├── README.md                # Project documentation and progress tracker
└── src/
    └── python_examples/     # Source modules and practice exercises
        ├── __init__.py      # Package entry point
        └── ...              # Topic modules, scripts, and practice labs
```

---

## 🛠️ Getting Started

### Prerequisites

- [Python](https://www.python.org/) 3.12+ (or 3.15+ if using preview builds)
- [uv](https://docs.astral.sh/uv/) (Recommended fast Python package manager)

Install `uv` (if not installed):
```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation & Execution

1. **Clone or navigate to the repository:**
   ```powershell
   cd d:\Projects\Python\Python_Examples
   ```

2. **Sync virtual environment & dependencies:**
   ```powershell
   uv sync
   ```

3. **Run the project:**
   ```powershell
   uv run python-examples
   ```

   Or run a specific script directly:
   ```powershell
   uv run python src/python_examples/__init__.py
   ```

---

## 📚 Learning Roadmap & Curriculum

Track course progression and topics covered:

- [ ] **Python Basics & Foundations**
  - Variables, Data Types, and Operators
  - Conditionals, Control Flow, and Loops
  - Functions, Scope, and Arguments
- [ ] **Data Structures & Collections**
  - Lists, Tuples, and Sets
  - Dictionaries and Comprehensions
  - Slicing and Advanced Indexing
- [ ] **Object-Oriented Programming (OOP)**
  - Classes, Instances, and Methods
  - Inheritance and Polymorphism
  - Encapsulation and Data Classes
- [ ] **Advanced Python Concepts**
  - Decorators and Generators
  - Context Managers (`with` statements)
  - Error and Exception Handling
  - File I/O and JSON Handling
- [ ] **Modern Python Tooling & Packaging**
  - Virtual environments and package management with `uv`
  - Code formatting, linting, and typing
- [ ] **AI-Assisted Development**
  - Prompting and pair programming with AI assistants
  - Automated testing and test case generation
  - Code refactoring and optimization with AI

---

## 📝 Notes & Practice Log

| Date | Topic / Section | Description / Key Takeaways | Code Path |
| :--- | :--- | :--- | :--- |
| *YYYY-MM-DD* | *Course Intro & Setup* | Project initialization with `uv` and workspace configuration | [`src/python_examples/__init__.py`](file:///d:/Projects/Python/Python_Examples/src/python_examples/__init__.py) |

---

## 👤 Author

- **Marlon** ([@marlonfsolisest](mailto:marlonfsolisest@gmail.com))
- Course: [Complete Python with AI Skills to Get Your Dream IT Job](https://www.udemy.com/course/complete-python-with-ai-skills-to-get-your-dream-it-job/)
