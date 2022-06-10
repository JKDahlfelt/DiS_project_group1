drop table if exists Drinks cascade;
drop table if exists Bars cascade;
-- drop table if exists Customers cascade;
drop table if exists SoldDrinks;


CREATE TABLE IF NOT EXISTS Drinks (
	rest_id int,
	d_id int,
	d_type varchar,
 	volume float,
 	maker varchar,
 	d_Name varchar,
 	price float,
 	PRIMARY KEY (rest_id, d_id)
);


CREATE TABLE IF NOT EXISTS Bars (
 	rest_id int,
 	bar_name varchar,
 	bar_type varchar,
 	age int,
 	website varchar,
 	addr varchar,
 	postal int,
 	PRIMARY KEY (rest_id)
);


CREATE TABLE IF NOT EXISTS SoldDrinks (
 	bar_id int REFERENCES Bars(Rest_id),
 	drink_id int,
 	qty_sold int,
 	FOREIGN KEY (bar_id, drink_id) REFERENCES Drinks(Rest_id, D_id) ON DELETE CASCADE
);

ALTER TABLE SoldDrinks ADD CONSTRAINT pk_SoldDrinks
	PRIMARY KEY (bar_id, drink_id);

COPY Drinks FROM 'C:\Users\Johannes\CBS_projects\data\out\drinks.csv' DELIMITER ',' CSV Header;
COPY Bars FROM 'C:\Users\Johannes\CBS_projects\data\out\bars.csv' DELIMITER ',' CSV Header;
COPY SoldDrinks FROM 'C:\Users\Johannes\CBS_projects\data\out\solddrinks.csv' DELIMITER ',' CSV Header;

ALTER TABLE Drinks
ADD Column halfliter_price float;

-- -- Calculates the price per liter for each beer at a given bar
UPDATE Drinks
set halfliter_price = (price::float / volume::float)/2.0
WHERE  (rest_id, d_id) = (rest_id, d_id);