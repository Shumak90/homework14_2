import sqlite3
import json


def get_step_6(type_move, release_year, listed_in):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""
               SELECT title, description
               FROM netflix
               WHERE `type` LIKE '%{type_move}%'   
               AND release_year = {release_year}
               AND listed_in LIKE '%{listed_in}%'

               """
    cur.execute(sqlite_query)
    rez = cur.fetchall()
    con.close()
    movies = []
    for i in rez:
        movies.append({
            "title": i[0],
            "description": i[1]
        })
    with open("movies.txt", 'w') as outfile:
        json.dump(movies, outfile, indent=2)
    return movies


print(get_step_6("Movie", 2017, "Dramas"))