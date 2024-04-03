-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    Id SERIAL PRIMARY KEY,
    FirstName CHARACTER VARYING(100),
    LastName CHARACTER VARYING(100),
    Email CHARACTER VARYING(100),
    Age INTEGER,
	phonework CHARACTER VARYING(100),
	phonecell CHARACTER VARYING(100),
	homeaddress CHARACTER VARYING(100),
	education CHARACTER VARYING(100),
	salary REAL,
	drivers_license CHARACTER VARYING(100),
	car CHARACTER VARYING(30),
	presence_of_diseases CHARACTER VARYING(100),
	medical_policy CHARACTER VARYING(100)
);

CREATE TABLE clients
(
    Id SERIAL PRIMARY KEY,
    FirstName CHARACTER VARYING(100),
    LastName CHARACTER VARYING(100),
    Email CHARACTER VARYING(100),
	phone CHARACTER VARYING(100),
	home_address CHARACTER VARYING(100),
	number_order_history_delivery CHARACTER VARYING(500),
	bonus_point INTEGER
);

CREATE TABLE orders
(
    Id SERIAL PRIMARY KEY,
    order_number CHARACTER VARYING(100),
    order_time CHARACTER VARYING(100),
	addrees CHARACTER VARYING(100),
    Email CHARACTER VARYING(100),
	order_composition CHARACTER VARYING(100),
	receipt_number CHARACTER VARYING(100),
	payment_method CHARACTER VARYING(100)

);


