# ----------------------------------------------------------------------------
# Welcome to the real world, I hope you'll enjoy it!
# Author:           Steve-P42
# Description:      Decision Support System
# Creation date:    2021-02-18 10:46:20
# Status:           finished
# ----------------------------------------------------------------------------
# %% IMPORTS
# datetime for due date calculations
import datetime
# regular expressions for the data input reading
import re


class TASK:
    def __init__(self, name='t1', time=0.0, due='01.03.2021', importance=10):
        self.task_name = name
        self.task_time = time
        self.time_multiplier = 0.0
        self.due_date_raw = due
        x = re.match(r"(\d\d)\.(\d\d)\.(\d\d\d\d)", self.due_date_raw)
        self.due_date = datetime.date(int(x.groups()[2]), int(x.groups()[1]), int(x.groups()[0]))
        self.days_left = 0
        self.days_multiplier = 1
        self.importance = importance
        self.imp_multiplier = 0.0
        self.dg_index = 0.0

    def set_task_name(self):
        self.task_name = input("\nTask name: ")

    def set_task_time(self):
        self.task_time = float(input("How many hours(1,1.5,etc.) will the task take: \n"))

        # setting the task time, automatically sets the time multiplier
        self.set_time_multiplier()

    def set_time_multiplier(self):
        if self.task_time <= 0.5:
            self.time_multiplier = 0.95
        elif 0.5 < self.task_time <= 1:
            self.time_multiplier = 0.97
        elif 1 < self.task_time <= 2:
            self.time_multiplier = 0.99
        elif 2 < self.task_time <= 3:
            self.time_multiplier = 1
        else:
            self.time_multiplier = 1
            print('You should consider splitting the task into subtasks. It takes too long.')

    def set_due_date(self):
        due_date_raw = str(input('Task due (DD.MM.YYYY):\n'))
        x = re.match(r"(\d\d)\.(\d\d)\.(\d\d\d\d)", due_date_raw)
        future_date = datetime.date(int(x.groups()[2]), int(x.groups()[1]), int(x.groups()[0]))
        self.due_date = future_date

        # setting the due date, automatically sets the days left and the days multiplier
        self.calculate_days_left()
        self.calculate_days_multiplier()

    def calculate_days_left(self):
        today = datetime.date.today()
        days = (self.due_date - today).days
        self.days_left = days

    def calculate_days_multiplier(self):
        if 0 <= self.days_left <= 5:
            self.days_multiplier = 1
        # elif 3 < self.days_left <= 6:
        #     self.days_multiplier = 0.8
        # elif 6 < self.days_left <= 10:
        #     self.days_multiplier = 0.7
        else:
            self.days_multiplier = 0.8

    def set_importance(self):
        self.importance = int(input('''Importance of decision area, between 1 < 10:
            o	directly related to study progress: 8-10
            o	indirectly related to study progress: 5-7
            o	not related to study progress: 1
        Importance level: '''))

        # setting the importance, automatically sets the importance multiplier
        self.set_imp_multiplier()

    def set_imp_multiplier(self):
        if self.importance >= 9:
            self.imp_multiplier = 1
        elif 9 > self.importance >= 8:
            self.imp_multiplier = 0.8
        elif 8 > self.importance >= 6:
            self.imp_multiplier = 0.3
        else:
            self.imp_multiplier = 0.1

    def calculate_dg_index(self):
        self.dg_index = self.time_multiplier * self.days_multiplier * self.imp_multiplier

    def get_answer(self):
        print(f'\nThe task "{self.task_name}" will take {self.task_time} hour(s).',
              f'It has importance level {self.importance} and is due on {self.due_date_raw},',
              f'which is in {self.days_left} day(s).')

        print(f'DG Index: {round(self.dg_index, 2)}')

        if self.dg_index > 0.7:
            print(f'The answer to the question: "Should you start this task ASAP?", is: ',
                  f'YES, with {round(self.dg_index * 100, 2)}% relevance.')

        if 0.5 <= self.dg_index <= 0.7:
            print(f'The answer to the question: "Should you start this task ASAP?",',
                  f'is: There\'s probably something more important to do,',
                  f'with {round(self.dg_index * 100, 2)}% relevance.')

        if self.dg_index < 0.5:
            print(f'The answer to the question: "Should you start this task ASAP?",',
                  f'is: HECK NO, why are you even asking me?, with {round(self.dg_index * 100, 2)}% relevance.')

        if int(self.dg_index * 100) == 69:
            print('(Nice, btw.)')

# %%


class DSS:
    def __init__(self, name, time, due_date, importance):
        self.task = TASK(name, time, due_date, importance)

        self.task.set_time_multiplier()
        self.task.calculate_days_left()
        self.task.calculate_days_multiplier()
        self.task.set_imp_multiplier()

        self.task.calculate_dg_index()
        self.task.get_answer()


#%% The DSS can now simply be executed by calling DSS with
#   'Task Name' string, Task Duration integer/float, Due Date DD.MM.YYYY string, and Importance 0-10 integer

DSS('Programming Practice', 2.0, '28.03.2021', 10)
DSS('Learn vocabulary', 1.2, '28.03.2021', 8)
DSS('Clean Windows', 1.5, '28.03.2021', 2)

DSS('Do stats HW', 3, '21.03.2021', 10)


