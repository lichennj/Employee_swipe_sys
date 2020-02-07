import sqlite3
import re
import csv
import sys


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

def insert_time(cursor ,connection, card_info):   
    #print(card_info)
    #card_info = str(card_info)
    #print(type(card_info))
    #print(card_info[0],card_info[6])
    # Card info here should be [card_info]
    cursor.execute("INSERT INTO in_time VALUES (?, DateTime('now', 'localtime'))", [card_info])
    connection.commit()

def insert_into_ids(cursor ,connection, id_list):
    cursor.executemany('INSERT INTO ids VALUES (?, ?);', id_list)
    # id_list.append((node_id, lat, lon))
    connection.commit()

def output_by_people():
    cursor.execute('')

def insert_into(cursor ,connection):
    # detect the input and automatically load into table
    #print('Please swipe the card')
    #raw_id = str(sys.argv[0])
    #match = re.match(';\d\d\d\d\d\d\d\d\d\d\d\d\d\?', raw_id)
    try:
        raw_id = str(input('Please swipe card'))
        
    except ValueError:
        print('Please swipe again!')

    print('Log success')
    
    # detect if the card is valid student card
    # Match the front and end part
    match = re.match(';\d\d\d\d\d\d\d\d\d\d\d\d\d\?', raw_id)    
    # ';7701147272401?'

    if not match:
        print('Invalid card')
        return
        # jump to the front
        
    # slice the specific student number
    student_id = raw_id[5:12]

    # insert the current swipe info into the database
    insert_time(cursor ,connection, student_id)

def load_db():
    connection = sqlite3.connect('signin.db')
    cursor = connection.cursor()

def load_emoloyee_id():
    id_list = []
    with open('ids.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            id_list.append((row[0][5:12], row[1]))
        #id_list = map(tuple, reader)
    return id_list

def main():
    print('Program start')
    connection = sqlite3.connect('signin.db')
    cursor = connection.cursor()
    initialize_table(cursor ,connection)
    insert_into_ids(cursor ,connection, load_emoloyee_id())
    while(1):
        insert_into(cursor ,connection)

main()










