import sqlite3

# This program is responsible for creating the table for swiping system
# It loads the data from provided 'ids.csv' that contains the employees' IDs and card swipe informations.
# Note that the 'ids.csv' should be in the same folder as this '.py' file.

################################ Initialize the table #############################
# Drop all the tables and create the following tables 
# ids   (id integer, name text, PRIMARY KEY(id))
# in_time (id integer, tm time, FOREIGN KEY(id) REFERENCES ids(id))
def initialize_table(cursor ,connection):
    cursor.execute("DROP TABLE IF EXISTS ids;")
    cursor.execute("DROP TABLE IF EXISTS in_time;")
    cursor.execute("CREATE TABLE ids (id text, name text, PRIMARY KEY(id));")
    cursor.execute("CREATE TABLE in_time (id text, tm DateTime, FOREIGN KEY(id) REFERENCES ids(id));")
    connection.commit()

# This program is responsible to insert all the data inside 'id_list' into the 'signin.db' database
def insert_into_ids(cursor ,connection, id_list):
    cursor.executemany('INSERT INTO ids VALUES (?, ?);', id_list)
    # id_list.append((node_id, lat, lon))
    connection.commit()

# This program loads the 'ids.csv' and pass all the needed information to the related program, it is a 'bridge program'
def load_emoloyee_id():
    id_list = []
    with open('ids.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            id_list.append((row[0][5:12], row[1]))
        #id_list = map(tuple, reader)
    return id_list
	
def main():
	# connect to the 'signin.db' database file
    connection = sqlite3.connect('signin.db')
    cursor = connection.cursor()
	initialize_table(cursor ,connection)
    insert_into_ids(cursor ,connection, load_emoloyee_id())


