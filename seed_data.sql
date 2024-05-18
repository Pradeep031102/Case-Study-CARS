INSERT INTO Victim (FirstName, LastName, DateOfBirth, Gender, ContactInformation)
VALUES 
('John', 'Doe', '1990-05-15', 'Male', 'johndoe@example.com, 1234567890'),
('Jane', 'Smith', '1985-09-20', 'Female', 'janesmith@example.com, 9876543210'),
('Michael', 'Johnson', '1978-12-10', 'Male', 'michaeljohnson@example.com, 5555555555'),
('Emily', 'Brown', '1995-03-25', 'Female', 'emilybrown@example.com, 1112223333'),
('David', 'Wilson', '1982-07-08', 'Male', 'davidwilson@example.com, 9998887777'),
('Sarah', 'Adams', '1988-06-12', 'Female', 'sarahadams@example.com, 4445556666'),
('Robert', 'Taylor', '1992-11-30', 'Male', 'roberttaylor@example.com, 7778889999'),
('Amanda', 'Jones', '1984-04-19', 'Female', 'amandajones@example.com, 3332221111'),
('James', 'Clark', '1976-08-22', 'Male', 'jamesclark@example.com, 1112223333'),
('Jessica', 'Miller', '1990-02-28', 'Female', 'jessicamiller@example.com, 5556667777');


INSERT INTO Suspect (FirstName, LastName, DateOfBirth, Gender, ContactInformation)
VALUES 
('Christopher', 'Brown', '1987-02-18', 'Male', 'christopherbrown@example.com, 3333333333'),
('Olivia', 'Martinez', '1993-08-05', 'Female', 'oliviamartinez@example.com, 4444444444'),
('Ryan', 'Garcia', '1975-11-30', 'Male', 'ryangarcia@example.com, 6666666666'),
('Megan', 'Robinson', '1989-04-12', 'Female', 'meganrobinson@example.com, 7777777777'),
('William', 'Hernandez', '1980-06-28', 'Male', 'williamhernandez@example.com, 8888888888'),
('Sophia', 'Lopez', '1985-09-15', 'Female', 'sophialopez@example.com, 1111111111'),
('Jacob', 'Gonzalez', '1991-12-20', 'Male', 'jacobgonzalez@example.com, 2222222222'),
('Emma', 'Perez', '1978-07-10', 'Female', 'emmaperez@example.com, 3333333333'),
('Ethan', 'Torres', '1983-03-05', 'Male', 'ethantorres@example.com, 4444444444'),
('Isabella', 'Rivera', '1996-05-08', 'Female', 'isabellarivera@example.com, 5555555555');


INSERT INTO Incident (IncidentType, IncidentDate, Location_Longitude, Location_Latitude, Description, Status, VictimID, SuspectID)
VALUES 
('Robbery', '2024-05-10', -73.9857, 40.7484, 'Armed robbery at a convenience store.', 'Investigating', 101, 1001),
('Homicide', '2024-05-20', -122.3331, 47.6097, 'Fatal shooting incident.', 'Closed', 102, 1002),
('Theft', '2024-05-22', -75.1652, 39.9526, 'Vehicle theft at a parking lot.', 'Open', 103, 1003),
('Theft', '2024-05-25', -77.0369, 38.9072, 'Theft reported on public property.', 'Investigating', 104, 1004),
('Robbery', '2024-06-01', -84.388, 33.749, 'Armed robbery at a gas station.', 'Closed', 105, 1005),
('Homicide', '2024-06-05', -96.7969, 32.7767, 'Stabbing incident resulting in death.', 'Under Investigation', 106, 1006),
('Robbery', '2024-06-10', -71.0589, 42.3601, 'Bank robbery with hostages.', 'Closed', 107, 1007),
('Theft', '2024-06-15', -118.2437, 34.0522, 'Shoplifting incident at a department store.', 'Open', 108, 1008),
('Robbery', '2024-06-20', -87.6298, 41.8781, 'Armed robbery at a jewelry store.', 'Closed', 109, 1009),
('Homicide', '2024-06-25', -0.1278, 51.5074, 'Murder case with multiple suspects.', 'Under Investigation', 110, 1010);


