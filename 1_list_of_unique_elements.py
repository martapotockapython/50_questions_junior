# QUESTION 1 - A list of unique elements
# Using provided original_list create a unique_list
# that contains only unique elements of original_list.

original_list = [1, 2, 3, 3, 2, 1, 2, 3]  # -> unique_list = [1,2,3]

unique_list = []                     # create empty list unique_list
for element in original_list:        # for each element in list original_list
    if element not in unique_list:   # if element does not exist in list unique_list
        unique_list.append(element)  # add element to list unique_list
print(unique_list)                   # print list unique_list

unique = list(set(original_list))    # create unique_list from the set created from original_list
print(unique)
