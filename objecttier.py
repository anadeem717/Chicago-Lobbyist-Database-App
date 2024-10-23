# Areesh Nadeem
# CS341, Fall 2024
# netID: anade2


#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:

   def __init__(self, id, fName, lName, phone):
      self._Lobbyist_ID = id
      self._First_Name = fName
      self._Last_Name = lName
      self._Phone = phone

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Phone(self):
      return self._Phone



##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:

    def __init__(self, id, salutation, fName, midName, lName, suffix, addr1, addr2,
                 city, stateInit, zipCode, country, email, phone, fax, yearsReg,
                 employers, totalComp):

        self._Lobbyist_ID = id
        self._First_Name = fName
        self._Last_Name = lName
        self._Phone = phone
        self._Salutation = salutation
        self._Middle_Initial = midName
        self._Suffix = suffix
        self._Address_1 = addr1
        self._Address_2 = addr2
        self._City = city
        self._State_Initial = stateInit
        self._Zip_Code = zipCode
        self._Country = country
        self._Email = email
        self._Fax = fax
        self._Years_Registered = yearsReg
        self._Employers = employers
        self._Total_Compensation = totalComp

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone

    @property
    def Salutation(self):
        return self._Salutation

    @property
    def Middle_Initial(self):
        return self._Middle_Initial

    @property
    def Suffix(self):
        return self._Suffix

    @property
    def Address_1(self):
        return self._Address_1

    @property
    def Address_2(self):
        return self._Address_2

    @property
    def City(self):
        return self._City

    @property
    def State_Initial(self):
        return self._State_Initial

    @property
    def Zip_Code(self):
        return self._Zip_Code

    @property
    def Country(self):
        return self._Country

    @property
    def Email(self):
        return self._Email

    @property
    def Fax(self):
        return self._Fax

    @property
    def Years_Registered(self):
        return self._Years_Registered

    @property
    def Employers(self):
        return self._Employers

    @property
    def Total_Compensation(self):
        return self._Total_Compensation


##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:

    def __init__(self, id, fName, lName, phone, totalComp, clients):
        self._Lobbyist_ID = id
        self._First_Name = fName
        self._Last_Name = lName
        self._Phone = phone
        self._Total_Compensation = totalComp
        self._Clients = clients

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone

    @property
    def Total_Compensation(self):
        return self._Total_Compensation

    @property
    def Clients(self):
        return self._Clients


##################################################################
#
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   sql = """
         SELECT COUNT(*) FROM LobbyistInfo
         """
         
   row = datatier.select_one_row(dbConn, sql)

   if row is not None:
      return row[0]
   else :
      return -1        # error


##################################################################
#
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   sql = """
         SELECT COUNT(*) FROM EmployerInfo
         """
         
   row = datatier.select_one_row(dbConn, sql)

   if row is not None:
      return row[0]
   else :
      return -1        # error

##################################################################
#
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   sql = """
         SELECT COUNT(*) FROM ClientInfo
         """
         
   row = datatier.select_one_row(dbConn, sql)

   if row is not None:
      return row[0]
   else :
      return -1        # error

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and %
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID;
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   
   # finds lobbyist with matching pattern first name or last name
   sql = """
         SELECT Lobbyist_ID, First_Name, Last_Name, Phone
         FROM LobbyistInfo
         WHERE First_Name LIKE ?
         OR Last_Name LIKE ?
         GROUP BY Lobbyist_ID
         ORDER BY Lobbyist_ID ASC
         """
         
   rows = datatier.select_n_rows(dbConn, sql, [pattern,pattern])

   if rows is None:  # error
       return []

   # store lobbyists objects
   lobbyists = []

   if rows:
       # create object using data and append to list
       for row in rows:
           lobbyists.append(Lobbyist(row[0],row[1],row[2],row[3]))

   return lobbyists




