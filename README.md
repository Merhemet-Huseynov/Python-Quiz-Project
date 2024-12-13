# Python Quiz Project

## Project Description

This Python project allows users to take a quiz based on questions stored in a `questions.txt` file. The questions and answer options are read from the file, and the user's answers are checked for correctness. The project is structured into several modules for clear separation of concerns and easy maintenance:

### Modules:

- **`file_reader.py`**: This module reads the questions from the `questions.txt` file and processes them into a structured format (blocks).
- **`quiz_process.py`**: This module handles the quiz logic. It presents questions to the user, collects their responses, and checks if the answers are correct.
- **`scorer.py`**: This module checks the user's answers and calculates their score, displaying the results in a table format.
- **`main.py`**: The main entry point for the project, where the quiz is started and user interaction occurs.

## Installation

To run this project on your local machine, follow these steps:

### 1. Download the Project:

Clone or download the project from GitHub or another source.

### 2. Install Required Libraries:

Navigate to the project's root folder and install the necessary libraries using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt


To run the project, run the command in the terminal:
   ```bash
   python main.py