# ⚙️ Project Statement: Engineering Fundamentals Quiz Application

## 1. Problem Statement

University education, particularly in the foundational first year of engineering, relies heavily on students mastering core principles across multiple disciplines (e.g., Physics, Mechanics, Programming). Students often struggle to self-assess their preparedness in these diverse subjects.

The primary problem this project addresses is the **lack of an accessible, self-directed tool for immediate knowledge verification and assessment of first-year engineering fundamentals.** Traditional methods involve lengthy exams or passive revision. This tool seeks to provide a quick, efficient, and objective metric of a student's grasp of basic concepts.

## Project Aim & Objectives

The aim of this project is to develop a **Command Line Interface (CLI) application** that serves as a self-assessment platform for students.

### Key Objectives:
* To design a modular Python application that encapsulates the quiz questions and scoring logic using **Object-Oriented Programming (OOP)** principles.
* To implement a **robust input validation system** that prevents application failure due to incorrect user input (e.g., entering text instead of numbers).
* To establish **data persistence** by logging the results of every quiz attempt (score, date, and performance remarks) to an external file.
* To provide **qualitative, actionable feedback (remarks)** based on the final score, guiding the student on areas requiring further revision.

---

## 2. Scope of the Project

The scope of the Engineering Fundamentals Quiz Application is strictly confined to the following functionalities and boundaries:

| Area | Scope Description | Fulfillment Mechanism |
| :--- | :--- | :--- |
| **Quiz Content** | Five (5) Multiple Choice Questions (MCQs) covering foundational topics from the First Year Engineering syllabus (e.g., Electrical, Mechanics, C/Python Basics). | Data is stored statically within the `QuizApp` class definition. |
| **User Interface** | Limited to a **Command Line Interface (CLI)** environment only. No graphical user interface (GUI) or web interface is utilized. | Uses standard Python `print()` and `input()` functions. |
| **Core Functions** | Collect user input, grade the answers, calculate the final score, provide descriptive remarks, and save the session data. | Managed by the `run_quiz`, `get_user_choice`, and `save_result` methods. |
| **Data Storage** | All historical score data is saved to a simple text file (`engineering_quiz_history.txt`). The system does not utilize external databases (e.g., SQL, SQLite). | Achieved via native Python file I/O operations (`open()` and `write()`). |
## 3. Target User

The primary user is a **First-Year University Engineering Student** who needs a quick, objective tool to self-assess their foundational knowledge across core disciplines.

---

## 4. High-Level Features

* **Quiz Engine (OOP-based):** A core module designed using Object-Oriented Programming principles to manage questions, answers, and scoring logic.
* **Input Validation:** Robust system to handle and reject incorrect user inputs (e.g., non-numeric entries).
* **Score Calculation & Feedback:** Calculates the final score and provides **qualitative, actionable remarks** based on performance (e.g., "Excellent," "Needs Revision").
* **Historical Data Logging:** Saves the date, score, and performance remarks of every quiz session to an external text file for tracking progress.
* **CLI Interface:** User interaction is conducted entirely through the Command Line.
