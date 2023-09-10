# Stretch Goal: Include Association with Owner
# 🛑 mapping SQL logic to separate methods that are easier to call using Python



#  STOPPED AT 30 MINS



import sqlite3 # 🛑 imports library

# 🛑 see debug.py for importing and using CONN, CURSOR
# 🛑 creates connection to database
# https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
CONN = sqlite3.connect('lib/resources.db') 
#🛑 access point to fire off CRUD sql queries
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()
 
class Pet:

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    # 🛑 id will refer to id created by sqlite3
    # 💡 do we need id=None or can we ignore that as a param
    def __init__(self, name, species, breed, temperament):
        self.name = name
        self.species = species
        self.breed = breed 
        self.temperament = temperament
        self.id = None 

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    # 💡 why should we make this a class method? only doing it once for all pets, individual pet not responsible for whole table
    @classmethod 
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets
                (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    species TEXT,
                    breed TEXT,
                    temperament TEXT
                );
        """
        CURSOR.execute(sql)
        
    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets;
        """
        CURSOR.execute(sql)
        

    # ✅ 4. Add "save" Method to Persist New "pet" Instances to DB
    # 💡 why instance method?
    # 🛑 won't be visible until we create get_all
    def save(self):
       
        # not sure if below works
        # sql = f""" 
        #     INSERT INTO pets(name, species, breed, temperament)
        #     VALUES ('{self.name}', '{self.species}', '{self.breed}', '{self.temperament}');
        # """

        # CURSOR.execute(sql)

        sql = """
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?, ?, ?, ?);
        """

        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament))

    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    # 🛑 combines the instantiation and persistance of pet object 
    @classmethod
    def create(cls, name, species, breed, temperament):
        # 🛑 __init__ method firing off
        pet = cls(name, species, breed, temperament)
        pet.save()

        return pet

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    # 🛑 row is a tuple that gets passed in 
    @classmethod
    def new_from_db(cls, row):
        # 🛑 same order as INSERT sql statement
        pet = cls(
            name=row[1],
            species=row[2],
            breed=row[3],
            temperament=row[4],
            id=row[0]
        )
        return pet 

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        sql = """ 
            SELECT * FROM pets;
        """
        # 🛑 fetchall is builtin to Python's cursor (you can also fetchmany, fetchone)
        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]
    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

        # If No "pet" Found, return "None"

    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

        # If No "pet" Found, return "None"

    # ✅ 10. Add "find_or_create_by" Class Method to:

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes

