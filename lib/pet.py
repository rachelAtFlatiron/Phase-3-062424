# Stretch Goal: Include Association with Owner
# 🛑 mapping SQL logic to separate methods that are easier to call using Python

import sqlite3 # 🛑 imports library

# 🛑 see debug.py for importing and using CONN, CURSOR
# 🛑 creates connection to database, an object
# https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
# 🛑 timeout to avoid database lock on failed queries 
CONN = sqlite3.connect('lib/resources.db', timeout=10) 
#🛑 access point to fire off CRUD sql queries, an object
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()
 
class Pet:

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    # 🛑 id will refer to id created by sqlite3
    # 💡 do we need id=None or can we ignore that as a param
    def __init__(self, name, age, species, owner_id = None, id=None):
        self.name = name
        self.age = age
        self.species = species
        self.owner_id = owner_id
        self.id = id

    # ✅ 2. Create table
    # 💡 why should we make this a class method? only doing it once for all pets, individual pet not responsible for whole table
    @classmethod 
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets
                (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    test TEXT,
                    species TEXT,
                    owner_id INTEGER
                    FOREIGN KEY (owner_id) REFERENCES owners(id)
                );
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    # ✅ 3. Drop table
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets;
        """
        CURSOR.execute(sql)
        CONN.commit()
        

    # ✅ 4. Insert instance into DB
    # 💡 why instance method?
    # 🛑 won't be visible until we create get_all
    def save(self):
        try: 
            
            sql = """
                INSERT INTO pets (name, age, species, owner_id)
                VALUES (?, ?, ?, ?);
            """
            # 🛑 execute is a pre-existing method, SQLAlchemy will automate a lot of this for us
            # 🛑 pass in a tuple for arguments
            # 🛑 ??? NOT VISIBLE VIA SQLITE YET, need get_all() - then we will see all the instances popping up for us
            CURSOR.execute(sql, (self.name, self.age, self.species, self.owner_id))
            CONN.commit()
        except Exception as x: 
            
            print(f'something went wrong, {x}')

    # ✅ 5. Initialize instance and insert into database
    # 🛑 combines the instantiation and persistance of pet object 
    @classmethod
    def create(cls, name, age, species, owner_id):
        # 🛑 __init__ method firing off
        pet = cls(name, age, species, owner_id)
        pet.save()

        return pet

    # ✅ 6. Create instance from DB, thus getting the ID
    # 🛑 row is a tuple that gets passed in 
    # 🛑 may be out of index if there is no ID
    # 🛑 will be passed into #7
    @classmethod
    def create_instance(cls, row):
        # 🛑 same order as INSERT sql statement
        pet = cls(
            name=row[1],
            age=row[2],
            species=row[3],
            owner_id=row[4],
            id=row[0] #🛑 this is where we get the id from database
        )
        return pet 

    # ✅ 7. Get all rows
    @classmethod
    def get_all(cls):
        sql = """ 
            SELECT * FROM pets;
        """
        # 🛑 fetchall is builtin to Python's cursor (you can also fetchmany, fetchone)
        return [cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]
    

    # ✅ 8. Get row by name
    @classmethod 
    def find_by_name(cls, name):
        # If No "pet" Found, return "None"
        sql = """
            SELECT * FROM pets WHERE name = ? LIMIT 1;
        """

        row = CURSOR.execute(sql, (name, )).fetchone()
        if not row:
            return None 
        else:
            return cls.create_instance(row)

    # ✅ 9. Get row by id
    # 🛑 more likely to be used as a callback
    @classmethod 
    def find_by_id(cls, id):
        sql = """ 
            SELECT * FROM pets WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone() 
        if not row:
            return None 
        else: 
            return cls.create_instance(row)
        
    # ✅ 10. Find row, otherwise create row
    @classmethod 
    def find_or_create_by(cls, name=None, age=None, species=None, owner_id = None):
        # ✅ 10a. Search for pet
        sql = """ 
            SELECT * FROM pets WHERE 
            (name, age, species, owner_id) = (?, ?, ?, ?);
        """
        row = CURSOR.execute(sql, (name, age, species, owner_id)).fetchone()
        #✅ 10b. Insert pet if it does not exist
        if not row: 
            sql = """ INSERT INTO pets(name, age, species, owner_id) VALUES (?, ?, ?, ?);"""
            CURSOR.execute(sql, (name, age, species, owner_id))
            CONN.commit()
            #🛑 last_row_id is built-in, does not handle if INSERT fails
            return cls.find_by_id(CURSOR.lastrowid)
        # ✅ 10c. Return pet if it does exist
        else:
            return cls.create_instance(row)
        
    # ✅ 11. Update row
    # 🛑 1. find pet (find_or_create_by)
    # 🛑 2. change a pet's attribute 
    # 🛑 3. use update
    def update(self):
        sql = """ 
            UPDATE pets SET name = ?, age = ?, species = ?, owner_id = ? WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.age, self.species, self.owner_id, self.id))
        CONN.commit()


    def __repr__(self):
        return f"<{self.id} Pet {self.name} is a {self.age} yr old {self.species}>"

