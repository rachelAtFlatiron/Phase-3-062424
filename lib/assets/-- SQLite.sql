-- SQLite
-- ✅ 1. Select specific columns

-- ✅ 2. Create new database structure
DROP TABLE IF EXISTS pets;
-- ✅ 2a. Remove owners table

-- ✅ 2b. Create owners table
CREATE TABLE owners(
    id INTEGER PRIMARY KEY,
    name TEXT
);

-- ✅ 2c. Create pets table
CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    breed TEXT
);

CREATE TABLE appointments(
    id INTEGER PRIMARY KEY,
    procedure TEXT,
    owner_id INTEGER,
    pet_id INTEGER,
    FOREIGN KEY(owner_id) REFERENCES owners(id),
    FOREIGN KEY(pet_id) REFERENCES pets(id)
);

-- CREATE
INSERT INTO owners (name) VALUES ('Alice Johnson');
INSERT INTO owners (name) VALUES ('Bob Smith');
INSERT INTO owners (name) VALUES ('Charlie Brown');
INSERT INTO owners (name) VALUES ('Diana Ross');
INSERT INTO owners (name) VALUES ('Edward Norton');
INSERT INTO owners (name) VALUES ('Fiona Gallagher');
INSERT INTO owners (name) VALUES ('George Washington');
INSERT INTO owners (name) VALUES ('Hannah Montana');
INSERT INTO owners (name) VALUES ('Isaac Newton');
INSERT INTO owners (name) VALUES ('Jessica Alba');


-- READ 
SELECT name FROM owners;

-- UPDATE 
UPDATE owners SET name='Billy' WHERE id=1;

-- DELETE 
DELETE FROM owners WHERE id=1;



INSERT INTO pets (name, age, breed) VALUES ('Bella', 1, 'Labrador');
INSERT INTO pets (name, age, breed) VALUES ('Max', 2, 'Beagle');
INSERT INTO pets (name, age, breed) VALUES ('Charlie', 3, 'Poodle');
INSERT INTO pets (name, age, breed) VALUES ('Lucy', 4, 'Bulldog');
INSERT INTO pets (name, age, breed) VALUES ('Molly', 5, 'Siamese');
INSERT INTO pets (name, age, breed) VALUES ('Daisy', 6, 'Maine Coon');
INSERT INTO pets (name, age, breed) VALUES ('Luna', 7, 'Chihuahua');
INSERT INTO pets (name, age, breed) VALUES ('Rocky', 8, 'German Shepherd');
INSERT INTO pets (name, age, breed) VALUES ('Sadie', 9, 'Beagle');
INSERT INTO pets (name, age, breed) VALUES ('Zoe', 10, 'Cocker Spaniel');
INSERT INTO pets (name, age, breed) VALUES ('Toby', 1, 'Bichon Frise');
INSERT INTO pets (name, age, breed) VALUES ('Ginger', 2, 'Bulldog');
INSERT INTO pets (name, age, breed) VALUES ('Rusty', 3, 'Boxer');
INSERT INTO pets (name, age, breed) VALUES ('Bella', 4, 'Rottweiler');
INSERT INTO pets (name, age, breed) VALUES ('Oscar', 5, 'Pug');
INSERT INTO pets (name, age, breed) VALUES ('Riley', 6, 'Sphynx');
INSERT INTO pets (name, age, breed) VALUES ('Jack', 7, 'Great Dane');
INSERT INTO pets (name, age, breed) VALUES ('Lily', 8, 'Scottish Fold');
INSERT INTO pets (name, age, breed) VALUES ('Sam', 9, 'Shih Tzu');
INSERT INTO pets (name, age, breed) VALUES ('Maggie', 10, 'Airedale Terrier');

-- Insert 40 appointments
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Vaccination', 2, 1);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Check-up', 3, 2);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Dental Cleaning', 4, 3);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Surgery', 5, 4);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Grooming', 6, 5);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Flea Treatment', 7, 6);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Vaccination', 8, 7);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Check-up', 9, 8);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Dental Cleaning', 10, 9);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Surgery', 11, 10);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Grooming', 2, 11);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Flea Treatment', 3, 12);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Vaccination', 4, 13);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Check-up', 5, 14);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Dental Cleaning', 6, 15);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Surgery', 7, 16);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Grooming', 8, 17);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Flea Treatment', 9, 18);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Vaccination', 10, 19);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Check-up', 11, 20);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Dental Cleaning', 2, 1);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Surgery', 3, 2);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Grooming', 4, 3);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Flea Treatment', 5, 4);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Vaccination', 6, 5);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Check-up', 7, 6);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Dental Cleaning', 8, 7);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Surgery', 9, 8);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Grooming', 10, 9);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Flea Treatment', 11, 10);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Vaccination', 2, 11);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Check-up', 3, 12);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Dental Cleaning', 4, 13);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Surgery', 5, 14);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Grooming', 6, 15);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Flea Treatment', 7, 16);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Vaccination', 8, 17);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Check-up', 9, 18);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Dental Cleaning', 10, 19);
INSERT INTO appointments (procedure, owner_id, pet_id) VALUES ('Surgery', 11, 20);
-- ✅ 3. Modify pets table
-- <columns> FROM <table> JOIN <other table> ON <criteria>
-- SELECT breed, owner_id FROM pets;
-- SELECT pets.breed, pets.age, pets.name AS pet_name, owners.id, owners.name AS owner_name FROM pets JOIN owners ON pets.owner_id=owners.id WHERE pets.age < 5 OR pets.age > 8 LIMIT 5;

-- one to many (appointments and pets) 
-- appointment belongs to an owner (it has one and only one owner)
-- owner has many appointments 
SELECT pets.name, pets.breed, appointments.procedure FROM pets JOIN appointments ON pets.id=appointments.pet_id;

-- many to many (through appointments)
SELECT pets.name, owners.name, appointments.procedure FROM pets JOIN appointments ON pets.id=appointments.pet_id JOIN owners ON owners.id=appointments.owner_id;

-- count the number of appointments per owner 
SELECT owners.name AS owner_name,
COUNT(appointments.id) AS num_appts 
FROM 
owners JOIN appointments ON owners.id=appointments.owner_id GROUP BY owners.id;


-- join, limit, where, count, min, max, avg, sum, order by, group by, 
-- create: INSERT, update: UPDATE...WHERE..., delete: DELETE...WHERE..., read: SELECT
-- one-to-many: 1 join
-- many-to-many: 2 joins 