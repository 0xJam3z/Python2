# Numerology.py Class File created by James Ross
# To be edited for next submission -- transfer equations to __init__ to reduce redundancy. Add properties.

class Numerology:
    def __init__(self, sName:str, sDOB:str): # Not using -> object because there is no case when __init__ is not an object.
        '''Initializing our numerology class beginning by defining
            sName accounting for white spaces & force upper for dictionary comparison.
            Declaring our DOB using .replace to account for -/. Initializing our point system alphabet dictionary. Privitizing our sName, dob, and dictAlphabet!'''
        self.__sName = sName.strip().upper() 
        self.__originalDOB = sDOB
        self.__dob = sDOB.replace('-', '').replace('/', '')
        # Creating our dictionary here for their key:pair values to be used for arthimatic later. Used tuples so I could
        # group them together as seen in assignment. Cleaner this way, in my opinion.
        self.__dictAlphabet = { ('A', 'J', 'S'):1,
                                ('B', 'K', 'T'):2,
                                ('C', 'L', 'U'):3,
                                ('D', 'M', 'V'):4,
                                ('E', 'N', 'W'):5,
                                ('F', 'O', 'X'):6,
                                ('G', 'P', 'Y'):7,
                                ('H', 'Q', 'Z'):8,
                                ('I', 'R')     :9}
    # Creating a decorator to handle our numeric operations (if a number is greater than 9, deduce it to a single digit and sum). 
    # Ensuring this data is private as to not be manipulated.
    # I COULD haved used recursion here, and understand it's the best option & how to impliment, but I will save that for inheritance addition! Also big shoutout to Mikey for explaining it to me.
    def _deduceNumDeco(func):
        def wrapper(self):
            iNum = func(self)
            while iNum > 9:
                iNum = sum(int(iNum) for iNum in str(iNum))
            return iNum
        return wrapper
    
    # Assigning our private attributes to be returned when the function is invoked.
    def getName(self) -> str:
        return self.__sName # Uppercase value and stripped for input sanitation.
    
    # Get birthdate excluding /- for calculations
    def getBirthdate(self) -> str:
        return self.__dob
    
    # Get original DOB for call with /-
    def getOriginalDOB(self) -> str:
        return self.__originalDOB
    
    # Summing digits of month and day using our decorator and their relevant index positions, grabbing from a for loop.
    @_deduceNumDeco
    def getAttitude(self) -> int:
        sAttitude = self.getBirthdate()[:4] #Grabbing index position 0-3 (Month & Day) to calculate attitude
        iSum = 0
        for sNumber in sAttitude:
            iSum += int(sNumber)
        return iSum
    
    # Summing the numbers of the day of birth using index positions and passing them to our decorator!
    @_deduceNumDeco
    def getBirthDay(self) -> int:
        return int(self.getBirthdate()[2:4]) # Grabbing day out of getBirthdate()
    
    # Decorating our lifePath by taking all digits and summing them together.
    @_deduceNumDeco
    def getLifePath(self) -> int:
        iSum = 0
        for sNumber in self.getBirthdate(): 
            iSum += int(sNumber)
        return iSum
    
    # Decorating our getPersonality which is using our dictionary to iterate through our tuples for consonants and returning their value to be summed.
    @_deduceNumDeco
    def getPersonality(self) -> int:
        iSum = 0
        for sChar in self.getName():
            if sChar not in 'AEIOU': # Avoiding our vowels
                for key, value in self.__dictAlphabet.items():
                    if sChar in key:
                        iSum += value
                        break
        return iSum

    # Decorating our getSoul which looks for any vowels in our dictionary and grabbing their value to be added.
    @_deduceNumDeco
    def getSoul(self) -> int:
        iSum = 0
        for sChar in self.getName():
            if sChar in 'AEIOU':
                for key, value in self.__dictAlphabet.items():
                    if sChar in key:
                        iSum += value
                        break
        return iSum
    # Using decoration for this function to be passed into. Here we are calculating the sum of our getSoul along with getPersonality.
    @_deduceNumDeco
    def getPowerName(self) -> int:
        return self.getSoul() + self.getPersonality()


    # Big thanks to Mikey for showing this to us during S.I. session. 
    # __str__ used in a class will, when we call a print on the object, have this nice and neat code print out for us!
    def __str__(self) -> str:
        # Returns all of our calculations to match assignment requirements!
        return f'Name: {self.getName()}\
        \nDOB: {self.getOriginalDOB()}\
        \nLife Path: {self.getLifePath()}\
        \nAttitude: {self.getAttitude()}\
        \nBirthday: {self.getBirthDay()}\
        \nPersonality: {self.getPersonality()}\
        \nPower Name: {self.getPowerName()}\
        \nSoul: {self.getSoul()}'
