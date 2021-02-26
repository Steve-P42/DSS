# ----------------------------------------------------------------------------
# Welcome to the real world, I hope you'll enjoy it!
# Author:           Steve-P42
# Description:      Decision Support System
# Creation date:    2021-02-18 10:46:20
# Status:           in development
# ----------------------------------------------------------------------------
# %%
import datetime



# --------- TASK NAME ---------
task_name = input("\nTask name: ")
# task_name = 'Read Chapter 42'

# --------- TASK TIME ---------
task_time = float(input("How many hours(1,1.5,etc.) will the task take: \n"))
# task_time = 1.5

# --------- DUE DATE CALCULATION ---------


#%%
today = datetime.date.today()

# due date input, ask user
# due_date = str(input('Task due (DD.MM.YYYY):\n'))
due_date = '01.03.2021'

date_list = due_date.split('.')
future_date = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))

now = datetime.datetime.now()
mnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
seconds = (mnight - now).seconds
days = (future_date - today).days
hms = str(datetime.timedelta(seconds=seconds))

# only for datetime testing
# print("%d days %s" % (days, hms))
#%%
import datetime
print(datetime.date.today())
# print(datetime.date(2021, 2, 19))
#%%



# --------- IMPORTANCE MULTIPLIER ---------

# importance of decision area
importance = int(input('''Importance of decision area, between 1 < 10:
    o	directly related to study progress: 7-10
    o	indirectly related to study progress: 5-6
    o	not related to study progress: 1
Importance level: '''))

if importance >= 7:
    imp_multiplier = 1
elif 7 > importance >= 5:
    imp_multiplier = 0.7
else:
    imp_multiplier = 0.1

# print("Importance Multiplier: ", imp_multiplier)


# --------- TIME MULTIPLIER ---------

if task_time <= 0.5:
    t_multiplier = 0.95
elif 0.5 < task_time <= 1:
    t_multiplier = 0.97
elif 1 < task_time <= 2:
    t_multiplier = 0.99
elif 2 < task_time <= 3:
    t_multiplier = 1
else:
    t_multiplier = 1
    print('You should consider splitting the task into subtasks. It takes too long.')

# print("Task Time Multiplier: ", t_multiplier)


# --------- DUE DATE MULTIPLIER ---------

if 0 <= int(days) <= 10:
    if int(days) == 0:
        days_multiplier = 1
    days_multiplier = 1 - (int(days) / 10) ** 2
# elif int(days) > 10 and int(days) <= 25:
#     days_multiplier = 0.2
# else:
#     if imp_multiplier < 0.6:
#         days_multiplier = 0.1
#     else:
#         days_multiplier = 0.8

# print("Due Day Multiplier: ", days_multiplier)


dg_index = t_multiplier * days_multiplier * imp_multiplier

# print("DG Index:", round(dg_index,2),'\n')


print(f'\nThe task "{task_name}" will take {task_time} hour(s), has importance level {importance} and is due in \
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

# %%

# for i in range(0,10,1):
#   print (1-(int(i)/10)**2)


# %%
