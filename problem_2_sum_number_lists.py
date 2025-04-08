def sum_number_lists(list1, list2):
    if len(list1) != len(list2):
        return "Error: The lists are of different lengths."

    try:
        list1 = [float(item) for item in list1]  
        list2 = [float(item) for item in list2]  
    except ValueError:
        return "Error: The lists contain non-number characters."

    return [list1[i] + list2[i] for i in range(len(list1))]

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 3, 4, 4, 5, 5, 6]

result = sum_number_lists(list1, list2)

if isinstance(result, str):  
    print(result)
else:
    print("The resulting list is:", result)