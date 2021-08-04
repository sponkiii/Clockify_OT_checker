# for opening file and saving files
from tkinter import filedialog
from tkinter import *
import numpy as np
import pandas as pd
import csv

# ===============================OPENING FILE================================
#used tkinter ans asked to choose the file to use and store it on variable root.filename
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
#print (root.filename)

# read csv file with pandas
clockify_data = pd.read_csv(root.filename)

# took cols that I only need
data_frame = clockify_data.filter(items=['User', 'Date', 'Time (h)','Time (decimal)'])

# Cleaning rows with empty cells
cleaned_rows_with_null = data_frame.dropna()


# ===============================FILTERING PROCESS================================
# convert pandas to list so we can edit data
data_list = cleaned_rows_with_null.values.tolist()

# ====now we make new table with rounded off OTs to 8hrs only
user_data = []
date_data = []
Time_in_hours = []
Time_in_decimal = []
Time_in_OT = []

for x in range(len(data_list)):
    user_data.append(data_list[x][0])
    date_data.append(data_list[x][1])
    Time_in_hours.append(data_list[x][2])
    Time_in_decimal.append(data_list[x][3])
    if data_list[x][3] < 8:
        Time_in_OT.append(data_list[x][3])
    elif data_list[x][3] >= 8:
        Time_in_OT.append(8)

# ===========make dictionary
data_dictioinary = {
    "user_data" : user_data,
    "date_data" : date_data,
    "Time_in_hours" : Time_in_hours,
    "Time_in_decimal" : Time_in_decimal,
    "Time_in_OT" : Time_in_OT
}

# turn dictionary into pandas
data_df = pd.DataFrame.from_dict(data_dictioinary)

# ==================print testings
print(cleaned_rows_with_null)
print(data_df)

# ===============================SAVING FILE================================

# ==========used root1 to select file loc to save============
root1 = Tk()
root1.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))


# ====saved file loc to new name var then check if file name has .csv on the end
new_name = root1.filename
last_4_char = str(new_name[-4] + new_name[-3] +new_name[-2] + new_name[-1])

if last_4_char != ".csv":
    new_name = root1.filename + (".csv")
else:
    new_name = root1.filename

# ================converting df to csv and save as csv file, used root1 asa directory
new_data_csv = data_df.to_csv(new_name, index = False) 



# =====================file name and location
print('\nCSV String:\n', root1.filename) 
print(new_name)
print(last_4_char)

