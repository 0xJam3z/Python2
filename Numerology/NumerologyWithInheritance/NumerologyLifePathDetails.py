# Numerology Life Path Details by James Ross

class Numerology:
    def __init__(self, sName: str, sDOB: str): 
        '''
        Define our private variables and do most of our computation
        '''
        self.__sName = sName.strip().upper()
        self.__originalDOB = sDOB
        self.__dob = sDOB.replace('-', '').replace('/', '')
        
        # Directly calculate and reduce numbers in one go.
        self.__iLifePathNumber = self.__reduceNumber(self.__calcLifePath())
        self.__iAttitudeNumber = self.__reduceNumber(self.__calcAttitude())
        self.__iBirthdayNumber = self.__reduceNumber(int(self.__dob[2:4]))
        self.__iPersonalityNumber = self.__reduceNumber(self.__calcCharacterSum('sConsonants'))
        self.__iSoulNumber = self.__reduceNumber(self.__calcCharacterSum('sVowels'))
        self.__iPowerName = self.__reduceNumber(self.__iPersonalityNumber + self.__iSoulNumber)

    
    def __reduceNumber(self, iNumber: int) -> int:
        '''Found this neat little piece of code called Digital Root method. Fastest processing time for this type of calculation!
         Made it look nice and neat! Reference: https://stackoverflow.com/questions/40875066/digital-root-without-loops-python'''
        return 1 + (iNumber - 1) % 9 if iNumber else 0

    
    def __convertCharToInteger(self, sCharacter: str) -> int:
        '''Converts a character to its numerology value using manipulation of ascii (Credit to Prof. Candido)'''
        return (ord(sCharacter.upper()) - 65) % 9 + 1 if sCharacter.isalpha() else 0

    # Fixed from previous version to only loop over self.__sName once.
    def __calcCharacterSum(self, sChar: str) -> int:
        '''Using a single loop, we can get the sum of char values for our vowels/consonants avoiding redundandy'''
        return sum(self.__convertCharToInteger(char) for char in self.__sName 
            if char.isalpha() and ((sChar == 'sVowels' and char in 'AEIOU') or (sChar == 'sConsonants' and char not in 'AEIOU')))

    def __calcLifePath(self) -> int:
        '''Calcs life path by summing all digits in dob'''
        return sum(int(digit) for digit in self.__dob)

    def __calcAttitude(self) -> int:
        '''Calculates attitude by summing the month and day of dob'''
        return sum(int(digit) for digit in self.__dob[:4])

    # Redefined our getters adding @property so we can access their methods by name.
    @property
    def Name(self) -> str:
        return self.__sName
    @property
    def Birthdate(self) -> str:
        return self.__dob
    @property
    def OriginalDOB(self) -> str:
        return self.__originalDOB
    @property
    def LifePath(self) -> int:
        return self.__iLifePathNumber
    @property
    def Attitude(self) -> int:
        return self.__iAttitudeNumber
    @property
    def BirthDay(self) -> int:
        return self.__iBirthdayNumber
    @property
    def Personality(self) -> int:
        return self.__iPersonalityNumber
    @property
    def Soul(self) -> int:
        return self.__iSoulNumber
    @property
    def PowerName(self) -> int:
        return self.__iPowerName
    
    # Prints our Numerology class calculations from Numerology class. 
    def __str__(self) -> str:
        return (
        f'Name: {self.Name}\n'
        f'DOB: {self.OriginalDOB}\n'
        f'Life Path: {self.LifePath}\n'
        f'Attitude: {self.Attitude}\n'
        f'Birthday: {self.BirthDay}\n'
        f'Personality: {self.Personality}\n'
        f'Power Name: {self.PowerName}\n'
        f'Soul: {self.Soul}'
    )

class NumerologyLifePathDetails(Numerology):
    def __init__(self, sName: str, sDOB: str): # Again, __init__ should never return anything, and if it does it'll be a ValueError if it's anything other than None.
        '''
        Initializing our new Inherited child class NumerologyLifePathDetails
        '''
        Numerology.__init__(self, sName, sDOB)
    
    # Decorating our LifePathDescription so we can call it from the object.
    @property
    def LifePathDescription(self) -> str:
        # Key:Value paired dictionary for our return on Life Path.
        dictDescriptions = {
            1: 'The Independent: Wants to work/think for themselves',
            2: 'The Mediator: Avoids conflict and wants love and harmony',
            3: 'The Performer: Likes music, art and to perform or get attention',
            4: 'The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful',
            5: 'The Adventurer: Likes to travel and meet others, often an extrovert',
            6: 'The Inner Child: Is meant to be a parent and/or one that is young at heart',
            7: 'The Naturalist: Enjoys nature and water and alternative life paths, open to spirituality',
            8: 'The Executive: Gravitates to money and power',
            9: 'The Humanitarian: Helps others and/or experiences pain and learns the hard way'
            }
        return dictDescriptions.get(self.LifePath) # Returns the correct description based on our LifePath number
    
    # Finally, print our life path description when called by NumerologyInherit.py!
    def __str__(self) -> str:
        '''Prints our life path once called from NumerologyInherit'''
        return (f'Life Path Details: {self.LifePathDescription}')