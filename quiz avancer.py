from tkinter import *
from tkinter import messagebox as mb
import json


# Créer une classe pour le quiz
class Quiz:
    def __init__(self, category):
        self.category = category
        self.q_no = 0
        self.correct = 0

        # Filtrer les questions par catégorie
        self.filtered_questions = [q for q in data['quiz'] if q['category'] == category]
        self.data_size = len(self.filtered_questions)

        self.display_title()
        self.display_question()

        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == self.filtered_questions[q_no]['answer']:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="dark olive green", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)

        quit_button = Button(gui, text="Quit", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, "bold"))
        quit_button.place(x=700, y=50)

    def display_options(self):
        self.opt_selected.set(0)
        for i, option in enumerate(self.filtered_questions[self.q_no]['options']):
            self.opts[i]['text'] = option

    def display_question(self):
        question = self.filtered_questions[self.q_no]['question']
        q_no = Label(gui, text=question, width=60,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)

    def display_title(self):
        title = Label(gui, text=f"QUIZ - {self.category}",
                      width=50, bg="gray25", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        for i in range(4):
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=i + 1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list


# Fenêtre principale
gui = Tk()
gui.geometry("800x450")
gui.title("Quiz PS1")

# Charger les données depuis le fichier JSON


with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# Choisir une catégorie
def start_quiz(category):
    Quiz(category)

def choose_category():
    category_window = Toplevel(gui)
    category_window.title("Choose a Category")
    category_window.geometry("300x200")
    
    Label(category_window, text="Choose a Category:", font=("ariel", 14)).pack(pady=20)

    for category in set([q['category'] for q in data['quiz']]):
        Button(category_window, text=category, command=lambda c=category: (category_window.destroy(), start_quiz(c))).pack(pady=10)

choose_category()

gui.mainloop()
