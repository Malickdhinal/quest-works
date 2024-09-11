create table employeedetails(
empid int primary key auto_increment,
firstname varchar(30),
lastname varchar(30),
salry int,
dept varchar(30),
gender varchar(30));
insert into employeedetails values(5,"arman","malick",300000,"hr","female")
,(4,"falah","falah",100000,"coo","male"),
(1,"malick","dhinal",100000,"hr","male")
,(2,"sahal","pk",200000,"hr","male")
,(3,"aysha","fathima",900000,"ceo","female")
;

-- third question paper
select * from employeedetails;-- 1
select firstname from employeedetails;-- 2
SELECT CONCAT(firstname, ' ', lastname) AS name FROM employeedetails;-- 3
select * from employeedetails where firstname like "%h";-- 4
SELECT DISTINCT dept FROM employeedetails;-- 5
-- select empid,firstname,lastname,dept,gender,max(salry) from employeedetails group by max(salry);-- 6
select min(salry)as result from employeedetails;-- 7
select * from employeedetails where firstname in("malick","sahal");-- 8
select * from employeedetails where firstname not in("malick","sahal");-- 9
select concat("hello ",firstname) from employeedetails;-- 10
select * from employeedetails where salry<200000;-- 11
select * from employeedetails where salry between 100000 and 800000;-- 12
select distinct salry from employeedetails ORDER BY salry asc limit 2;-- 13
select sum(salry) ,dept from employeedetails group by dept having sum(salry);-- 14
select dept,count(dept),sum(salry) from employeedetails group by dept having count(dept);-- 16
select dept, max(salry) from employeedetails group by dept order by max(salry) asc ;-- 17

















create table projectdetails(
proid int primary key auto_increment,
employeeid int ,
proname varchar(30)
);
insert into projectdetails values(1,11,"project 1"),
(2,12,"project 2"),
(3,13,"project 3"),
(4,14,"project 4"),
(5,15,"project 5");
select * from projectdetails;

