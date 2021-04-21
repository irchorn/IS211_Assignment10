#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3 as lite

def print_data():
    con = lite.connect('pets.db')

    with con:
        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM person")

        rows = cur.fetchall()

    for row in rows:
        print ("{} {} {}".format(row["id"], row["first_name"], row["last_name"], row["age"]))


# In[7]:


    cur.execute("SELECT * FROM pet")

    rows = cur.fetchall()

    for row in rows:
        print ("{} {} {}".format(row["name"], row["breed"], row["age"]))
        
    while True:
        user_input = input("Enter your ID number:")
        id = int(user_input)
        if id >= 1:
            select_stmt = "select person.first_name, person.last_name, person.age, pet.name, pet.age from person, pet, person_pet where person_id = {}".format(id)
            cur.execute(select_stmt)
            results = cur.fetchall()
            for record in results:
                print(f"Person {row[0]} {row[1]} has a pet name {row[2]}")
        else:
            print('Wrong ID')
            exit(1)
        
if __name__ == "__main__":
    print_data()        


# In[ ]:




