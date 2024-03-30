import re

#read the
def read_file(file):
    lines = []
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines
#remove the spaces from each line
def remove_spaces(lines):
    no_spaces = []
    for line in lines:
        # Remove comments
        line = re.sub(r'#.*', '', line)
        # Remove spaces
        line_without_spaces = line.replace(" ", "")
        no_spaces.append(line_without_spaces)
    return no_spaces
def main():
    # Define the file
    file = "input.txt"
    # Read the lines from the file


if __name__ == "__main__":
    main()