# Create your views here.
from django.shortcuts import render
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from django_pandas.io import *
import pandas as pd
import csv
from django.http import HttpResponse 
#import tkinter.filedialog
text1 = str()
text2 = str()

# for showing an entire page
def home(request):
    
    #file_path_string = tkFileDialog.askopenfilename()
    return render(request,'home.html',{'name':'Arvin Ramirez'})

def compute(request):
    # for POST
    val1 = request.POST["File1"]
    val2 = request.POST["File2"]
    # new code
    text1 = val1
    text2 = val2
    # new code
    res = open_file1(text1)
    # res = open_file1(val1)

    filtered = confirm_over_time(res)

    #can use for aother val to show
    res1 = filtered

    
    res2 = save_file(res1)

    return render(request, 'result.html',{'result':res,'result1':res1, 'result2':res2})

def open_file1(dito):
    # read csv file with pandas
    clockify_data = pd.read_csv(dito)
    
    # took cols that I only need
    data_frame = clockify_data.filter(items=['User', 'Date', 'Time (h)','Time (decimal)'])

    # Cleaning rows with empty cells
    cleaned_rows_with_null = data_frame.dropna()

    # convert pandas to list so we can edit data
    #data_list = cleaned_rows_with_null.values.tolist()
    return cleaned_rows_with_null

def save_file(etoPre):
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
    new_data_csv = etoPre.to_csv(new_name, index = False)
    root1.destroy()
    
    return new_name

def confirm_over_time(eto):
    # convert pandas to list so we can edit data
    data_list = eto.values.tolist()

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
    return data_df











def ChooseFile1(request):
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    # new code1
    from_text2 = text2

    val = root.filename
    root.destroy()

    return render(request,'home.html',{'file1':val,'file2':from_text2})
    # return HttpResponse(request,'home.html',{'file1':val})

def ChooseFile2(request):
    # new code1
    from_text1 = text1

    val2 = "printed with btn2"
    return render(request,'home.html',{'file2':val2,'file1':from_text1})

# for showing single line and single html line
# def home(request):

#     return HttpResponse(welcome())

# def welcome():
#     return "<h1>Hello World pre</h1> <p>eto na ang lama ng page na to</p> <div>this div</div>"
    
    # to run ven:
    # myVirtualEnvironment\Scripts\activate.bat

    # to run server:
    # python manage.py runserver

    #pip install django-pandas
    #pip install tkfilebrowser