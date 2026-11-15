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

## Assignment Overview
This repository contains my completed work for the **Diwali Independent Learning Assignment — The Digital Detective**. The purpose of this project is to explore how modern computers operate under the hood through hands-on practical investigation across 9 structured missions. 

Throughout these missions, I explore core hardware and the IPOS cycle, basic and intermediate Terminal navigation, operating system processes and file security permissions, program translation differences between compilers and interpreters, number representation and binary/hex conversion with Python, collaborative Git and GitHub workflows (including branching and pull requests), and foundational networking protocols.

### Development Approach
In accordance with the assignment guidelines:
- Every mission was tackled sequentially in strict numerical order (Mission 0 through Mission 8).
- Each mission has its own dedicated folder containing a comprehensive `README.md` documenting the exact tasks performed, tools used, conceptual explanations in my own words, real observations, difficulties faced, and how they were resolved.
- Each mission was verified, staged, and committed independently with a descriptive commit message representing a checkpoint before advancing to the next mission.
- Privacy was preserved by redacting local network addresses, usernames, and sensitive system identifiers.

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
| **Mission 8** | Final review and submission | [mission-08-final-report/](mission-08-final-report/README.md) | Pending |

---

## My Learning
Through the hands-on missions completed so far, I have gained practical, under-the-hood insights into computing systems:
1. **The Operating System as a Master Resource Arbiter**: Working with `ps aux`, `df -h`, and UNIX permissions (`rwx`) demonstrated that the OS is not just a graphical wrapper, but a protective layer that isolates memory, schedules CPU time across hundreds of competing threads, and prevents processes from compromising storage integrity.
2. **Data Representation & Information Encoding**: Manually breaking numbers down into binary bit-patterns and hexadecimal nibbles—and then confirming the mathematics in Python—solidified how all human symbols, text characters (via ASCII/UTF-8), and instructions boil down to fundamental high and low electrical states.
3. **Composability of Command-Line Utilities**: Moving away from the GUI showed the immense power of UNIX philosophy—combining single-purpose CLI utilities like `ls`, `grep`, and `head` via in-memory pipes (`|`) to filter and inspect system data without creating messy temporary files.

---

## Quick Start: Running the Python Programs
As part of Missions 4 and 5, Python scripts are included in the repository.

### 1. Hello World (`mission-04-programs/hello.py`)
```bash
python3 mission-04-programs/hello.py
```

### 2. Number Converter Tool (`mission-05-numbers-data/number_converter.py`)
```bash
python3 mission-05-numbers-data/number_converter.py
```
This utility prompts for a positive base-10 integer and computes its binary and hexadecimal equivalents.
