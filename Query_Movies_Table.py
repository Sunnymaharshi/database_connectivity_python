import sqlite3

# connecting to the movies database
connection = sqlite3.connect("movies_database.db")
print("Connected to database")
  
# cursor to work with the database
crsr = connection.cursor()

print("Enter actor name to search movies with specific actor")
print("Enter all to get all movies")
print("Enter exit or Press CTRL + C to Exit")

def Query(actor):

    if(actor=="exit"):
        exit()
    elif(actor=="all"):
        # select all from the Movies table
        crsr.execute("SELECT * FROM Movies")
        movies = crsr.fetchall()

        if(len(movies)==0):
            print("No Movies with",actor)
        # print row by row
        for movie in movies:
            # omitting id of movie
            print("  ".join(movie[1:]))
    else:
        # search for movies with given actor
        crsr.execute("SELECT * FROM Movies WHERE actor LIKE ?",("%"+actor+"%",))
        movies = crsr.fetchall()

        if(len(movies)==0):
            print("No Movies with",actor)
        # print row by row
        for movie in movies:
            # omitting id of movie
            print("  ".join(movie[1:]))

while(True):
    actor = input()
    Query(actor)
    
