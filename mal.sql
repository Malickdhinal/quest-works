create database malick;
use malick;
select * from student;
alter table student drop place;
alter table student add column age int,add phoneno bigint;
alter table student change column age age1 int;
alter table student drop phoneno;
alter table student modify create table student1(
sid int,
phoneno bigint,
price decimal(10,2)
);
drop table student1;
insert into student1 values(1,87430256446821,10.56);
select * from student1;age1 varchar(30);
insert into student values(1,"ammu","kollam",23),(2,"abhi","calicut",25);
create table student1(
sid int,
phoneno bigint,
price decimal(10,2)
);
drop table student1;

insert into student1 values(1,87430256446821,10.56);
select * from student1;
create table student2(
sid int , status enum("inactive","active","cancelled"));
insert into student2 values(1,"inactive");
select * from student2;
create table exdate(
id int,
date_col date,
time_col time,
date_time datetime,
time_stamp timestamp,
year_ year
);
insert into exdate(id,date_col,time_col,date_time,time_stamp,year_)values
(1,"2024-04-02","14:30:00","2024-04-02 14:30:00","2024-04-02 14:30:00","2024");
select * from exdate;
select id from exdate;
select * from exdate where id="kollam";
drop table exdate;


create table salesman1(
salesman_id int,
name varchar(50),
city varchar(50),
commission decimal(3,2)
);
insert into salesman1 values(5001,"james hoog","new york",0.15),
(5002,"nail knite","paris",0.13),
(5005,"pit alex","london",0.11),
(5006,"mc lyon","paris",0.14),
(5003,"lauson hen","",0.12),
(5007,"paul adam","rome",0.13);
select * from salesman1;
create table customer1(
customer_id int,
cust_name varchar(50),
city varchar(50),
grade int,
salesman_id int
);
insert into customer1 values(3002,"nick rimando","new york",100,5001),
(3005,"graham zusi","california",200,5002),
(3001,"brad guzan","london",null,5005),
(3002,"nick rimando","new york",100,5001);
select * from customer1;
select * from customer1 where city="new york";

