# 🖥️ Simple Keylogger (Educational Project)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![pynput](https://img.shields.io/badge/Library-pynput-green.svg)  
![License](https://img.shields.io/badge/Use-Educational%20Only-red.svg)

---

## 📌 Overview
This project is a **simple keylogger** built in Python using the [`pynput`](https://pypi.org/project/pynput/) library.  
It records keystrokes and saves them to a local file (`log.txt`).  

⚠️ **Disclaimer**: This project is created strictly for **educational and ethical purposes only**.  
Do **not** use this code to monitor others without explicit permission.  

---

## ✨ Features
- ✅ Captures all keystrokes
- ✅ Handles **special keys** (`Space`, `Enter`, `Tab`, etc.)
- ✅ Supports **Backspace** (removes last character in log)
- ✅ Stops gracefully when **ESC** is pressed
- ✅ Saves logs into a file (`log.txt`) with **UTF-8 encoding**  
- ✅ Cross-platform (Windows / Linux / macOS)

---

## 🛠️ Requirements
- Python **3.8+**
- Install dependencies:
```bash
pip install pynput
