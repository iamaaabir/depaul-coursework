# Problem 1:

def calculate_boost_distance(speed, time): 
    return speed*time 
    
# boost_distance = calculate_boost_distance(40, 2.5) 
# print (boost_distance)

# Problem 2:

def generate_silly_name():
    name = input('Enter your name: ')
    repeat = input('Enter a non-negative whole number: ')
    repeat = int(repeat)
    return name*repeat
    
# silly_name = generate_silly_name() 
# print (silly_name)

# Problem 3:

def generate_first_track():
    for nums in range(6, 22, 3):
        print (nums, end = ' ')
    print()
    for nums in range(4, 5):
        print (nums, end = ' ')
    print()
    for nums in range(7, 22, 7):
        print (nums, end = ' ')
    print()
    for nums in range(49, 12, -9):
        print (nums, end = ' ')
    print()
        
# generate_first_track()

# Problem 4:

def remove_from_pool(powerups):
    removePower = input('Enter an item to remove: ')

    for power in powerups:
        if removePower.lower() != power.lower():
            print (power)
            
# powerups = ["Blue Shell", "lightning", "GREEN SHELL"]
# remove_from_pool(powerups)

# Problem 5:

def select_powerup(index, powerups):
    if index >= -len(powerups) and index < len(powerups):
        print(powerups[index])
        
# powerups = ["Blue Shell", "lightning", "GREEN SHELL"]
# select_powerup(-4, powerups)

# END
    

        


    
    

    
