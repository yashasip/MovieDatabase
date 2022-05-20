import sqlite3

# create and initiate database connection and cursor
with sqlite3.connect('moviesdb.sqlite') as conn:
    cur = conn.cursor()

def create_table(): # creates Movies table
    cur.execute('''CREATE TABLE IF NOT EXISTS Movies(
                    Name TEXT NOT NULL,
                    Actor TEXT,
                    Actress TEXT,
                    Director TEXT,
                    Year YEAR
                    )''')

def insert_movie_data(): # Inserts Movie records
    cur.execute('''INSERT INTO Movies VALUES(
                "DJANGO UNCHAINED", "LEONARDO DICAPRIO", "KERRY WASHINGTON","QUENTIN TARANTINO",  2012
                )''')
    cur.execute('''INSERT INTO Movies VALUES(
                "ANDHADHUN", "AYUSHMANN KHURANA", "TABU", "SRIRAM RAGHAVAN", 2018
                )''')
    cur.execute('''INSERT INTO Movies VALUES(
                "RRR", "RAM CHARAN", "ALIA BHATT", "RAJAMOULI", 2022
                )''')
    cur.execute('''INSERT INTO Movies VALUES(
                "INCEPTION", "LEONARDO DICAPRIO", "MARION COTILLARD", "CHRISTOPHER NOLAN",  2010
                )''')


def query_all_data(): # display all entered records
    result = cur.execute('''SELECT * FROM MOVIES''')
    display_result(result)

def query_actor_name(actor_name): # display records based on parameter
    result = cur.execute(f'''SELECT Name 
                        FROM MOVIES
                        WHERE Actor='{actor_name}'
                        ''')
    display_result(result)

def display_result(result): # helper function to display result
    for record in result:
        print(record)

def main(): # main function
    create_table()
    insert_movie_data()
    query_all_data()
    query_actor_name("LEONARDO DICAPRIO")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()