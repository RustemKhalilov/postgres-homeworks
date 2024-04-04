-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employee_id CHARACTER VARYING(30),
    first_name CHARACTER VARYING(100),
    last_name CHARACTER VARYING(100),
    birth_date CHARACTER VARYING(100),
    title CHARACTER VARYING(100),
	notes text
);

CREATE TABLE customers
(
    customer_id CHARACTER VARYING(30),
    company_name CHARACTER VARYING(100),
    contact_name CHARACTER VARYING(100)
);

CREATE TABLE orders
(
    order_id CHARACTER VARYING(30),
    customer_id CHARACTER VARYING(100),
    employee_id CHARACTER VARYING(100),
	order_date CHARACTER VARYING(100),
    ship_city CHARACTER VARYING(100)
);


