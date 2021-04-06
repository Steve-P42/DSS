# ----------------------------------------------------------------------------
# Welcome to the real world, I hope you'll enjoy it!
# Author:           Steve-P42
# Description:      Eisenhower Decision Matrix
# Creation date:    2021-03-21 08:41:09
# Status:           in development
# ----------------------------------------------------------------------------
# %%
# %% useful link: http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
# %%
import tkinter as tk
import csv


class Matrix:

    def __init__(self, tasklist=None):
        # if no arguments are given, the tasks are retrieved from the tasks.csv file
        if tasklist is None:
            tasklist = []
            with open('tasks.csv') as task_file:
                t_list = csv.reader(task_file)
                for row in t_list:
                    try:
                        #print(f'{row[0]}, {int(row[1])}, {int(row[2])}')
                        tasklist.append([f'{row[0]}', int(row[1]), int(row[2])])
                    except IndexError:
                        pass
        self.task_list = tasklist

        # main window configuration
        root = tk.Tk()
        root.title('Decision Matrix')
        root.geometry('1030x720+900+400')
        root.configure(bg='black')         # redundant, since image is used as bg
        root.resizable(False, False)

        # image credit goes to Nasa and the Hubble Space Telescope (https://svs.gsfc.nasa.gov/30946)
        # Add image file
        bg = tk.PhotoImage(file="UDF.png")

        # Show image using label
        label1 = tk.Label(root, image=bg)
        label1.place(x=0, y=0)

        # creating the canvas for the matrix
        blue = tk.Canvas(root, width=1000, height=500)
        blue.pack(padx=5, pady=10)

        # drawing a blue rectangle in the middle
        blue.create_rectangle(1000, 500, 5, 5, fill="blue")
        # drawing a white line across (dashed line)
        blue.create_line(0, 250, 1000, 250, fill="white", dash=(4, 4))
        # drawing a white vertical line (dashed line)
        blue.create_line(500, 0, 500, 500, fill="white", dash=(4, 4))

        # frame that contains text entry functionality
        frame1 = tk.Frame(root, bg='blue4', bd=5)
        frame1.pack()

        # frame that contains save button and exit button
        frame2 = tk.Frame(root, bg='blue4', bd=5)
        frame2.pack(pady=10)

        # label to display what to input into the task_entry field
        t_var = "Taskname, Importance, Urgency"
        label = tk.Label(frame1, text=t_var, bg="dark slate grey", fg="cyan2")
        label.pack()

        # text entry field for new tasks
        task_entry = tk.Entry(frame1, width=20, bg="dark slate blue", fg="green")
        task_entry.insert(0, 'NiceTask, 6, 9')
        task_entry.pack(padx=7, pady=7)

        # function to get the tasks from the text entry field
        def new_task_function():
            try:
                task = task_entry.get().split(',')
                try:
                    new_task = [task[0], int(task[1].strip()), int(task[2].strip())]
                    self.task_list.append(new_task)
                    put_task_on_matrix(new_task)
                except IndexError:
                    print('Missing parameters.')
            except ValueError:
                print('Missing parameters.')

        # entry confirmation button
        entry_button = tk.Button(frame1, text="Put into Matrix..", command=new_task_function, bg="light slate grey")
        entry_button.pack(side=tk.LEFT, padx=5, pady=5)

        # function to draw tasks on matrix
        def put_task_on_matrix(tsk):
            x = tsk[1] * 100
            y = 500 - tsk[2] * 50

            x1, y1, x2, y2 = x, y, x + 3, y + 3

            blue.create_oval(x1, y1, x2, y2, fill="red", outline="red", width=10)
            blue.create_text(x, y + 18, text=f"{tsk[0]}: ({tsk[1]},{tsk[2]})", fill="#40ff00")

        for item in self.task_list:
            put_task_on_matrix(item)

        # function to ..
        def save_new_tasks_in_csv():
            with open('tasks.csv', mode='w') as task_file2:
                w = csv.writer(task_file2)
                w.writerows(self.task_list)

        # button to save all tasks on the matrix into the tasks.csv file
        save_button = tk.Button(frame2, text="Save Tasks to file.", command=save_new_tasks_in_csv, bg="light slate grey")
        save_button.pack(side=tk.LEFT, padx=5)

        # button to exit the program
        exit_button = tk.Button(frame2, text="Exit", command=root.destroy, bg="light slate grey")
        exit_button.pack(side=tk.RIGHT, padx=5)

        # function to ..
        def delete_task_by_name():
            t_raw = task_entry.get().strip()
            if ',' in t_raw:
                t = t_raw.split(',')[0]
            else:
                t = t_raw

            try:
                for i in range(len(self.task_list)):
                    if self.task_list[i][0] == t or self.task_list[i][0].lower() == t:
                        del(self.task_list[i])
                        print('Task deleted.')
                        # delete canvas entries
                        blue.delete("all")
                        # Draw a blue rectangle in the middle
                        blue.create_rectangle(1000, 500, 10, 10, fill="blue")
                        # Draw a yellow line across
                        blue.create_line(0, 250, 1000, 250, fill="red", dash=(4, 4))
                        # Draw a red vertical line (dashed line)
                        blue.create_line(500, 0, 500, 500, fill="red", dash=(4, 4))
                        for task in self.task_list:
                            put_task_on_matrix(task)
                        break
            except IndexError:
                pass

        # button to save all tasks on the matrix into the tasks.csv file
        del_button = tk.Button(frame1, text="Delete Task", command=delete_task_by_name, fg="orange red",
                               bg="dim grey")
        del_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # run tk window in a loop
        root.mainloop()


