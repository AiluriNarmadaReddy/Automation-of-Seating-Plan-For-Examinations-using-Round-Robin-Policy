import pandas as pd
import test as ts

hall_list = []
bname = {
    '01': "civ",
    '02': "eee",
    '03': "mec",
    '04': "ece",
    '05': "cse",
    '12': "it",
    '21': "aer",
    '66': "csm",
    '27': "xyz"
}
no_of_halls = round(ts.total_elements / 48)
for i in range(0,no_of_halls):
    hall_list.append(None)
#print(hall_list)
#print(no_of_halls)
for hall in range(0, no_of_halls):
    hall_list[hall] = pd.DataFrame(index=range(1, 7), columns=range(1, 9))
    #print(hall_plan)

i = 0
j = 0
for hall in range(0, no_of_halls):
    for odd_col in range(1, 5):
        for odd_row in range(1, 7):
            # if i < len(ts.odd_queue) and ts.odd_queue[i] != ts.odd_queue[-1]:
            hall_list[hall].at[odd_row, odd_col * 2 - 1] = ts.odd_queue[i]
            i += 1

    for even_col in range(1, 5):
        for even_row in range(1, 7):
            # if j < len(ts.even_queue) and ts.even_queue[j] != ts.even_queue[-1]:
            hall_list[hall].at[even_row, even_col * 2] = ts.even_queue[j]
            j += 1

    #print(hall_list[hall])
    #pd.set_option(display_columns,'None')
    pd.set_option('display.max_columns', None)

list_of_lists=[]

for df in hall_list:
    column_values=[]

    for col in df.columns:

        # Convert each value in the column to a string and get the 7th and 8th characters
        col_chars = [str(val)[6:8] for val in df[col]]
        #print(col_chars)
        # Add the characters to the list
        col_chars = list(set(col_chars))
        # Add the characters to the list
        column_values.append(col_chars)
    #print(column_values)
    list_of_lists.append(column_values)
  #  print(list_of_lists)

headers = []
for i in range(len(list_of_lists)):
    header = []
    for j in range(len(list_of_lists[i])):
        branches = list_of_lists[i][j]
        branch_names = [bname.get(b, '') for b in branches]
        non_empty_names = [name for name in branch_names if name != '']
        if non_empty_names:
            header.append(','.join(non_empty_names))
    headers.append(header)
    for i in range(len(hall_list)):
        if len(header) < 8:
            header.append('')
print(headers)

for i in range(len(hall_list)):
    hall_list[i].columns = headers[i]
print(hall_list)

all_college_codes=[]
for df in hall_list:
    df_values = df.values.flatten()  # flatten the dataframe values
    result = [value[2:4] for value in df_values if isinstance(value, str)]  # extract 2nd and 3rd characters from each value that is a string
    all_college_codes.append(list(set(result)))
