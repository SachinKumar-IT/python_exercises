# The user enters a string containing a number (e.g., ). Convert it to: 
#an integer
# a float 
#a string again
#Print all three values with their types. 

num_str=input("Enter a number:")

num_int=int(num_str)
num_float=float(num_str)
num_str=str(num_str)

print("The integer value is", num_int, "type is", type(num_int))
print("The float value is", num_float, "type is", type(num_float))
print("The string value is", num_str, "type is", type(num_str))