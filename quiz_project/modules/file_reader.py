class FileReader:
    def __init__(self):
        self.file_path = "D:/New folder/quiz_project/questions/questions.txt"
    
    def load_questions(self):
        """This function loads questions from a given file and divides 
                          them into blocks."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            blocks = content.split("\n\n")
        return blocks
    
    def extract_answer(self, answer_line, block):
        """If the string begins with "Answer", this function returns the 
                               correct answer."""
        if not answer_line.startswith("Answer: "):
            print(f"Warning: Skipping block with missing answer:\n{block}\n")
            return None
        return answer_line.split(": ")[1]
    
    def block_questions(self, blocks):
        """This method extracts the question, answer options, and
          correct answer from each block and stores them in memory."""
        questions = []
        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) < 6:
                print(f"Warning: Skipping malformed block:\n{block}\n")
                continue

            question = lines[0]
            options = [line.strip() for line in lines[1:5]]
            answer_line = lines[5].strip()

            correct_answer = self.extract_answer(answer_line, block)
            if correct_answer is None:
                continue
            
            questions.append((question, options, correct_answer))  
        
        return questions

    def read_and_process(self):
        """This method loads questions and processes them to obtain 
             the questions, answer options, and correct answers."""
        blocks = self.load_questions()
        return self.block_questions(blocks)

