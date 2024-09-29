## I created a Fidelity Account and they gave me my name in T9
## in the event I needed to access my account from a phone
## That got me to wondering how many possible letter combinations
## I could form using the digit version of my name.
## That inspired me to write this whimsical little program instead
## of getting work done.
## Enjoy! 😄


## ------------------------------------ imports
import itertools
import word_rules
'''
The itertools library in Python is a built-in module that provides various functions
that create iterators for efficient looping. We are using in the code to generate combinations.

word_rules handles sifting out the combinations that are unlikely to be real words
'''


## ------------------------------------ function definitions
# code and decode functions
def T9_to_letter_combinations(digit_code: str) -> list[str]:
    """
    Converts a string of digits into all possible letter combinations based on the T9 keypad mapping.
    
    The function takes a string of digits (using the T9 digit-to-letter mapping) and generates
    all possible letter combinations that could be represented by that digit sequence.
    """

    letter_lists = [t9_map[digit] for digit in digit_code if digit in t9_map]
    combinations = [''.join(comb) for comb in itertools.product(*letter_lists)] 
    return combinations

def translate_to_T9(input_string: str) -> str:
    """
    Converts an input string into its corresponding T9 digit encoding.
    
    The function takes a string of letters and spaces, and translates each character into the corresponding
    number using the T9 encoding system, where each digit (2-9) corresponds to a set of letters.
    """
    encoded_string = ''
    for char in input_string.lower():  
        if char == ' ': 
            encoded_string += ' '  
        elif char in reverse_t9_map:
            encoded_string += reverse_t9_map[char] 
        else:
            encoded_string += char 
    return encoded_string





def main() -> None:
    """
    The main user interface function for the T9 Encoder Decoder program.

    This function welcomes the user and enters a loop where it prompts for input,
    allowing the user to either encode a string of letters into T9 digits or decode
    a string of T9 digits into possible letter combinations. The user can exit the
    program by typing 'exit'. 

    The function validates user input to ensure only valid characters (letters and digits)
    are processed, and provides feedback for invalid inputs.
    """
    print("Welcome to the T9 Encoder Decoder! 🎤")
    
    while True:
        user_input = input("Enter a string to encode.\nEnter letters or digits only use 1 for space in digit.\nType 'exit' to quit.\n")
        
        if user_input.lower() == 'exit':
            print("Thanks for playing! 👋")
            break
        
        # Check for invalid input
        if not all(char.isalnum() or char.isspace() for char in user_input):
            print("Please enter only letters and digits. Special characters are not allowed. 🚫")
            continue

        # Ensure only letters or digits are inputted
        if any(char.isdigit() for char in user_input) and any(char.isalpha() for char in user_input):
            print("Oops! Please provide either letters or digits, not both. 😅")
            continue

        # If the user gave us numbers, pass it to T9_to_letter_combinations
        if user_input.isdigit():
            all_combos = T9_to_letter_combinations(user_input)
            likely_combos = word_rules.filter_combinations(all_combos)
            print(f'Possible decodes for "{user_input}": "{likely_combos}" 🎉')
            print("Total number of combos:", len(all_combos))
            print("Number of decodes returned:", len(likely_combos))
        # If the user gave us letters, pass it to translate_to_T9
        elif user_input.isalpha() or ' ' in user_input:
            t9_encoded = translate_to_T9(user_input)
            print(f'T9 encoded for "{user_input}": {t9_encoded} 🔢')


## variables
t9_map = {
    '1': [' '],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

reverse_t9_map = {}  # Creating a reverse mapping so we can go from letters to digits
for digit, letters in t9_map.items():
    for letter in letters:
        reverse_t9_map[letter] = digit



# Run the program
if __name__ == "__main__":
    main()
