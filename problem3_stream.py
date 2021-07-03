# Problem 3: Stream, Sensor Streaming
# David Khowanto
# temperature distribution random value: mean = 26.7, stdv = 0.7 
# humidity distribution random value: mean = 65, stdv = 5 

# The program streams data and write into log file every 2 minutes
#   Press button on GUI to stop streaming data
#   Mock data are used for test purposes (saved on mock_data.csv)
#   display and stream ratio 4000:500 ms for mock data

# import libraries
from csv import writer
from random import normalvariate
from time import time, localtime, strftime
import tkinter as tk

# constants 
SLEEP_TIME = 120 * 1000 # miliseconds
FILENAME = 'log.csv'
# FILENAME = 'mock_data.csv' #used_for_mock_data

## stream data every 2 minutes and write to log file
def writeCsvFile():
  # append log file (csv)
  with open(FILENAME, 'a', newline='') as log_file:
    # csv file is delimited with comma
    log_writer = writer(log_file, delimiter=',')
    for n in range(1,6):
      temp_val = normalvariate(26.9, 0.7) # mock temperature value
      humi_val = normalvariate(65, 5)     # mock humidity value
      room_number = "Room" + str(n)       # mock room number
      curr_time = time()                  # current epoch time
      # write to the end of log file 
      log_writer.writerow([curr_time, room_number, temp_val, humi_val])
    # notification for time of last streamed data
    text.set("Last Write: " + strftime("%a, %d %b %Y %H:%M:%S WIB", localtime(curr_time)))
    window.after(SLEEP_TIME, writeCsvFile)
    # window.after(500, writeCsvFile) #used_for_mock_data

window = tk.Tk()

window.rowconfigure([0,1,2], minsize=30, weight=1)
window.columnconfigure(0, minsize=250, weight=1)

text = tk.StringVar()
text.set("Start Streaming")

file_label = tk.Label(master=window, text="File: " + FILENAME)
file_label.grid(row=0, column=0)

time_label = tk.Label(master=window, textvariable=text)
time_label.grid(row=1, column=0)

btn_exit = tk.Button(
    master=window, text="Stop Streaming and Logging", command=window.destroy)
btn_exit.grid(row=2, column=0, sticky="nsew")

window.after(1000, writeCsvFile)  # After 1 second, call writeCsvFile

window.mainloop()
