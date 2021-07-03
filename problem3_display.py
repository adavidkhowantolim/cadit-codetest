from csv import reader
from time import localtime, strftime
from tkinter import *
from numpy import max, min, mean, median

# constants
SLEEP_TIME = 15 * 60 * 1000  # miliseconds
FILENAME = 'log.csv'
DEFAULT_VALUE = 0.0
ROOM_NUMBER = 5
AGG_NUMBER = 4
Temp = [[] for i in range(ROOM_NUMBER)]
Humd = [[] for i in range(ROOM_NUMBER)]

def setGuiText(last_time):
  global Temp, Humd
  setAggVal(1,Temp[0],Humd[0])                    # Room 1 statistics
  setAggVal(2,Temp[1],Humd[1])                    # Room 2 statistics
  setAggVal(3,Temp[2],Humd[2])                    # Room 3 statistics
  setAggVal(4,Temp[3],Humd[3])                    # Room 4 statistics
  setAggVal(5,Temp[4],Humd[4])                    # Room 5 statistics
  temp_all_text.set('{:.2f}'.format(mean(Temp)))  # all room average temp value
  humd_all_text.set('{:.2f}'.format(mean(Humd)))  # all room average humidity value
  time_text.set("Last Fetch Data: " + strftime("%a, %d %b %Y %H:%M:%S WIB", localtime(last_time)))

def setAggVal(room, temp, humd):
  temp_val_text[0][room-1].set('{:.2f}'.format(min(temp)))    # temp value minimum
  temp_val_text[1][room-1].set('{:.2f}'.format(max(temp)))    # temp value maximum
  temp_val_text[2][room-1].set('{:.2f}'.format(median(temp))) # temp value median
  temp_val_text[3][room-1].set('{:.2f}'.format(mean(temp)))   # temp value average
  humd_val_text[0][room-1].set('{:.2f}'.format(min(humd)))    # humidity value minimum
  humd_val_text[1][room-1].set('{:.2f}'.format(max(humd)))    # humidity value maximum
  humd_val_text[2][room-1].set('{:.2f}'.format(median(humd))) # humidity value median
  humd_val_text[3][room-1].set('{:.2f}'.format(mean(humd)))   # humidity value average

def readCsvFileFirst():
  global Temp, Humd
  last_time = 0
  with open('mock_data.csv', 'r', newline='') as csvfile:
    log_reader = reader(csvfile, delimiter=',')
    for row in log_reader:
      if (row[1] == "Room1"):
        Temp[0].append(float(row[2]))
        Humd[0].append(float(row[3]))
      elif (row[1] == "Room2"):
        Temp[1].append(float(row[2]))
        Humd[1].append(float(row[3]))
      elif (row[1] == "Room3"):
        Temp[2].append(float(row[2]))
        Humd[2].append(float(row[3]))
      elif (row[1] == "Room4"):
        Temp[3].append(float(row[2]))
        Humd[3].append(float(row[3]))
      elif (row[1] == "Room5"):
        Temp[4].append(float(row[2]))
        Humd[4].append(float(row[3]))
      last_time = float(row[0])
      print(last_time)
  setGuiText(last_time)
  # window.after(SLEEP_TIME, lambda: readCsvFileRepeat(last_time)) # After 15 mins, call readCsvFileRepeat
  window.after(4000, lambda: readCsvFileRepeat(last_time)) #used_for_mock_data

# Same as readCsvFileFirst, but read from end of file,
# so only need to add new data to the global list Temp and Humd
# determine which data to read is based on timestamps
def readCsvFileRepeat(last_time): 
  save_last_time = last_time
  global Temp, Humd
  with open('mock_data.csv', 'r', newline='') as csvfile:
    log_reader = reader(csvfile, delimiter=',')
    for row in reversed(list(log_reader)):
      if (float(row[0]) > save_last_time):
        save_last_time = float(row[0])
      if (float(row[0]) > last_time): 
        if (row[1] == "Room1"):
          Temp[0].append(float(row[2]))
          Humd[0].append(float(row[3]))
        elif (row[1] == "Room2"):
          Temp[1].append(float(row[2]))
          Humd[1].append(float(row[3]))
        elif (row[1] == "Room3"):
          Temp[2].append(float(row[2]))
          Humd[2].append(float(row[3]))
        elif (row[1] == "Room4"):
          Temp[3].append(float(row[2]))
          Humd[3].append(float(row[3]))
        elif (row[1] == "Room5"):
          Temp[4].append(float(row[2]))
          Humd[4].append(float(row[3]))
  setGuiText(last_time)
  print(last_time,save_last_time)
  # window.after(SLEEP_TIME, lambda: readCsvFileRepeat(last_time)) # After 15 mins, call readCsvFileRepeat
  window.after(4000, lambda: readCsvFileRepeat(save_last_time)) #used_for_mock_data

window = Tk()  # row = aggregation, column = room number

# head, filename, last updated, and exit button
temp_label = Label(master=window, text="T EMP \N{DEGREE SIGN}C", wraplength=20, font="bold").grid(
    row=1, column=0, rowspan=5)
humd_label = Label(master=window, text="HUMID%", wraplength=1, font="bold").grid(
    row=6, column=0, rowspan=5)
head_label = Label(master=window, text="-", font="bold")
head_label.grid(row=0, column=1)
file_label = Label(master=window, text="File: " + FILENAME)
file_label.grid(row=12, column=1, columnspan=6)
time_text = StringVar()
time_text.set("Start Displaying")
time_label = Label(master=window, textvariable=time_text)
time_label.grid(row=13, column=1, columnspan=6)
btn_increase = Button(master=window, text="Stop Reading and Displaying",
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
temp_val_text = [[StringVar(window, DEFAULT_VALUE)
                  for i in range(ROOM_NUMBER)] for j in range(AGG_NUMBER)]
temp_all_text = StringVar(window, DEFAULT_VALUE)
# Temperature Value Labels
temp_val_label = [[Label(master=window, textvariable=temp_val_text[j][i]).grid(
    row=j+1, column=i+2) for i in range(ROOM_NUMBER)] for j in range(AGG_NUMBER)]
temp_all_label = Label(master=window, textvariable=temp_all_text, font="bold").grid(
    row=5, column=2, columnspan=5, pady=(0, 20))

# Humidity Value Texts
humd_val_text = [[StringVar(window, DEFAULT_VALUE)
                  for i in range(ROOM_NUMBER)] for j in range(AGG_NUMBER)]
humd_all_text = StringVar(window, DEFAULT_VALUE)
# Humidity Value Labels
humd_val_label = [[Label(master=window, textvariable=humd_val_text[j][i]).grid(
    row=j+6, column=i+2) for i in range(ROOM_NUMBER)] for j in range(AGG_NUMBER)]
humd_all_label = Label(master=window, textvariable=humd_all_text, font="bold").grid(
    row=10, column=2, columnspan=5)

window.after(1000, readCsvFileFirst)  # After 1 second, call readCsvFileFirst

window.mainloop()
