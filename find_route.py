import sys
from file_operation import *

print("Number of arguments"), len(sys.argv), "arguments."
print("Argument List:"), str(sys.argv), "\n"

print_file("input1.txt")
