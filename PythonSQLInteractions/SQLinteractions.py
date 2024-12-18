# SQL Database Interaction with Python by James Ross
import sqlite3


def createDB():
    '''Create our database tables. If database file already exists,
      delete previous data and replace with new data.'''
    dbConnection = sqlite3.connect('retirement.db')
    dbCursor = dbConnection.cursor()

    # Creating our Employee table. Ensuring proper data types.
    dbCursor.execute('''
        CREATE TABLE IF NOT EXISTS Employee (
            EmployeeID INTEGER PRIMARY KEY,
            Name TEXT
        );
    ''')
    # Creating our Pay table with proper data types, key, and references!
    dbCursor.execute('''
        CREATE TABLE IF NOT EXISTS Pay (
            EmployeeID INTEGER,
            Year INTEGER,
            Earnings REAL,
            FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
        );
    ''')
    # Creating our SS min using proper data type.
    dbCursor.execute('''
        CREATE TABLE IF NOT EXISTS SocialSecurityMin (
            Year INTEGER PRIMARY KEY,
            Minimum REAL
        );
    ''')
    # Commit the data and end this transaction.
    dbConnection.commit()
    dbConnection.close()

def importData():
    '''All of our txt records will be imported here, placing them in their preestablished tables.'''
    dbConnection = sqlite3.connect('retirement.db')
    dbCursor = dbConnection.cursor()

    # Delete existing data if exists, assignment was vague on how we should proceed with this. Could have done if exists/read contents 
    # (probably better suited for future usability,) but for the sake of ease just showed an additional usecase of SQL with DELETE addition.
    dbCursor.execute('DELETE FROM Employee;')
    dbCursor.execute('DELETE FROM Pay;')
    dbCursor.execute('DELETE FROM SocialSecurityMin;')

    # Importing Employee data from our Employee.txt file. Skip header and read line by line (stripping and splitting the comma seperator) -> insert into their expected fields.
    with open('Employee.txt', 'r') as file:
        next(file)
        for line in file:
            employee_id, name = line.strip().split(',')
            dbCursor.execute(
                'INSERT INTO Employee (EmployeeID, Name) VALUES (?, ?);',
                (int(employee_id), name)
            )

    # Importing Pay data from our Pay.txt file. Skip header and read line by line (stripping and splitting the comma seperator) -> insert into their expected fields.
    with open('Pay.txt', 'r') as file:
        next(file)
        for line in file:
            employee_id, year, earnings = line.strip().split(',')
            dbCursor.execute(
                'INSERT INTO Pay (EmployeeID, Year, Earnings) VALUES (?, ?, ?);',
                (int(employee_id), int(year), float(earnings))
            )

    # Importing SSmin data from our SocialSecurityMin.txt file. Skip header and read line by line (stripping and splitting the comma seperator) -> insert into their expected fields.
    with open('SocialSecurityMin.txt', 'r') as file:
        next(file) 
        for line in file:
            year, minimum = line.strip().split(',')
            dbCursor.execute(
                'INSERT INTO SocialSecurityMin (Year, Minimum) VALUES (?, ?);',
                (int(year), float(minimum))
            )
    # Commit the data and end this transaction.
    dbConnection.commit()
    dbConnection.close()

def querySummary():
    '''Selecting our data to ready for print, ordering it per assignment specifications. Print final output to screen.'''
    dbConnection = sqlite3.connect('retirement.db')
    dbCursor = dbConnection.cursor()

    # Query our data, giving a shoutout to Github Copilot for readability, my code performed the same function but wasn't as clearly readable as this. Ordered by ascending name to match Professor Candido's printout
    query = '''
        SELECT 
            e.Name, 
            p.Year, 
            p.Earnings, 
            s.Minimum
        FROM Employee e
        JOIN Pay p ON e.EmployeeID = p.EmployeeID
        JOIN SocialSecurityMin s ON p.Year = s.Year
        ORDER BY e.Name ASC;
    '''
    # Storing our results of all the fetched data from our query into a variable to process my print statement.
    results = dbCursor.execute(query).fetchall()
    print(f'\n{'Employee Name':<20} {'Year':<10} {'Earnings':>15} {'Minimum':>14} {'Include':>18}')

    # Iterating through each record in our stored results to print, formatting to match Professors output as closely as possible.
    for name, year, earnings, minimum in results:
        status = 'Yes' if earnings >= minimum else 'No'
        print(f'{name:<20} {year:<10} {earnings:15,.2f} {minimum:15,.2f} {status:>15}')

    dbConnection.close()

createDB()
importData()
querySummary()

# Note to Prof. Candido: Loved this assignment, really enjoy working with SQL, and think this assignment was the perfect way to end the semester. 
# Greatly appreciate your wisdom and your methodology of teaching. Also yes, this comment is going on GitHub as well :)