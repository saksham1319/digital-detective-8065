# Mission 1 — Know your computer

## 1. Task / objective
The objective of this mission was to investigate the fundamental architecture of modern computing systems through the lens of the **IPOS** (Input, Processing, Output, Storage) model, classify physical hardware versus software categories (operating system, application, and utility), and examine real-world embedded computer systems we interact with every day outside of personal laptops and smartphones.

---

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
I selected the activity of **writing, compiling, and saving a Python script in a text editor (VS Code)**.

| Stage | What happens in this activity? | Hardware / Component involved |
| :--- | :--- | :--- |
| **Input** | I type lines of Python code using the physical keyboard and click buttons or select menus with the trackpad. The keyboard microcontroller scans keystroke matrices and generates electrical scan codes sent to the computer. | Keyboard, Trackpad / Optical Mouse |
| **Processing** | The CPU interprets keyboard interrupts from the OS, translates scan codes into UTF-8 character codes, and places the characters into an active memory buffer in RAM. When I hit run, the CPU schedules the Python runtime process to parse and execute instructions. | CPU (Processor cores), System RAM (Main Memory), Cache (L1/L2/L3) |
| **Output** | As I type, the GPU/Display controller updates the frame buffer and renders text characters and UI elements instantly on the screen with syntax highlighting. When the script runs, standard output prints text directly to the integrated terminal window. | Monitor / Retina Display, GPU |
| **Storage** | When I press `Cmd + S` (Save), the operating system's filesystem driver flushes the temporary text buffer held in volatile RAM across the bus into permanent non-volatile flash storage as a `.py` file. | NVMe Solid-State Drive (SSD) / Flash Storage |

#### How the activity flows from Input to Output and Storage:
When a key is struck, hardware generates an interrupt signal causing the CPU to pause background tasks momentarily, read the input register, and update the active application's memory space in RAM. Because RAM is fast, the display pipeline can refresh at 60Hz or 120Hz to render output on the screen with imperceptible latency. However, because RAM is volatile (it loses all data if power is cut), the work is not safe until the storage step occurs, where the OS filesystem (e.g. APFS) organizes the bytes into storage blocks on the SSD.

---

### Task 1.2 — Identify hardware and software
I cataloged 5 hardware components and 5 software components that I actively interact with on my system.

| Item / Software Name | Hardware or Software? | Software Type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Mechanical Keyboard** | Hardware | Not applicable | Captures tactile keystrokes and transmits USB HID input signals to the OS. |
| **Multi-touch Trackpad** | Hardware | Not applicable | Translates finger gestures (tapping, two-finger scrolling, pinching) into pointer coordinates. |
| **Retina Display Panel** | Hardware | Not applicable | Provides real-time visual output of graphical windows, text, and media at high pixel density. |
| **NVMe SSD Storage** | Hardware | Not applicable | Non-volatile flash storage storing the OS, applications, git repositories, and user data across reboots. |
| **Apple Silicon M-Series SoC** | Hardware | Not applicable | Combines CPU cores, GPU cores, Neural Engine, and unified memory architecture to process instructions. |
| **macOS (Darwin Kernel)** | Software | Operating System Software | Manages system resources, CPU process scheduling, virtual memory management, device drivers, and security isolation. |
| **Visual Studio Code** | Software | Application Software | An interactive development environment (IDE) for code editing, syntax checking, debugging, and terminal execution. |
| **Google Chrome** | Software | Application Software | Web browser used for accessing course material, online documentation, researching syntax, and testing web applications. |
| **Activity Monitor / htop** | Software | Utility Software | System monitoring utility that displays real-time CPU, RAM, disk I/O, and battery consumption per process. |
| **Disk Utility / fsck** | Software | Utility Software | Disk maintenance utility used to inspect drive health, partition disks, verify APFS container integrity, and format storage. |

---

### Task 1.3 — Computer systems around you
I investigated three automated, computer-based systems encountered in public infrastructure:

| System | Main Purpose | One Input | One Output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Allows banking customers to withdraw physical currency, check balances, and deposit funds autonomously without a bank teller. | Keypad / PIN pad entering authentication PIN (or card chip NFC reader). | Physical cash dispenser mechanism dispensing banknotes (and receipt paper printer). |
| **Smart Traffic Signal Controller** | Dynamically regulates the flow of vehicular and pedestrian traffic at road intersections based on real-time congestion levels. | Inductive loop magnetic sensors embedded under the road asphalt detecting vehicle presence. | High-visibility LED traffic signal lanterns displaying Red, Amber, or Green lights. |
| **Metro Ticket Vending Machine (TVM)** | Issues passenger transit tokens or recharges contactless smart cards in public rapid transit stations. | Touchscreen interface selecting the destination station and passenger quantity. | Dispenser chute dropping the physical encoded RFID travel token / printed QR ticket. |

---

## 3. Commands / tools used
- Conceptual modeling and analytical breakdown of system components.
- Terminal commands `system_profiler SPHardwareDataType` and `sw_vers` were used to verify exact hardware and OS specifications on my machine.

## 4. My understanding
Through this mission, I realized that every digital device—from a supercomputer down to a modest traffic light controller—relies on the same continuous loop: accepting raw input, running algorithmic processing on that data, rendering human-understandable or mechanical output, and persisting key states to non-volatile storage. 

Understanding the distinction between volatile memory (RAM) and non-volatile storage (SSD/HDD) made it obvious why auto-save features exist and why power loss before writing to storage causes data loss. Additionally, categorizing software helped clarify that application software cannot speak directly to hardware pins or raw memory blocks; it relies on the operating system layer to safely arbitrate resource access.

## 5. Difficulties faced
When analyzing utility software versus application software, tools like `htop` or `Activity Monitor` feel like applications because they have a GUI. I had to think carefully about what distinguishes a utility from an application.

## 6. How I resolved them
I reviewed the fundamental definition: applications serve the *user's end-goals* (e.g., editing text, browsing a website, playing a game), whereas utilities serve to *maintain, analyze, optimize, or protect the health and efficiency of the computer system itself*. Since Activity Monitor exists to inspect and diagnose OS processes and hardware resource limits, it firmly belongs in the utility software category.

## 7. Evidence / files
- `mission-01-computer-basics/README.md` (this report)
- Root `README.md` updated with completed status for Mission 1

## 8. Commit details
- **Commit Message**: `Complete computer basics and IPOS mission`
- **Pushed to Remote**: Branch `main` on `saksham1319/digital-detective-8065`.
