# QUESTION 4 - What data structure would you use to model a cabinet with 3 drawers,
# each with 3 compartments?
# Create such a model and place the string 'pen' in the middle compartment of the middle drawer.


cabinet = [[[], [], []], [[], [], []], [[], [], []]]
# A list 'cabinet' contains three nested lists, and each of them contains three nested lists.

cabinet[1][1] = 'pen'
# This line writes the string 'pen' to the middle list(representing the middle compartment)
# of the middle list (representing the middle drawer).


for a in cabinet:  # Loop printing three lists representing drawers.
    print(a)
