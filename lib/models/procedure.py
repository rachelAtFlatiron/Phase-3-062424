import sqlite3 

CONN = sqlite3.connect('resources.db', timeout=10) 
CURSOR = CONN.cursor()

class Procedure:

    def __init__(self, name, price, id=None):
        self.name = name 
        self.price = price
        self.id = id 
    
    @classmethod
    def create_table(cls):
        sql = """ 
            CREATE TABLE IF NOT EXISTS procedures 
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod 
    def drop_table(cls):
        sql = """ DROP TABLE IF EXISTS procedures; """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        try: 
            sql = """ INSERT INTO procedures(name, price) VALUES (?, ?); """
            CURSOR.execute(sql, (self.name, self.price))
            CONN.commit()
            find_sql = """ SELECT id FROM procedures WHERE id = ?;"""
            self.id = CURSOR.execute(find_sql, (CURSOR.lastrowid,)).fetchone()[0]
        except Exception as e:
            print(f'Something went wrong: {e}')

    @classmethod 
    def create(cls, name, price):
        proc = cls(name, price)
        proc.save()
        return proc 

    @classmethod
    def create_instance(cls, row):
        proc = cls(
            id=row[0],
            name=row[1],
            price=row[2]
        )
        return proc 
    
    @classmethod 
    def get_all(cls):
        sql = """ SELECT * FROM procedures; """
        return [cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]
    
    @classmethod 
    def find_by_id(cls, id):
        sql = """ 
            SELECT * FROM procedures WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone() 
        if not row:
            return None 
        else: 
            return cls.create_instance(row)
    

    def __repr__(self):
        return f'''< {self.id} Procedure {self.name} is ${self.price} >'''
