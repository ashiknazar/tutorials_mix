show databases;
use login_tkinter;
show tables;
#3,4,5,6 employees
#1,2,4,5  customer_data
select * from employees left outer join customer_data on employees.Empid=customer_data.Customerid;
select * from employees left join customer_data on employees.Empid=customer_data.Customerid;
select * from employees right outer join customer_data on employees.Empid=customer_data.Customerid;
select * from employees right join customer_data on employees.Empid=customer_data.Customerid;

select * from employees inner join customer_data on employees.Empid=customer_data.Customerid;

select * from employees left join customer_data on employees.Empid=customer_data.Customerid union select * from employees right join customer_data on employees.Empid=customer_data.Customerid;


select * from customer_data;
select * from employees;

select * from tkinter;
select * from order_data;
delete from order_data where oid=13;
delete from tkinter where st_id=125;

SELECT city, COUNT(DISTINCT salary) AS unique_salary_count
FROM employees
GROUP BY city;




ALTER TABLE tkinter
MODIFY COLUMN st_id INT AUTO_INCREMENT;
show databases;
delete from customer_data where Customerid=3;