from pet import Pet, CONN, CURSOR
from owner import Owner, CONN, CURSOR

# Pet : name: string species: string breed: string temperament:string, owner_id:int
# Owner: name: string, phone: string, email: string, address: string

class TestPet:
    '''Class Pet in pet.py'''

    def test_has_all_attributes(self):
        '''initializes with name, species, breed, temperament, and owner_id.'''
        pet = Pet(name="spot", species="dog", breed="chihuahua", temperament="feisty", owner_id=1)
        assert(pet.name == "spot" and pet.species == "dog" and pet.breed == "chihuahua" and pet.temperament == "feisty" and pet.owner_id == 1)

    def test_creates_table(self):
        '''contains method "create_table()" that creates table "dogs" if it does not exist.'''
        CURSOR.execute("DROP TABLE IF EXISTS pets")
        Pet.create_table()
        assert(CURSOR.execute("SELECT * FROM pets"))

    def test_drops_table(self):
        '''contains method "drop_table()" that drops table "dogs" if it exists.'''
        sql = """
            CREATE TABLE IF NOT EXISTS pets
                (id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEST,
                owner_id INTEGER)
        """
        CURSOR.execute(sql)
        Pet.drop_table()

        sql_table_names = """
            SELECT name FROM sqlite_master
            WHERE type='table'
            ORDER BY name
        """
        assert(len(CURSOR.execute(sql_table_names).fetchall()) == 0)

    # def test_saves_pet(self):
    #     '''contains method "save()" that saves a Pet instance to the database.'''
    #     Pet.drop_table()
    #     Pet.create_table()
    #     spot = Pet("spot", "dog", "chihuahua", "feisty", 1)
    #     spot.save()

    #     sql = """
    #         SELECT * FROM pets
    #         WHERE name='spot'
    #         LIMIT 1
    #     """
    #     assert(CURSOR.execute(sql).fetchone() == ("spot", "dog", "chihuahua", "feisty", 1))

    # def test_creates_dog(self):
    #     '''contains method "create()" that creates a new row in the database and returns a Dog instance.'''
    #     Dog.drop_table()
    #     Dog.create_table()
    #     joey = Dog.create("joey", "cocker spaniel")
    #     assert((joey.id, joey.name, joey.breed) == (1, "joey", "cocker spaniel"))

    # def test_creates_new_instance_from_db(self):
    #     '''contains method "new_from_db()" that takes a database row and creates a Dog instance.'''
    #     Dog.drop_table()
    #     Dog.create_table()
    #     sql = """
    #         INSERT INTO dogs (name, breed)
    #         VALUES ('joey', 'cocker spaniel')
    #     """
    #     CURSOR.execute(sql)
    #     sql = """
    #         SELECT * FROM dogs
    #         WHERE name='joey'
    #         LIMIT 1
    #     """
    #     row = CURSOR.execute(sql).fetchone()
    #     joey = Dog.new_from_db(row)
    #     assert((joey.id, joey.name, joey.breed) == (1, "joey", "cocker spaniel"))

    # def test_gets_all(self):
    #     '''contains method "get_all()" that returns a list of Dog instances for every record in the database.'''
    #     Dog.drop_table()
    #     Dog.create_table()
    #     Dog.create("joey", "cocker spaniel")
    #     Dog.create("fanny", "cockapoo")

    #     dogs = Dog.get_all()
    #     assert(
    #         (dogs[0].id, dogs[0].name, dogs[0].breed) == \
    #             (1, "joey", "cocker spaniel") \
    #         and (dogs[1].id, dogs[1].name, dogs[1].breed) == \
    #             (2, "fanny", "cockapoo")
    #     )

    # def test_finds_by_name(self):
    #     '''contains method "find_by_name()" that returns a Dog instance corresponding to its database record retrieved by name.'''
    #     Dog.drop_table()
    #     Dog.create_table()
    #     Dog.create("joey", "cocker spaniel")

    #     joey = Dog.find_by_name("joey")
    #     assert(
    #         (joey.id, joey.name, joey.breed) == \
    #             (1, "joey", "cocker spaniel")
    #     )

    # def test_finds_by_id(self):
    #     '''contains method "find_by_id()" that returns a Dog instance corresponding to its database record retrieved by id.'''
    #     Dog.drop_table()
    #     Dog.create_table()
    #     Dog.create("joey", "cocker spaniel")

    #     joey = Dog.find_by_id(1)
    #     assert(
    #         (joey.id, joey.name, joey.breed) == \
    #             (1, "joey", "cocker spaniel")
    #     )

    # def test_finds_by_name_and_breed(self):
    #     '''contains method "find_or_create_by()" that takes a name and a breed as arguments and returns a Dog instance matching that record.'''
    #     Dog.drop_table()
    #     Dog.create_table()
    #     Dog.create("joey", "cocker spaniel")

    #     joey = Dog.find_or_create_by("joey", "cocker spaniel")
    #     assert(
    #         (joey.id, joey.name, joey.breed) == \
    #             (1, "joey", "cocker spaniel")
    #     )

    # def test_finds_by_name_and_breed(self):
    #     '''contains method "find_or_create_by()" that takes a name and a breed as arguments and creates a Dog instance matching that record if it does not exist.'''
    #     Dog.drop_table()
    #     Dog.create_table()

    #     joey = Dog.find_or_create_by("joey", "cocker spaniel")
    #     assert(
    #         (joey.id, joey.name, joey.breed) == \
    #             (1, "joey", "cocker spaniel")
    #     )

    # def test_saves_with_id(self):
    #     '''contains a method "save()" that saves a Dog instance to the database and returns a Dog instance with id.'''
    #     Dog.drop_table()
    #     Dog.create_table()
    #     joey = Dog("joey", "cocker spaniel")
    #     joey.save()
    #     assert(
    #         (joey.id, joey.name, joey.breed) == \
    #             (1, "joey", "cocker spaniel")
    #     )
    
    # def test_updates_record(self):
    #     '''contains a method "update()" that updates an instance's corresponding database record to match its new attribute values.'''
    #     Dog.drop_table()
    #     Dog.create_table()
    #     joey = Dog.create("joey", "cocker spaniel")
    #     joey.name = "joseph"
    #     joey.update()

    #     assert(Dog.find_by_id(1).name == "joseph" \
    #         and Dog.find_by_name("joey") == None)