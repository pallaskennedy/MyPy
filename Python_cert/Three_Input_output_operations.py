''' 3. Input and Output Operations 
3.1 Construct and analyze code segments that perform file input and  
output operations 
• open, close, read, write, append, check existence, delete, with statement 



3.2 Construct and analyze code segments that perform console input  
and output operations 
• Read input from console, print formatted text (string.format() method,  
f-String method), use command-line arguments 
'''
###### string format methods #####

##  string format method:
def format_money(amount):
    return '${:,.2f}'.format(amount)

S = '{0} is derived from the {1} {2}'
print(S.format('none', 'no', 'one'))
print(S.format('Etymology', 'Greek', 'Ethos'))
print(S.format("December", "Latin", "decem"))

from math import pi
print('Pi rounded to {0} decimal places is {1:.2f}.'.format(2, pi))
for i in range(1, 10, 2):
    print('Pi rounded to {0} decimal places is {1:.{0}f}.'.format(i, pi))

# as long as the order doesn't change!
print('Pi rounded to {:.2f} decimal places is {:.2f}.'.format(2, pi))

## formated string literal method
name = "Alice"
age = 30
f_string = f"My name is {name} and I am {age} years old."
print(f_string)   # faster and more flexible than string concatenation
                  # could be excellent for loops

x = 5
y = 10
result = f"The sum of {x} and {y} is {x + y}."
print(result)

pi = 3.141592653589793
formatted_pi = f"Value of Pi: {pi:.2f}"
print(formatted_pi)

person = {"name": "Bob", "age": 25}
info = f"Name: {person['name']}, Age next year: {person['age'] + 1}"
print(info)

multiline_string = f"""
This is a
multiline
f-string.
"""
print(multiline_string)

'''
f-strings:
   Pros:
    Conciseness and Readability:  F-strings provide a concise and readable syntax for
    embedding expressions within string literals.
    The syntax is more natural and resembles the final output, making it easier to
    understand.
    
    Expression Evaluation: Expressions inside f-strings are evaluated at runtime,
    allowing for dynamic content and complex expressions.

    Direct Access to Variables: F-strings have direct access to variables in the current
    scope, making it convenient to reference them directly.
    
    Performance: F-strings are often faster than other formatting methods due to their
    optimized implementation.

  Cons:
    Compatibility: F-strings are available in Python 3.6 and later, so code using them
    may not be compatible with earlier Python versions.
    
    Limited to Literal Strings: F-strings are limited to string literals and expressions.
    They cannot be used for more complex formatting scenarios or for formatting
    elements of data structures.

str.format() method:
  Pros:
    Compatibility: The str.format() method is available in Python 2 and all versions
    of Python 3, making it a more compatible choice for older codebases.
    
    Flexibility: str.format() allows more flexibility and control over formatting,
    especially in complex scenarios or when formatting elements of data structures.

    Localization: str.format() supports localization features, allowing for the
    customization of formatting based on language or regional preferences.
    
  Cons:
    Verbosity: The syntax can be more verbose compared to f-strings, especially
    for simple cases.
    
    Readability: For simple cases, the syntax might not be as clear as f-strings,
    leading to potentially less readable code.
    
    Performance: In some scenarios, str.format() might be slightly slower than f-strings
    due to its more generic nature.
    
Recommendations:
    Use F-strings for Simplicity: Use f-strings when simplicity and readability are crucial.
    F-strings are particularly well-suited for straightforward string formatting within
    the context of modern Python versions.
    
    Use str.format() for Complex Scenarios: Use str.format() when dealing with more
    complex formatting scenarios or when you need to maintain compatibility with
    older Python versions.
'''
