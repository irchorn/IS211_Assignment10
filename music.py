import sqlite3 as lite


def insert_data():
    con = lite.connect('music.db')  # Connect to the music.db database

    with con:
        cur = con.cursor()  # Get the cursor object

        cur.execute("DROP TABLE IF EXISTS artists")

        cur.execute("CREATE TABLE artists(artist_id INT, artist_name TEXT)")
        cur.execute("INSERT INTO artists VALUES(1,'Prince')")
        cur.execute("INSERT INTO artists VALUES(2,'U2')")

        cur.execute("DROP TABLE IF EXISTS albums")

        cur.execute("CREATE TABLE albums(album_id INT, album_title TEXT, artist_id INT)")
        cur.execute("INSERT INTO albums VALUES(1,'Purple Rain', 1)")
        cur.execute("INSERT INTO albums VALUES(2,'Songs Of Innocence', 2)")

        cur.execute("DROP TABLE IF EXISTS songs")

        cur.execute("CREATE TABLE songs(song_id INT, song_name TEXT, album_id INT, track_number INT, song_length INT)")
        cur.execute("INSERT INTO songs VALUES(1,'Purple Rain',1, 9, '8:41')")
        cur.execute("INSERT INTO songs VALUES(2,'Volcano',2, 6, '3:14')")


def retrieve_data():
    try:
        con = lite.connect('music.db')

        cur = con.cursor()
        cur.execute('SELECT song_name, song_length  from songs')
        data = cur.fetchall()

        for row in data:
            print(f"Song {row[0]} lasts {row[1]} minutes")
    except lite.Error as e:
        print(f"Error {e}:")

    finally:
        if con:
            con.close()


if __name__ == "__main__":
    insert_data()
    retrieve_data()


