import word_rules

def generate_combinations(word: str) -> list[str]:
    """
    Generate all possible combinations of the letters in the input word.
    """
    if len(word) == 0:
        return ['']  # Return an empty string for an empty input

    combinations = []
    
    # Generate combinations using recursion
    def combine(prefix: str, remaining: str):
        if len(remaining) == 0:
            combinations.append(prefix)
            return
        
        for i in range(len(remaining)):
            # Include the current letter and move to the next
            combine(prefix + remaining[i], remaining[:i] + remaining[i+1:])

    combine('', word)
    return combinations

def main() -> None:
    while True:
        word = input("Enter a word to generate combinations: ")
        
        all_combos = generate_combinations(word)
        filtered_combos = word_rules.filter_combinations(all_combos)

        print(f"Number of combinations for '{word}': {len(all_combos)}")
        print(f"Possible usable combinations: {filtered_combos}")
        print("Number of possible usable combinations:", len(filtered_combos))

        # Save to file
        save = input("Do you want to save the filtered combinations to a text file? (yes/no): ").strip().lower()
        if save == 'yes':
            filename = f"{word}.txt"
            with open(filename, 'w') as file:
                for combo in filtered_combos:
                    file.write(combo + '\n')
            print(f"Saved to {filename}")

        # Ask to continue or exit
        again = input("Do you want to generate combinations for another word? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
