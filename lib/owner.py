# Stretch Goal: Build Out Corresponding Owner Class Methods

# Owner Attributes: 
# name: string 
# phone: string 
# email: string 
# address: string

import sqlite3
# from pet import Pet, CONN, CURSOR

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Owner:
    
    def __init__(self, name, id="None"):
        self.name = name 
        self.id = id

    # one-to-many, owner has many pets, pet belongs to an owner

    @classmethod 
    def create_table(cls):
        sql = """
            CREATE TABLE owners(
                id INTEGER PRIMARY KEY,
                name text
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """  
            INSERT INTO owners(name) VALUES (?);
        """
        CURSOR.execute(sql, (self.name, ))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def delete(self):
        sql = """
            DELETE FROM owners WHERE id=?;
        """
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()
        
    @classmethod 
    def find_by_id(cls, id):
        sql = """ 
            SELECT * FROM owners WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        return Owner.convert_to_instance(row)


    @classmethod 
    def convert_to_instance(cls, row):
        owner = Owner(name=row[1], id=row[0])
        return owner 
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM owners;"
        rows = CURSOR.execute(sql).fetchall()
        #convert each row into an Owner instance
        return [Owner.convert_to_instance(owner) for owner in rows]
    
    #getting all pets for owner
    # def get_pets(self):
    #     sql = """
    #         SELECT * FROM pets WHERE owner_id=?;
    #     """
    #     rows = CURSOR.execute(sql).fetchall()
    #     return [Pet.create_instance(row) for row in rows]

    def __repr__(self):
        return f'<Owner id={self.id} name={self.name} />'