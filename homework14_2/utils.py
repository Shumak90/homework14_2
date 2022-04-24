import sqlite3


def get_movie_by_title(title):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""
    SELECT title, country, release_year, listed_in, description
    FROM netflix
    WHERE title LIKE "%{title}%"
    ORDER BY release_year DESC
    LIMIT 1
    """
    cur.execute(sqlite_query)
    rez = cur.fetchall()
    con.close()
    movies = []
    for i in rez:
        movies.append({
            "title": i[0],
            "country": i[1],
            "release_year": i[2],
            "genre": i[3],
            "description": i[4]
        })

    return movies


def get_movie_by_year(s_year, po_year):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""
    SELECT title, release_year
    FROM netflix
    WHERE release_year BETWEEN {s_year} AND {po_year}
    ORDER BY release_year DESC 
    LIMIT 100
    """
    cur.execute(sqlite_query)
    rez = cur.fetchall()
    con.close()
    movies = []
    for i in rez:
        movies.append({
            "title": i[0],
            "release_year": i[1]
        })
    return movies


def get_movie_by_rating(rating):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""
        SELECT title, rating, description
        FROM netflix
        WHERE rating IN ({rating})
        """
    cur.execute(sqlite_query)
    rez = cur.fetchall()
    con.close()
    movies = []
    for i in rez:
        movies.append({
            "title": i[0],
            "rating": i[1],
            "description": i[2]
        })
    return movies


def get_movie_by_genre(genre):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""
           SELECT title, description, release_year, listed_in
           FROM netflix
           WHERE listed_in LIKE '%{genre}%'
           ORDER BY release_year DESC 
           LIMIT 10          
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
    return movies








