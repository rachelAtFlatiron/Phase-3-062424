import sqlite3

CONN = sqlite3.connect('resources.db')
CURSOR = CONN.cursor()

class Owner:
    
    def __init__(self, name, email, id="None"):
        self.name = name 
        self.email = email 
        self.id = id

    @classmethod 
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        );"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS owners;"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        try:
            sql = """
                INSERT INTO owners (name, email)
                VALUES (?, ?);
            """
            CURSOR.execute(sql, (self.name, self.email))
            CONN.commit()
            find_sql = """ SELECT id FROM owners WHERE id = ?;"""
            self.id = CURSOR.execute(find_sql, (CURSOR.lastrowid,)).fetchone()[0]
        except Exception as x:
            print(f'something went wrong, {x}')
            
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
        

    @classmethod 
    def delete_row(cls, id):
        try:
            sql = """ 
                DELETE FROM owners WHERE id = ?;
            """
            CONN.execute(sql, (id, ))
            CONN.commit()
            print("success")
        except Exception as e:
            print(f'error: {e}')

    @classmethod
    def create(cls, name, email):
        owner = cls(name, email)
        owner.save()
        return owner



    def update(self):
        try:
            sql = """ 
                UPDATE owners SET name = ?, email = ? WHERE id = ?;
            """
            CURSOR.execute(sql, (self.name, self.email, self.id))
            CONN.commit()
            print('success')
        except Exception as e:
            print(f'Error: {e}')

    def __repr__(self):
        return(f'<{self.id} Owner "{self.name}" {self.email} />')
