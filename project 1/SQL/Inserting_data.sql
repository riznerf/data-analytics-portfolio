insert into warehouse
(warehouse_id,location)
values
('WH001', 'Dallas Central HUB'),
('WH002', 'Dallas Overflow Depot'),
('WH003', 'Dallas Cold Storage');

insert into departments (department_id,department_name,location,budget)
values
(1,'IT','New York',12000000),
(2,'HR','Chichago',3500000),
(3,'Finance','Boston',8000000),
(4,'Sales','Los Angeles',10000000),
(5,'Logistics','Dallas',6500000),
(6,'Procurement','Seattle',5000000);

UPDATE employees
SET employee_id = CONCAT('EMP', LPAD(employee_id, 4, '0'));