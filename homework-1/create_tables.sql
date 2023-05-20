--SQL-команды для создания таблиц

CREATE TABLE customers_data
(
	id int PRIMARY KEY,
	customer_id	varchar(50),
	company_name varchar(50),
	contact_name varchar(100)
)

CREATE TABLE employees_data
(
	employees_id int PRIMARY KEY,
	first_name	varchar(50),
	last_name varchar(50),
	title varchar(100),
	birth_date date,
	notes varchar(10000)
)

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(50),
	employee_id int,
	order_date date,
	ship_city varchar(50)
)
