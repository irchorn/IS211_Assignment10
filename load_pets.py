import sqlite3 as lite
def insert_data():
    con = lite.connect('pets.db')

    with con:
        

        con = lite.connect('pets.db')

        with con:

            cur = con.cursor()

            cur.execute("DROP TABLE IF EXISTS person")

            cur.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
            cur.execute("INSERT INTO person VALUES(1,'James','Smith',41)")
            cur.execute("INSERT INTO person VALUES(2,'Diana','Greene',23)")
            cur.execute("INSERT INTO person VALUES(3,'Sara','White',27)")
            cur.execute("INSERT INTO person VALUES(4,'William','Gibson',23)")

            cur.execute("DROP TABLE IF EXISTS pet")

            cur.execute("CREATE TABLE pet(id INTEGER PRIMARY KEY, name TEXT,breed TEXT, age INTEGER, dead INTEGER)")
            cur.execute("INSERT INTO pet VALUES(1,'Rusty','Dalmation',4,1)")
            cur.execute("INSERT INTO pet VALUES(2,'Bella','AlaskanMalamute',3,0)")
            cur.execute("INSERT INTO pet VALUES(3,'Max','CockerSpaniel',1,0)")
            cur.execute("INSERT INTO pet VALUES(4,'Rocky','Beagle',7,0)")
            cur.execute("INSERT INTO pet VALUES(5,'Rufus','CockerSpaniel',1,0)")
            cur.execute("INSERT INTO pet VALUES(6,'Spot','Bloodhound',2,1)")

            cur.execute("DROP TABLE IF EXISTS person_pet")

            cur.execute("CREATE TABLE person_pet(person_id INTEGER, pet_id INTEGER)")
            cur.execute("INSERT INTO person_pet VALUES(1, 1)")
            cur.execute("INSERT INTO person_pet VALUES(1, 2)")
            cur.execute("INSERT INTO person_pet VALUES(2, 3)")
            cur.execute("INSERT INTO person_pet VALUES(2, 4)")
            cur.execute("INSERT INTO person_pet VALUES(3, 5)")
            cur.execute("INSERT INTO person_pet VALUES(4, 6)")

if __name__ == "__main__":
    insert_data()


