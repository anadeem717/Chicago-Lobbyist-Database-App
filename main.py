
# Areesh Nadeem
# CS341, Fall 2024
# netID: anade2

import sqlite3
import objecttier


def findLobbyistsWithName(dbConn, name):
    """Uses the name given to find lobbyists with matching first
    or last name. If greater than 100 results, asks user to narrow down search

    Args:
        dbConn: db connection
        name: first/last name to match
    """
    
    # get list of lobbyists from obj tier
    lobbyists = objecttier.get_lobbyists(dbConn, name)
    
    size = len(lobbyists)
    
    print("\nNumber of lobbyists found:", size)
    print()
    
    if (size > 100):
        print("There are too many lobbyists to display, please narrow your search and try again...")
    
    elif (size == 0):
        return
   
    else:
        # if valid # of lobbyists, print relevant info for each person
        for person in lobbyists:
            print(person.Lobbyist_ID,':',person.First_Name,person.Last_Name,"Phone:",person.Phone)

    print()



def findLobbyistInfo(dbConn, id):
    """Finds detailed info about the lobbyist with matching ID

    Args:
        dbConn: db connection
        id: lobbyistID
    """
    
    # get the lobbyist from obj tier
    lobbyist = objecttier.get_lobbyist_details(dbConn, id)
    
    if lobbyist is None:
        print("\nNo lobbyist with that ID was found.")
    
    else:
        # format the info from the object, and print it out
        print()
        employers = ', '.join(lobbyist.Employers)
        yearsReg = ', '.join(str(i) for i in lobbyist.Years_Registered)
        yearsReg += ','
        employers += ','
        
        print(lobbyist.Lobbyist_ID, ':')
        print("  Full Name:", lobbyist.Salutation,lobbyist.First_Name, 
              lobbyist.Middle_Initial, lobbyist.Last_Name, lobbyist.Suffix)
        print("  Address:", lobbyist.Address_1, lobbyist.Address_2, ',', lobbyist.City, ',', 
              lobbyist.State_Initial, lobbyist.Zip_Code, lobbyist.Country)
        print("  Email:",lobbyist.Email)
        print("  Phone:",lobbyist.Phone)
        print("  Fax:",lobbyist.Fax)
        print("  Years Registered:",yearsReg)
        print("  Employers:",employers)
        print("  Total Compensation:", '$'+(f"{lobbyist.Total_Compensation:,.2f}"))
    print()
    
    
    
def findTopNLobbyists(dbConn, N, year):
    """Finds the top N lobbyists by total comp

    Args:
        dbConn: db connection
        N: # of lobbyists to calculate
        year: specific year
    """
    
    # get the top N lobbyist list from obj tier
    lobbyists = objecttier.get_top_N_lobbyists(dbConn, N, str(year))
    
    if (len(lobbyists) == 0):
        print()
        return
    
    print()
    
    num = 1 # for numbering lobbyists 
    
    # format info for each person, and output
    for person in lobbyists:
        clients = ', '.join(person.Clients)
        clients += ','
        
        print(num, '.', person.First_Name, person.Last_Name)
        print("  Phone:", person.Phone)
        print("  Total Compensation:",'$'+(f"{person.Total_Compensation:,.2f}"))
        print("  Clients:", clients)
        num += 1
    print()
    
    
    
def registerYear(dbConn, year, id):
    """Registers a year for the given lobbyist ID

    Args:
        dbConn: db connection
        year: year to add
        id: lobbyist ID
    """
    
    res = objecttier.add_lobbyist_year(dbConn, id, year)
    
    # success
    if res == 1:
        print ("\nLobbyist successfully registered.\n")
    
    # either id not found, or datatier failed
    else:
        print("\nNo lobbyist with that ID was found.\n")



def setSalutation(dbConn, id, salutation):
    """Sets a salutation for given lobbyist iD

    Args:
        dbConn: db connection
        salutation: salutation to add
        id: lobbyist ID
    """
    
    res = objecttier.set_salutation(dbConn, id, salutation)
    
    # success
    if res == 1:
        print ("\nSalutation successfully set.\n")
    
    # either id not found, or datatier failed
    else:
        print("\nNo lobbyist with that ID was found.\n")



##################################################################  
#
# main
#
def main():
    
    # setup database connection
    dbConn = sqlite3.connect("Chicago_Lobbyists.db")
    
    print('** Welcome to the Chicago Lobbyist Database Application **\n')
    
    # calculate general statistics
    numLobbyists = objecttier.num_lobbyists(dbConn)
    numEmployers = objecttier.num_employers(dbConn)
    numClients = objecttier.num_clients(dbConn)
    
    # display general statistics
    print("General Statistics:")
    print("  Number of Lobbyists: " + (f"{numLobbyists:,}"))
    print("  Number of Employers: " + (f"{numEmployers:,}"))
    print("  Number of Clients: " + (f"{numClients:,}"))
    print()
    
    while (True):
        choice = input("Please enter a command (1-5, x to exit): ")
    
        match (choice):
            
            # find lobbyist with matching name
            case '1':
                print()
                name = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
                findLobbyistsWithName(dbConn, name)
            
            # find detailed info about lobbyist given ID 
            case '2':
                print()
                id = input("Enter Lobbyist ID: ")
                findLobbyistInfo(dbConn, id)
                
            # find top N lobbyists by total comp    
            case '3':
                print()
                N = int(input("Enter the value of N: "))
                
                if (N < 1):
                    print("Please enter a positive value for N...\n")
                    continue
                
                year = int(input("Enter the year: "))
                findTopNLobbyists(dbConn, N, year)
            
            # register a year for a lobbyist   
            case '4':
                print()
                year = int(input("Enter year: "))
                id = input("Enter the lobbyist ID: ")
                
                registerYear(dbConn, year, id)
            
            # set a salutation for a lobbyist
            case '5':
                print()
                id = input("Enter the lobbyist ID: ")
                salutation = input("Enter the salutation: ")
                setSalutation(dbConn, id, salutation)
            
            # done with program
            case 'x':
                break
            
            case _:
                print("**Error, unknown command, try again...")
                print()
        
#
# done
#

main()