##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    
    # get lobbyist details
    sql = """
          SELECT LobbyistInfo.Lobbyist_ID, Salutation, First_Name, Middle_Initial,
          Last_Name, Suffix, Address_1, Address_2, City, State_Initial,
          ZipCode, Country, Email, Phone, Fax
          FROM LobbyistInfo WHERE LobbyistInfo.Lobbyist_ID = ?
          """

    # get employer info matching with lobbyistID
    sqlEmployers =  """
                    SELECT DISTINCT Employer_Name FROM EmployerInfo
                    JOIN LobbyistAndEmployer
                    ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
                    WHERE Lobbyist_ID = ?
                    ORDER BY Employer_Name ASC
                    """

    sqlYearsReg = """
                  SELECT Year FROM LobbyistYears
                  WHERE Lobbyist_ID = ?
                  """

    sqlCompensation = """
                      SELECT SUM(Compensation_Amount) FROM
                      Compensation WHERE Lobbyist_ID = ?
                      """

    # get rows for the lobbyistDetails, if error return None
    res = datatier.select_one_row(dbConn, sql, [lobbyist_id])
    if res is None or not res:
        return None

    employers = datatier.select_n_rows(dbConn, sqlEmployers, [lobbyist_id])
    yearsReg = datatier.select_n_rows(dbConn, sqlYearsReg, [lobbyist_id])
    totalCompRes = datatier.select_one_row(dbConn, sqlCompensation, [lobbyist_id])

    # if totalComp is invalid from query, leave it at 0
    # otherwise change it to val from query
    totalComp = 0.0
    if totalCompRes and totalCompRes[0] is not None:
        totalComp = totalCompRes[0]

    # add employer names to list
    employerNames = []
    if employers:
        for row in employers:
            employerNames.append(row[0])

    # add years to list
    years = []
    if yearsReg:
        for row in yearsReg:
            years.append(row[0])

    # create object using all details, and return the lobbyist
    lobbyist = LobbyistDetails(res[0], res[1], res[2], res[3], res[4],
                               res[5], res[6], res[7], res[8], res[9],
                               res[10], res[11], res[12], res[13], res[14],
                               years, employerNames, totalComp)
    return lobbyist



##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid.
#          An empty list is also returned if an internal error
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):

   # calc the compensation for top lobbyists for certain year
   sqlCompensation = """
                     SELECT Compensation.Lobbyist_ID, First_Name, Last_Name, Phone, SUM(Compensation_Amount) as Comp
                     FROM Compensation
                     JOIN LobbyistInfo ON Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
                     WHERE strftime('%Y', Period_End) = ?
                     GROUP BY Compensation.Lobbyist_ID
                     ORDER BY Comp DESC
                     LIMIT ?
                     """
                     
   # get all clients matching the year and lobbyistID
   sqlClients = """
                SELECT Compensation.Client_ID, Client_Name FROM ClientInfo
                JOIN Compensation ON Compensation.Client_ID = ClientInfo.Client_ID
                WHERE strftime('%Y', Period_End) = ? AND Compensation.Lobbyist_ID = ?
                GROUP BY Compensation.Client_ID
                ORDER BY Client_Name ASC
                """

   rows = datatier.select_n_rows(dbConn, sqlCompensation, [year,N])

   # error
   if rows is None or not rows:
       return []

   lobbyists = []
   for row in rows:
       
       # for each lobbyists, find the clients
       clientsRes = datatier.select_n_rows(dbConn, sqlClients, [year,row[0]])

       # add all clients to a list
       clients = []
       if clientsRes:
           for clientRow in clientsRes:
               clients.append(clientRow[1])

       # create obj with details, and append
       lobbyists.append(LobbyistClients(row[0],row[1],row[2],row[3],row[4],clients))

   return lobbyists


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below),
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
   sql = """
         INSERT INTO LobbyistYears(Lobbyist_ID, Year)
         VALUES(?, ?);
         """
         
   # find if lobbyist exists     
   sqlFindLobbyist =  """
                      SELECT Lobbyist_ID FROM LobbyistInfo
                      WHERE Lobbyist_ID = ?
                      """
                      
   row = datatier.select_one_row(dbConn, sqlFindLobbyist, [lobbyist_id])
    
   if not row: # lobbyist not found
       return 0
                      
   res = datatier.perform_action(dbConn, sql, [lobbyist_id, year])
   
   if res == -1: # error
       return 0
   else:
       return 1  # success


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   sql = """
         UPDATE LobbyistInfo
            SET Salutation = ?
            WHERE Lobbyist_ID = ?
         """
         
   # find if lobbyist exists       
   sqlFindLobbyist =  """
                      SELECT Lobbyist_ID FROM LobbyistInfo
                      WHERE Lobbyist_ID = ?
                      """
                      
   row = datatier.select_one_row(dbConn, sqlFindLobbyist, [lobbyist_id])
    
   if not row: # lobbyist not found
       return 0
   
   res = datatier.perform_action(dbConn, sql, [salutation, lobbyist_id])
   
   if res == -1: # error
       return 0
   else:
       return 1  # success