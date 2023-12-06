import sqlite3 

CONN = sqlite3.connect('resources.db', timeout=10) 
CURSOR = CONN.cursor()
 
class Pet:

    def __init__(self, name, age, species, owner_id = None, id=None):
        self.name = name
        self.age = age
        self.species = species
        self.owner_id = owner_id
        self.id = id

    @classmethod 
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets
                (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    species TEXT,
                    owner_id INTEGER,
                    FOREIGN KEY (owner_id) REFERENCES owners(id)
                );
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        try: 
            
            sql = """
                INSERT INTO pets (name, age, species, owner_id)
                VALUES (?, ?, ?, ?);
            """
            CURSOR.execute(sql, (self.name, self.age, self.species, self.owner_id))
            CONN.commit()
            find_sql = """ SELECT id FROM pets WHERE id = ?;"""
            self.id = CURSOR.execute(find_sql, (CURSOR.lastrowid,)).fetchone()[0]
        except Exception as x: 
            
            print(f'something went wrong, {x}')

    @classmethod
    def create(cls, name, age, species, owner_id):
        pet = cls(name, age, species, owner_id)
        pet.save()
        return pet

    @classmethod
    def create_instance(cls, row):
        pet = cls(
            name=row[1],
            age=row[2],
            species=row[3],
            owner_id=row[4],
            id=row[0] 
        )
        return pet 


    @classmethod
    def get_all(cls):
        sql = """ 
            SELECT * FROM pets;
        """
        return [cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]
    
    @classmethod 
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM pets WHERE name = ? LIMIT 1;
        """

        row = CURSOR.execute(sql, (name, )).fetchone()
        if not row:
            return None 
        else:
            return cls.create_instance(row)

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
        
    @classmethod 
    def find_or_create_by(cls, name=None, age=None, species=None, owner_id = None):
        sql = """ 
            SELECT * FROM pets WHERE 
            (name, age, species, owner_id) = (?, ?, ?, ?);
        """
        row = CURSOR.execute(sql, (name, age, species, owner_id)).fetchone()
        if not row: 
            sql = """ INSERT INTO pets(name, age, species, owner_id) VALUES (?, ?, ?, ?);"""
            CURSOR.execute(sql, (name, age, species, owner_id))
            CONN.commit()
            return cls.find_by_id(CURSOR.lastrowid)
        else:
            return cls.create_instance(row)

    def update(self):
        sql = """ 
            UPDATE pets SET name = ?, age = ?, species = ?, owner_id = ? WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.age, self.species, self.owner_id, self.id))
        CONN.commit()

    @classmethod
    def get_owner_pets(cls, id):
        if(id):
            sql = """ 
                SELECT * FROM pets WHERE owner_id = ?;
            """
            return [cls.create_instance(row) for row in CURSOR.execute(sql, (id, )).fetchall()]
        else:
            return None 
        



    def __repr__(self):
        return f"<{self.id} Pet {self.name} is a {self.age} yr old {self.species}>"

