create table employeee1(
empid int primary key auto_increment,
name varchar(30) not null,
phone bigint unique not null,
age int not null check(age>18) default 26);
insert into employeee1(name,phone)values("ammu",5678423);
-- drop table employeee1;


