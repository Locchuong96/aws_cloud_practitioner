'''
utils/remove_blank.py /path/to/file.txt
'''
import sys

file_path = sys.argv[1]

with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove blank lines
non_blank_lines = [line for line in lines if line.strip()]

with open(file_path, 'w') as file:
    file.writelines(non_blank_lines)
