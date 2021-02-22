# ----------------------------------------------------------------------------
# Welcome to the real world, I hope you'll enjoy it!
# Author:           Steve-P42
# Description:      Decision Support System
# Creation date:    2021-02-18 10:46:20
# Status:           in development
# ----------------------------------------------------------------------------
# %%
import datetime
import re
# %%


class TASK:
    def __init__(self):
        self.task_name = ''
        self.task_time = 0.0
        self.due_date = ''

    def get_task_name(self):
        self.task_name = input("\nTask name: ")

    def get_task_time(self):
        self.task_time = float(input("How many hours(1,1.5,etc.) will the task take: \n"))

    def get_due_date(self):
        due_date_raw = str(input('Task due (DD.MM.YYYY):\n'))
        x = re.match(r"(\d\d)\.(\d\d)\.(\d\d\d\d)", due_date_raw)
        future_date = datetime.date(int(x.groups()[2]), int(x.groups()[1]), int(x.groups()[0]))
        self.due_date = future_date





#%% setting up a first task and checking if the methods and attributes work as expected
task1 = TASK()

task1.get_task_name()
task1.get_task_time()
task1.get_due_date()

print(task1.task_name, task1.task_time)




#%%









class DSS:
    def __init__(self):
        self.today = datetime.date.today()

    def calculate_time_multiplier(self, task):
        if task.self.task_time <= 0.5:
            t_multiplier = 0.95
        elif 0.5 < task.self.task_time <= 1:
            t_multiplier = 0.97
        elif 1 < task.self.task_time <= 2:
            t_multiplier = 0.99
        elif 2 < task.self.task_time <= 3:
            t_multiplier = 1
        else:
            t_multiplier = 1
            print('You should consider splitting the task into subtasks. It takes too long.')
        return t_multiplier

    def answer(self, task):
        print(f'\nThe task "{task.self.task_name}" will take {task.self.task_time} hour(s), has importance level {importance} and is due in \
        {days} day(s).')
        print(f'DG Index: {round(dg_index, 2)}')
        if dg_index > 0.7:
            print(f'The answer to the question: "Should you start this task ASAP?", is: YES, with \
        {round(dg_index * 100, 2)}% relevance.')

        if 0.5 <= dg_index <= 0.7:
            print(f'The answer to the question: "Should you start this task ASAP?", is: There\'s probably something more \
        important to do, with {round(dg_index * 100, 2)}% relevance.')

        if dg_index < 0.5:
            print(f'The answer to the question: "Should you start this task ASAP?", is: HECK NO, why are you even asking me?, \
        with {round(dg_index * 100, 2)}% relevance.')

# threading


# %%

# %%

# %%

# %%

# %%

# %%

# %%
