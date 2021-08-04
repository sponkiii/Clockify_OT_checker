import numpy as np
import pandas as pd
import csv



# clockify_data = open("Data/Clockify_Summary_Report_01_06_2021-01_31_2021.csv", "r",encoding='utf-8-sig')
#data_location = "Data/Clockify_Summary_Report_01_06_2021-01_31_2021.csv"
#filtered = pd.Series(clockify_data)

# read csv file with pandas
clockify_data = pd.read_csv('Data/Clockify_Summary_Report_01_06_2021-01_31_2021.csv')

# took cols that I only need
data_frame = clockify_data.filter(items=['User', 'Date', 'Time (h)','Time (decimal)'])

# Cleaning rows with empty cells
cleaned_rows_with_null = data_frame.dropna()

# convert pandas to list so we can edit data
data_list = cleaned_rows_with_null.values.tolist()


# ====now we make new table with rounded off OTs to 8hrs only
# new_table = []
#user_data = [[3,4,6,],[25,36,75],[35,6,93]]
user_data = []
date_data = []
Time_in_hours = []
Time_in_decimal = []
Time_in_OT = []

# ====this don't work
# x=0
# for x in user_data:
#     print(user_data[x][0],user_data[x][1],user_data[x][2])
# =======
# ======these motherfuckers work tho
# x = 2
# y = 1
# print(user_data[x][y])
# for i in range(3):
#     print(user_data[i][2])
# print(user_data[0][0],user_data[1][1],user_data[2][2])
# ============================

# for x in data_list:
#     for i in range(3):
#         if i == 0:
#             user_data.append(data_list[x][i])
#         elif i == 1:
#             date_data.append(data_list[x][i])
#         elif i == 2:
#             Time_in_hours.append(data_list[x][i])
#         elif i == 3:
#             Time_in_decimal.append(data_list[x][i])
#             if data_list[x][i] < 8:
#                 Time_in_OT.append(data_list[x][i])
#             elif data_list[x][i] > 8:
#                 Time_in_OT.append(8)
# for rows in data_list:
#     user_data.append(rows[0])
#     date_data.append(rows[1])
#     Time_in_hours.append(rows[2])
#     Time_in_decimal.append(rows[3])
#     if rows[3] < 8:
#         Time_in_OT.append(rows[0])
#     elif rows[3] > 8:
#         Time_in_OT.append(8)
# for rows in data_list:
#     user_data.append(data_list[rows][0])
#     date_data.append(data_list[rows][1])
#     Time_in_hours.append(data_list[rows][2])
#     Time_in_decimal.append(data_list[rows][3])
#     if data_list[rows][3] < 8:
#         Time_in_OT.append(data_list[rows][0])
#     elif data_list[rows][3] > 8:
#         Time_in_OT.append(8)
for x in range(len(data_list)):
# for x in range(981):
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
# data_df = pd.DataFrame(data_dictioinary, columns = [
#     "user_data", "date_data", "Time_in_hours", "Time_in_decimal", "Time_in_OT"
# ]
# )

# then print new csv file with new data

# ==================print testings
print(cleaned_rows_with_null)
#print(data_list)
#print(data_list[0][0],data_list[0][1],data_list[0][2],data_list[0][3])
print(data_df)

# print("==========================")
# print(data_df)

# ================converting df to csv and save as csv file
new_data_csv = data_df.to_csv('Data/Generated_data/new_data.csv', index = False) 
print('\nCSV String:\n', "new_data_csv") 



# User = []
# Date = []
# Time_in_decimal = [] 

# for infos in clockify_data["items"]:
#     User.append()
#     Date.append()
#     Time_in_decimal.append()


# f = open("demofile.txt", "r")
# print(f.read())
# C:/Users/arvin/source/Exam/
# print(Needed_cols.head(15)) prints top 15
# print(Needed_cols.tail(15)) prints last 15

# https://datatofish.com/convert-pandas-dataframe-to-list/
# https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
# https://docs.python.org/3/library/tk.html#:~:text=tkinter%20is%20a%20set%20of%20wrappers%20that%20implement,which%20includes:%20references,%20tutorials,%20a%20book%20and%20others.
