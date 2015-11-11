'''This module allows imports into a
   sqlite3 Stats database the name
   of a player, thier plays, wins, and
   percentage of wins (wins/plays)'''


import sqlite3

def top_percent():
    '''Returns up to 5 records with the highest
    percentage of wins from the Statistics table'''
    conn = sqlite3.connect('stats.db')
    c_pylint = conn.cursor()
    c_pylint.execute("SELECT * FROM Stats ORDER BY percent DESC;")
    result_rows = c_pylint.fetchmany(3)
    conn.close()
    return result_rows


def insert_stat(name, wins, plays):
    '''inserts a player and their records
    into the database'''
    conn = sqlite3.connect("stats.db")
    c_pylint = conn.cursor()
    percent = wins / float(plays)
    #print percent
    c_pylint.execute("INSERT INTO Stats VALUES (?, ?, ?, ?);",
             (name, wins, plays, percent))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    for s in top_percent():
        print s
