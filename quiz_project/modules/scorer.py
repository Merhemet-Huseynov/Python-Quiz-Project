from prettytable import PrettyTable

class Scorer:
    def __init__(self):
        self.total_questions = 0
        self.correct_answers_count = 0
        self.wrong_answers_count = 0
        self.unanswered_questions = 0

    def display_score(self):
        """Bu metod cari nəticəni cədvəl şəklində göstərir."""
        table = PrettyTable()
        table.field_names = ["Result", "Count"]
        
        table.add_row(["Total Questions", self.total_questions])
        table.add_row(["Correct Answers", self.correct_answers_count])
        table.add_row(["Wrong Answers", self.wrong_answers_count])
        table.add_row(["Unanswered Questions", self.unanswered_questions])
        
        print(table)
