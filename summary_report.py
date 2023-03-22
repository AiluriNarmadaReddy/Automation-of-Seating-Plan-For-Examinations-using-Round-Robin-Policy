import pandas as pd
import sys
#hallticket_sheet=input("enter hallticket sheet name")
hallticket_sheet=sys.argv[1]
seating_xl = pd.ExcelFile(hallticket_sheet+'.xlsx')
sheetnames = seating_xl.sheet_names
summary_df = pd.DataFrame()
count_list = []
sheet_list = []
for sheet in sheetnames:
	seating_df = pd.read_excel(seating_xl , sheet)
	no_of_studs = int(seating_df.pivot_table(index = ['SubjectCode'], aggfunc ='size'))
	sheet_wise = seating_df.drop_duplicates(subset =['SubjectCode'],keep = 'first')
	summary_df = pd.concat([summary_df, sheet_wise],ignore_index=True)
	count_list.append(no_of_studs) 
	sheet_list.append(sheet)
summary_df['tot_count'] = count_list
summary_df['sheet_name'] = sheet_list
summary_df.drop(['Hallticketno','Serial No'],axis = 1,inplace = True)
summary_df.sort_values(by=['tot_count'],ascending=False,inplace = True)
summary_df.to_excel(hallticket_sheet+'_summary.xlsx',index = False)
