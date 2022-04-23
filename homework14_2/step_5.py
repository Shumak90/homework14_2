import sqlite3


def get_step_5(name_1, name_2):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""
    SELECT `cast`
    FROM netflix      
    WHERE `cast` LIKE '%{name_1}%'
    AND `cast` LIKE '%{name_2}%'  
    """
    cur.execute(sqlite_query)
    rez = cur.fetchall()
    con.close()
    cast = []
    new_cast = []
    for rez_ in rez:
        cast.append(rez_[0])
    for cast_ in cast:
        new_cast += (cast_.split(', '))
    cast.clear()
    for new in new_cast:
        if name_1.lower() not in new.lower() and name_2.lower() not in new.lower():
            if new_cast.count(new) > 2:
                cast.append(new)
    cast = set(cast)
    return list(cast)

print(get_step_5("Ben Lamb", "Rose McIve"))