CREATE DATABASE UniversityP50122;
GO 

use UniversityP50122; 
go

CREATE TABLE MPTY(
 ID_MPTY int primary key identity(1,1),
 title varchar (30) not null,
 addressMPTY varchar (80)
);
GO


create table mtc23(
   ID_mtc23 int primary key identity(1,1),
    firstName varchar(25) not null,
     lastName varchar(25),
	 MPTY_ID int not null, 
	 foreign key (MPTY_ID) references MPTY(ID_MPTY)
);
go 
drop table MPTY

create table teacher(
	ID_teacher INT primary key identity(1,1),
	surname varchar(30) not null,
	firstName varchar(30) not null,
	middlename varchar (30)
);
go 

