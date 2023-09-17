# Stretch Goal: Build Out Corresponding Owner Class Methods

# Owner Attributes: 
# name: string 
# phone: string 
# email: string 
# address: string

import sqlite3

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Owner:
    
    def __init__(self, name, email, id="None"):
        self.name = name 
        self.email = email 
        self.id = id

    # ✅ 12. Create table
    @classmethod 
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        );"""

        CURSOR.execute(sql)

    # ✅ 13. Drop table
    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS owners;"""
        CURSOR.execute(sql)

    # ✅ 14. Insert row
    def save(self):
        try:
            sql = """
                INSERT INTO owners (name, email)
                VALUES (?, ?);
            """
            CURSOR.execute(sql, (self.name, self.email))
            # ✅ 14a. Update instance with new row's id
            find_sql = """ SELECT id FROM owners WHERE id = ?;"""
            self.id = CURSOR.execute(find_sql, (CURSOR.lastrowid,)).fetchone()[0]
        except Exception as x:
            print(f'something went wrong, {x}')
            

    # ✅ 15. Get all rows
    # ✅ 15a. Create helper method to turn a row into an owner instance
    @classmethod 
    def create_instance(cls, row):
        owner = cls(
            id = row[0],
            name = row[1], 
            email = row[2]
        )
        return owner 
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM owners;"
        return [cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]

    # ✅ 16. Get row by id
    @classmethod 
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM owners WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        if not row: 
            return None 
        else: 
            return cls.create_instance(row)
        

    # ✅ 17. Delete row by id
    @classmethod 
    def delete_row(cls, id):
        try:
            sql = """ 
                DELETE FROM owners WHERE id = ?;
            """
            CONN.execute(sql, (id, ))
            print("success")
        except Exception as e:
            print(f'error: {e}')


    # ✅ 18. Update row by id
    def update(self):
        try:
            sql = """ 
                UPDATE owners SET name = ?, email = ? WHERE id = ?;
            """
            CURSOR.execute(sql, (self.name, self.email, self.id))
            print('success')
        except Exception as e:
            print(f'Error: {e}')
