import re
from tokenize_file import tokenize 

# Read the file
def read_file(file):
    lines = []
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines

# Remove the spaces from each line
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
    lines = read_file(file)
    # Remove spaces from the lines
    no_spaces = remove_spaces(lines)
    # Tokenize the code using tokenize from the other file
    tokens = tokenize(no_spaces)  # Using tokenize function from tokenize.py

    # Print tokens (for demonstration)
    print("CODE WITHOUT SPACES AND COMMENTS:")
    for line in no_spaces:
        print(line.strip())

    print("\nTOKENIZED CODE:")
    for line in no_spaces:
        tokens = tokenize(line)  # Correcting the function call
        for category, token in tokens:
            print(f'{category}: {token}')

if __name__ == "__main__":
    main()
