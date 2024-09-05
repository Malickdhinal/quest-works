create table sstu(
id int primary key auto_increment,
name varchar(60) not null,
eid int,
phoneno bigint not null unique,
age int not null,
foreign key (eid)
references ssstu(empid)
);
insert into sstu value(1,"ammu",101,748645211,23);
insert into sstu value(2,"amu",102,758645211,53);
drop table sstu;
select * from sstu;
create table ssstu(
empid int primary key);
insert into ssstu(empid)values(101);
drop table ssstu;


