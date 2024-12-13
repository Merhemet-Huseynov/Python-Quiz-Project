import sys
import os

# File path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.file_reader import FileReader
from modules.scorer import Scorer


class QuizProcess:
    def __init__(self):
        self.scorer = Scorer()

    def answer_check(self, choice_answer, correct_answer):
        """Method that checks user response"""
        self.scorer.total_questions += 1

        if choice_answer == correct_answer:
            self.scorer.correct_answers_count += 1
        elif not choice_answer:
            self.scorer.unanswered_questions += 1
        else:
            self.scorer.wrong_answers_count += 1

    def start_quiz(self):
        """Basic method to start a Quiz"""
        file_reader = FileReader()
        questions = file_reader.read_and_process()

        for question, options, correct_answer in questions:
            print(f"Question: {question}\n")
            for option in options:
                print(option)

            choice_answer = input("Please enter the correct option: ").strip().upper()
            self.answer_check(choice_answer, correct_answer)

        self.scorer.display_score()