from tkinter import * 
from quiz_brain import QuizBrain
import os

os.chdir(os.path.dirname(__file__))

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)

        self.canvas = Canvas(width= 300, height = 250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125, text="", fill= THEME_COLOR, font=('Arial',20,'italic'), width= 280)
        self.canvas.grid(column= 1, row=2, columnspan=2, pady=25)
        

        self.score_label = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", bg= THEME_COLOR, fg= "white", font=('Arial', 12,'bold'))
        self.score_label.grid(column= 2, row= 1)

        self.question_number_label = Label(text=f"Question {self.quiz.question_number + 1} of {len(self.quiz.question_list)}", bg= THEME_COLOR, fg= "white", font=('Arial', 10,'bold'))
        self.question_number_label.grid(column= 1, row= 1)


        true_img = PhotoImage(file=r"images\true.png")
        self.true_button = Button(image= true_img, highlightthickness=0, command= self.true_guess)
        self.true_button.grid(column=1,row=3)
        false_img = PhotoImage(file=r"images\false.png")
        self.false_button = Button(image= false_img, highlightthickness=0, command=self.false_guess)
        self.false_button.grid(column=2,row=3)
        # false_img.grid(column=3,row=3)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        #changes question text on canvas. updates score.
        if self.quiz.still_has_questions():    
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.question_number_label.config(text=f"Question {self.quiz.question_number + 1} of {len(self.quiz.question_list)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.game_over()


    def true_guess(self):
        guess_is_correct = self.quiz.check_answer("True")
        self.give_feedback(guess_is_correct)



    def false_guess(self):
        guess_is_correct = self.quiz.check_answer("False")
        self.give_feedback(guess_is_correct)

    def give_feedback(self, guess_is_correct):
        if guess_is_correct == True:
            self.canvas.config(bg="green")
        elif guess_is_correct == False:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

    def game_over(self):
        self.score_label.config(text="")
        self.question_number_label.config(text="")
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, text=f"Final Score:\n{self.quiz.score}/{self.quiz.question_number}")
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)