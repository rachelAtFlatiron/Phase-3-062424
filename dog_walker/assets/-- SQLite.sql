-- SQLite
-- ✅ 1. Select specific columns
-- SELECT id, name, address, email, phone
-- FROM owners;

-- SELECT name, address, email, phone
-- FROM owners;

-- 🛑 ctrl+click on dog_walker in SQLite Explorer to view SQL to create table

-- ✅ 2. Create new database structure
-- ✅ 2a. Remove owners table
DROP TABLE IF EXISTS owners ;
DROP TABLE IF EXISTS pets ;
DROP TABLE IF EXISTS appointments ;
DROP TABLE IF EXISTS staff ;
-- ✅ 2b. Create owners table
-- 🛑 Owner table corresponds to Python Owner class
CREATE TABLE owners(
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    email TEXT,
    phone INTEGER
);
-- ✅ 2c. Create pets table
-- 💡 where will the FK go between owner and pets?
CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    name TEXT,
    owner_id INTEGER, 
    birthdate INTEGER,
    breed TEXT,
    favorite_treats TEXT,
    last_fed_at DATETIME, -- includes hour and minute
    last_walked_at DATETIME,
        FOREIGN KEY (owner_id) REFERENCES owners(id)
);

-- ✅ 3. Modify pets table

-- ✅ 3a. Add image_url to pets
ALTER TABLE pets 
ADD COLUMN image_url TEXT;


-- ✅ 3b. Rename column
-- 🛑 sqlite cannot alter the datatype of a column
ALTER TABLE pets
RENAME COLUMN birthdate TO age; 

-- ✅ 4. Create new instances

INSERT INTO owners(name, address, email, phone)
VALUES ('Louis', '123 Street', 'myemail@gmail.com', '555-555-5555');


-- ✅ 4a. Use chatGPT to create random owners
-- ^ "given an sql table 'owners' with columns 'name' (text), 'address' (text), 'email' (text), 'phone' (text) create 5 instances with dummy data"

-- Inserting the first owner
INSERT INTO owners (name, address, email, phone)
VALUES ('John Doe', '123 Main Street, Cityville', 'john.doe@email.com', '555-123-4567');

-- Inserting the second owner
INSERT INTO owners (name, address, email, phone)
VALUES ('Jane Smith', '456 Elm Avenue, Townsville', 'jane.smith@email.com', '555-987-6543');

-- Inserting the third owner
INSERT INTO owners (name, address, email, phone)
VALUES ('Robert Johnson', '789 Oak Lane, Villageton', 'robert.johnson@email.com', '555-555-5555');

-- Inserting the fourth owner
INSERT INTO owners (name, address, email, phone)
VALUES ('Emily Davis', '101 Pine Road, Hamletville', 'emily.davis@email.com', '555-777-8888');

-- Inserting the fifth owner
INSERT INTO owners (name, address, email, phone)
VALUES ('Michael Wilson', '222 Cedar Street, Suburbia', 'michael.wilson@email.com', '555-444-3333');

-- ✅ 4b. Use chat GPT to create sample data for pets

-- Sample data for cats
INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Whiskers', 5, 1, 'Siamese', 'Tuna', '2023-08-30 09:00:00', NULL, 'https://example.com/whiskers.jpg');

INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Fluffy', 3, 2, 'Persian', 'Salmon', '2023-08-29 18:30:00', NULL, 'https://example.com/fluffy.jpg');

-- Sample data for dogs
INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Buddy', 2, 3, 'Golden Retriever', 'Biscuits', '2023-08-30 07:45:00', '2023-08-30 16:00:00', 'https://example.com/buddy.jpg');

INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Max', 4, 4, 'German Shepherd', 'Peanut Butter', '2023-08-29 19:15:00', '2023-08-29 20:30:00', 'https://example.com/max.jpg');

-- Adding two more cats
INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Smokey', 2, 4, 'Russian Blue', 'Catnip', '2023-08-30 10:15:00', NULL, 'https://example.com/smokey.jpg');

INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Luna', 1, 3, 'Scottish Fold', 'Tuna', '2023-08-29 20:45:00', NULL, 'https://example.com/luna.jpg');

-- Adding two birds
INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Rio', 1, 1, 'Parrot', 'Sunflower Seeds', '2023-08-30 08:30:00', NULL, 'https://example.com/rio.jpg');

INSERT INTO pets (name, age, owner_id, breed, favorite_treats, last_fed_at, last_walked_at, image_url)
VALUES ('Sunny', 3, 2, 'Canary', 'Millet', '2023-08-29 16:00:00', NULL, 'https://example.com/sunny.jpg');


-- ✅ 5. Read data

-- ✅ 5a. Get all columns from pets

