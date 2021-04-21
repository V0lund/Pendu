# MODULES
import sqlite3

"""
create a table with the players game related statistics. The columns are identical whit the keys of dictionary 
'player_stat' from file pendu.py from witch the data will be uploaded after each game. The command is executed one time.
After that will be commented.
player_stat = {'name': '', 'level': '', 'tries': '', 'time': ''}
c.execute(
CREATE TABLE players_stat
(
name nvarchar,
level int,
tries int,
time float
))
c.fetchone()
connect_db.commit()
"""

def db_insert(dict):
    """
    FUNCTION to INSERT INTO table players_stat from
    :param dict: dictionary
    :return: none
    """
    connect_db = sqlite3.connect('leadersboard.db')
    c = connect_db.cursor()
    c.execute("""
    INSERT INTO players_stat
    VALUES (:name, :level, :tries, :time)""", dict)
    connect_db.commit()
    connect_db.close()


def show_leadersboard():
    connect_db = sqlite3.connect('leadersboard.db')
    c = connect_db.cursor()
    c.execute("""
    SELECT * FROM players_stat
    ORDER BY level DESC, tries, time
    """)
    print('#########################')
    print("# ALL TIME BEST PLAYERS #")
    print("name   level  tries  time")
    print('#########################')
    leadersboard = c.fetchall()
    for i in range(5):
        print(leadersboard[i], end=' ')
        print('')
    connect_db.commit()
    connect_db.close()


