CREATE DATABASE pharmacy;

USE pharmacy;

CREATE TABLE Medicine_items(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) UNIQUE,
    produced_time DATE,
    end_time DATE,
    expiration_date float,
    price INT,
    count INT
);

INSERT INTO Medicine_items(name, produced_time, end_time, expiration_date, price, count) VALUES
("Parasetamol", '2023.05.03', '2027.05.03', 4, 5000, 120),
("Trimol", '2022.09.01', '2025.09.01', 3, 12400, 120);


CREATE TABLE Admins_data (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(32) UNIQUE,
    password VARCHAR(32), 
);

INSERT INTO Admins_data (username, password) VALUES
("Sirojiddin", "Medical123"),
("Muhammadaziz", "Shifo123");

CREATE TABLE Users_data(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(32) UNIQUE,
    password VARCHAR(32),
    phone_number VARCHAR(15)
);

SELECT * FROM Medicine_items;