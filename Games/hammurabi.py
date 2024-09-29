## This was a game I played as a young child in the 70s.
## Version 2:  Refactored most of the logic into functions

import random

# Initialize game variables
def initialize_game():
    state = {
        "year": 1,
        "population": 100,
        "grain": 2800,  # in bushels
        "land": 1000,   # in acres
        "harvest_per_acre": 3,
        "rats_ate": 200,  # bushels
        "land_price": random.randint(17, 26),
        "bushels_to_feed": 0  # Track grain allocated to feeding population
    }
    return state

# Display current status to the player
def display_status(state):
    print(f"\nYear {state['year']}:")
    print(f"Population: {state['population']} people")
    print(f"Grain in storage: {state['grain']} bushels")
    print(f"Land owned: {state['land']} acres")
    print(f"Current land price: {state['land_price']} bushels per acre")

# Ask player for their decision each year
def player_decision(state):
    # Buy or sell land
    acres_to_buy = int(input(f"How many acres do you wish to buy? (0 to sell land, negative to sell): "))
    if acres_to_buy > 0:
        cost = acres_to_buy * state['land_price']
        if cost > state['grain']:
            print("You don't have enough grain to buy that much land!")
            return False
        state['grain'] -= cost
        state['land'] += acres_to_buy
    elif acres_to_buy < 0:
        state['land'] += acres_to_buy  # selling land
        state['grain'] -= acres_to_buy * state['land_price']

    # Feed the people
    bushels_to_feed = int(input("How many bushels to feed your people? "))
    if bushels_to_feed > state['grain']:
        print("You don't have enough grain to feed that much!")
        return False
    state['grain'] -= bushels_to_feed
    state['bushels_to_feed'] = bushels_to_feed  # Store in state

    # Planting crops
    acres_to_plant = int(input("How many acres do you wish to plant? "))
    if acres_to_plant > state['land']:
        print("You don't have enough land to plant that much!")
        return False
    if acres_to_plant * 2 > state['grain']:
        print("You don't have enough grain to plant that much!")
        return False
    state['grain'] -= acres_to_plant * 2

    return True

# Handle harvest, rats, and population events
def resolve_year(state):
    # Harvest
    state['harvest_per_acre'] = random.randint(1, 6)
    harvest = state['harvest_per_acre'] * state['land']
    state['grain'] += harvest
    print(f"Harvested {harvest} bushels at {state['harvest_per_acre']} bushels per acre.")

    # Rats eating grain
    if random.random() < 0.3:  # 30% chance of rats
        rats_ate = int(state['grain'] * random.uniform(0.1, 0.3))  # Eat 10%-30% of grain
        state['grain'] -= rats_ate
        print(f"Rats destroyed {rats_ate} bushels of grain!")

    # Population growth or death
    starved = max(0, state['population'] - state['bushels_to_feed'] // 20)
    state['population'] -= starved
    immigrants = random.randint(0, 10)
    state['population'] += immigrants
    print(f"{starved} people starved, {immigrants} people immigrated.")

    # Update year and land price
    state['year'] += 1
    state['land_price'] = random.randint(17, 26)

def check_end_condition(state):
    if state['population'] <= 0:
        print("Everyone in your city has starved. Game over!")
        return True
    if state['year'] > 10:
        print("You have ruled for 10 years. Here's your final report:")
        display_status(state)
        return True
    return False

# Main game loop
def hammurabi_game():
    state = initialize_game()
    print("Welcome to Hammurabi! You are the ruler of a small city.")
    
    while True:
        display_status(state)
        
        if not player_decision(state):
            print("Invalid decision! Please try again.")
            continue
        
        resolve_year(state)
        
        if check_end_condition(state):
            break

# Run the game
hammurabi_game()
