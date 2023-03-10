from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN="#308014"
RED="#FF0000"

class Quizinterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white",bg= THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas= Canvas(width=300, height=250 ,bg="white")
        self.question_text= self.canvas.create_text(
        150,
        125,
        width=280,
        text="Some Question Text",
        font=("Ariel", 20,"italic") )
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,bd=0,command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image= PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,bd=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")
        self.score.config(text=f"Score:{self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.buttons_state(DISABLED)

    def true_pressed(self):
        self.givefeed_back(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.givefeed_back(self.quiz.check_answer("False"))

    def givefeed_back(self,is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000,self.get_next_question)

    def buttons_state(self,state:str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)
