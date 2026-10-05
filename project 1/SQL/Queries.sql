-- Total revenue
select sum(quantity*unit_price) as total_revenue
from order_items;

-- Units Sold by Product
select product_id,
sum(quantity) as units_sold
from order_items
group by product_id
order by units_sold Desc;

-- Monthly Order
Select
Year(order_date) as year,
month(order_date) as month,
count(*) as order_count
from orders
group by year(order_date), month(order_date)
order by year,month;

-- Revenue by Product

select p.product_name, sum(oi.quantity*oi.unit_price)as revenue from order_items oi
join products p on oi.product_id=p.product_id
group by p.product_id,p.product_name
order by revenue desc;

-- Revenue by Employee
select e.employee_id,e.first_name, e.last_name,sum(oi.quantity*oi.unit_price)as revenue
from employees e
join orders o on e.employee_id=o.employee_id
join order_items oi on o.order_id=oi.order_id
group by e.employee_id, e.first_name,e.last_name
order by revenue desc;

select e.employee_id, concat(e.first_name,' ',e.last_name) as employee_name,
count(distinct o.order_id) as orders_handled,
sum(oi.quantity) as units_sold,
sum(oi.quantity*oi.unit_price) as revenue
from employees e
join orders o on e.employee_id=o.employee_id
join order_items oi on o.order_id=oi.order_id
group by e.employee_id,e.first_name,e.last_name
order by revenue desc;

-- Top 10 products + having
select p.product_id, p.product_name, sum(quantity) as products_sold
from products p
join order_items oi on p.product_id=oi.product_id
group by p.product_id,p.product_name
having products_sold >=100
limit 10;

-- customer spending
select c.customer_id,concat(c.first_name,' ',c.last_name)as customer_name, sum(oi.quantity*oi.unit_price)as total_spent
from customers c
join orders o on c.customer_id=o.customer_id
join order_items oi on o.order_id=oi.order_id
group by customer_id,customer_name
order by total_spent desc;

-- Cte+ above-avarage products

with product_revenue as
	(
    select p.product_id,p.product_name,SUM(oi.quantity*oi.unit_price) as revenue
    from products p 
    join order_items oi on p.product_id=oi.product_id
    group by p.product_id,p.product_name
    order by revenue desc
    )
select * 
from product_revenue 
where revenue> (select avg(revenue) from product_revenue);

-- product revenue ranking/rank()
with product_revenue as
	(
    select p.product_id,p.product_name,SUM(oi.quantity*oi.unit_price) as revenue
    from products p 
    join order_items oi on p.product_id=oi.product_id
    group by p.product_id,p.product_name
    order by revenue desc
    )
select product_id,product_name, revenue, rank()over(order by revenue  desc) as revenue_ranking
from product_revenue
order by revenue desc;

-- Monthly Revenue + YoY/MoM Analysis

with monthly_revenue as(
select year(o.order_date)as year, month(o.order_date) as month, sum(oi.quantity*oi.unit_price) as revenue
from orders o
join order_items oi on o.order_id=oi.order_id
group by year(o.order_date),month(o.order_date)
)
select year,month,revenue, 
	lag(revenue) over(order by year,month) as previous_month_revenue,
	lag(revenue,12)over(order by year,month) as previous_year_revenue
from monthly_revenue
order by year,month;
