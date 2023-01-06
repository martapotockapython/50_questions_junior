# QUESTION 3 - Write a code, that will present the main differences between a list a nda tuple.

L = [1, 2, 3, True, (1, 2)]          # A list containing different data types, including a tuple.
T = (4, 5, 6, False, ['x', 'y'])     # A tuple containing different data types, including a list.
                                     # Write a list in brackets [] and a tuple in parentheses ().

L[2] = 'three'                       # List modification - legal operation.
print(L)

T[2] = 'six'                         # A tuple modification - illegal operation, resulting in TypeError.
