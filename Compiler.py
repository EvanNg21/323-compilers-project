import re


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

#tokenize the code
def tokenize(no_spaces):
    tokens = []
    # Initialize lists of each category
    keywords = ["def", "return", "print", "input"]
    operators = ["+", "-", "*", "/", "%", "**", "++", "--", "==", ">", "<", "!=", "&&", "||"]
    delimiters = ["(", ")", "{", "}", "[", "]", ",", ";", ":"]

    # Define lists of patterns of each category
    keyword_pattern = '|'.join([re.escape(kw) for kw in keywords])
    identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
    operator_pattern = '|'.join([re.escape(op) for op in operators])
    delimiter_pattern = '|'.join([re.escape(d) for d in delimiters])
    literal_pattern = r'\d+'

    # Concatenate lines into a single string
    code_without_spaces = ''.join(no_spaces)

    # Tokenize the concatenated code
    for token in re.findall(f'{keyword_pattern}|{identifier_pattern}|{operator_pattern}|{delimiter_pattern}|{literal_pattern}', code_without_spaces):
        if token in keywords:
            tokens.append(('Keyword', token))
        elif re.match(identifier_pattern, token):
            tokens.append(('Identifier', token))
        elif token in operators:
            tokens.append(('Operator', token))
        elif token in delimiters:
            tokens.append(('Delimiter', token))
        elif re.match(literal_pattern, token):
            tokens.append(('Literal', token))
    return tokens

    


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
        line = line.strip()
        if line:
            print(line)

    print("\nTOKENIZED CODE:")
    for line in no_spaces:
        tokens = tokenize(line)  # Correcting the function call
        for category, token in tokens:
            print(f'{category}: {token}')

if __name__ == "__main__":
    main()
