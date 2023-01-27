# QUESTION 3 - Write a code, that will present the main differences between a list and a tuple.

my_list = [1, 2, 3, True, (1, 2)]          # A list containing different data types, including a tuple.
my_tuple = (4, 5, 6, False, ['x', 'y'])    # A tuple containing different data types, including a list.
                                           # Lists are defined using square brackets [].
                                           # Tuples are definedusing parenthesis ().

my_list[2] = 'three'                       # List modification.
print(my_list)

#my_tuple[2] = 'six'                        # Tuple modification - forbidden operation, resulting in TypeError.
