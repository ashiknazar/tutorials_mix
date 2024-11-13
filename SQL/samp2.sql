create table products (pid int primary key auto_increment,product_name varchar(10),product_price float,product_category varchar(10));
insert into products (product_name,product_price,product_category) values("nike",2000,"tshirt");

insert into products (product_name,product_price,product_category) values("sony",3000,"headphone");
insert into products (product_name,product_price,product_category) values("omen17",200000,"laptop");
insert into products (product_name,product_price,product_category) values("adidas",4000,"shoe");
insert into products (product_name,product_price,product_category) values("aviator",5000,"sunglasses");
select * from order_data;
delete from order_data where oid=3;
CREATE TABLE order_data (oid INT AUTO_INCREMENT PRIMARY KEY,uid INT,pids TEXT,amount INT,ostatus VARCHAR(20));

alter table products add column img varchar(10);
show tables;
ALTER TABLE order_data
CHANGE COLUMN code username VARCHAR(10);

update products set img="sun.png" where pid=5;
update products set img="omen.png" where pid=3;
update products set img="heads.png" where pid=2;