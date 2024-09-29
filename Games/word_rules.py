import re

'''
The re library is for searching, matching, and manipulating strings based on specific patterns.
We are using it to filter out combinations of letters that are unlikely to be words.
'''

def is_vowel(letter: str) -> bool:
    """
    Checks if a given letter is a vowel.
    """
    return letter in 'aeiou'

def is_consonant(letter: str) -> bool:
    """
    Checks if a given letter is a consonant.
    """
    return letter.isalpha() and not is_vowel(letter)

def is_pronounceable(combo: str) -> bool:
    """
    Checks if a given letter combination is pronounceable. 
    """
    for pattern in unpronounceable_patterns:
        if pattern in combo:
            return False
    return True

def filter_combinations(combos: list[str]) -> list[str]:
    """
    Filters a list of letter combinations to remove unreasonable or unlikely patterns.

    The function applies several criteria to each combination, including checks for:
    - All vowels or no vowels.
    - Three or more of the same letter in a row.
    - Four consecutive consonants.
    - Starting with three or more consonants.
    - A 'q' not followed by a 'u' and then a vowel.
    - Three consecutive vowels.
    - Pronounceable patterns.
    - Removes duplicate combinations.
    """
    filtered_combos = []
    seen_combos = set()  # To track unique combinations

    for combo in combos:
        # Remove combos that are all vowels or have no vowels
        if all(is_vowel(char) for char in combo) or not any(is_vowel(char) for char in combo):
            continue
        
        # Remove combos with 3 or more of the same letter in a row
        if re.search(r'(.)\1{2,}', combo):
            continue
        
        # Remove combos with 4 consecutive consonants
        if re.search(r'[^aeiou]{4,}', combo):
            continue
        
         # Remove combos ending with double vowels
        if combo.endswith(('aa'', 'ii', 'uu')):
            continue
        
        # Remove combos starting with 3 or more consonants
        if re.match(r'^[^aeiou]{3,}', combo):
            continue
        
        # Remove combos with 3 consecutive vowels
        if re.search(r'[aeiou]{3,}', combo):
            continue
        
        # Check if a 'q' is followed by a 'u' and then a vowel
        if 'q' in combo:
            q_index = combo.index('q')
            if (q_index + 1 >= len(combo) or combo[q_index + 1] != 'u' or 
                (q_index + 2 >= len(combo) or not is_vowel(combo[q_index + 2]))):
                continue

        # Check for pronounceable patterns
        if not is_pronounceable(combo):
            continue
        
        # Add to filtered combos if it's unique
        if combo not in seen_combos:
            filtered_combos.append(combo)
            seen_combos.add(combo)  # Track the combination to prevent duplicates
    
    return filtered_combos

# List of unpronounceable patterns or rare/forbidden pairings
unpronounceable_patterns = [
    'jq', 'zx', 'qv', 'xc', 'xz', 'vq', 'bz', 'qw', 'kp', 'sv', 'mv', 
    'bcdf', 'bcfg', 'bcdg', 'cdfg', 'ghjk', 'jklm', 'mnop', 'qrs', 'tvw', 
    'vwxyz', 'bq', 'cq', 'dq', 'fq', 'gq', 'hq', 'kq', 'lq', 'mq', 'nq', 
    'pq', 'rq', 'sq', 'tq', 'vq', 'wq', 'xq', 'yq', 'zq'
]
