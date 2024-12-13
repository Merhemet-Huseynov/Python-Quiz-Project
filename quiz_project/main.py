import sys
import os

# File path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from modules.quiz_process import QuizProcess

def main():
    print("Welcome to the Python Quiz!")
    print("Answer the questions by typing the correct option (e.g., A, B, C, D).")
    print("To skip a question, just press Enter.\n")

    quiz = QuizProcess()
    quiz.start_quiz()

if __name__ == "__main__":
    main()
