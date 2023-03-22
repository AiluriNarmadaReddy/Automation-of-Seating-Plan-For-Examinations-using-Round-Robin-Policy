import hall_plan as hz
import dataframes as di
from collections import defaultdict

sheet_names = []
for i in range(0, hz.no_of_halls):
    sheet_names.append(di.hall_df.iloc[i, 0])
    sheet_names = list(sheet_names)

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


for_room = []
data = []
for df in hz.hall_list:

    halltickets_by_branch = {}
    for branch in bname.values():
        halltickets_by_branch[branch] = []
    for i, row in df.iterrows():
        for j, cell in row.iteritems():
            if cell != None:
                hallticket = cell.strip()
                if len(hallticket) != 10:
                    continue
                branch_code = hallticket[6:8]
                if branch_code not in bname:
                    continue
                branch = bname[branch_code]
                halltickets_by_branch[branch].append(hallticket)

    empty_branches = [branch for branch in halltickets_by_branch if len(halltickets_by_branch[branch]) == 0]
    for branch in empty_branches:
        del halltickets_by_branch[branch]

    for_room.append(halltickets_by_branch)

    collegecodes_by_branch = {}
    for branch, halltickets in halltickets_by_branch.items():
        collegecodes = []
        for hallticket in halltickets:
            collegecode = hallticket[2:4]
            if collegecode not in collegecodes:
                collegecodes.append(collegecode)
        collegecodes_by_branch[branch] = collegecodes

    #number = sheet_names[i]
    keynames = list(halltickets_by_branch.keys())
    data.append({'keynames':keynames, 'collegecodes_by_branch': collegecodes_by_branch})
    #print(hz.no_of_halls)
    code=[]
    for i in range(0,len(data)):
        code.append(data[i]['collegecodes_by_branch'].values())
#for i in range(0,len(sheet_names)):
#    print(i)
for d in for_room:
    for key in d:
        print(f"{key}: {len(d[key])}")

output_dict = {}

for i in range(len(sheet_names)):
    halltickets_by_branch = for_room[i]

    sheet_dict = {}
    for branch in halltickets_by_branch:
        count = len(halltickets_by_branch[branch])
        sheet_dict[branch] = count

    output_dict[sheet_names[i]] = sheet_dict

print(output_dict)
merge_dict={}
for key, value in output_dict.items():
    count = len(value.keys())
    merge_dict[key] = count
print(merge_dict)
#print(code)

#print(type(rooms[0]))
#print(keynames)
#print(for_room)