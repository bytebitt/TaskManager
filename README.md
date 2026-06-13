# Task Manager (File-based Java CLI)

A simple console-based task manager written in Java.  
Tasks are stored locally in a text file and persist between program runs.

---

## 📌 Features

- View all tasks
- Add new tasks
- Remove tasks by index
- Clear entire task list
- Persistent storage using a local file (`user_tasks.txt`)

---

## 🛠️ Tech Stack

- Java 17+
- File I/O (`java.io`, `java.nio.file`)
- Collections (`ArrayList`)
- Console-based UI (Scanner)

---

## 📂 How it works

The program stores all tasks in memory during runtime and synchronizes them with a file:

- On startup → tasks are loaded from `user_tasks.txt`
- On every change → file is automatically updated
- On exit → data is already saved

---

## ▶️ How to run

### 1. Compile
```bash
javac Main.java
```
### 2. Run
```bash
java Main
```
