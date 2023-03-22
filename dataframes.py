import pandas as pd
import summary_report as sr
import sys



#workbook = openpyxl.load_workbook('22fn_1.xls')
# TODO:1 Converting halls.xlsx to dataframe
size = []
#tsheet_path = input("enter hallsheet name: ")#"halls.xlsx"
tsheet_path=sys.argv[2]
tsheet_path=tsheet_path+".xlsx"
hall_df = pd.read_excel(tsheet_path, header=None, sheet_name=0, skiprows=1)
l = len(hall_df)
for i in range(0, l):
    size.append(hall_df.iat[i, 1] * hall_df.iat[i, 2])
hall_df['size'] = size
#print(hall_df)
# TODO :2 Converting 22fn.xlsx to dataframe
#sheet1=input("enter sheet1 name: ")
#sheet1=sheet1+".xlsx"
session_df = pd.read_excel(sr.hallticket_sheet+"_summary.xlsx", header=None, sheet_name=0, skiprows=1)
#print(session_df)
year=list(session_df[0])
sem=list(session_df[1])
#print(year,sem)
# TODO:3 making a dictionary having 6th column of session_df as key and its value is list of rollno

session_xl = pd.ExcelFile(sr.hallticket_sheet+'.xlsx')

sheetnames = session_xl.sheet_names

#print(sheetnames)
stu_list = []
for sheet in sheetnames:
    seating_df = pd.read_excel(session_xl, sheet)
    sheetwise_stu_list = seating_df.iloc[:, 6].tolist()
    stu_list.append(sheetwise_stu_list)
subject_list=[]
for sheet in sheetnames:
    seating_df = pd.read_excel(session_xl, sheet)
    sheetwise_subject_list = seating_df.iloc[:, 5].tolist()
    subject_list.append(sheetwise_subject_list)
#print(stu_list)
#print(subject_list)
#for i in range (0,len(stu_list)):
#   x= len(stu_list[i])
sheet_names_to_stu_list=dict(zip(sheetnames,stu_list))
sheet_names_to_subject_list=dict(zip(sheetnames,subject_list))
#print(sheet_names_to_stu_list)
#print(sheet_names_to_subject_list)

#TODO 4:CONVERT sheet_names_to_stu_list to dataframe
main_dataframe = pd.DataFrame.from_dict(sheet_names_to_stu_list, orient='index')
main_dataframe=main_dataframe.transpose()
#print(main_dataframe)




