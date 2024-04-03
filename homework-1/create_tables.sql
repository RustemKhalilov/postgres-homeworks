-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    Id SERIAL PRIMARY KEY,
    FirstName CHARACTER VARYING(30),
    LastName CHARACTER VARYING(30),
    Email CHARACTER VARYING(30),
    Age INTEGER,
	phonework CHARACTER VARYING(30),
	phonecell CHARACTER VARYING(30),
	phonehomeaddress CHARACTER VARYING(30),
	education CHARACTER VARYING(100),
	salary REAL,
	drivers_license CHARACTER VARYING(30),
	car CHARACTER VARYING(30),
	presence_of_diseases CHARACTER VARYING(30),
	medical_policy CHARACTER VARYING(30)
);

CREATE TABLE clients
(
    Id SERIAL PRIMARY KEY,
    FirstName CHARACTER VARYING(30),
    LastName CHARACTER VARYING(30),
    Email CHARACTER VARYING(30),
	phone CHARACTER VARYING(30),
	home_address CHARACTER VARYING(30),
	number_order_history_delivery CHARACTER VARYING(500),
    bonus_point INTEGER
);

CREATE TABLE orders
(
    Id SERIAL PRIMARY KEY,
    order_number CHARACTER VARYING(30),
    order_time CHARACTER VARYING(30),
	addrees CHARACTER VARYING(30),
    Email CHARACTER VARYING(30),
	order_composition CHARACTER VARYING(30),
	receipt_number CHARACTER VARYING(30),
	Payment_method CHARACTER VARYING(30)
);
