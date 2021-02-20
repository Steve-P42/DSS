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
        y = f'{x.groups()[2]}-{x.groups()[1]}-{x.groups()[0]}'
        future_date = datetime.date(y)


        self.due_date


class DSS:
    def __init__(self):
        self.today = datetime.date.today()

# threading


# %%
import re
due_date_raw = '01.03.2021'
due_date_sep = re.match(r"(\d\d)\.(\d\d)\.(\d\d\d\d)", due_date_raw)
print(int(due_date_sep.groups()[1]))
# %%

# %%

# %%

# %%

# %%

# %%
