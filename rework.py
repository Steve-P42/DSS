# ----------------------------------------------------------------------------
# Welcome to the real world, I hope you'll enjoy it!
# Author:           Steve-P42
# Description:      Decision Support System
# Creation date:    2021-02-18 10:46:20
# Status:           in development
# ----------------------------------------------------------------------------
# %%
import datetime
# %%


class DSS:
    def __init__(self):
        self.task_name = ''
        self.task_time = 0.0
        self.due_date = ''
        self.today = datetime.date.today()

    def get_task_name(self):
        self.task_name = input("\nTask name: ")

    def get_task_time(self):
        self.task_time = float(input("How many hours(1,1.5,etc.) will the task take: \n"))

    def get_due_date(self):
        self.due_date = str(input('Task due (DD.MM.YYYY):\n'))


# %%

# %%

# %%

# %%

# %%

# %%

# %%
