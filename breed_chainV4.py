import pandas as pd
import time
import random
import math

attempt_counter = {}

def calculate_offspring(pal_1, pal_2, excluded_pals):
    global attempt_counter

    # Normalize pal names to lower case
    pal_1 = pal_1.lower()
    pal_2 = pal_2.lower()

    # Create a unique key for the pair
    pair_key = tuple(sorted([pal_1, pal_2]))

    # Increment the attempt count for this pair
    attempt_counter[pair_key] = attempt_counter.get(pair_key, 0) + 1

    # Check if the same pair has been attempted 3 times
    if attempt_counter[pair_key] >= 3:
        print(f"\nAttempt limit reached for {pal_1.title()} and {pal_2.title()}. Process halted... This target pal is likely not possible!")
        return -1, -1
    
    # List of Pals that can only be born from two parents of the same type
    special_breed_pals = ['frostallion', 'jetragon', 'paladius', 'necromus', 'jormuntide ignis']

    # List of special combination pals
    special_combinations = 'Relaxaurus Lux, Incineram Noct, Mau Cryst, Vanwyrm Cryst, Eikthyrdeer Terra, Elphidran Aqua, Pyrin Noct, Mammorest Cryst, Mossanda Lux, Dinossom Lux, Jolthog Cryst, Frostallion Noct, Kingpaca Cryst, Lyleen Noct, Leezpunk Ignis, Blazehowl Noct, Robinquill Terra, Broncherry Aqua, Surfent Terra, Gobfin Ignus, Suzaku Aqua, Reptyro Cryst, Hangyu Cryst, Lyleen, Faleris, Grizzbolt, Orserk, Shadowbeak'
    special_combinations_list = [pal.lower() for pal in special_combinations.split(', ')]

    # Create a local copy of excluded_pals and extend it
    local_excluded_pals = excluded_pals.copy()
    local_excluded_pals.extend(special_combinations_list)

    # Calculate the raw power using the formula
    offspring_power_raw = math.floor((breed_power_dict[pal_1.lower()] + breed_power_dict[pal_2.lower()] + 1) / 2)

    # Iterate through the breeds to find the closest match
    closest_name = None
    closest_diff = float('inf')
    for name, power in breed_power_dict.items():
        if name in local_excluded_pals:
            continue

        # Check if the breed is one of the special breeds
        if name in special_breed_pals:
            if pal_1.lower() != name or pal_2.lower() != name:
                continue  # Skip to the next breed if parents don't match for special breeds

        diff = abs(offspring_power_raw - power)
        if diff < closest_diff or (diff == closest_diff and power < breed_power_dict.get(closest_name, float('inf'))):
            closest_name = name
            closest_diff = diff

    return closest_name, breed_power_dict.get(closest_name, None)




def find_key_of_closest_value(target_value, dictionary, excluded_pals):
    closest_key = None
    smallest_difference = float('inf')
    
    for key, value in dictionary.items():
        if key in excluded_pals:
            continue
        current_difference = abs(target_value - value)
        if current_difference < smallest_difference:
            smallest_difference = current_difference
            closest_key = key
        # If there's a tie, choose the smaller value (hence the closer key)
        elif current_difference == smallest_difference and value < dictionary[closest_key]:
            closest_key = key

    return closest_key

def find_adjacent_key(d, current_key, direction):
    """
    Finds the next key in the dictionary with a lower or higher value than the current key.

    :param d: Dictionary to search.
    :param current_key: The current key to find the adjacent key for.
    :param direction: 'lower' for the next lower key, 'higher' for the next higher key.
    :return: The adjacent key or None if not found.
    """
    # Ensure the current key is in the dictionary
    if current_key not in d:
        return None

    # Sort the dictionary by values
    sorted_items = sorted(d.items(), key=lambda x: x[1])

    # Find the index of the current key in the sorted list
    current_index = next((i for i, kv in enumerate(sorted_items) if kv[0] == current_key), None)

    if current_index is None:
        return None

    # Find the adjacent key based on the specified direction
    if direction == 'lower' and current_index > 0:
        return sorted_items[current_index - 1][0]
    elif direction == 'higher' and current_index < len(sorted_items) - 1:
        return sorted_items[current_index + 1][0]
    else:
        return None
    
