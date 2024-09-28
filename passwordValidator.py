# Password Validator by James Ross

def main():
    
    # Grab users first & last name
    sName = input("Enter your first and last name: ")
    # Extract users first letter of First & last name using sName[0] to grab the index the first index of first name.
    # Utilizing .find we can leverage the space between first and last name and concatenate the first index to obtain our last name letter.
    sUserInitials = sName[0] + sName[sName.find(" ") + 1]

# Begin our while True statement procedurally going through each step outlined in assignment.
    while True:
        sPassword = input("Input a password: ")
        # Collect a log of all potential error messages used later in code to be appended to this list.
        listOfErrors = []
    
    # Begin password validation steps
        if len(sPassword) < 8 or len(sPassword) > 12:
            listOfErrors.append("Password must be between 8 and 12 characters")
        if sPassword.lower().startswith('pass'):
            listOfErrors.append("Password cannot start with pass.")
            
        # For char upper, lower, digit, special let's define variable booleans
        # and use a for x in sPassword to ensure conditionals according to assignment are met.
        bCharIsUpper = False
        bCharIsLower = False
        bCharHasDigit = False
        bCharHasSpecial = False
        sSpecialChar = ('!@#$&^')
        # Initializing a dictionary for use in incrimenting our char+count for sPassword.
        dCharCount = {}
        # Using if conditionals to set bools to true if conditons are met 
        for char in sPassword:
            if char.isupper():
                bCharIsUpper = True
            if char.islower():
                bCharIsLower = True
            if char.isdigit():
                bCharHasDigit = True
            if char in sSpecialChar:
                bCharHasSpecial = True
            # Instead of using char.lower() in dCharCount, learned for efficiencies sake it's wiser to define a variable assigned to char.lower() so the  
            # method isn't being ran twice. So we will define a variable, assign it to char.lower(), and begin our dictionary char count process!
            sCharCountLower = char.lower()
            dCharCount[sCharCountLower] = dCharCount.get(sCharCountLower, 0) + 1 # This expression allows us to use our dict .get() method to call on our dict, check if a value associated with the key 
            # sCharCountLower exists, if not return 0 (although this could be assumed without the 0). The 1 at the end adds it's value to the dictionary, which will thereby incriment for each occurrence.
            
        # If none of above conditions are met, begin the process of printing the correct error message
        if not bCharIsUpper:
            listOfErrors.append("Password must contain at least 1 uppercase letter.")
        if not bCharIsLower:
            listOfErrors.append("Password must have at least 1 lowercase letter.")  
        if not bCharHasDigit:
            listOfErrors.append("Password must contain at least 1 digit.")
        if not bCharHasSpecial:
            listOfErrors.append("Password must contain at least 1 of thse special characters: ! @ # $ % ^")
        # Check for user initials 
        if sUserInitials.upper() in sPassword.upper():
            listOfErrors.append("Password must not contain user initials.")
        
        # Running another boolean check for duplicates using a list and for loop to append duplicates from our dictionary to our empty list.
        bDuplicates = False
        listOfDuplicates = []
        for char, charCount in dCharCount.items(): # Iterating through each key:pair value in dictionary
            if charCount > 1: 
                listOfDuplicates.append(f"{char}: {charCount} times") # If count is >1 we append to our empty list the char and charcount.
                bDuplicates = True 
        # If duplicates are found, we'll print our error message.
        if bDuplicates:
            listOfErrors.append("These characters appear more than once: \n" + "\n".join(listOfDuplicates)) # Newline & Prints our list!
        # Now that we've collected all our potential error messages, if any exist print them & continue back to the loop!    
        if listOfErrors:
            print("\n".join(listOfErrors))
            continue
        
        # Given that all above conditions are satisfied, we now have a valid password!
        print("Password is valid and OK to use.")
        break
    
main()