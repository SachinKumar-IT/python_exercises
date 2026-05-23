import math

def calculation(height, width, coverage):
    no_of_cans = (height * width) / coverage
    no_of_cans = math.ceil(no_of_cans)
    print(f" required cans:{no_of_cans}")

height = int(input("Enter the height of can in meters:"))
width = int(input("Enter the width of can in meters:"))
coverage = 7

