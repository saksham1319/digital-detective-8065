# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The goal of Mission 2 was to master essential command-line interface (CLI) interactions, safely manage files and directories without relying on a graphical user interface (GUI), understand how command-line flags and UNIX pipes transform data, and investigate how operating system package managers streamline software maintenance.

---

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations
I systematically practiced each standard POSIX terminal operation inside the project repository and recorded the observed behavior:

| Operation / Command Name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the absolute, full path of the working directory from the root `/`. | Output displayed `/Users/[redacted]/digital-detective-8065`. |
| **Directory listing (`ls`)** | Lists the non-hidden files and subdirectories located within the current folder. | Clean multi-column listing displaying `README.md`, `evidence`, and mission folders. |
| **Detailed listing (`ls -l`)** | Displays files in long format including permissions (`rwx`), hard link count, owner, group, byte size, and timestamp. | Output listed rows showing file metadata (e.g., `-rw-r--r-- 1 [redacted] staff 3486 Nov 16 01:16 README.md`). |
| **Change directory (`cd ..` and `cd <dir>`)** | Moves the shell context up or down within the directory hierarchy. | Running `cd ..` placed me in the parent directory; running `cd digital-detective-8065` returned me to the assignment root. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new directory at the specified target path. | Directory `terminal-practice` was created instantly without any warning or error. |
| **Create empty file (`touch sample.txt`)** | Creates an empty 0-byte file or refreshes the access/modification timestamps of an existing file. | File `sample.txt` was created with an initial size of 0 bytes. |
| **Copy file (`cp sample.txt sample_backup.txt`)** | Duplicates the source file into a distinct destination file while keeping the source intact. | Both `sample.txt` and `sample_backup.txt` coexisted independently in `terminal-practice/`. |
| **Move / rename file (`mv sample_backup.txt sample_archive.txt`)** | Renames a file or moves it to another directory path without creating a duplicate. | `sample_backup.txt` ceased to exist, and `sample_archive.txt` appeared containing the exact same data. |
| **Display file contents (`cat sample.txt`)** | Concatenates and prints the raw contents of a text file directly to the terminal stdout. | The text lines typed into `sample.txt` printed cleanly on the screen. |

---

### Task 2.2 — Practise file changes safely
Inside the dedicated `terminal-practice/` folder:
1. Created `sample.txt`.
2. Added the first line using output redirection:
   ```bash
   echo "Line 1: Exploring terminal file management as a digital detective." > sample.txt
   ```
3. Appended a second line without clobbering the first using append redirection:
   ```bash
   echo "Line 2: Appending a second line safely using redirection." >> sample.txt
   ```
4. Displayed with `cat sample.txt` and verified that both lines were preserved:
   ```text
   Line 1: Exploring terminal file management as a digital detective.
   Line 2: Appending a second line safely using redirection.
   ```
5. Made a backup copy (`cp sample.txt sample_backup.txt`) and renamed the backup (`mv sample_backup.txt sample_archive.txt`).

#### Conceptual Questions:
- **What is the difference between replacing a file's contents and adding text to the end?**
  Using the single right angle bracket `>` (overwrite redirection) opens the file in write/truncate mode. If the file exists, the operating system erases its existing contents and writes the new stream from byte 0. In contrast, the double right angle bracket `>>` (append redirection) opens the file in append mode, positioning the write pointer at the end of the existing file stream so existing text remains intact and the new line is added to the bottom.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) reads data from the source file and allocates brand new storage blocks to create a distinct second copy; modifying one copy later has no effect on the other. Moving (`mv`) in the same filesystem simply updates the directory pointer / inode link name without duplicating underlying disk blocks; no duplicate remains at the original name.
- **What information does the current-directory display provide?**
  The `pwd` (print working directory) command reveals the exact, unambiguous absolute path starting from the root directory `/` down to the current working location. This prevents dangerous mistakes such as accidentally executing deletion or overwrite commands in the wrong folder.
- **Why is a directory-listing operation useful?**
  `ls` gives immediate situational awareness. It lets you confirm whether expected files exist, check their spellings and extensions, inspect file permissions, check disk sizes, and identify hidden files that might affect build or configuration scripts.

---

### Task 2.3 — Understand flags and pipes

#### Flags Exploration:
- Default command: `ls`
  - Output: Bare names of files and folders in columns.
