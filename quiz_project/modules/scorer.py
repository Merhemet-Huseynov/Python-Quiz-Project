class Scorer:
    def __init__(self):
        self.total_questions = 0
        self.correct_answers_count = 0
        self.wrong_answers_count = 0
        self.unanswered_questions = 0

    def display_score(self):
        """This method displays the current score."""
        print(f"Total Questions: {self.total_questions}")
        print(f"Correct Answers: {self.correct_answers_count}")
        print(f"Wrong Answers: {self.wrong_answers_count}")
        print(f"Unanswered Questions: {self.unanswered_questions}")
