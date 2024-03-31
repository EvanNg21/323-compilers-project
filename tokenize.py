```import re

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

```