import random
from question_model import Question
from data import question_data
from data import api_question_data
from quiz_brain import QuizBrain




default_question_bank = []
for q in range(len(question_data)):
    to_append = Question(question_data[q]['text'], question_data[q]['answer'])
    default_question_bank.append(to_append)

api_question_bank = []
for q in range(len(api_question_data["results"])):
    to_append = Question(api_question_data["results"][q]['question'], api_question_data["results"][q]['correct_answer'])
    api_question_bank.append(to_append)


quiz = QuizBrain(default_question_bank)
quiz2 = QuizBrain(api_question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

# print(f"You have completed the quiz.")
# print(f"Your final score is {self.score}/{self.question_number}")


while quiz2.still_has_questions():
    quiz2.next_question()

print(f"You have completed the quiz.")
print(f"Your final score is {quiz2.score}/{quiz2.question_number}")