SELECT * FROM pets;
-- ✅ 5b. Select pet by name
SELECT * FROM pets WHERE name = 'Luna';
-- ✅ 5c. Select pets by favorite treats
SELECT * FROM pets WHERE favorite_treats = 'Tuna';
-- ✅ 5d. Select pets by age 
SELECT * FROM pets WHERE age < 2;

-- ✅ 6. Update data
-- ✅ 6a. Update pet's age by name
UPDATE pets 
SET age = 12 
WHERE name = 'Luna';
-- ✅ 6b. Update multiple pets' favorite_treats
UPDATE pets 
SET favorite_treats = 'cheese';

-- ✅ 7. Delete data
DELETE FROM pets WHERE name = 'Luna';

-- ✅ 8. Join data 
-- ✅ 8a. One to many
SELECT pets.name, owners.name as 'owner' FROM pets 
JOIN owners ON pets.owner_id = owners.id;
-- ✅ 8b. Many to many: create staff table 
CREATE TABLE staff(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone INTEGER 
);
-- ✅ 8c. Many to many: create appointments table
CREATE TABLE appointments(
    id INTEGER PRIMARY KEY, 
    time DATETIME,
    request TEXT,
    pet_id INTEGER,
    staff_id INTEGER,
    FOREIGN KEY (staff_id) REFERENCES staff(id),
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

-- ✅ 9. Seed data

-- ✅ 9a. Create two staff members using ChatGPT?
INSERT INTO staff (name, email, phone) VALUES
    ('Alice Wonderland', 'alice.wonderland@gmail.com', 1234567890),
    ('Bob Marley', 'bob.marley@gmail.com', 9876543210);
-- ✅ 9b. Create six appointments using ChatGPT
-- Instance 1
INSERT INTO appointments (time, request, pet_id, staff_id)
VALUES ('2023-09-02 09:00:00', 'Regular checkup', 1, 101);

-- Instance 2
INSERT INTO appointments (time, request, pet_id, staff_id)
VALUES ('2023-09-02 10:30:00', 'Vaccination', 2, 1);

-- Instance 3
INSERT INTO appointments (time, request, pet_id, staff_id)
VALUES ('2023-09-03 15:15:00', 'Dental cleaning', 3, 1);

-- Instance 4
INSERT INTO appointments (time, request, pet_id, staff_id)
VALUES ('2023-09-04 11:45:00', 'Emergency visit', 4, 2);

-- Instance 5
INSERT INTO appointments (time, request, pet_id, staff_id)
VALUES ('2023-09-05 14:00:00', 'Spaying surgery', 5, 2);

-- Instance 6
INSERT INTO appointments (time, request, pet_id, staff_id)
VALUES ('2023-09-06 16:30:00', 'Grooming', 6, 2);

-- ✅ 10. Join tables
-- 🛑 inner joins: matching values in both tables
-- 🛑 outer joins: null values for columns that do not have matching row in other table
-- ✅ 10a. Basic join
SELECT 
    pets.name, 
    staff.name,
    appointments.request,
    appointments.time 
FROM appointments 
JOIN pets 
    ON appointments.pet_id = pets.id 
JOIN staff 
    ON appointments.staff_id = staff.id;

-- ✅ 10b. Basic join with specific values
SELECT 
    pets.name,
    staff.name 
FROM appointments 
JOIN pets 
    ON appointments.pet_id = pets.id 
JOIN staff 
    ON appointments.staff_id = staff.id 
AND staff.name = 'Alice Wonderland';

-- ✅ 10c. Inner join?
-- 🛑 functionally equivalent to join / inner intersection of venn diagram
SELECT pets.name, appointments.request
FROM appointments
INNER JOIN pets on pets.id = appointments.pet_id;


-- ✅ 10d. Outer join
-- 🛑 includes values that do not have any intersection (null values)
-- 🛑 left outer: all rows from left table and matching records between both tables
-- 🛑 right outer: all rows from right table and matching records between both tables
INSERT INTO staff (name, email, phone) VALUES
("Tom Riddle", "tom@hogwards.com", "7777777777");

-- 🛑 returns all rows in appointments and matching rows to staff
SELECT staff.name, appointments.request 
FROM staff
RIGHT OUTER JOIN appointments on staff.id = appointments.staff_id;

-- 🛑 Tom's appointment requests will come back NULL
-- 🛑 returns all rows in staff and matching rows to appointments
SELECT staff.name, appointments.request 
FROM staff 
LEFT OUTER JOIN appointments on staff.id = appointments.staff_id;


-- ✅ Full outer join
-- 🛑 combo of left and right joins, null values for every column that does not have matching column
INSERT INTO appointments (time, request, pet_id, staff_id)
VALUES ('2023-09-06 14:00:00', 'Grooming', 5, 2);
INSERT INTO appointments (time, request, pet_id, staff_id)
VALUES ('2023-09-07 14:00:00', 'Grooming', 5, 2);

SELECT appointments.request, pets.name 
FROM appointments 
FULL OUTER JOIN pets on appointments.pet_id = pets.id;