def select_random_key_within_range(d, target_value, range_threshold, excluded_pals):
    """
    Selects a random key from the dictionary where the value is within a specified range of the target value.

    :param d: The dictionary to search.
    :param target_value: The target value to compare against.
    :param range_threshold: The range within which the value should be (default 200).
    :return: A random key within the range or None if no key is found.
    """
    # Filter keys based on the value range condition
    filtered_keys = [key for key, value in d.items() if abs(value - target_value) <= range_threshold]

    # Randomly select a key if the list is not empty
    if filtered_keys:
        result = random.choice(filtered_keys)
    else:
        result = None
    
    # If a valid key is returned, get the corresponding value from the dictionary
    if result is not None:
        corresponding_value = breed_power_dict[result]
        print(f"Random Breed Result: {result}, Corresponding Value: {corresponding_value}")
    else:
        print("No key found within the specified range.")

    return result

def find_extreme_pals(breed_power_dict, excluded_pals):
    # Filter out the excluded pals
    filtered_dict = {pal: power for pal, power in breed_power_dict.items() if pal not in excluded_pals}

    # Find the highest and lowest breed power pals
    highest_pal = max(filtered_dict, key=filtered_dict.get, default=None)
    lowest_pal = min(filtered_dict, key=filtered_dict.get, default=None)

    return highest_pal, lowest_pal

breed_power_dict = {'Chikipi': 1500,
'Teafant': 1490,
'Mau': 1480,
'Lamball': 1470,
'Cattiva': 1460,
'Cremis': 1455,
'Vixy': 1450,
'Mau Cryst': 1440,
'Lifmunk': 1430,
'Hangyu Cryst': 1422,
'Hangyu': 1420,
'Sparkit': 1410,
'Flambelle': 1405,
'Foxparks': 1400,
'Hoocrates': 1390,
'Depresso': 1380,
'Jolthog': 1370,
'Jolthog Cryst': 1360,
'Pengullet': 1350,
'Tocotoco': 1340,
'Fuack': 1330,
'Bristla': 1320,
'Ribunny': 1310,
'Swee': 1300,
'Killamari': 1290,
'Flopie': 1280,
'Kelpsea Ignis': 1270,
'Kelpsea': 1260,
'Tanzee': 1250,
'Gumoss': 1240,
'Gumoss (Special)': 1240,
'Daedream': 1230,
'Fuddler': 1220,
'Dazzi': 1210,
'Woolipop': 1190,
'Nox': 1180,
'Wixen': 1160,
'Rooby': 1155,
'Maraith': 1150,
'Leezpunk Ignis': 1140,
'Rushoar': 1130,
'Leezpunk': 1120,
'Lunaris': 1110,
'Gobfin Ignis': 1100,
'Gobfin': 1090,
'Cawgnito': 1080,
'Beegarde': 1070,
'Direhowl': 1060,
'Vaelet': 1050,
'Gorirat': 1040,
'Galeclaw': 1030,
'Robinquill': 1020,
'Felbat': 1010,
'Robinquill Terra': 1000,
'Verdash': 990,
'Fenglope': 980,
'Loupmoon': 950,
'Lovander': 940,
'Caprity': 930,
'Eikthyrdeer': 920,
'Mozzarina': 910,
'Eikthyrdeer Terra': 900,
'Dumud': 895,
'Melpaca': 890,
'Reindrix': 880,
'Celaray': 870,
'Broncherry': 860,
'Digtoise': 850,
'Broncherry Aqua': 840,
'Kitsun': 830,
'Dinossom': 820,
'Dinossom Lux': 810,
'Chillet': 800,
'Arsox': 790,
'Petallia': 780,
'Foxcicle': 760,
'Tombat': 750,
'Rayhound': 740,
'Blazehowl': 710,
'Katress': 700,
'Univolt': 680,
'Blazehowl Noct': 670,
'Vanwyrm': 660,
'Bushi': 640,
'Vanwyrm Cryst': 620,
'Incineram': 590,
'Incineram Noct': 580,
'Anubis': 570,
'Surfent': 560,
'Surfent Terra': 550,
'Elphidran': 540,
'Elphidran Aqua': 530,
'Penking': 520,
'Grintale': 510,
'Azurobe': 500,
'Cinnamoth': 490,
'Wumpo Botan': 480,
'Kingpaca': 470,
'Wumpo': 460,
'Sibelyx': 450,
'Ice Kingpaca': 440,
'Mossanda': 430,
'Nitewing': 420,
'Sweepa': 410,
'Mossanda Lux': 390,
'Ragnahawk': 380,
'Faleris': 370,
'Pyrin': 360,
'Quivern': 350,
'Warsect': 340,
'Elizabee': 330,
'Reptyro': 320,
'Jormuntide Ignis': 315,
'Jormuntide': 310,
'Mammorest': 300,
'Mammorest Cryst': 290,
'Relaxaurus': 280,
'Relaxaurus Lux': 270,
'Menasting': 260,
'Lyleen': 250,
'Pyrin Noct': 240,
'Ice Reptyro': 230,
'Beakon': 220,
'Lyleen Noct': 210,
'Grizzbolt': 200,
'Helzephyr': 190,
'Astegon': 150,
'Orserk': 140,
'Cryolinx': 130,
'Frostallion': 120,
'Frostallion Noct': 100,
'Jetragon': 90,
'Paladius': 80,
'Necromus': 70,
'Shadowbeak': 60,
'Suzaku': 50,
'Suzaku Aqua': 30,
'Blazamut': 10}

