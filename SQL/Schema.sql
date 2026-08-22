Create table employees 
(employee_id varchar(12) Primary Key,
 last_name varchar(255)not null,
 first_name varchar(255)not null,
 date_of_birth date ,
 hire_date date,
 department_id int (20),
 salary int(20)
);
Create table departments
(department_id int(20) Primary Key,
department_name varchar(255) not null,
location varchar(255),
budget int(20)
);
Create table customers
(customer_id bigint Primary Key,
last_name varchar(255)not null,
first_name varchar(255)not null,
date_of_birth date,
email_address varchar(255),
phone_number varchar(250)
);
Create table orders
(order_id varchar(255) Primary Key, 
order_date date,
customer_id bigint,
employee_id varchar(12)
);
Create table order_items
(order_item_id varchar(16) Primary Key,
order_id varchar(255),
product_id varchar(12),
quantity int,
unit_price int
);
Create table products
(product_id int(12) Primary Key, 
product_name varchar(255),
supplier_id varchar(250),
unit_price int
);
Create table suppliers
(supplier_id varchar(250) Primary Key, 
supplier_name varchar(255),
start_of_contract date,
end_of_contract date
);
Create table warehouse
(warehouse_id varchar(12) Primary Key, 
location varchar(255)
);

create table warehouse_stock(
warehouse_id varchar(12),
product_id varchar(12),
stock_quantity int,
primary key(warehouse_id,product_id),
foreign key(warehouse_id)
	references warehouse(warehouse_id),
foreign key(product_id)
	references products(product_id)
);


ALTER TABLE employees
ADD CONSTRAINT fk_department_assign
FOREIGN KEY (department_id)
REFERENCES departments(department_id);
alter table products
add constraint fk_supplier_assignment
foreign key(supplier_id)
references suppliers(supplier_id);

alter table warehouse_stock
add constraint fk_product_assignemnt
foreign key(product_id)
references products(product_id);

alter table warehouse_stock
add constraint fk_warehouse_assignemnt
foreign key(warehouse_id)
references warehouse(warehouse_id);

alter table orders
add constraint fk_cust_assignment
foreign key(customer_id)
references customers(customer_id);

alter table orders
add constraint fk_emp_assignment
foreign key(employee_id)
references employees(employee_id);

alter table order_items
add constraint fk_pd_assignment
foreign key(product_id)
references products(product_id);

alter table order_items
add constraint fk_ord_assignment
foreign key(order_id)
references orders(order_id);