import sys
import os

# File path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from colorama import Fore, init
from modules.quiz_process import QuizProcess

# Automatically launched for Windows
init(autoreset=True)


def main():
    print(Fore.RED + "Welcome to the Python Quiz!")
    print(Fore.RED + "Answer the questions by typing the correct option (e.g., A, B, C, D).")
    print(Fore.RED + "To skip a question, just press Enter.\n")

    quiz = QuizProcess()
    quiz.start_quiz()

if __name__ == "__main__":
    main()
