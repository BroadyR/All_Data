drop database if exists FinalProject;
create database FinalProject;
use FinalProject;

create table department(
	did int not null,
    dname varchar(50),
    primary key(did)
    );
    
CREATE TABLE Professor (
    PID INT NOT NULL AUTO_INCREMENT UNIQUE,
    PName VARCHAR(50),
    DID INT,
    PEmail VARCHAR(50),
    PRIMARY KEY (PID),
    FOREIGN KEY (DID)
        REFERENCES department (did)
        ON DELETE CASCADE
);

create table Student(
	SID int NOT NULL AUTO_INCREMENT Unique,
    DID int,
    SEmail varchar(50),
    primary key(SID),
    foreign key(DID) references department(did)
    on delete cascade
);

create table course(
	CID int NOT NULL UNIQUE,
    DID int,
    Section varchar(50) ,
    ClassSize int,
    TimeSlot VARCHAR(50),
    primary key(CID),
    foreign key(DID) references department(did)
       on delete cascade
);
create table take(
	S_SID int,
    C_CID int,
	foreign key(S_SID) references Student(SID)
    on delete cascade,
    foreign key(C_CID) references course(CID)
       on delete cascade
);

create table teach(
	P_PID int,
    C_CID int,
	foreign key(P_PID) references Professor(PID)
       on delete cascade,
    foreign key(C_CID) references course(CID)
       on delete cascade
);

create table administrator(
	AID int NOT NULL unique,
    primary key(AID)
);

CREATE TABLE assign (
    A_AID INT,
    P_PID INT,
    C_CID INT,
    FOREIGN KEY (A_AID)
        REFERENCES administrator (AID)
        ON DELETE CASCADE,
    FOREIGN KEY (P_PID)
        REFERENCES Professor (PID)
        ON DELETE CASCADE,
    FOREIGN KEY (C_CID)
        REFERENCES course (CID)
        ON DELETE CASCADE
);

DELIMITER $$
USE `finalproject`$$
CREATE DEFINER=`root`@`localhost` TRIGGER
 `course_BEFORE_UPDATE` BEFORE UPDATE ON
 `course` FOR EACH ROW BEGIN
	declare msg varchar(255);
	if (new.ClassSize > 200) then
    /*Error Message*/		
			set msg = ' Max Class size for this Section has been Reached, No more students can be added to this Section';
        signal sqlstate '45000' set message_text = msg;
	end if;
END$$
DELIMITER ;

drop view if exists teachercourse;
create view teachercourse as
	select p.Pname, d.dname, c.CID, c.section, c.classsize
    from professor p, course c, department d, teach t
    where p.pid = t.p_pid and d.DID = C.DID and c.cid = t.c_cid;
