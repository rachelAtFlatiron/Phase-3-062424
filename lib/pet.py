
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
import sqlite3
from owner import Owner, CONN, CURSOR
#connect to database file (we are not using :memory:)
CONN = sqlite3.connect('lib/resources.db', timeout=10)
#create firing off point for sql queries
CURSOR = CONN.cursor()
 
 #C - table, instances/rows
 #R - instances/rows
 #U  
 #D
 
 #class Pet <--> pets table in SQL
 #attributes <--> columns
class Pet:

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    #id is still going to represent the auto-generated id column in SQL
    def __init__(self, name='', age=1, breed='', owner_id=None, id=None):
        self.name = name 
        self.age = age 
        self.breed = breed 
        self.owner_id = owner_id
        self.id = id 


    # ✅ 2. Create table
    @classmethod 
    def create_table(cls):
        sql = """
            CREATE TABLE pets (
                id INTEGER PRIMARY KEY,
                age INTEGER,
                name TEXT,
                breed TEXT,
                owner_id INTEGER,
                FOREIGN KEY (owner_id) REFERENCES owners(id)
            );
        """
        #fire off query
        CURSOR.execute(sql)
        #save change to database
        CONN.commit()

    # ✅ 3. Drop table
    @classmethod 
    def drop_table(cls):
        sql = """ 
            DROP TABLE IF EXISTS pets;
        """
        CURSOR.execute(sql)
        CONN.commit()

    # ✅ 4. Insert current pet instance (self) into DB
    def save(self):
        try:
            sql = """
                INSERT INTO pets (name, age, breed, owner_id) VALUES (?, ?, ?, ?);
            """
            #(self.name, self.age, self.breed, ) is a tuple so don't forget the trailing comma if you only have one item
            CURSOR.execute(sql, (self.name, self.age, self.breed, self.owner_id,))
            CONN.commit()
            #if all went well, we can get the most recent entry 
            #CURSOR.lastrowid
            #and update self.id
            self.id = CURSOR.lastrowid
        except Exception as e:
            print (f'{e}')

    # ✅ 6. Create instance from DB, thus getting the ID
    @classmethod 
    def create_instance(cls, row):
        #row = ['id', 'name', 'age, 'breed']
        pet = cls(
            name=row[2],
            age=row[1],
            breed=row[3],
            owner_id=row[4],
            id=row[0]
        )
        return pet 

    # ✅ 7. Get all rows, convert each row back into an instance, return a list of pet objects
    @classmethod 
    def get_all(cls):
        sql = "SELECT * FROM pets;"
        pets = CURSOR.execute(sql).fetchall()
        if not pets:
            return None 
        return [Pet.create_instance(pet) for pet in pets]
    
    # ✅ 8. Get row by name
    @classmethod 
    def find_by_name(cls, name):
        sql = """  
            SELECT * FROM pets WHERE name=?;
        """
        row = CURSOR.execute(sql, (name, )).fetchone()
        if not row:
            return None 
        return Pet.create_instance(row)

    # ✅ 9. Get row by id
    @classmethod 
    def find_by_id(cls, id):
        sql = """  
            SELECT * FROM pets WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        return Pet.create_instance(row)

    # ✅ 10. Find row, otherwise create row
    @classmethod 
    def find_or_create(cls, name=None, age=None, breed=None):
        # ✅ 10a. Search for pet
        sql = """
            SELECT * FROM pets WHERE name=? AND age=? AND breed=?;
        """
        row = CURSOR.execute(sql, (name, age, breed, )).fetchone()
        if not row:
            #create a new instance, and save the pet 
            pet = Pet(name, age, breed)
            pet.save()
            return pet
        else: 
            return cls.create_instance(row)

        #✅ 10b. Insert pet if it does not exist
        # ✅ 10c. Return pet if it does exist

    # ✅ 11. Update row
    # assuming we have altered the instance attributes, and need to apply those changes to the table 
    def update(self):
        sql = """ 
            UPDATE pets SET name=?, age=?, breed=?, owner_id=? WHERE id=?;
        """
        CURSOR.execute(sql, (self.name, self.age, self.breed, self.owner_id, self.id, ))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM pets WHERE id=?;
        """
        CURSOR.execute(sql, (self.id, ))
        CONN.commit()

    def get_owner(self):
        sql = """ 
            SELECT * FROM owners WHERE id=?;
        """
        row = CURSOR.execute(sql, (self.owner_id, )).fetchone()
        if not row:
            return "this is a stray"
        else: 
            #convert row into an owner instance 
            return Owner.convert_to_instance(row)
        
    def __repr__(self):
        return f"<{self.id} Pet {self.name} is a {self.age} yr old {self.breed}>"

