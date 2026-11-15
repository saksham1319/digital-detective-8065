# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 was to delve into core operating system responsibilities: auditing the running host operating system and hardware architecture, monitoring active background processes and process IDs (PIDs), understanding hierarchical filesystem paths (absolute vs. relative), inspecting UNIX file permissions (`rwx`), and summarizing how an OS manages computing resources.

---

## 2. Work completed

### Task 3.1 — Explore your operating system
I executed standard system diagnostic commands to query host platform details, storage quotas, and execution contexts. All user identifiers have been sanitized with `[redacted]` to comply with privacy requirements.

| Information Explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS kernel name, kernel release, CPU hardware architecture, and user-facing OS version. | macOS 27.0.1 (Build 26A434), Darwin Kernel Release 27.0.0, architecture `arm64` (Apple Silicon 64-bit). |
| **Current account identity** | Identifies the numeric User ID (UID), primary Group ID (GID), and active group memberships enforcing security boundaries. | `uid=501([redacted]) gid=20(staff) groups=20(staff),12(everyone),80(admin) ...` |
| **Available and used storage** | Shows overall filesystem capacity, consumed storage blocks, available free space, and mount points. | Root APFS container mounted on `/`: Total size `926 GiB`, Used `13 GiB`, Available `191 GiB` (7% capacity utilized). |
| **System activity snapshot** | Displays a real-time list of executing processes, CPU utilization percentages, and memory consumption. | Snapshot displayed active processes including `WindowServer` (PID 409, ~23% CPU), `locationd` (PID 386), and UI helper processes. |

---

### Task 3.2 — Understand processes

#### 1. What is a process?
A **process** is an active, executing instance of a computer program. When an application binary stored on a disk is launched, the operating system loads its machine instructions into memory (RAM), allocates private virtual address space, assigns execution threads, tracks CPU registers, and opens file descriptors. While a program is passive code residing on storage, a process is dynamic, living execution state managed by the CPU scheduler.

#### 2. What does the PID column represent?
The **PID (Process Identifier)** is a unique positive integer assigned by the operating system kernel to every single process when it is spawned. The OS kernel uses PIDs as indexing keys in its process table to schedule CPU time slices, allocate memory quotas, track parent-child relationships, and handle signal dispatching (such as pausing with `SIGSTOP` or terminating with `kill -9 <PID>`).

#### 3. Two examples of processes running on my computer:
1. **WindowServer (PID 409)**: A crucial macOS display compositing process that coordinates drawing windows, compositing visual surfaces, and routing keyboard/mouse events from hardware to active applications.
2. **zsh / Terminal (PID 1604 / 1617)**: The active interactive shell process providing the command-line interface, interpreting typed commands, and spawning sub-processes.

---

### Task 3.3 — Understand paths and permissions

#### Absolute Path vs. Relative Path:
- **Absolute Path**: An absolute path specifies the full, unambiguous location of a file or folder starting from the root of the filesystem (`/`). It is completely independent of where the user or shell is currently working.
  - *Example from assignment*: `/Users/[redacted]/digital-detective-8065/mission-03-operating-system/README.md`
- **Relative Path**: A relative path specifies a location starting from the shell's current working directory, using navigational indicators such as `.` (the current directory) or `..` (the parent directory).
  - *Example from assignment*: While working inside `terminal-practice/`, the relative path to this mission's README is `../mission-03-operating-system/README.md`.

#### Permissions Breakdown:
In UNIX-like operating systems, file permissions are expressed as a 10-character string (e.g., `-rw-r--r--`). The first character denotes file type (`-` for regular file, `d` for directory), followed by three triads representing **Owner**, **Group**, and **Others**.

| Permission | Meaning | Practical Example |
| :--- | :--- | :--- |
| **r — Read** | Grants permission to open and read the byte contents of a file (or list entries in a directory). | Opening and viewing a `.txt` or `.md` file in an editor or with `cat`. |
| **w — Write** | Grants permission to modify, overwrite, append to, or truncate file contents. | Saving edits made in a file, or redirecting text with `>` or `>>`. |
| **x — Execute** | Grants permission to execute the file as a program/binary/script (or traverse/enter a directory). | Running a compiled executable `./app` or Python shell script `./run.sh`. |

