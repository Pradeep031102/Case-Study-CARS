CREATE DATABASE CARS
USE CARS

--victims

Create table victim(
VictimID int identity(101,1)NOT NULL primary key,
FirstName varchar(28),
LastName varchar(28),
DateOfBirth date,
Gender varchar(10),
ContactInformation varchar(400),
);

--Suspects

Create table Suspect(
SuspectID int identity(1001,1)NOT NULL primary key,
FirstName varchar(28),
LastName varchar(28),
DateOfBirth date,
Gender varchar(10),
ContactInformation varchar(400),
);


CREATE table Incident(
IncidentID int identity(1,1) NOT NULL primary key,
IncidentType varchar(50),
IncidentDate date,
Location_Longitude DECIMAL(10, 6),
Location_Latitude DECIMAL(10, 6),
[Description] varchar(250),
[Status] varchar(50),
VictimID int,
Foreign key(VictimID) References victim(VictimID),
SuspectID int,
Foreign key(SuspectID) References Suspect(SuspectID)
);


--Law Enforcement Agencies

Create table LawEnforcementAgency (
AgencyID int identity(10001,1)NOT NULL primary key,
AgencyName varchar(51),
Jurisdiction varchar(49),
ContactInformation varchar(400),

);

--Officers

Create table Officers(
OfficerID int identity(100001,1)NOT NULL primary key,
FirstName varchar(28),
LastName varchar(28),
BadgeNumber varchar(25),
[Rank] varchar(25),
ContactInformation varchar(400),
AgencyId int,
Foreign key(AgencyId) References LawEnforcementAgency(AgencyId)
);

--Evidence

CREATE table Evidence(
EvidenceID int identity(5001,1) NOT NULL primary key,
[Description] varchar (199),
LocationFound varchar (300),
IncidentID int,
Foreign key (IncidentID) References Incident(IncidentID)
);

--Reports

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

CREATE TABLE [Case] (
    caseID INT PRIMARY KEY IDENTITY NOT NULL,
    caseDescription VARCHAR(MAX),
    incidentIDs VARCHAR(MAX)
);