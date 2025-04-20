# Compiler System Components

➡️ *Refer to this folder for the complete Python source files and C code examples used in macro processing and compiler stages.*

📁 [Click Here to Access Source Files & Examples](https://tinyurl.com/Expspcc)  

This repository contains a complete compiler system implementation with various components that work together to process and optimize code. Below is a detailed explanation of each component:

## 1. Lexical Analyzer (`LexicalAnalyzer.py`)

The Lexical Analyzer is the first phase of the compiler that converts the source code into a sequence of tokens. It uses regular expressions to identify different types of tokens:

- Keywords: `if`, `else`, `while`, `int`, `return`, `float`
- Operators: `+`, `-`, `*`, `/`, `=`, `==`, `<`, `>`, `!=`
- Numbers: Integer and floating-point numbers
- Identifiers: Variable and function names
- Special characters: Parentheses, semicolons

The analyzer uses a token specification list to match patterns and categorize tokens appropriately.

## Detailed Code Explanations

### 1. LexicalAnalyzer.py Line-by-Line Explanation

```python
import re  # Import regular expression module for pattern matching

def lexical_analyzer(source_code):
    # Define sets of keywords and operators for token classification
    keywords = {'if', 'else', 'while', 'int', 'return', 'float'}
    operators = {'+', '-', '*', '/', '=', '==', '<', '>', '!='}
    tokens = []  # List to store the generated tokens

    # Define token patterns using regular expressions
    token_spec = [
        ('NUMBER', r'\d+(\.\d*)?'),  # Matches integers and floating-point numbers
        ('IDENT', r'[A-Za-z_]\w*'),  # Matches identifiers (variable names)
        ('OP', r'==|!=|<=|>=|[+\-*/=<>]'),  # Matches operators
        ('SEMI', r';'),  # Matches semicolons
        ('LPAREN', r'\('),  # Matches left parentheses
        ('RPAREN', r'\)'),  # Matches right parentheses
        ('SKIP', r'[ \t]+'),  # Matches whitespace (to be skipped)
        ('MISMATCH', r'.'),  # Matches any other character (error case)
    ]

    # Create a single regular expression from all token patterns
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)
    
    # Process the source code character by character
    for mo in re.finditer(tok_regex, source_code):
        kind = mo.lastgroup  # Get the type of token matched
        value = mo.group()   # Get the actual value of the token
        
        # Process each token type and add to tokens list
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
            continue  # Skip whitespace
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value}')
    return tokens
```

## 2. Shift-Reduce Parser (`Shift-ReduceParser.py`)

This component implements a shift-reduce parsing algorithm for a simple arithmetic expression grammar. It:

- Uses a grammar defined for expressions (E → E+T | T, T → T*F | F, F → (E) | id)
- Implements a parsing table with shift and reduce actions
- Processes input strings to validate their grammatical correctness
- Provides detailed parsing steps showing the stack and input at each stage

## 3. Intermediate Code Generation (`IntermediateCodeGeneration.py`)

This module converts infix expressions into three-address code (3AC). It includes:

- `precedence()`: Determines operator precedence
- `infix_to_postfix()`: Converts infix expressions to postfix notation
- `generate_3ac()`: Generates three-address code from postfix expressions

The generated intermediate code is optimized for further processing and makes the code more machine-independent.

## 4. Code Optimization (`CodeOptimization.py`)

This module implements several code optimization techniques:

- **Constant Folding**: Evaluates constant expressions at compile time
- **Constant Propagation**: Replaces variables with their known constant values
- **Dead Code Elimination**: Removes unused code
- **Common Subexpression Elimination**: Eliminates redundant computations
- **Loop Unrolling**: Expands loops to reduce loop overhead

Each optimization technique can be applied independently or in combination.

## 5. Macro Processor Pass 1 (`MacroProcessorPass1.py`)

The first pass of the macro processor that:

- Reads source code containing macro definitions
- Creates a Macro Name Table (MNT)
- Generates a Macro Definition Table (MDT)
- Handles macro parameters and their substitution
- Processes macro definitions and their arguments

## 6. Macro Processor Pass 2 (`MacroProcessorPass2.py`)

The second pass of the macro processor that:

- Expands macro calls in the source code
- Maintains an Argument List Array (ALA)
- Substitutes actual arguments for formal parameters
- Generates the final expanded code

## Usage Example

```python
# Example of using the complete system
source_code = "int a = b + 3;"

# 1. Lexical Analysis
tokens = lexical_analyzer(source_code)

# 2. Parsing
# Use Shift-Reduce Parser for expression parsing

# 3. Intermediate Code Generation
expr = "a+b*c"
postfix = infix_to_postfix(expr)
tac = generate_3ac(postfix)

# 4. Code Optimization
code = ["a = 2 + 3", "b = a", "c = b + 5"]
optimized = constant_folding(code)

# 5. Macro Processing
# First pass processes macro definitions
macro_pass1("macro_input.txt")
# Second pass expands macro calls
expanded = macro_pass2(source_program)
```

## Dependencies

- Python 3.x
- No external libraries required

## File Structure

```
.
├── LexicalAnalyzer.py
├── Shift-ReduceParser.py
├── IntermediateCodeGeneration.py
├── CodeOptimization.py
├── MacroProcessorPass1.py
└── MacroProcessorPass2.py
```

Each component can be used independently or as part of the complete compiler system. The modules are designed to be modular and can be extended with additional functionality as needed. 
