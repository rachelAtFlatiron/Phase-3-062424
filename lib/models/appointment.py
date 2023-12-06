#join table between pets and procedures
import sqlite3 

CONN = sqlite3.connect('resources.db', timeout=10) 
CURSOR = CONN.cursor()

class Appointment:

    def __init__(self, pet_id=None, procedure_id=None, id=None):
        self.pet_id = pet_id 
        self.procedure_id = procedure_id
        self.id = id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS appointments 
            (
                id INTEGER PRIMARY KEY,
                pet_id INTEGER,
                procedure_id INTEGER,
                FOREIGN KEY (pet_id) REFERENCES pets(id),
                FOREIGN KEY (procedure_id) REFERENCES procedures(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql=""" 
            DROP TABLE IF EXISTS appointments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        try: 
            sql = """ 
                INSERT INTO appointments(pet_id, procedure_id)
                VALUES (?, ?);
            """
            CURSOR.execute(sql, (self.pet_id, self.procedure_id))
            find_sql = """ SELECT id FROM appointments WHERE id = ?;"""
            self.id = CURSOR.execute(find_sql, (CURSOR.lastrowid,)).fetchone()[0]
            CONN.commit()
        except Exception as e:
            print(f'something went wrong: {e}')

    @classmethod 
    def create(cls, pet_id, procedure_id):
        app = cls(pet_id, procedure_id)
        app.save()
        return app 
    
    @classmethod 
    def create_instance(cls, row):
        app = cls(
            id=row[0],
            pet_id=row[1],
            procedure_id=row[2]
        )
        return app 
    
    @classmethod 
    def get_all(cls):
        sql = """ SELECT * FROM APPOINTMENTS; """
        return [cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]
        

    @classmethod 
    def find_by_id(cls, id):
        sql = """ SELECT * FROM APPOINTMENTS WHERE id = ?;"""
        row = CURSOR.execute(sql, (id, )).fetchone() 
        if not row:
            return None 
        else: 
            return cls.create_instance(row)
        
    @classmethod 
    def get_owner_apps(cls, id):
        sql = """ 
            SELECT appointments.id, pet_id, procedure_id FROM appointments JOIN pets ON appointments.pet_id = pets.id WHERE pets.owner_id = ?;
        """
        return[cls.create_instance(row) for row in CURSOR.execute(sql, (id, )).fetchall()]
    
    @classmethod
    def get_pet_apps(cls, id):
        sql = """ 
            SELECT appointments.id, pet_id, procedure_id FROM appointments JOIN pets ON appointments.pet_id = pets.id WHERE pets.id = ?;
        """
        return[cls.create_instance(row) for row in CURSOR.execute(sql, (id, )).fetchall()]
        
    def __repr__(self):
        return f'''<Appointment for {self.pet_id}: {self.procedure_id}>'''
    