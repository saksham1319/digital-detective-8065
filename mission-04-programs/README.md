# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 was to write and execute a baseline Python script (`hello.py`) from the terminal, observe how high-level code translates into execution, and analyze the architectural differences between compiled languages and interpreted languages.

---

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created `hello.py` inside `mission-04-programs/` containing the required one-line print statement:
  ```python
  print("Hello from Python")
  ```
- Executed the script from the command line using the Python 3 interpreter:
  ```bash
  python3 hello.py
  ```
- **Observed Terminal Output**:
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point of Comparison | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | The complete source code is analyzed, optimized, and translated into target machine code **ahead of time** (build/compile time) before any execution occurs. | The source code is parsed, translated, and evaluated **at runtime**, executing instructions line-by-line (or via just-in-time bytecode execution). |
| **Typical output** | A standalone executable binary file (e.g. Mach-O on macOS, ELF on Linux, `.exe` on Windows) or intermediate object files (`.o`). | Immediate direct execution in memory; no standalone native machine-code binary is persisted to disk. |
| **One example** | **C / C++** (using `gcc` or `clang`), **Rust** (`rustc`), or **Go**. | **Python** (CPython runtime), **Ruby**, or **JavaScript** (Node.js engine). |
| **One advantage** | **High execution performance and optimization**: Because compilation occurs beforehand, machine instructions run directly on bare metal CPU registers without translation overhead. | **Portability and rapid development cycle**: Source code runs on any machine with the interpreter installed, and developers can test code interactively without repeated recompilation steps. |

#### Synthesis of Differences:
A **compiler** and an **interpreter** serve the same ultimate goal—translating human-written code into machine-executable electrical instructions—but they do so at completely different stages of the development lifecycle. A compiler converts the entire program all at once before runtime, producing a self-contained binary tailored specifically to the host CPU architecture, which makes it extremely fast but platform-dependent. In contrast, an interpreter processes instructions dynamically on the fly while the program is running, making debugging and cross-platform sharing much more flexible at the cost of some execution speed. Modern runtimes like Python actually bridge this gap by compiling source code into portable bytecode (`.pyc`) before feeding it to an internal virtual machine interpreter.

---

## 3. Commands / tools used
- `touch hello.py`: Created the Python source script.
- `cat << 'EOF' > hello.py`: Authored the one-line print statement.
- `python3 hello.py`: Invoked the CPython 3.9 interpreter runtime to execute the script.

## 4. My understanding
Before completing this task, I assumed languages were strictly either "compiled" or "interpreted". By running Python and studying compilation pipelines, I learned that compilation is actually an implementation detail rather than an inherent property of a language. Python code is first compiled into intermediate Python Bytecode (represented by opcodes), which is then interpreted by the CPython virtual machine. Understanding this distinction clarifies why compiled binaries run orders of magnitude faster in performance-critical software like games or operating systems, while interpreted scripts shine in scripting, automation, and data analysis.

## 5. Difficulties faced
When typing the command in the shell, running `python hello.py` instead of `python3 hello.py` initially caused an error (`zsh: command not found: python`) because modern versions of macOS no longer alias `python` to Python 2 after its deprecation.

## 6. How I resolved them
I explicitly used `python3 hello.py`, targeting the installed Apple Developer Python 3.9.6 toolchain. I verified that using the full `python3` binary name is best practice across modern UNIX systems.

## 7. Evidence / files
- `mission-04-programs/hello.py`
- `mission-04-programs/README.md` (this report)

## 8. Commit details
- **Commit Message**: `Compare compilers and interpreters`
- **Pushed to Remote**: Branch `main` on `saksham1319/digital-detective-8065`.
