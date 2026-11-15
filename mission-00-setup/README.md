# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The goal of Mission 0 was to establish a clean, well-structured local working environment and remote GitHub repository following the prescribed naming convention (`digital-detective-<last 4 digits of USN>`), verify prerequisite software installations (Python 3 and Git), and set up the mission folder hierarchy and placeholder files for the entire project.

## 2. Work completed
- Determined the project repository name based on my USN (`2402608065`): `digital-detective-8065`.
- Initialized a local Git repository on my machine with the primary branch set to `main`.
- Verified that both Python 3 and Git were installed, operational, and accessible via the terminal.
- Created all 9 designated mission folders along with the `evidence/` directory.
- Created initial placeholder files including `README.md` in each mission directory and `number_converter.py` in `mission-05-numbers-data/`.
- Prepared and styled the root `README.md` containing student identification details, assignment objectives, and navigation links.
- Created the public repository on GitHub and linked it with the local repository.

### Directory Structure Created
```text
digital-detective-8065/
├── README.md
├── evidence/
├── mission-00-setup/
│   └── README.md
├── mission-01-computer-basics/
│   └── README.md
├── mission-02-terminal/
│   └── README.md
├── mission-03-operating-system/
│   └── README.md
├── mission-04-programs/
│   └── README.md
├── mission-05-numbers-data/
│   ├── README.md
│   └── number_converter.py
├── mission-06-git-github/
│   └── README.md
├── mission-07-networking/
│   └── README.md
└── mission-08-final-report/
    └── README.md
```

## 3. Commands / tools used
- `git --version`: Verified the installed version of Git (`git version 2.54.0 (Apple Git-157)`).
- `python3 --version`: Verified the installed version of Python (`Python 3.9.6`).
- `git init -b main`: Initialized a new local Git repository with `main` as the default branch.
- `mkdir -p <folders>`: Created all folder hierarchies cleanly in one command.
- `touch <files>`: Created empty template files and READMEs across all mission directories.
- `gh repo create saksham1319/digital-detective-8065 --public --source=. --remote=origin`: Created the remote public GitHub repository and linked it as the remote origin.

## 4. My understanding
A **Git repository** acts as a time machine and tracker for a software project. Instead of just saving files over each other or keeping clumsy copies like `project_final_v2`, Git tracks line-by-line diffs and records states as immutable commits. 

Organizing the repository into dedicated mission folders right at the start is important for several reasons:
1. **Separation of Concerns**: Each concept (OS internals, file management, data representation, networking) stays self-contained without cluttering the project root.
2. **Clear Audit Trail**: It allows the instructor and myself to review the evolution of each assignment task sequentially.
3. **Reproducibility**: Anyone cloning or browsing the repository can immediately jump to the specific mission of interest using the root index.

## 5. Difficulties faced
When planning to publish the repository to GitHub, GitHub's web interface has an option to "Add a README file" or "Add .gitignore". In past projects, checking that box when creating an online repo caused non-fast-forward merge conflicts when pushing an already prepared local folder with its own `README.md`.

## 6. How I resolved them
I avoided creating an online README during repository setup on GitHub. Instead, I initialized the repo locally, authored the initial root `README.md`, created an empty public repository on GitHub via the GitHub CLI without initializing boilerplate files, and linked the remote origin so the first push was completely smooth and clean.

## 7. Evidence / files
- Root `README.md`
- `mission-00-setup/README.md`
- Placeholder files across `mission-01` to `mission-08`
- Local `.git` folder initialization

## 8. Commit details
- **Commit Message**: `Set up Digital Detective mission structure`
- **Pushed to Remote**: Verified on branch `main` at `https://github.com/saksham1319/digital-detective-8065`.
