
class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def next_question(self):
        self.guess = input(f"Q{self.question_number + 1}: {self.question_list[self.question_number].question} True or False: ")
        self.check_answer(self.guess, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            self.score += 1
        print(f"Your score is {self.score}/{self.question_number+1}")
        print("\n")


    # def play_game():
    #     print("Let's play the game!")
    #     correct = 0
    #     for i in range(len(Self.question_list)):
    #         guess = input(f"{self.question_list[i].question} True or False: ")
    #         if guess == question_bank[i].answer:
    #             correct += 1
    #         print(f"You have guessed {correct} correct out of {i+1} questions. {100*correct/(i+1)}%\n")