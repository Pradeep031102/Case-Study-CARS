>CREATE DATABASE CARS

>USE CARS

### victims

>Create table victims(
VictimID int identity(101,1)NOT NULL primary key,
FirstName varchar(28),
LastName varchar(28),
DateOfBirth date,
Gender varchar(10),
ContactInformation varchar(400),
);

### Suspects

>Create table Suspects(
SuspectID int identity(1001,1)NOT NULL primary key,
FirstName varchar(28),
LastName varchar(28),
DateOfBirth date,
Gender varchar(10),
ContactInformation varchar(400),
);

### Incident

>CREATE table Incident(
IncidentID int identity(1,1) NOT NULL primary key,
IncidentType varchar(50),
IncidentDate date,
[Location] geography,
[Description] varchar(250),
[Status] varchar(50),
VictimID int,
Foreign key(VictimID) References Victims(VictimID),
SuspectId int,
Foreign key(SuspectId) References Suspects(SuspectId)
);


### Law Enforcement Agencies

>Create table LawEnforcementAgencies (
AgencyID int identity(10001,1)NOT NULL primary key,
AgencyName varchar(51),
Jurisdiction varchar(49),
ContactInformation varchar(400),
);

### Officers

>Create table Officers(
OfficerID int identity(100001,1)NOT NULL primary key,
FirstName varchar(28),
LastName varchar(28),
BadgeNumber varchar(25),
[Rank] varchar(25),
ContactInformation varchar(400),
AgencyId int,
Foreign key(AgencyId) References LawEnforcementAgencies(AgencyId)
);

### Evidence

>CREATE table Evidence(
EvidenceId int identity(5001,1) NOT NULL primary key,
[Description] varchar (199),
LocationFound varchar (300),
IncidentId int,
Foreign key (IncidentID) References Incident(IncidentID)
);

### Reports

CREATE table Reports(
ReportId int identity(7001,1) NOT NULL primary key,
IncidentID int,
Foreign key (IncidentID) References Incident(IncidentID),
ReportingOfficer int,
Foreign key (ReportingOfficer) References Officers(OfficerID),
ReportDate date,
ReportDetails varchar(400),
[Status] varchar (600)
);


### Inserting values into Victims table


>INSERT INTO Victims (FirstName, LastName, DateOfBirth, Gender, ContactInformation)
VALUES ('John', 'Doe', '1990-05-15', 'Male', 'john.doe@example.com'),
       ('Jane', 'Smith', '1985-09-20', 'Female', 'jane.smith@example.com');

### Inserting values into Suspects table
>INSERT INTO Suspects (FirstName, LastName, DateOfBirth, Gender, ContactInformation)
VALUES ('Michael', 'Johnson', '1978-07-10', 'Male', 'michael.johnson@example.com'),
       ('Emily', 'Davis', '1992-12-30', 'Female', 'emily.davis@example.com');

### Inserting values into Incident table
>ALTER TABLE Incident
ADD CONSTRAINT CK_Incident_IncType
CHECK(incidentType IN('Robbery','Homicide','Theft'))

>ALTER TABLE Incident
ADD CONSTRAINT CK_Incident_Status
CHECK(Status IN('Open','Closed','Under Investigation'))

>INSERT INTO Incident (IncidentType, IncidentDate, Location, Description, Status, VictimID, SuspectID)
VALUES ('Robbery', '2024-04-25', geography::STPointFromText('POINT(-122.335197 47.608013)', 4326), 'Armed robbery at a convenience store', 'Under Investigation', 101, 1001),
       ('Theft', '2024-04-26', geography::STPointFromText('POINT(-122.33164 47.60621)', 4326), 'Theft reported in a shop', 'Open', 102, 1002);


### Inserting values into LawEnforcementAgencies table
>INSERT INTO LawEnforcementAgencies (AgencyName, Jurisdiction, ContactInformation)
VALUES ('Oslo Police Department', 'Oslo', 'contact@oslotownpolice.com');

### Inserting values into Officers table
>INSERT INTO Officers (FirstName, LastName, BadgeNumber, Rank, ContactInformation, AgencyID)
VALUES ('David', 'Brown', '12345', 'Detective', 'david.brown@anytownpolice.com', 10001),
       ('Lisa', 'Wilson', '67890', 'Officer', 'lisa.wilson@anytownpolice.com', 10001);

### Inserting values into Evidence table
>INSERT INTO Evidence (Description, LocationFound, IncidentID)
VALUES ('Security camera footage', 'At the crime scene', 1),
       ('Bloody knife', 'In the alley behind the bar', 2);

### Inserting values into Reports table
>ALTER TABLE Reports
ADD CONSTRAINT CK_Reports_Status_Set
CHECK(Status IN('Draft','Finalized'))

>INSERT INTO Reports (IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status)
VALUES (1, 100001, '2024-04-25', 'Initial incident report filed', 'Draft'),
       (2, 100002, '2024-04-26', 'Witness statements collected', 'Finalized');



	 



