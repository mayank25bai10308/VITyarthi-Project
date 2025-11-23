Author Name - Mayank Sharma
Registration No - 25BAI10308

# ⚙️ Engineering Fundamentals Quiz Application (CLI)

## 🌟 Project Title & Overview
This project is a **Command Line Interface (CLI) quiz application** designed to test fundamental concepts taught in the first year of an engineering curriculum. It is built entirely in Python and uses an **Object-Oriented Programming (OOP) approach** to ensure code modularity and cleanliness.

The system features robust **input validation** and **score persistence**, logging every quiz attempt to an external file for tracking performance over time, thereby fulfilling the project's non-functional requirements.

---

## ✨ Features
* **5 MCQ Questions:** Focused on core topics like Electrical Engineering, Engineering Mechanics, Programming, and Materials Science.
* **Input Validation:** Prevents the program from crashing if the user enters letters or symbols instead of numbers.
* **Score Persistence:** Automatically logs the session's score, date, and time to a file (`engineering_quiz_history.txt`).
* **Qualitative Feedback:** Provides specific remarks (e.g., "Excellent Performance," "Needs Serious Revision") based on the final percentage score.
* **Modular Architecture:** Uses the `EngineeringQuizApp` class to logically separate the Data, Logic, and Reporting components.

---

## 🛠️ Technologies & Tools Used
* **Language:** Python 3.x
* **Core Libraries:** `datetime`, `time`, `sys` (All standard Python libraries, requiring no extra installation).
* **Version Control:** Git

---

## 🚀 Steps to Install & Run the Project

The project is designed to run directly without needing any package installation (`pip install`).

### 1. Cloning the Repository
Open your terminal or command prompt and clone the repository:

```bash
git clone [YOUR_GITHUB_REPO_URL]
cd [YOUR_REPO_NAME] 
# Example: cd Engineering-Fundamentals-Quiz