- Flagged command: `ls -lah`
  - `-l`: Long format showing permissions, owner, group, size, and date.
  - `-a`: All files, including hidden entries beginning with a dot (`.` and `..`, `.git`, `.DS_Store`).
  - `-h`: Human-readable size format (displaying sizes in `B`, `K`, `M`, or `G` instead of raw byte counts).
- **Comparison**: While plain `ls` only informs us that a file exists, `ls -lah` reveals crucial operational metadata—such as whether the file is executable, when it was last modified, and its exact storage footprint.

#### Pipes Exploration:
```bash
ls -la | head -n 5
```
- **Privacy-safe Output Observed**:
  ```text
  total 8
  drwxr-xr-x@ 15 [redacted]  staff   480 Nov 16 01:16 .
  drwxr-xr-x@  8 [redacted]  staff   256 Nov 16 01:15 ..
  drwxr-xr-x@ 12 [redacted]  staff   384 Nov 16 01:16 .git
  -rw-r--r--@  1 [redacted]  staff  3486 Nov 16 01:16 README.md
  ```
- **Explanation of the Pipe Operator (`|`)**:
  The vertical bar `|` connects the standard output (`stdout`) of the command on the left (`ls -la`) directly to the standard input (`stdin`) of the command on the right (`head -n 5`) via an in-memory unidirectional data stream.
- **Contribution of each side**:
  - **Left side (`ls -la`)**: Acts as the data producer. It reads the filesystem directory structure and emits the full detailed multi-line listing to its output stream.
  - **Right side (`head -n 5`)**: Acts as the stream consumer/filter. It captures the incoming stream line by line, prints only the first 5 lines to the terminal screen, and terminates the stream, discarding the remainder without requiring temporary intermediate files.

---

### Task 2.4 — Understand package managers
I checked the package management setup on my macOS environment:
- Command: `brew --version`
- Output: `Homebrew 7.0.13-134-g7b68472`
- Managed packages: Running `brew list` showed installed packages including `git`, `python@3.14`, `gh`, `node`, `ripgrep`, `cmake`, and `curl`.

#### Why package managers are useful:
A package manager automates the entire software lifecycle on an operating system—handling software discovery, checksum verification, dependency resolution, installation, and future version updates with single terminal commands. Without a package manager, developers would have to manually locate tarballs, compile C/C++ source code, link dynamic shared libraries, and troubleshoot missing dependencies manually. By centralizing repository management, tools like Homebrew on macOS or `apt` on Linux ensure software environments remain reproducible, secure, and easy to maintain.

---

## 3. Commands / tools used
- `pwd`: Displayed current working directory.
- `ls`, `ls -l`, `ls -lah`: Directory listing and detailed metadata inspection.
- `cd`: Path navigation.
- `mkdir`: Directory creation.
- `touch`: File creation.
- `cp`: File replication.
- `mv`: File renaming.
- `cat`: File contents inspection.
- `>`, `>>`: Stream redirection (truncate vs. append).
- `|`: UNIX pipe operator connecting stdout to stdin.
- `head -n 5`: Stream filter limiting output to 5 lines.
- `brew --version` / `brew list`: Inspected Homebrew package manager state.

## 4. My understanding
Working in the terminal fundamentally changes how you interact with a computer. In a GUI, you are limited by what buttons and menus a software designer decided to put on the screen. In the terminal, every command is a modular tool following the UNIX philosophy: write programs that do one thing well, and connect them together using pipes and redirection to build custom data processing pipelines. Understanding redirect operators (`>` vs `>>`) is also vital because a typo using `>` can accidentally wipe an important configuration file.

## 5. Difficulties faced
When practicing the pipe command `ls -la | head -n 5`, the output included system usernames and timestamps that needed to be redacted to conform to the strict assignment privacy rules before committing.

## 6. How I resolved them
I sanitized the terminal logs, replacing the active username and machine names with `[redacted]` and confirming that no sensitive IP addresses or private device identifiers were exposed in markdown tables or logs.

## 7. Evidence / files
- `terminal-practice/sample.txt`
- `terminal-practice/sample_archive.txt`
- `mission-02-terminal/README.md` (this report)

## 8. Commit details
- **Commit Message**: `Complete Terminal and file management mission`
- **Pushed to Remote**: Branch `main` on `saksham1319/digital-detective-8065`.
