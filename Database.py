import sqlite3 # import sqlite3 database library
# class for database connection
class DatabaseConnection:
  def __init__(self, database_name):
    self.database_name = database_name  # database name

  # Function for connecting to the database
  def connection(self):
    '''
    This function will connect python to the database
    '''
    try:
      self.sqlite_connection = sqlite3.connect('C:\\Users\\admin\\Desktop\\BOOTCAMP\\final_task_info\\' + self.database_name) # database connection
      print('Successfully connected to the database')
    except sqlite3.Error as e:
      print(f'Error connecting to the database {e}')

  # function for executing the query for retrieving the information from the database
  def database_execute_query(self, query, *args):
    '''
    This function will execute the SQL query
    and retrieve the information from the database
    '''
    self.query = query                                # assign the query to the variable self.query
    self.args = args                                  # assign user id and cart id to a variable it will be collected as a tuple
    if self.sqlite_connection:                        # if there is a sql connection execute the following 
        self.cursor = self.sqlite_connection.cursor() # cusrsor method create a cursor object to run the sql queries
        self.cursor.execute(self.query, (self.args))  # excute method of cursor object execute the sql query
        self.sqlite_connection.commit()               # save changes
    return self.cursor.fetchall() 
  
  # disconnecting the database
  def database_disconnect(self):
    if self.sqlite_connection:
      self.sqlite_connection.close()
  