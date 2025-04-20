import re

def lexical_analyzer(source_code):
    keywords = {'if', 'else', 'while', 'int', 'return', 'float'}
    operators = {'+', '-', '*', '/', '=', '==', '<', '>', '!='}
    tokens = []

    token_spec = [
        ('NUMBER', r'\d+(\.\d*)?'),
        ('IDENT', r'[A-Za-z_]\w*'),
        ('OP', r'==|!=|<=|>=|[+\-*/=<>]'),
        ('SEMI', r';'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('SKIP', r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]

    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)
    for mo in re.finditer(tok_regex, source_code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            tokens.append(('NUMBER', value))
        elif kind == 'IDENT':
            if value in keywords:
                tokens.append(('KEYWORD', value))
            else:
                tokens.append(('IDENTIFIER', value))
        elif kind == 'OP':
            tokens.append(('OPERATOR', value))
        elif kind == 'SEMI':
            tokens.append(('SEMICOLON', value))
        elif kind == 'LPAREN':
            tokens.append(('LPAREN', value))
        elif kind == 'RPAREN':
            tokens.append(('RPAREN', value))
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value}')
    return tokens

# Example:
print(lexical_analyzer("int a = b + 3;"))