breed_power_dict = {key.lower(): value for key, value in breed_power_dict.items()}


def calculate_breed_chain(target_pal, inherited_pals, excluded_pals):  
    step = 1
    special_breed_pals = ['frostallion', 'jetragon', 'paladius', 'necromus', 'jormuntide ignis']

    target_pal = target_pal.lower()
    inherited_pals = [pal.lower() for pal in inherited_pals]
    excluded_pals = [pal.lower() for pal in excluded_pals]

    special_combinations = 'Relaxaurus Lux, Incineram Noct, Mau Cryst, Vanwyrm Cryst, Eikthyrdeer Terra, Elphidran Aqua, Pyrin Noct, Mammorest Cryst, Mossanda Lux, Dinossom Lux, Jolthog Cryst, Frostallion Noct, Kingpaca Cryst, Lyleen Noct, Leezpunk Ignis, Blazehowl Noct, Robinquill Terra, Broncherry Aqua, Surfent Terra, Gobfin Ignus, Suzaku Aqua, Reptyro Cryst, Hangyu Cryst, Lyleen, Faleris, Grizzbolt, Orserk, Shadowbeak'
    # Split the string into a list and extend the excluded_pals list
    special_combinations_list = [pal.lower() for pal in special_combinations.split(', ')]
    excluded_pals.extend(special_combinations_list)
    try:
        if target_pal.lower() in special_combinations_list:
            print(f'{target_pal.title()} is a special pal and only has one specific breeding combination. Try something different.')
            return None
        
        if target_pal.lower() in special_breed_pals:
                if len(inherited_pals) > 1:
                    print(f'{target_pal.title()} can only be bred with itself. Oops.')
                    return None
                elif target_pal != inherited_pals[0]:
                    print(f'{target_pal.title()} can only be bred with itself. Oops.')
                    return None

                if target_pal == inherited_pals[0]:
                    print(f'Step {step}: Breed: {target_pal.title()} + {inherited_pals[0].title()} = {target_pal.title()}; Offspring Power: {breed_power_dict[target_pal]}')
                    return None



        time1 = time.time()
        # Ensure that the target pal and all inherited pals are in the breed_power_dict

        if target_pal not in breed_power_dict:
            print(f"Error: Target pal '{target_pal.title()}' not found. Type better :)")
            return f"Error: Target pal '{target_pal.title()}' not found."
        
        if len(inherited_pals) > 1:
            for pal in inherited_pals:
                if pal not in breed_power_dict:
                    print(f"Error: Inherited pal '{pal.title()}' not found. Type better :)")
                    print(f'\nBut also... If selecting multiple inherited pals, don\'t place a space after each comma. For two species, for example, youd write: Jetragon,Bristla')
                    return f"Error: Inherited pal '{pal.title()}' not found."
        else: 
            if inherited_pals[0] not in breed_power_dict:
                print(f"Error: Inherited pal '{pal.title()}' not found. Type better :)")
                print(f'\nBut also... If selecting multiple inherited pals, don\'t place a space after each comma. For two species, for example, youd write: Jetragon,Bristla')
                return f"Error: Inherited pal '{pal.title()}' not found."
            
        #Force the inherited traits by first breeding all the species desired in the inherited list

        current_pal = inherited_pals[0]
        print('--------------------------------')
        print('Breeding Desired Traits...\n')
        if len(inherited_pals) >= 1:      
            for inherited_pal in inherited_pals[1:]:
                old_pal = current_pal
                current_pal, current_power = calculate_offspring(current_pal, inherited_pal, excluded_pals)
                if current_pal == -1:
                    return None
                print(f'Bred {old_pal.title()} with {inherited_pal.title()} to get {current_pal.title()} with power {current_power}')
            else: 
                current_power = breed_power_dict[current_pal]


        print('\nDesired Trait Breeding Complete.')
        print('--------------------------------')


        target_power = breed_power_dict[target_pal]

        name = None

        offspring_power = current_power
        offspring_name = current_pal

        input_breed1 = None
        input_breed_2 = None

        while offspring_name != target_pal:

            power_req = 2*target_power - offspring_power 
            
            highest_avail_pal, lowest_avail_pal = find_extreme_pals(breed_power_dict, excluded_pals)

            if power_req >= 1500:
                old_offspring = offspring_name
                #Breed with highest available pal
                offspring_name, offspring_power = calculate_offspring(offspring_name, highest_avail_pal, excluded_pals)
                if offspring_name == -1:
                    return None

                print(f'Step {step}: Breed: {old_offspring.title()} + {highest_avail_pal.title()} = {offspring_name.title()}; Offspring Power: {offspring_power}')

            elif power_req <= 10:
                #Breed with lowest available pal
                old_offspring = offspring_name
                offspring_name, offspring_power = calculate_offspring(offspring_name, lowest_avail_pal, excluded_pals)
                if offspring_name == -1:
                    return None
                print(f'Step {step}: Breed: {old_offspring.title()} + {lowest_avail_pal.title()} = {offspring_name.title()}; Offspring Power: {offspring_power}')
            else: 
                #Breed with closest pal to power required (rounded up)
                next_breed = find_key_of_closest_value(power_req, breed_power_dict, excluded_pals)
                old_offspring = offspring_name
                
                offspring_name, offspring_power = calculate_offspring(offspring_name, next_breed, excluded_pals)
                if offspring_name == -1:
                    return None
                
                if offspring_name != target_pal:
                    print(f"\nTwo Step Lookahead Detected Infinite Loop on Breed with: {offspring_name.title()} & {next_breed.title()}. Randomizing Breeding Target...\n")
                    #Shuffle the breeding by mixing the offspring with a random pal within 200 points:
                    next_breed = select_random_key_within_range(breed_power_dict, breed_power_dict[offspring_name], 100, excluded_pals)

                    offspring_name, offspring_power = calculate_offspring(old_offspring, next_breed, excluded_pals)
                    if offspring_name == -1:
                        return None

            
                print(f'Step {step}: Breed: {old_offspring.title()} + {next_breed.title()} = {offspring_name.title()}; Offspring Power: {offspring_power}')
            step += 1

        time2 = time.time()

        total_time = time2- time1

        print('--------------------------------')
        print(f'\nTime To Solve: {total_time:.6f} seconds')

    except Exception as e:
        print(f"An unknown error occurred: {str(e)}")
        return f"An unknown error occurred: {str(e)}"


if __name__ == "__main__":
    target_pal = 'Shadowbeak'
    inherited_pals = ['Chikipi']
    excluded_pals = []

    calculate_breed_chain(target_pal, inherited_pals, excluded_pals)