#### Owner Permissions Inspection:
Running `ls -l README.md` inside `terminal-practice/` or root yielded:
```text
-rw-r--r--@ 1 [redacted] staff 3486 Nov 16 01:16 README.md
```
- **Owner Permissions**: `rw-` (Read and Write enabled; Execute disabled).
- **Interpretation**: As the owner, my user account can view the text contents and make modifications. However, the file cannot be executed directly as an independent executable binary because the execute bit (`x`) is not set.

---

### Task 3.4 — Explain operating-system responsibilities

| OS Responsibility | Your explanation in your own words | Concrete Example |
| :--- | :--- | :--- |
| **Process management** | The OS creates, schedules, prioritizes, and terminates processes. It rapidly switches CPU core execution between multiple threads (context switching) to give the illusion of seamless simultaneous execution. | Allocating CPU time slices between Google Chrome, a Python build script, and background audio playback without freezing the user interface. |
| **Memory management** | The OS tracks every byte of physical RAM and virtual memory, allocating chunks to processes upon request and reclaiming them when processes exit to prevent memory leaks and unauthorized cross-process memory access. | Allocating 400 MB of heap memory when launching an IDE and isolating it so other apps cannot corrupt its address space. |
| **Device management** | The OS abstracts physical peripherals (printers, keyboards, network cards, GPUs) through specialized device drivers, translating generic software requests into hardware-specific electrical signals. | Translating an application's print command into low-level printer control language signals transmitted over USB or Wi-Fi. |
| **File management** | The OS organizes persistent data on storage drives into structured directories, managing file creation, deletion, naming, metadata, permissions, and disk block allocation tables (e.g., APFS, ext4). | Creating a nested folder structure like `mission-03-operating-system/` and mapping file byte ranges to specific flash memory blocks on an SSD. |
| **User interface / shell** | The OS provides an interface layer allowing human users to interact with hardware and kernel services, either graphically via a GUI desktop or programmatically through a CLI shell. | The macOS Finder graphical desktop allowing drag-and-drop file operations, and the Zsh command-line shell executing terminal instructions. |
| **Security and permissions** | The OS enforces authentication (passwords, biometrics) and authorization matrices (POSIX permissions, sandboxing) to ensure users and programs only access resources they have rights to use. | Requiring Touch ID / `sudo` administrative elevation before modifying protected system root directories like `/System` or `/usr/bin`. |

---

## 3. Commands / tools used
- `uname -srm`: Inspected kernel name (`Darwin`), kernel version (`27.0.0`), and machine architecture (`arm64`).
- `sw_vers`: Identified macOS product version and build number.
- `id`: Inspected active user ID, group ID, and group permissions.
- `df -h /`: Verified disk partition usage and available free gigabytes in human-readable format.
- `ps aux | head -n 8`: Inspected active process table snapshots, CPU/memory shares, and process identifiers (PIDs).
- `ls -l`: Inspected file permission strings (`rwx`) and ownership metadata.

## 4. My understanding
Before this mission, I thought of an operating system simply as the visual skin of my computer. Investigating processes, storage mounts, and permission bits showed me that the OS is essentially a master referee and resource broker. Every hardware access—reading a byte from disk, sending a network packet, or claiming a megabyte of RAM—is mediated by the OS kernel. Without strict process isolation and file permissions, any buggy or malicious script could overwrite operating system files or read private data from another program's memory.

## 5. Difficulties faced
Initially, understanding why a directory needs execute (`x`) permission was confusing, since directories are not executable programs.

## 6. How I resolved them
I researched UNIX filesystem semantics and learned that for directories, the execute (`x`) bit signifies "search/traverse" permission. Without the execute bit on a folder, you cannot enter it using `cd` or access files inside it, even if you have read (`r`) permission on the folder itself.

## 7. Evidence / files
- `mission-03-operating-system/README.md` (this report)
- Root `README.md` updated with completed status for Mission 3

## 8. Commit details
- **Commit Message**: `Document operating system and file management`
- **Pushed to Remote**: Branch `main` on `saksham1319/digital-detective-8065`.
