#
# datatier.py
#
# Executes SQL queries against the given database.
#
# Original author: Prof. Joe Hummel, Ellen Kidane
#
import sqlite3


##################################################################
#
# select_one_row:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# the first row retrieved by the query (or the empty
# tuple () if no data was retrieved). The query can
# be parameterized, in which case pass the values as
# a list via parameters; this parameter is optional.
#
# Returns: first row retrieved by the given query, or
#          () if no data was retrieved. If an error
#          occurs, a msg is output and None is returned.
#
def select_one_row(dbConn, sql, parameters = None):
    dbCursor = dbConn.cursor()
    
    try:
        # check if there are parameters
        if parameters:
            dbCursor.execute(sql, parameters)
        else:
            dbCursor.execute(sql)
            
        row = dbCursor.fetchone() # get first row
        
        # check if data is returned or not
        if row:
            return row
        else:
            return ()
        
    except Exception as err:
        print("select_one_row failed:", err)
        return None
    
    finally:
        dbCursor.close()


##################################################################
#
# select_n_rows:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# a list of rows retrieved by the query. If the query
# retrieves no data, the empty list [] is returned.
# The query can be parameterized, in which case pass 
# the values as a list via parameters; this parameter 
# is optional.
#
# Returns: a list of 0 or more rows retrieved by the 
#          given query; if an error occurs a msg is 
#          output and None is returned.
#
def select_n_rows(dbConn, sql, parameters = None):
    dbCursor = dbConn.cursor()
    
    try:
        # check if there are parameters
        if parameters:
            dbCursor.execute(sql, parameters)
        else:
            dbCursor.execute(sql)
            
        rows = dbCursor.fetchall() # get all rows
        
        # check if data is returned or not
        if rows:
            return rows
        else:
            return []
        
    except Exception as err:
        print("select_n_rows failed:", err)
        return None
    
    finally:
        dbCursor.close()


##################################################################
#
# perform_action: 
# 
# Given a database connection and a SQL action query,
# executes this query and returns the # of rows
# modified; a return value of 0 means no rows were
# updated. Action queries are typically "insert", 
# "update", "delete". The query can be parameterized,
# in which case pass the values as a list via 
# parameters; this parameter is optional.
#
# Returns: the # of rows modified by the query; if an 
#          error occurs a msg is output and -1 is 
#          returned. Note that a return value of 0 is
#          not considered an error --- it means the
#          query did not change the database (e.g. 
#          because the where condition was false?).
#
def perform_action(dbConn, sql, parameters = None):
    dbCursor = dbConn.cursor()
    
    try:
        # check if there are parameters
        if parameters:
            dbCursor.execute(sql, parameters)
        else:
            dbCursor.execute(sql)
            
        dbConn.commit() # commit changes
        
        return dbCursor.rowcount # get # rows modified
    
    except Exception as err:
        print("perform_action failed:", err)
        return -1
    
    finally:
        dbCursor.close()
