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

CREATE TABLE Arxiv_items (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    produced_time DATE NOT NULL,
    end_time DATE NOT NULL,
    expiration_date INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    count INT NOT NULL
);



SELECT * FROM Medicine_items;


INSERT INTO Medicine_items (name, produced_time, end_time, expiration_date, price, count)
VALUES ('Aspirin', '2022-01-01', '2021-01-01', 1, 5000, 100),  
       ('Paracetamol', '2021-02-15', '2024-02-15', 1, 8000, 200),  
       ('Ibuprofen', '2024-03-10', '2026-03-10', 2, 12000, 150),  
       ('Amoxicillin', '2021-04-05', '2023-04-05', 3, 15000, 120),  
       ('Cough Syrup', '2024-05-20', '2027-05-20', 3, 9500, 80),  
       ('Vitamin C', '2024-06-25', '2027-06-25', 3, 6500, 250),  
       ('Antihistamine', '2024-07-15', '2028-07-15', 4, 17000, 90),  
       ('Antibiotic A', '2024-08-01', '2027-08-01', 3, 20000, 110),  
       ('Antibiotic B', '2024-08-20', '2028-08-20', 4, 22000, 130),  
       ('Pain Relief', '2024-09-10', '2026-09-10', 2, 13000, 160),  
       ('Fever Reducer', '2024-10-01', '2025-10-01', 1, 12000, 140),  
       ('Anti-inflammatory', '2024-10-15', '2027-10-15', 3, 18000, 130),  
       ('Antiseptic', '2024-11-01', '2027-11-01', 3, 25000, 110),  
       ('Allergy Relief', '2024-11-15', '2026-11-15', 2, 14000, 120),  
       ('Antacid', '2024-12-01', '2025-12-01', 1, 750, 1700),  
       ('Cold Medicine', '2024-12-10', '2026-12-10', 2, 10000, 100),  
       ('Sleep Aid', '2024-12-20', '2027-12-20', 3, 28000, 80),  
       ('Stomach Relief', '2024-12-25', '2026-12-25', 2, 17000, 90),  
       ('Heartburn Relief', '2025-01-10', '2026-01-10', 1, 20000, 110),  
       ('Headache Relief', '2025-01-15', '2027-01-15', 2, 25000, 130),  
       ('Digestive Aid', '2025-02-01', '2026-02-01', 1, 8000, 140),  
       ('Skin Cream', '2025-02-10', '2027-02-10', 2, 16000, 100),  
       ('Eye Drops', '2025-03-01', '2026-03-01', 1, 9500, 120),  
       ('Ear Drops', '2025-03-10', '2027-03-10', 2, 12000, 80),  
       ('Nasal Spray', '2025-04-01', '2026-04-01', 1, 15000, 90),  
       ('Throat Lozenges', '2025-04-15', '2027-04-15', 2, 8500, 130),  
       ('Antiviral', '2025-05-01', '2027-05-01', 2, 30000, 70),  
       ('Antifungal', '2025-05-15', '2028-05-15', 3, 28000, 110),
       ('Anti-parasitic', '2025-06-01', '2028-06-01', 3, 26000, 90),  
       ('Anti-viral', '2025-06-15', '2029-06-15', 4, 35000, 120),  
       ('Hemorroid Cream', '2025-07-01', '2027-07-01', 2, 19000, 85),  
       ('Acne Treatment', '2025-07-10', '2028-07-10', 3, 20000, 95),  
       ('Mouthwash', '2025-08-01', '2026-08-01', 1, 11000, 150),  
       ('Cough Drops', '2025-08-15', '2026-08-15', 1, 8000, 110),  
       ('Hair Growth', '2025-09-01', '2028-09-01', 3, 30000, 100),  
       ('Dandruff Shampoo', '2025-09-10', '2027-09-10', 2, 17000, 90),  
       ('Foot Cream', '2025-10-01', '2027-10-01', 2, 12000, 80),  
       ('Wound Ointment', '2025-10-15', '2028-10-15', 3, 22000, 120);  




-- Muddati o'tkan mahsulotlar

INSERT INTO Medicine_items (name, produced_time, end_time, expiration_date, price, count)
VALUES ('Aspiri', '2022-01-01', '2021-01-01', 1, 5000, 100),  
       ('Paracetamo', '2021-02-15', '2024-02-15', 1, 8000, 200),  
       ('Ibupro', '2024-03-10', '2024-04-10', 2, 12000, 150),  
       ('Amoxicilin', '2021-04-05', '2023-04-05', 3, 15000, 120),  
       ('Cough Sy', '2024-05-20', '2024-06-20', 3, 9500, 80);  