#l1 = [['Coding', 8, 7], ['Cleaning', 4, 6], ['OneOne', 1, 1]]

m1 = Matrix()



# %%
# https://www.geeksforgeeks.org/python-tkinter-create-different-type-of-lines-using-canvas-class/

# %%

# %%

# %%

# %% just for fun from here: https://sites.google.com/a/pythonlake.com/www/tkintercanvascreate_oval
# from tkinter import *
#
# master = Tk()
# master.title("Click to generate random ovals")
#
#
# def bpress(click):
#     import random
#     color_list = ['snow', 'ghostwhite', 'whitesmoke', 'gainsboro', 'floralwhite', 'oldlace',
#                   'linen', 'antiquewhite', 'papayawhip', 'blanchedalmond', 'bisque', 'peachpuff',
#                   'navajowhite', 'lemonchiffon', 'mintcream', 'azure', 'aliceblue', 'lavender',
#                   'lavenderblush', 'mistyrose', 'darkslategray', 'dimgray', 'slategray',
#                   'lightslategray', 'gray', 'lightgrey', 'midnightblue', 'navy', 'cornflowerblue', 'darkslateblue',
#                   'slateblue', 'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue', 'blue',
#                   'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'lightsteelblue',
#                   'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise', 'mediumturquoise', 'turquoise',
#                   'cyan', 'lightcyan', 'cadetblue', 'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen',
#                   'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen', 'palegreen', 'springgreen',
#                   'lawngreen', 'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen',
#                   'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod', 'lightgoldenrodyellow',
#                   'lightyellow', 'yellow', 'gold', 'lightgoldenrod', 'goldenrod', 'darkgoldenrod', 'rosybrown',
#                   'indianred', 'saddlebrown', 'sandybrown',
#                   'darksalmon', 'salmon', 'lightsalmon', 'orange', 'darkorange',
#                   'coral', 'lightcoral', 'tomato', 'orangered', 'red', 'hotpink', 'deeppink', 'pink', 'lightpink',
#                   'palevioletred', 'maroon', 'mediumvioletred', 'violetred',
#                   'mediumorchid', 'darkorchid', 'darkviolet', 'blueviolet', 'purple', 'mediumpurple',
#                   'thistle', 'snow2', 'snow3',
#                   'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
#                   'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
#                   'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
#                   'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
#                   'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
#                   'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
#                   'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
#                   'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
#                   'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
#                   'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
#                   'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
#                   'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
#                   'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
#                   'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
#                   'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
#                   'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
#                   'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
#                   'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
#                   'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
#                   'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
#                   'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
#                   'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
#                   'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
#                   'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
#                   'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
#                   'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
#                   'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
#                   'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
#                   'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
#                   'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
#                   'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
#                   'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
#                   'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
#                   'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
#                   'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
#                   'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
#                   'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
#                   'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
#                   'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
#                   'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
#                   'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
#                   'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
#                   'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
#                   'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
#                   'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
#                   'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
#                   'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
#                   'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
#                   'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
#                   'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
#                   'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
#                   'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
#                   'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
#                   'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
#                   'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
#                   'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
#                   'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
#
#     r = range(0, 1000)
#     for i in reversed(r):
#         x1 = click.x - i
#         y1 = click.y - i
#         x2 = click.x + i
#         y2 = click.y + i
#         color = random.sample(color_list, 1)
#         canvas.create_oval(x1, y1, x2, y2, fill=color)
#
#
# canvas = Canvas(master, width=1000, height=1000, background="black")
# canvas.pack(expand=YES)
# canvas.bind("<Double-1>", bpress)
#
# master.mainloop()
# %%
