# ----------------------------------------------------------------------------
# Welcome to the real world, I hope you'll enjoy it!
# Author:           Steve-P42
# Description:      Decision Support System
# Creation date:    2021-02-18 10:46:20
# Status:           in development
# ----------------------------------------------------------------------------
# %% IMPORTS
# datetime for due date calculations
import datetime
# regular expressions for the data input reading
import re


# %%


class TASK:
    def __init__(self, name='t1', time=0.0, due=datetime.date(1999, 12, 31), importance=0):
        self.task_name = name
        self.task_time = time
        self.time_multiplier = 0.0
        self.due_date = due
        self.days_left = 0
        self.days_multiplier = 1
        self.importance = importance
        self.imp_multiplier = 0.0
        self.dg_index = 0.0

    def set_task_name(self):
        self.task_name = input("\nTask name: ")

    def set_task_time(self):
        self.task_time = float(input("How many hours(1,1.5,etc.) will the task take: \n"))

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
        return self.time_multiplier

    def set_due_date(self):
        due_date_raw = str(input('Task due (DD.MM.YYYY):\n'))
        x = re.match(r"(\d\d)\.(\d\d)\.(\d\d\d\d)", due_date_raw)
        future_date = datetime.date(int(x.groups()[2]), int(x.groups()[1]), int(x.groups()[0]))
        self.due_date = future_date

    def calculate_days_left(self):
        today = datetime.date.today()
        days = (self.due_date - today).days
        self.days_left = days

    def calculate_days_multiplier(self):
        if 0 <= self.days_left <= 3:
            self.days_multiplier = 1
        elif 3 < self.days_left <= 6:
            self.days_multiplier = 0.8
        elif 6 < self.days_left <= 10:
            self.days_multiplier = 0.7
        else:
            self.days_multiplier = 0.5

    def set_importance(self):
        self.importance = int(input('''Importance of decision area, between 1 < 10:
            o	directly related to study progress: 7-10
            o	indirectly related to study progress: 5-6
            o	not related to study progress: 1
        Importance level: '''))

    def set_imp_multiplier(self):
        if self.importance >= 8:
            self.imp_multiplier = 1
        elif 8 > self.importance >= 6:
            self.imp_multiplier = 0.7
        elif 6 > self.importance > 4:
            self.imp_multiplier = 0.4
        else:
            self.imp_multiplier = 0.1

    def calculate_dg_index(self):
        self.dg_index = self.time_multiplier * self.days_multiplier * self.imp_multiplier

    def get_answer(self):
        print(f'\nThe task "{self.task_name}" will take {self.task_time} hour(s).',
              f'It has importance level {self.importance} and is due on {self.due_date}, in {self.days_left} day(s).')

        print(f'DG Index: {round(self.dg_index, 2)}')

        if self.dg_index > 0.7:
            print(f'The answer to the question: "Should you start this task ASAP?", is: ',
                  f'YES, with {round(self.dg_index * 100, 2)}% relevance.')

        if 0.5 <= self.dg_index <= 0.7:
            print(f'The answer to the question: "Should you start this task ASAP?",',
                  f'is: There\'s probably something more important to do, with {round(self.dg_index * 100, 2)}% relevance.')

        if self.dg_index < 0.5:
            print(f'The answer to the question: "Should you start this task ASAP?",',
                  f'is: HECK NO, why are you even asking me?, with {round(self.dg_index * 100, 2)}% relevance.')

        if int(self.dg_index * 100) == 69:
            print('\n(Nice, btw.)')


# %% setting up a first task and checking if the methods and attributes work as expected
# def __init__(self, name='t1', time=0.0, due=datetime.date(1999, 12, 31), importance=0):

task1 = TASK('Task 1', 1.5, datetime.date(2021, 2, 28), 7)

task1.set_time_multiplier()
task1.calculate_days_left()
task1.calculate_days_multiplier()
task1.set_imp_multiplier()
task1.calculate_dg_index()
task1.get_answer()


# print(task1.task_name,
#       task1.task_time,
#       task1.time_multiplier,
#       task1.due_date,
#       task1.days_left,
#       task1.days_multiplier,
#       task1.importance,
#       task1.imp_multiplier,
#       task1.dg_index
#      )


# %%

# class DSS:
#     def __init__(self, name):
#         self.task = name

# threading


# %%

# %%

# %%

# %%

# %%

# %%

# %%
