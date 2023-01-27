# QUESTION 4 - What data structure would you use to model a cabinet with 3 drawers,
# each with 3 compartments?
# Create such a model and place the string 'pen' in the middle compartment of the middle drawer.

# A list 'cabinet' contains three nested lists, and each of them contains three nested lists.
cabinet = [[[], [], []], [[], [], []], [[], [], []]]

# Add the string 'pen' to the middle list(representing the middle compartment)
# of the middle list (representing the middle drawer).
cabinet[1][1].append('pen')


# Loop over the cabinet list and print sub-lists representing the drawers.
for drawer in cabinet:
    print(drawer)


