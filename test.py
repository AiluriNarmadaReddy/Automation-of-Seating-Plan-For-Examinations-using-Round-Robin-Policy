import queue
import dataframes as df


list_of_lists =df.stu_list

# calculate total number of elements
total_elements = sum(len(sublist) for sublist in list_of_lists)
no_of_halls=round(total_elements/48)
# calculate target number of elements for each queue
target_elements = total_elements // 2

# initialize the two queues
temp_odd_queue = []
temp_even_queue = []

# iterate over the sublists and push them into queue1 until the target is reached
current_elements = 0
for sublist in list_of_lists:
    if current_elements + len(sublist) <= target_elements:
        temp_odd_queue.append(sublist)
        current_elements += len(sublist)
    else:
        break

# push the remaining sublists into queue2
for sublist in list_of_lists[len(temp_odd_queue):]:
    temp_even_queue.append(sublist)

# print the two queues
#print(temp_odd_queue)
#print(temp_even_queue)
odd_queue = [item for sublist in temp_odd_queue for item in sublist]
even_queue= [item for sublist in temp_even_queue for item in sublist]

accom_length=48*no_of_halls

for i in range(len(odd_queue),accom_length//2):
    odd_queue.append(None)

for i in range(len(even_queue),accom_length//2):
    even_queue.append(None)
#print(odd_queue)
#print(even_queue)