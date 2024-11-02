# Inter Planetery Weights by James Ross
import pickle

def main():
    # Create dictionary with planets as key & their constant weight as value
    dictGravityFactors = {
        'Mercury': 0.38,
        'Venus': 0.91,
        'Moon': 0.165,
        'Mars': 0.38,
        'Jupiter': 2.34,
        'Saturn': 0.93,
        'Uranus': 0.92,
        'Neptune': 1.12,
        'Pluto': 0.066
    }

    # Attempt to open previous version of db and assign to new dictionary, if none exists, create an empty dictionary (try/except)
    try:
        with open('jrPlanetaryWeights.db', 'rb') as file: # Reading in binary stream, assign object as file (read/load data)
            dictPlanetHistory = pickle.load(file) # Load serialiazed data into our dictionary
    except FileNotFoundError:
        dictPlanetHistory = {} # File doesn't exist, so let's initialize a new empty dictionary.

    # Prompt user to see if they want to see previous DB history.
    sHistory = input("Do you wish to see previous Planetary Weight history? (Y/N) ").lower() # Use .lower() to account for case sensitivy in next line.
    if sHistory == 'y':
        for sName, fWeights in dictPlanetHistory.items(): # Extrapolate key:value pair dictionary values
            print(f"{sName}, here are your weights on our Solar System's Planets:") # Begin printing our dictPlanetHistory items starting with sName on this line.
            # Using fWeight.items(), pull both planet name & factored weights for sName formatting to meet assignment requirement. Print to screen.
            print("\n".join(f"Weight on {sPlanet:10}: {fWeights: 10.2f}" for sPlanet, fWeights in fWeights.items())) # Use newline & then join function so formatting meets assignment requirement.
            print() # For the sake of readability, blank line.

    # We'll run a while True loop here to begin performing proper checks.
    while True:
        sName = input("Enter a unique name (or press Enter to exit): ").strip()  # Get name from user. Using .strip() to account for white spaces at beginning/end of chars.
        if sName == "": # Nothing entered? Exit the program.
            break
        # Check if the entered name already exists in the history via .keys() , accounting for case sensitivity.
        if any(sDictNames.lower() == sName.lower() for sDictNames in dictPlanetHistory.keys()):
            print("Name already exists. Please enter a different unique name.")
            continue  # Return to the start of the loop to obtain a unique name.
        # Check to ensure valid weight is entered using a boolean check method.
        boolValidWeight = False
        while not boolValidWeight:
            try:
                fEarthWeight = float(input("Enter your weight on Earth: ")) # Float conversion to ensure any valid int/float value is inputted to account for decimal input. 
                boolValidWeight = True # Set this boolean flag to true so we can continue to our next segment of code.
            except ValueError: # Our exception handler if criteria above isn't met, leading us back to our while not loop!
                print("Invalid input. Please enter a numeric value.")

        # Initialize a new dictionary to store our calculations of person's weight using our previous dictGravityFactors dictionary as our base for calculations!
        dictPersonWeights = {}
        for sPlanet, fWeightFactor in dictGravityFactors.items(): # Grab key:value pairs to begin our calculations.
            # Iterate through each planet fetched from dictGravityFactors.items() to get our gravity (weightFactor) to multiply by our fEarthyWeight. 
            dictPersonWeights[sPlanet] = fEarthWeight * fWeightFactor # Store these results into dictPersonWeights in format of key: planet(name), value: weightFactor * fEarthWeight result.
        
        # Update dictPlanetHistory with persons weight. This will create a nested dictionary starting with: sName as key, and value being dictionary with PlanetName: Converted weight between fEarthWeight * weightFactor.
        dictPlanetHistory[sName] = dictPersonWeights

        # Print out our formatted weights for inputted sName.
        print(f"{sName}'s Solar System's Weights: ")
        for sPlanet, fWeightFactor in dictPersonWeights.items(): # Grab both key:pair values from dictPersonWeights.items()
            print(f"{sPlanet:10}: {fWeightFactor:10.2f}") # Utilize these values with key (planet) to be right-aligned by 10-character spaces, and weightFactor taking up 10 white spaces with two decimal points.
        
        # Finally we will write out our binary stream (from existing to new) to file (if there was previous data, it was already applied to our dictionary so no lost data when we use .dump()).
        with open('jrPlanetaryWeights.db', 'wb') as file: 
            pickle.dump(dictPlanetHistory, file) # Dumps our new/updated dictionary to our jrPlanetaryWeights.db

main()