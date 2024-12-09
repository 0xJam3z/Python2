# UseNumerology.py by James Ross
from NumerologyLifePathDetails import NumerologyLifePathDetails
from NumerologyLifePathDetails import Numerology

def main():
    # Ensure our sName meets requirements of assignment. Added a couple additional input checks I learned along the way!
    while True:
        sName = input('Enter your first and last name: ')
        if len(sName.split()) != 2: # Grabbing the length of our name split to a list to ensure a first and last name are entered!
            print('Only enter your first and last name.')
            continue        
        if sName.replace(' ', '').isalpha(): # Ensure our input is alphabetic by using replace() method to rid us of any spaces in sName so we can use .isalpha() method!
            break
        else:
            print('Name can only contain letters in the alphabet!')

    # Ensure our sDOB meets requirements of assignments with a little additional sanitation I've learned along the way.
    while True:
        sDOB = input('Enter your date of birth (MM-DD-YYYY or MM/DD/YYYY): ')
        sSeperator = sDOB[2] # Storing to ensure seperators are at index position 2 & 5, also ensuring seperators match (- OR / but not both!)
        sStrippedDOB = (sDOB.replace('-', '').replace('/', '')) # Stripping our -/ to check if there is anything outside of digits in the next line
        if not sStrippedDOB.isdigit() or len(sStrippedDOB) !=8: # calling .isdigit() method to ensure our string only includes digits & that there are only 8 digits.
            print(f'Only enter digits using MM-DD-YYYY or MM/DD/YYYY')
            continue 
        if sSeperator not in ['-', '/'] or sDOB[5] != sSeperator:
            print(f'Only use / or - and they must be placed in order of MM-DD-YYYY or MM/DD/YYYY')
            continue
        break

    numerObject = Numerology(sName, sDOB) # Instantiate numerology for our __str__ in Numerology.
    numerInherit = NumerologyLifePathDetails(sName, sDOB) # Instantiate numerologyLifePathDetails for our __str__ in NumerologyLifePathDetails
    print(numerObject, numerInherit, sep='\n') # Finally found a use for sep!

main()