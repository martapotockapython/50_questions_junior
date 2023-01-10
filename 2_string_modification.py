# QUESTION 2 - What will happen when you run the code below?

my_string = "abcdefg"            # Assign string 'abcdefg' to variable 'a'.
print(my_string[1])              # Print element located under index=1 in string 'a'.
my_string[1] = 'X'               # Try to modify the string. This will raise TypeError

string_as_list = list(my_string)        # Create a list containing letters from string 'a'.
string_as_list[1] = 'X'                 # Modify element located under index=1. List are mutable objects so this operation is allowed.
my_string = "".join(string_as_list)     # Create string 'a' by joining elements of a list using an empty string as a separator.
print(my_string)

new_string = my_string.replace('b', 'X')  # Create NEW string. Replace method will replace all occurence of 'b'.
my_string = new_string                    # Assign new_string to my_string variable.
print(my_string)