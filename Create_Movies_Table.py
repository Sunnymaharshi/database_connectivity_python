import sqlite3

# connecting to the movies database
connection = sqlite3.connect("movies_database.db")
print("Connected to database")
  
# cursor to work with the database
crsr = connection.cursor()

# SQL command to create Movies table in the database
create_table_sql = """CREATE TABLE IF NOT EXISTS Movies ( 
id INTEGER PRIMARY KEY AUTOINCREMENT, 
name VARCHAR(30), 
actor VARCHAR(20), 
actress VARCHAR(20),
director VARCHAR(20),
release_year VARCHAR(5));"""
  

crsr.execute(create_table_sql)
print("Movies table created in the database")

# Movies data
movies = [("Interstellar","Matthew McConaughey","Anne Hathaway","Christopher Nolan","2014"),
          ("Inception","Leonardo DiCaprio","Marion Cotillard","Christopher Nolan","2010"),
          ("Dune","Timothe Chalamet","Zendaya","Denis Villeneuve","2021"),
          ("Tenet","John David Washington","Elizabeth Debicki","Christopher Nolan","2020"),
          ("Harry Potter and the Philosopher's Stone","Daniel Radcliffe","Emma Watson","Chris Columbus","2001"),
          ("The Dark Knight","Christian Bale","Maggie Gyllenhaal","Christopher Nolan","2008"),
          ("The Matrix","Keanu Reeves","Carrie-Anne Moss","Wachowskis","1999"),
          ("Gladiator","Russell Crowe","Connie Nielsen","Ridley Scott","2000"),
          ("300","Gerard Butler","Lena Headey","Zack Snyder","2007"),
          ("Jai Bhim","Suriya","Lijomol Jose","T. J. Gnanavel","2021"),
          ("Pushpa: The Rise","Allu Arjun","Rashmika Mandanna","Sukumar","2021"),
          ("Akhanda","Nandamuri Balakrishna","Pragya Jaiswal","Boyapati Srinu","2021"),
          ("Pokiri","Mahesh Babu","Ileana D'Cruz","Puri Jagannadh","2006")
        ]

# Inserting data into Movies table
crsr.executemany('insert into Movies(name,actor,actress,director,release_year) values (?,?,?,?,?)', movies)

# commit the data
connection.commit()
print("Data inserted into Movies table")


# close the connection
connection.close()
print("Closing the database connection")

