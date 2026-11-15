# Mission 6 — Git, GitHub, branches and Pull Requests

## 1. Task / objective
The objective of Mission 6 was to understand version control workflows using Git and GitHub. This included mastering the lifecycle of file staging and committing, creating and isolating work on a separate Git feature branch (`update-about`), publishing the branch to GitHub, opening a formal Pull Request (PR), reviewing and merging the PR into the `main` branch, synchronizing the merged changes back to the local repository, and compiling a comprehensive Git command glossary.

---

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git Operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Queries Git's tracking engine to display which branch is active, which files are untracked, which modified files have been staged for the next commit, and which remain unstaged. |
| **Stage selected changes (`git add <file>`)** | Moves specific file modifications from the working directory into the Git staging area (also known as the index), letting you selectively curate the contents of the upcoming snapshot. |
| **Create a commit (`git commit -m "..."`)** | Captures a permanent, cryptographically-hashed snapshot of all currently staged changes, tagging it with author metadata, a timestamp, and a descriptive log message. |
| **View commit history (`git log --oneline`)** | Lists the chronological series of commits on the current branch, showing shortened commit hashes and their corresponding commit messages to inspect project history. |

#### Difference between staging a change and committing it:
Staging (`git add`) is like packing specific items into a shipping carton: you inspect your files and decide exactly which changes belong in the box, with the freedom to add or remove items before finalizing. Committing (`git commit`) is like sealing, stamping, and recording the carton in the shipping ledger: it permanently bakes that collection of changes into the project's immutable timeline with a unique commit hash.

---

### Task 6.2 — Create and use a branch
1. Created and switched to a new branch named `update-about`:
   ```bash
   git checkout -b update-about
   ```
2. Opened the root `README.md` and authored a new section titled `## My Learning` detailing three key computer science takeaways.
3. Inspected the branch status using `git status`, staged the modified root `README.md`, and committed the changes:
   ```bash
   git add README.md
   git commit -m "Add My Learning section to root README on update-about branch"
   ```
4. Published the branch to GitHub:
   ```bash
   git push -u origin update-about
   ```

---

### Task 6.3 — Create a Pull Request (PR)
1. Opened the repository on GitHub and initiated a Pull Request from `update-about` into `main`.
2. Created **Pull Request #1**: *Add My Learning section to root README* (`https://github.com/saksham1319/digital-detective-8065/pull/1`).
3. Reviewed the line-by-line diff of the modified `README.md`.
4. Merged the Pull Request on GitHub into the `main` branch.
5. Returned to the local terminal, checked out the `main` branch, and pulled the remote merge commit:
   ```bash
   git checkout main
   git pull origin main
   ```
6. Verified with `git log --oneline` that the merge commit `5097668` was cleanly integrated into the local history.

#### Why branches and Pull Requests are essential:
- **Branches**: A branch provides an isolated sandbox where a developer can experiment, fix bugs, or build features without risking breakage on the production-ready `main` branch. Multiple team members can work on separate branches simultaneously without stepping on each other's toes.
- **Pull Requests**: A Pull Request is a collaborative discussion and review checkpoint. It allows peers to inspect line-by-line code diffs, run automated tests, suggest optimizations, and ensure quality standards before merging changes into the primary codebase.

---

### Task 6.4 — Build your Git command glossary

| Git Operation | One-Line Explanation |
| :--- | :--- |
| **Initialise a repository** | `git init` creates an internal `.git` metadata directory, converting any local folder into an active Git version-controlled project. |
| **Check status** | `git status` displays the current active branch and lists all untracked, modified, or staged files. |
| **Stage changes** | `git add <file>` adds specified file modifications to the staging index in preparation for committing. |
| **Commit changes** | `git commit -m "..."` records an immutable historical snapshot of all currently staged changes along with a descriptive message. |
| **View history** | `git log` displays the chronological timeline of recorded commits, showing hashes, authors, and timestamps. |
| **Create or list branches** | `git branch` lists all local branches, while `git branch <name>` establishes a new divergent line of development. |
| **Switch branches** | `git checkout <branch>` (or `git switch <branch>`) moves the `HEAD` pointer and updates local files to match the chosen branch. |
| **Publish changes** | `git push` uploads committed local branch revisions to synchronize with a designated remote repository on GitHub. |
| **Retrieve remote changes** | `git pull` fetches the latest commits from the remote repository and immediately merges them into the current local branch. |

---

## 3. Commands / tools used
- `git checkout -b update-about`: Created and switched to the feature branch.
- `git status`: Monitored modified files and staging state.
- `git add README.md`: Staged the root README edits.
- `git commit -m "..."`: Committed the staged edits on the feature branch.
- `git push -u origin update-about`: Published the feature branch to GitHub.
- `gh pr create`: Created Pull Request #1 on GitHub via the GitHub CLI.
- `gh pr merge --merge`: Merged the Pull Request on GitHub.
- `git checkout main`: Switched back to the primary branch.
- `git pull origin main`: Synchronized local `main` with the remote merge commit.
- `git log --oneline`: Inspected the commit graph.

## 4. My understanding
Version control is the backbone of modern software engineering. Before Git, collaborating on code involved manually sharing zipped folders or risking accidental overwrites. Working through this branching and PR workflow made it clear that Git is not just for backup—it is a collaboration framework. Creating a branch allows you to take risks safely; opening a Pull Request turns code integration into a transparent conversation; and merging updates the master record only after verification.

## 5. Difficulties faced
When switching branches, if you have unstaged or uncommitted changes, Git can prevent the checkout to avoid overwriting your working directory.

## 6. How I resolved them
I verified via `git status` that the working tree was completely clean and that all edits were committed before switching branches with `git checkout main`.

## 7. Evidence / files
- Feature branch `update-about` on GitHub
- Pull Request #1: `https://github.com/saksham1319/digital-detective-8065/pull/1` (Merged)
- Root `README.md` updated with `## My Learning`
- `mission-06-git-github/README.md` (this report)

## 8. Commit details
- **Commit Message**: `Complete Git and GitHub collaboration mission`
- **Pushed to Remote**: Branch `main` on `saksham1319/digital-detective-8065`.
