# QUESTION 2 - What will happen when you run the code below?

a = "abcdefg"            # Assign string 'abcdefg' to variable 'a'.
print(a[1])              # Print element located under index=1 in string 'a'.
# a[1] = 'X'             # Try to modify the string. Forbidden operation resulting in TypeError.

a_lista = list(a)        # Create a list containing letters from string 'a'.
a_lista[1] = 'X'         # Modify element located under index=1. List are mutable objects so this operation is allowed.
a = "".join(a_lista)     # Create string 'a' by joining elements of a list using an empty string as a separator.
print(a)
