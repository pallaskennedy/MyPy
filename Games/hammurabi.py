### imports
import random

### State Variables
year = 0
population = 95
bushels_in_store = 2800
acres_owned = 3000
bushels_eaten_by_rats = acres_owned - bushels_in_store
harvest_per_acre = 3
acres_per_person = acres_owned / harvest_per_acre
new_immigrants = 5
user_input = 1
total_number_starved = 0
percent_of_population_that_starved = 0

# New variables for rat patrol and education
rat_patrol = 0
education_level = 0
rat_population = 50  # Initial rat population (affects grain loss and health)
illness_outbreak = False

#### Game loop
while year < 11:
    # Display the stats for the current year
    print(
        f"\nHAMURABI: I BEG TO REPORT TO YOU, IN YEAR {year}, {total_number_starved} PEOPLE STARVED, {new_immigrants} CAME TO THE CITY.")
    print(f"POPULATION IS NOW {population}")
    print(f"THE CITY NOW OWNS {acres_owned} ACRES.")
    print(f"YOU HARVESTED {harvest_per_acre} BUSHELS PER ACRE.")
    print(f"THE RATS ATE {bushels_eaten_by_rats} BUSHELS.")
    print(f"YOU NOW HAVE {bushels_in_store} BUSHELS IN STORE.\n")

    # Rat patrol allocation
    while True:
        rat_patrol = int(input(f"HOW MANY PEOPLE WILL YOU ASSIGN TO RAT PATROL? (Max: {population}): "))
        if 0 <= rat_patrol <= population:
            break
        else:
            print("You can't assign more people than you have!")

    # Education allocation
    while True:
        education_level = int(input(f"HOW MANY PEOPLE WILL YOU SEND TO EDUCATION? (Max: {population - rat_patrol}): "))
        if 0 <= education_level <= (population - rat_patrol):
            break
        else:
            print("You can't assign more people than you have!")

    # Remaining people are allocated to farming
    farmers = population - rat_patrol - education_level
    print(
        f"POPULATION IS NOW {population}, WITH {farmers} FARMERS, {rat_patrol} PEOPLE ON RAT PATROL, AND {education_level} IN EDUCATION.")

    # Rat patrol effectiveness
    rat_effectiveness = random.uniform(0.2, 0.5) * rat_patrol  # More people reduce rats
    rat_population = max(0, rat_population - rat_effectiveness)
    if rat_population > 100:
        illness_outbreak = True
    else:
        illness_outbreak = False

    # Check for illness outbreak
    if illness_outbreak:
        plague_deaths = int(0.1 * population)  # 10% die in a plague if rats are too numerous
        population -= plague_deaths
        print(f"AN ILLNESS OUTBREAK OCCURRED! {plague_deaths} PEOPLE DIED DUE TO RATS!")

    # Education consequences
    if education_level > 0.6 * population:
        print("YOUR PEOPLE HAVE BECOME TOO EDUCATED AND OVERTHREW YOU!")
        exit()


    # Randomize the amount of bushels eaten by rats (if rats invade)
    random_variable = random.randint(1, 10)  # Properly initialize this before use
    if random_variable % 2 == 0:  # Rats invade if random_variable is even
        bushels_eaten_by_rats = int(bushels_in_store * random.uniform(0.1, 0.2))  # Rats eat 10-20% of bushels
    else:
        bushels_eaten_by_rats = 0  # No rats invade
    print(f"THE RATS ATE {bushels_eaten_by_rats} BUSHELS.")
    bushels_in_store -= bushels_eaten_by_rats

    print(f"YOU NOW HAVE {bushels_in_store} BUSHELS IN STORE.\n")

    if year == 9:  # End the game after 10 years
        break

    # Determine the new land price for this year (random between 17 and 26 bushels per acre)
    harvest_per_acre = random.randint(17, 26)
    print(f"LAND IS TRADING AT {harvest_per_acre} BUSHELS PER ACRE.")

    # Buying land
    while True:
        user_input = int(input("HOW MANY ACRES DO YOU WISH TO BUY? "))
        if user_input < 0:
            exit("Game Over!")
        if harvest_per_acre * user_input <= bushels_in_store:  # Check if enough bushels to buy land
            break
        else:
            print("HAMURABI: THINK AGAIN. YOU DON'T HAVE ENOUGH BUSHELS.")

    acres_owned += user_input
    bushels_in_store -= harvest_per_acre * user_input

    # Selling land
    while True:
        user_input = int(input("HOW MANY ACRES DO YOU WISH TO SELL? "))
        if user_input < 0:
            exit("Game Over!")
        if user_input <= acres_owned:  # Check if user owns enough land to sell
            break
        else:
            print("HAMURABI: THINK AGAIN. YOU CAN'T SELL MORE ACRES THAN YOU OWN.")

    acres_owned -= user_input
    bushels_in_store += harvest_per_acre * user_input

    # Feeding the population
    while True:
        user_input = int(input("HOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE? "))
        if user_input < 0:
            exit("Game Over!")
        if user_input <= bushels_in_store:  # Check if enough bushels in storage to feed people
            break
        else:
            print("HAMURABI: THINK AGAIN. YOU DON'T HAVE ENOUGH BUSHELS.")

    bushels_in_store -= user_input

    # Planting crops
    while True:
        acres_to_plant = int(input("HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED? "))
        if acres_to_plant < 0:
            exit("Game Over!")
        if acres_to_plant <= acres_owned and acres_to_plant <= population * 10:  # Ensure enough acres and people to plant
            if acres_to_plant // 2 <= bushels_in_store:  # Ensure enough bushels for planting
                break
            else:
                print("HAMURABI: THINK AGAIN. YOU DON'T HAVE ENOUGH BUSHELS FOR SEED.")
        else:
            print("HAMURABI: THINK AGAIN. YOU CAN'T PLANT MORE ACRES THAN YOU OWN OR HAVE PEOPLE TO TEND.")

    # Use half a bushel per acre to plant
    bushels_in_store -= acres_to_plant // 2

    # Harvest calculation
    bushels_harvested = acres_to_plant * harvest_per_acre
    bushels_in_store += bushels_harvested

    # New immigrants calculation
    new_immigrants = random.randint(0, 5) if total_number_starved == 0 else 0

    # Starvation calculation
    people_fed = user_input // 20
    starved = population - people_fed
    if starved > 0:
        total_number_starved += starved
        print(f"YOU STARVED {starved} PEOPLE IN ONE YEAR!!!")

    # If more than half the population starves, you are impeached and lose the game
    if starved > population // 2:
        print("DUE TO EXTREME MISMANAGEMENT, YOU HAVE BEEN IMPEACHED AND THROWN OUT OF OFFICE!")
        exit()

    # Update year and population
    population -= starved
    year += 1

# End of the game - final report
percent_of_population_that_starved = (total_number_starved / (population + total_number_starved)) * 100
acres_per_person = acres_owned / population
print(
    f"\nIN YOUR 10-YEAR TERM OF OFFICE, {percent_of_population_that_starved:.2f}% OF THE POPULATION STARVED PER YEAR ON AVERAGE.")
print(f"YOU STARTED WITH 10 ACRES PER PERSON AND ENDED WITH {acres_per_person:.2f} ACRES PER PERSON.")

# Rating the player's performance based on results
if percent_of_population_that_starved > 33 or acres_per_person < 7:
    print("YOUR RULE WAS A DISASTER!")
elif percent_of_population_that_starved > 10 or acres_per_person < 9:
    print("YOUR RULE WAS MEDIOCRE.")
elif percent_of_population_that_starved > 3 or acres_per_person < 10:
    print("YOUR RULE WAS FAIRLY GOOD.")
else:
    print("A FANTASTIC PERFORMANCE!!!")

print("SO LONG FOR NOW.")
