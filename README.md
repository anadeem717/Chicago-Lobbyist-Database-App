# Chicago-Lobbyist-Database-App

## Overview

The Chicago Lobbyist Database-App is a Python application designed to manage and retrieve information about lobbyists, their employers, clients, and compensation details. The application uses N-Tier design to interact with a database to perform various operations, such as adding lobbyist information, querying details, and tracking their years of registration.

## Features

- Retrieve the total number of lobbyists, employers, and clients in the database.
- Search for lobbyists by first or last name using wildcard patterns.
- Get detailed information about a specific lobbyist.
- Retrieve the top N lobbyists based on their total compensation for a given year.
- Add a year to a lobbyist's registration history.
- Update lobbyist salutations.

## Technologies

- Python 3.x
- SQLite (as the database management system)
- SQL for data retrieval and manipulation

## Usage

1. Start the application:
   ```bash
   python main.py
   ```

2. Use the various functions provided in the application to interact with the database, such as:
   - `num_lobbyists(dbConn)`
   - `get_lobbyists(dbConn, pattern)`
   - `get_lobbyist_details(dbConn, lobbyist_id)`
   - `get_top_N_lobbyists(dbConn, N, year)`
   - `add_lobbyist_year(dbConn, lobbyist_id, year)`
   - `set_salutation(dbConn, lobbyist_id, salutation)`

## Database Schema

The application uses the following database tables:

- **LobbyistInfo**
  - `Lobbyist_ID` (Primary Key)
  - `First_Name`
  - `Last_Name`
  - `Phone`
  - `Salutation`
  - (Other fields as necessary)

- **EmployerInfo**
  - `Employer_ID` (Primary Key)
  - `Employer_Name`

- **ClientInfo**
  - `Client_ID` (Primary Key)
  - `Client_Name`

- **Compensation**
  - `Lobbyist_ID`
  - `Client_ID`
  - `Compensation_Amount`
  - `Period_End`

- **LobbyistYears**
  - `Lobbyist_ID`
  - `Year`

## Functions

- `num_lobbyists(dbConn)`: Returns the number of lobbyists in the database.
- `num_employers(dbConn)`: Returns the number of employers in the database.
- `num_clients(dbConn)`: Returns the number of clients in the database.
- `get_lobbyists(dbConn, pattern)`: Retrieves lobbyists matching the given name pattern.
- `get_lobbyist_details(dbConn, lobbyist_id)`: Retrieves details for a specific lobbyist.
- `get_top_N_lobbyists(dbConn, N, year)`: Retrieves the top N lobbyists based on compensation for a specific year.
- `add_lobbyist_year(dbConn, lobbyist_id, year)`: Adds a registration year for a lobbyist.
- `set_salutation(dbConn, lobbyist_id, salutation)`: Sets or updates a lobbyist's salutation.
