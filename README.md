<img width="1584" height="396" alt="Abstract Technology Profile LinkedIn Banner" src="https://github.com/user-attachments/assets/bc0f49ed-b4a4-4ae5-9fb4-89c1af2e339d" />

68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f706f77657265642d62792d636f666665652e737667 




# 🔐 Password Manager

A command-line Password Manager built with Python that allows users to securely store, view, search, and delete passwords using JSON-based local storage.

This project was created to practice Python fundamentals such as file handling, JSON manipulation, functions, loops, conditionals, and modular program design.

---

## Features

✅ Add new passwords

✅ View all saved passwords

✅ Search passwords by website name

✅ Delete stored passwords

✅ Persistent storage using JSON

✅ Menu-driven interface

✅ Input validation

----

## Technologies Used

- Python 3
- JSON
- File Handling
- Functions
- Lists
- Dictionaries

No external libraries are required.

---

## Project Structure

```text
password-manager/
│
├── password_manager.py
├── vault.json
├── README.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

---

## File Description

| File                | Purpose                              |
| ------------------- | ------------------------------------ |
| password_manager.py | Main application                     |
| vault.json          | Stores saved password data           |
| README.md           | Project documentation                |
| CHANGELOG.md        | Records project versions and updates |
| LICENSE             | Open-source license                  |
| .gitignore          | Git ignored files                    |


---

## How It Works

The program stores passwords inside a local JSON file.

Example:

```json
{
    "gmail.com": "gmail_password",
    "github.com": "github_password",
    "linkedin.com": "linkedin_password"
}
```

The application loads data from the JSON file, performs the requested operation, and updates the file automatically.

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/parthh001/password-manager.git
```

### 2. Navigate to Project Folder

```bash
cd password-manager
```

### 3. Run Program

```bash
python password_manager.py
```

---

## Example Usage

```text
PASSWORD MANAGER

1. Add Password
2. View Passwords
3. Search Password
4. Delete Password
5. Exit

Choose an option: 1

Website: github.com
Password: mypassword123

Password Saved Successfully.
```

---



```md
![Password Manager Screenshot](screenshot.png)
```

---

## Learning Outcomes

While building this project, I practiced:

- Python Functions
- Loops
- Conditional Statements
- Dictionaries
- JSON Handling
- Reading and Writing Files
- Program Structure
- Git and GitHub Workflow

---

## Future Improvements

Potential upgrades for future versions:

- Password Encryption
- Master Password Authentication
- Password Generator Integration
- Password Strength Checker
- Export to CSV
- GUI Version using Tkinter
- Database Storage using SQLite

---

## Version

Current Release:

```text
v1.0.0
```

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

## Author

**Parth Patil**

GitHub: https://github.com/parthh001
