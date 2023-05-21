--SQL-команды для создания таблиц

CREATE TABLE customers_data
(
	customer_id	varchar(100),
	company_name varchar(100),
	contact_name varchar(100)
)

CREATE TABLE employees_data
(
	first_name	varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date date,
	notes varchar(10000)
)

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(100),
	employee_id int,
	order_date date,
	ship_city varchar(50)
)
