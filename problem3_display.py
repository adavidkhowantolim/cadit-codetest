from csv import reader
from time import time, localtime, strftime
from tkinter import *

# constants
SLEEP_TIME = 120 * 1000  # miliseconds
FILENAME = 'log.csv'
DEFAULT_VALUE = 0.0
ROOM_NUMBER = 5
AGG_NUMBER = 4
# with open('mock_data.csv', 'r', newline='') as csvfile:
#   log_reader = reader(csvfile, delimiter=',')
# for row in log_reader:
# if (row[1] == 'Room1')

window = Tk()  # row = aggregation, column = room number

# head, filename, last updated, and exit button
temp_label = Label(master=window, text="TEMP", wraplength=1, font="bold").grid(
    row=1, column=0, rowspan=5)
humd_label = Label(master=window, text="HUMID", wraplength=1, font="bold").grid(
    row=6, column=0, rowspan=5)
head_label = Label(master=window, text="-", font="bold")
head_label.grid(row=0, column=1)
file_label = Label(master=window, text="File: " + FILENAME)
file_label.grid(row=12, column=1, columnspan=6)
time_text = StringVar()
time_text.set("Start Displaying")
time_label = Label(master=window, textvariable=time_text)
time_label.grid(row=13, column=1, columnspan=6)
btn_increase = Button(master=window, text="Stop Streaming and Logging",
                      command=window.destroy, wraplength=55)
btn_increase.grid(row=0, column=7, sticky="nsew", rowspan=14)

# row label
agg_text = ["Minimum", "Maximum", "Median", "Average"]
temp_agg_label = [Label(master=window, text=agg_text[i]
                        ).grid(row=i+1, column=1) for i in range(AGG_NUMBER)]
temp_avg_all_label = Label(master=window, text="All avg").grid(
    row=5, column=1, pady=(0, 20))
humd_agg_label = [Label(master=window, text=agg_text[i]
                        ).grid(row=i+6, column=1) for i in range(AGG_NUMBER)]
humd_avg_all_label = Label(
    master=window, text="All avg").grid(row=10, column=1)

# column label
room_label = [Label(master=window, text="Room " + str(i+1)
                    ).grid(row=0, column=i+2) for i in range(ROOM_NUMBER)]

# Temperature Value Texts
temp_val_text = [[DoubleVar(window, DEFAULT_VALUE)
                  for i in range(ROOM_NUMBER)] for j in range(AGG_NUMBER)]
temp_all_text = DoubleVar(window, DEFAULT_VALUE)
# Temperature Value Labels
temp_val_label = [[Label(master=window, textvariable=temp_val_text[j][i]).grid(
    row=j+1, column=i+2) for i in range(ROOM_NUMBER)] for j in range(AGG_NUMBER)]
temp_all_label = Label(master=window, textvariable=temp_all_text, font="bold").grid(
    row=5, column=2, columnspan=5, pady=(0, 20))

# Humidity Value Texts
humd_val_text = [[DoubleVar(window, DEFAULT_VALUE)
                  for i in range(ROOM_NUMBER)] for j in range(AGG_NUMBER)]
humd_all_text = DoubleVar(window, DEFAULT_VALUE)
# Humidity Value Labels
humd_val_label = [[Label(master=window, textvariable=temp_val_text[j][i]).grid(
    row=j+6, column=i+2) for i in range(ROOM_NUMBER)] for j in range(AGG_NUMBER)]
humd_all_label = Label(master=window, textvariable=temp_all_text, font="bold").grid(
    row=10, column=2, columnspan=5)

# window.after(1000, writeCsvFile)  # After 1 second, call writeCsvFile

window.mainloop()
