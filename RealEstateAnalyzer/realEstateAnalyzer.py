# Real Estate Analyzer by James Ross

import csv

def getDataInput() -> list: # Initially had list[list[str]]: but was told just list would suffice (was being very technical here-- but for the sake of understanding this in-depth was nice to know this method was also correct.)
    """Learning documentation when hovering over a function! Read in our CSV file, skipping the header, and appending row(s) of information into a list"""
    listRecords = []
    with open('RealEstateData.csv', 'r') as file:
        csvReader = csv.reader(file) 
        next(csvReader)
        for row in csvReader:
            listRecords.append(row) # No need to split "," as csv.reader() automatically does this for us!
    return listRecords

def getMedian(listPrice: list[float]) -> float:
    """Our calculations for grabbing median price to see if odd/even & returning the median."""
    iCount = len(listPrice)
    if iCount % 2 == 1:
        return float(listPrice[iCount // 2])
    else:
        iMiddle = iCount // 2
        return (float(listPrice[iMiddle - 1]) + float(listPrice[iMiddle])) / 2
        

def main(): # Since this is just processing & output, we can assume it's a null return (thanks Mikey.) Originally did a -> None: but was told this is automatically inferred!
    """All of our custom records specific for City, Zip, Type, Price, and records themselves are made here. Performs our assignments and calculations and prints the output in the format matching assignment requirements."""
    listRecords = getDataInput()
    listPrices = []
    dictType = {}
    dictZips = {}
    dictCity = {}

    
    # Start initializing variables for our records to be used in processing our output! 
    for record in listRecords:
        sCity = record[1]
        sZip = record[2]
        sType = record[7]
        fPrice = float(record[8]) # Ensuring our data comes back as a floating point num!
        
        listPrices.append(fPrice)

        # Using if x not in dict to account for duplicates. Decided against the .get() method for the sake of not copypasting from S.I. sessions. 
        
        if sCity not in dictCity:
            dictCity[sCity] = 0
        dictCity[sCity] += fPrice

        if sZip not in dictZips:
            dictZips[sZip] = 0
        dictZips[sZip] += fPrice

        if sType not in dictType:
            dictType[sType] = 0
        dictType[sType] += fPrice


    
    # Sort our prices list to be used before calculations!
    listPrices.sort()
    
    # Calculations for min, max, total, average, and lastly, median.
    minPrice = min(listPrices)
    maxPrice = max(listPrices)
    totalPrice = sum(listPrices)
    averagePrice = totalPrice / len(listPrices)
    medianPrice = getMedian(listPrices)
    
    # Print above calculations spacing to match expected output from assignment.
    print(f'{'Minimum':15s}{minPrice:21,.2f}')
    print(f'{'Maximum':15s}{maxPrice:21,.2f}')
    print(f'{'Sum':15s}{totalPrice:21,.2f}')
    print(f'{'Average':15s}{averagePrice:21,.2f}')
    print(f'{'Median':15s}{medianPrice:21,.2f}')
    
    # City and Property Type totals printed with format expected per assignment.
    print('\nTotal Sales by Property Type:')
    for propertyType, total in dictType.items():
        print(f'{propertyType:15s} {total:20,.2f}')

    print('\nTotal Sales by City:')
    for city, total in dictCity.items():
        print(f'{city:15s} {total:20,.2f}')

main()
