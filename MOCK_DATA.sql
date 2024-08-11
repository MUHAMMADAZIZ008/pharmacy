CREATE DATABASE pharmacy;

USE pharmacy;

CREATE TABLE Medicine_items(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) UNIQUE,
    produced_time DATE,
    end_time DATE,
    expiration_date INT,
    price INT,
    count INT
);

INSERT INTO Medicine_items(name, produced_time, end_time, expiration_date, price, count) VALUES
("Parasetamol", '2023.05.03', '2027.05.03', 4, 5000, 120),
("Trimol", '2022.09.01', '2025.09.01', 3, 12400, 120);


CREATE TABLE Admins_data (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(32) UNIQUE,
    password VARCHAR(32)
);

INSERT INTO Admins_data (username, password) VALUES
("Sirojiddin", "Medical123"),
("Muhammadaziz", "Shifo123");

CREATE TABLE Users_data(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(32) UNIQUE,
    password VARCHAR(32),
    phone_number VARCHAR(15) UNIQUE
);



SELECT * FROM Medicine_items;


INSERT INTO Medicine_items (name, produced_time, end_time, expiration_date, price, count)
VALUES ('Aspirin', '2022-01-01', '2021-01-01', 1, 500, 100),  -- Saqlash muddati 1 yil
       ('Paracetamol', '2021-02-15', '2024-02-15', 1, 800, 200),  -- Saqlash muddati 1 yil
       ('Ibuprofen', '2024-03-10', '2026-03-10', 2, 1200, 150),  -- Saqlash muddati 2 yil
       ('Amoxicillin', '2021-04-05', '2023-04-05', 3, 1500, 120),  -- Saqlash muddati 3 yil
       ('Cough Syrup', '2024-05-20', '2027-05-20', 3, 950, 80),  -- Saqlash muddati 3 yil
       ('Vitamin C', '2024-06-25', '2027-06-25', 3, 650, 250),  -- Saqlash muddati 3 yil
       ('Antihistamine', '2024-07-15', '2028-07-15', 4, 1700, 90),  -- Saqlash muddati 4 yil
       ('Antibiotic A', '2024-08-01', '2027-08-01', 3, 2000, 110),  -- Saqlash muddati 3 yil
       ('Antibiotic B', '2024-08-20', '2028-08-20', 4, 2200, 130),  -- Saqlash muddati 4 yil
       ('Pain Relief', '2024-09-10', '2026-09-10', 2, 1300, 160),  -- Saqlash muddati 2 yil
       ('Fever Reducer', '2024-10-01', '2025-10-01', 1, 1200, 140),  -- Saqlash muddati 1 yil
       ('Anti-inflammatory', '2024-10-15', '2027-10-15', 3, 1800, 130),  -- Saqlash muddati 3 yil
       ('Antiseptic', '2024-11-01', '2027-11-01', 3, 2500, 110),  -- Saqlash muddati 3 yil
       ('Allergy Relief', '2024-11-15', '2026-11-15', 2, 1400, 120),  -- Saqlash muddati 2 yil
       ('Antacid', '2024-12-01', '2025-12-01', 1, 750, 170),  -- Saqlash muddati 1 yil
       ('Cold Medicine', '2024-12-10', '2026-12-10', 2, 1000, 100),  -- Saqlash muddati 2 yil
       ('Sleep Aid', '2024-12-20', '2027-12-20', 3, 2800, 80),  -- Saqlash muddati 3 yil
       ('Stomach Relief', '2024-12-25', '2026-12-25', 2, 1700, 90),  -- Saqlash muddati 2 yil
       ('Heartburn Relief', '2025-01-10', '2026-01-10', 1, 2000, 110),  -- Saqlash muddati 1 yil
       ('Headache Relief', '2025-01-15', '2027-01-15', 2, 2500, 130),  -- Saqlash muddati 2 yil
       ('Digestive Aid', '2025-02-01', '2026-02-01', 1, 800, 140),  -- Saqlash muddati 1 yil
       ('Skin Cream', '2025-02-10', '2027-02-10', 2, 1600, 100),  -- Saqlash muddati 2 yil
       ('Eye Drops', '2025-03-01', '2026-03-01', 1, 950, 120),  -- Saqlash muddati 1 yil
       ('Ear Drops', '2025-03-10', '2027-03-10', 2, 1200, 80),  -- Saqlash muddati 2 yil
       ('Nasal Spray', '2025-04-01', '2026-04-01', 1, 1500, 90),  -- Saqlash muddati 1 yil
       ('Throat Lozenges', '2025-04-15', '2027-04-15', 2, 850, 130),  -- Saqlash muddati 2 yil
       ('Antiviral', '2025-05-01', '2027-05-01', 2, 3000, 70),  -- Saqlash muddati 2 yil
       ('Antifungal', '2025-05-15', '2028-05-15', 3, 2800, 110),  -- Saqlash muddati 3 yil
       ('Anti-parasitic', '2025-06-01', '2028-06-01', 3, 2600, 90),  -- Saqlash muddati 3 yil
       ('Anti-viral', '2025-06-15', '2029-06-15', 4, 3500, 120),  -- Saqlash muddati 4 yil
       ('Hemorroid Cream', '2025-07-01', '2027-07-01', 2, 1900, 85),  -- Saqlash muddati 2 yil
       ('Acne Treatment', '2025-07-10', '2028-07-10', 3, 2000, 95),  -- Saqlash muddati 3 yil
       ('Mouthwash', '2025-08-01', '2026-08-01', 1, 1100, 150),  -- Saqlash muddati 1 yil
       ('Cough Drops', '2025-08-15', '2026-08-15', 1, 800, 110),  -- Saqlash muddati 1 yil
       ('Hair Growth', '2025-09-01', '2028-09-01', 3, 3000, 100),  -- Saqlash muddati 3 yil
       ('Dandruff Shampoo', '2025-09-10', '2027-09-10', 2, 1700, 90),  -- Saqlash muddati 2 yil
       ('Foot Cream', '2025-10-01', '2027-10-01', 2, 1200, 80),  -- Saqlash muddati 2 yil
       ('Wound Ointment', '2025-10-15', '2028-10-15', 3, 2200, 120);  -- Saqlash muddati 3 yil






-- Muddati o'tkan mahsulotlar

INSERT INTO Medicine_items (name, produced_time, end_time, expiration_date, price, count)
VALUES ('Aspiri', '2022-01-01', '2021-01-01', 1, 500, 100),  -- Saqlash muddati 1 yil
       ('Paracetamo', '2021-02-15', '2024-02-15', 1, 800, 200),  -- Saqlash muddati 1 yil
       ('Ibuprofn', '2024-03-10', '2026-03-10', 2, 1200, 150),  -- Saqlash muddati 2 yil
       ('Amoxicilin', '2021-04-05', '2023-04-05', 3, 1500, 120),  -- Saqlash muddati 3 yil
       ('Cough Syup', '2024-05-20', '2027-05-20', 3, 950, 80);  -- Saqlash muddati 3 yil