INSERT INTO Evidence ([Description], LocationFound, IncidentID)
VALUES 
('Fingerprint found on the cash register.', 'Near the entrance', 2),
('Bullet casing found at the crime scene.', 'Behind the counter', 2),
('Vehicle registration document left behind.', 'In the parking lot', 3),
('Surveillance footage from nearby camera.', 'On the street', 4),
('Mask worn by the suspect recovered.', 'Near the gas pumps', 5),
('Bloody knife found in the alley.', 'Behind the building', 6),
('Note with demands left at the bank.', 'Near the vault', 7),
('Stolen items recovered in suspect''s bag.', 'Inside the department store', 8),
('Empty cash drawer found in the alley.', 'Near the jewelry store', 9),
('DNA sample collected from the crime scene.', 'On the victim''s body', 10);


INSERT INTO Officers (FirstName, LastName, BadgeNumber, [Rank], ContactInformation, AgencyId)
VALUES 
('John', 'Smith', '12345', 'Detective', 'johnsmith@example.com, 1002003000', 10001),
('Emily', 'Williams', '54321', 'Sergeant', 'emilywilliams@example.com, 2003004000', 10002),
('Daniel', 'Brown', '98765', 'Lieutenant', 'danielbrown@example.com, 3004005000', 10003),
('Jessica', 'Davis', '56789', 'Officer', 'jessicadavis@example.com, 4005006000', 10004),
('Matthew', 'Martinez', '98765', 'Captain', 'matthewmartinez@example.com, 5006007000', 10005),
('Olivia', 'Johnson', '12345', 'Detective', 'oliviajohnson@example.com, 6007008000', 10006),
('Michael', 'Taylor', '54321', 'Sergeant', 'michaeltaylor@example.com, 7008009000', 10007),
('Sophia', 'Hernandez', '98765', 'Lieutenant', 'sophiahernandez@example.com, 8009001000', 10008),
('William', 'Garcia', '56789', 'Officer', 'williamgarcia@example.com, 9001002000', 10009),
('Ethan', 'Lopez', '98765', 'Captain', 'ethanlopez@example.com, 10020030000', 10010);


INSERT INTO LawEnforcementAgency (AgencyName, Jurisdiction, ContactInformation)
VALUES 
('New York Police Department', 'New York', 'nypd@example.com, 1234567890'),
('Los Angeles Police Department', 'Los Angeles', 'lapd@example.com, 9876543210'),
('Chicago Police Department', 'Chicago', 'cpd@example.com, 5555555555'),
('London Metropolitan Police Service', 'London', 'metpolice@example.com, 1112223333'),
('Miami Police Department', 'Miami', 'mpd@example.com, 9998887777'),
('Tokyo Metropolitan Police Department', 'Tokyo', 'tmpd@example.com, 4445556666'),
('Sydney Police Department', 'Sydney', 'spd@example.com, 7778889999'),
('Toronto Police Service', 'Toronto', 'tps@example.com, 8889990000'),
('Berlin Police Department', 'Berlin', 'bpd@example.com, 1112223333'),
('Paris Police Prefecture', 'Paris', 'ppp@example.com, 2223334444');


INSERT INTO Reports (IncidentID, ReportingOfficer, ReportDate, ReportDetails, [Status])
VALUES 
(4, 100002, '2024-05-12', 'Interviewed witnesses and collected evidence.', 'Pending Review'),
(2, 100002, '2024-05-21', 'Conducted forensic analysis of the crime scene.', 'Reviewed'),
(3, 100003, '2024-05-23', 'Interviewed the victim and reviewed surveillance footage.', 'Closed'),
(4, 100004, '2024-05-26', 'Processed evidence and submitted for further analysis.', 'Under Investigation'),
(5, 100005, '2024-06-02', 'Completed investigation and filed report.', 'Closed'),
(6, 100006, '2024-06-06', 'Coordinated with forensic team for evidence analysis.', 'Pending Review'),
(7, 100007, '2024-06-11', 'Interviewed hostages and analyzed security footage.', 'Closed'),
(8, 100008, '2024-06-16', 'Reviewed security footage and interviewed suspects.', 'Under Investigation'),
(9, 100009, '2024-06-21', 'Processed evidence and submitted for analysis.', 'Pending Review'),
(10, 100010, '2024-06-26', 'Conducted interviews and collected additional evidence.', 'Under Investigation');
