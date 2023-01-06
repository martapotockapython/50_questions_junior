# QUESTION 1 - A list of unique elements
# Using provided list A create a list B that contains only unique elements of list A.

A = [1, 2, 3, 3, 2, 1, 2, 3]  # -> B = [1,2,3]

B = []  # create empty list B
for element in A:  # for each element in list A
    if element not in B:  # if element does not exist in list B
        B.append(element)  # add element to list B
print(B)  # print list B

B = list(set(A))  # create list B from the set created from list A
print(B)
