# The Digital Detective: Explore Your Computer • Build a Mini System Report

## Student Information
| Field | Details |
| :--- | :--- |
| **Name** | Saksham Jaiswal |
| **USN** | 2402608065 |
| **Campus / Section** | A1 |
| **GitHub Username** | saksham1319 |
| **Repository Name** | digital-detective-8065 |
| **Repository URL** | https://github.com/saksham1319/digital-detective-8065 |

---

## Assignment Overview & Purpose
This repository contains my complete submissions and investigations for the **Diwali Independent Learning Assignment — The Digital Detective**. The primary objective of this project is to explore how personal computers and operating systems work beneath the surface through hands-on practical terminal activities, code execution, data representation modeling, and network inspections.

### Topics Explored
Across the 9 structured missions, this project investigates:
1. **Computer Fundamentals & the IPOS Cycle**: Input, Processing, Output, and Storage mechanics, along with hardware and software classifications.
2. **Terminal Navigation & File Operations**: POSIX shell commands, stream redirection (`>` vs `>>`), flags, UNIX pipes (`|`), and package managers.
3. **Operating System Architecture**: Kernel diagnostics, process scheduling, process IDs (PIDs), absolute vs. relative paths, and POSIX permissions (`rwx`).
4. **Execution Paradigms**: Comparing compilers and interpreters using a baseline Python execution test.
5. **Data Representation & Encodings**: Manual and programmatic conversions between base 10 (decimal), base 2 (binary), and base 16 (hexadecimal), character encodings (ASCII vs UTF-8), and an interactive Python number converter.
6. **Version Control & Collaboration**: Git staging, commits, feature branching (`update-about`), and a merged GitHub Pull Request workflow.
7. **Computer Networks**: Network scale (LAN, MAN, WAN), live diagnostics (`ping`, `nslookup`), DNS resolution, and the 6-stage lifecycle of opening a webpage.
8. **Synthesis & Verification**: Full quality assurance checklist, structural auditing, and submission reporting.

### Development & Commit Discipline
In strict adherence to the assignment guidelines:
- Every mission was tackled sequentially in strict numerical order (Mission 0 through Mission 8).
- Each mission has its own dedicated directory containing an extensive, standardized `README.md` detailing the tasks, tools, observations, difficulties faced, and resolutions in my own words.
- Each completed mission was verified, staged, and committed separately with a descriptive, meaningful commit message before proceeding to the next mission.
- All personal identifiable identifiers (usernames, local IPs, network IDs) have been safely redacted to protect privacy.

---

## Mission Index
| Mission | Focus Area | Directory Link | Status |
| :--- | :--- | :--- | :--- |
| **Mission 0** | Repository and workspace setup | [mission-00-setup/](mission-00-setup/README.md) | Completed |
| **Mission 1** | Computer fundamentals and IPOS | [mission-01-computer-basics/](mission-01-computer-basics/README.md) | Completed |
| **Mission 2** | Terminal and file management | [mission-02-terminal/](mission-02-terminal/README.md) | Completed |
| **Mission 3** | Operating system, processes and permissions | [mission-03-operating-system/](mission-03-operating-system/README.md) | Completed |
| **Mission 4** | How programs run | [mission-04-programs/](mission-04-programs/README.md) | Completed |
| **Mission 5** | Number systems, Python and text encoding | [mission-05-numbers-data/](mission-05-numbers-data/README.md) | Completed |
| **Mission 6** | Git, GitHub, branches and Pull Requests | [mission-06-git-github/](mission-06-git-github/README.md) | Completed |
| **Mission 7** | Computer networks | [mission-07-networking/](mission-07-networking/README.md) | Completed |
| **Mission 8** | Final review and submission | [mission-08-final-report/](mission-08-final-report/README.md) | Completed |

---

## My Learning
Completing these hands-on missions provided essential insights into the lower layers of computing:
1. **The Operating System as a Master Resource Arbiter**: Working with `ps aux`, `df -h`, and UNIX permissions (`rwx`) demonstrated that the OS is not just a graphical wrapper, but a protective layer that isolates memory, schedules CPU time across hundreds of competing threads, and prevents processes from compromising storage integrity.
2. **Data Representation & Information Encoding**: Manually breaking numbers down into binary bit-patterns and hexadecimal nibbles—and then confirming the mathematics in Python—solidified how all human symbols, text characters (via ASCII/UTF-8), and instructions boil down to fundamental high and low electrical states.
3. **Composability of Command-Line Utilities**: Moving away from the GUI showed the immense power of UNIX philosophy—combining single-purpose CLI utilities like `ls`, `grep`, and `head` via in-memory pipes (`|`) to filter and inspect system data without creating messy temporary files.
4. **Collaborative Engineering Discipline**: Managing branching, Pull Requests, and clear, granular commit checkpoints reinforced how professional software teams maintain codebase integrity and transparency.

---

## Running the Python Programs

### 1. Hello World (`mission-04-programs/hello.py`)
Run from the repository root:
```bash
python3 mission-04-programs/hello.py
```
Or navigate into the mission folder:
```bash
cd mission-04-programs
python3 hello.py
```

### 2. Number Converter Tool (`mission-05-numbers-data/number_converter.py`)
Run directly from its mission folder:
```bash
cd mission-05-numbers-data
python3 number_converter.py
```
Or run from the repository root:
```bash
python3 mission-05-numbers-data/number_converter.py
```
**Usage**: Enter any positive base-10 integer (e.g. `42`, `255`, or `8065`) to view its binary (`0b...`) and hexadecimal (`0x...`) conversions.
