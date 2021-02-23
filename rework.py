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
        self.importance = 0
        self.imp_multiplier = 0.0
        self.time_multiplier = 0.0
        self.dg_index = 0.0

    def set_task_name(self):
        self.task_name = 'task1'#input("\nTask name: ")

    def set_task_time(self):
        self.task_time = 1.5#float(input("How many hours(1,1.5,etc.) will the task take: \n"))

    def set_due_date(self):
        due_date_raw = '01.01.2021'#str(input('Task due (DD.MM.YYYY):\n'))
        x = re.match(r"(\d\d)\.(\d\d)\.(\d\d\d\d)", due_date_raw)
        future_date = datetime.date(int(x.groups()[2]), int(x.groups()[1]), int(x.groups()[0]))
        self.due_date = future_date

    def set_importance(self):
        self.importance = 10
        # importance = int(input('''Importance of decision area, between 1 < 10:
        #     o	directly related to study progress: 7-10
        #     o	indirectly related to study progress: 5-6
        #     o	not related to study progress: 1
        # Importance level: '''))

        if self.importance >= 8:
            self.imp_multiplier = 1
        elif 8 > self.importance >= 6:
            self.imp_multiplier = 0.7
        elif 6 > self.importance > 4:
            self.imp_multiplier = 0.4
        else:
            self.imp_multiplier = 0.1

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

    def calculate_dg_index(self):
        #todo calculate the index XD


    def get_answer(self):
        print(f'\nThe task "{self.task_name}" will take {self.task_time} hour(s), has importance level\
         {self.importance} and is due on {self.due_date}.')     #in {days} day(s).')
        print(f'DG Index: {round(self.dg_index, 2)}')
        if self.dg_index > 0.7:
            print(f'The answer to the question: "Should you start this task ASAP?", is: YES, with \
        {round(self.dg_index * 100, 2)}% relevance.')

        if 0.5 <= self.dg_index <= 0.7:
            print(f'The answer to the question: "Should you start this task ASAP?", is: There\'s probably something more \
        important to do, with {round(self.dg_index * 100, 2)}% relevance.')

        if self.dg_index < 0.5:
            print(f'The answer to the question: "Should you start this task ASAP?", is: HECK NO, why are you even asking me?, \
        with {round(self.dg_index * 100, 2)}% relevance.')


#%% setting up a first task and checking if the methods and attributes work as expected
task1 = TASK()

task1.set_task_name()
task1.set_task_time()
task1.set_due_date()
task1.set_importance()
task1.set_time_multiplier()

print(task1.task_name, task1.task_time, task1.due_date, task1.imp_multiplier, task1.time_multiplier)




#%%






class DSS:
    def __init__(self):
        self.today = datetime.date.today()



# threading


# %%

# %%

# %%

# %%

# %%

# %%

# %%
