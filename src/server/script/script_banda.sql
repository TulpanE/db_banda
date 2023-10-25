create table post(
	 id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50)  NOT NULL
);
create table user(
id INTEGER NOT NULL PRIMARY KEY,
login VARCHAR(50),
password VARCHAR(50)
);
create table staff(
id INTEGER PRIMARY KEY,
name VARCHAR (50),
surname VARCHAR(50),
post_id INTEGER,
user_id INTEGER,
foreign key (post_id) references post(id),
foreign key (user_id) references user(id)
);

  CREATE TABLE Operations (
        OperationID INTEGER PRIMARY KEY,
        Name TEXT,
        Type TEXT,
        Success TEXT
    );
    CREATE TABLE SecurityIncident (
        IncidentID INTEGER PRIMARY KEY,
        SafetyInspectionID INTEGER,
        Description TEXT,
        Status TEXT,
        FOREIGN KEY (SafetyInspectionID) REFERENCES SafetyInspection(SafetyInspectionID)
    );
CREATE TABLE SafetyInspection (
        CheckID INTEGER PRIMARY KEY,
        LocationID INTEGER,
        Date DATE,
        Result TEXT,
        Notes TEXT,
        FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
    );
 CREATE TABLE Victim (
        VictimID INTEGER PRIMARY KEY,
        Name TEXT,
        LocationID integer,
        LossAmount TEXT,
        IncidentDate DATE,
        FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
    );
  CREATE TABLE MoneyCashing (
        CashingID INTEGER PRIMARY KEY,
        VictimID INTEGER,
        Amount TEXT,
        type_transaction VARCHAR,
        time_transaction date,
        Success TEXT,
        FOREIGN KEY (VictimID) REFERENCES Victims(VictimID)
    );
create table suppliers(
id INTEGER NOT NULL PRIMARY KEY,
data_deliveries date,
time_deliveries time,
product VARCHAR(255)
);
create table storehouse(
id INTEGER NOT NULL PRIMARY KEY,
product VARCHAR(255),
count integer,
suppliers_id integer,
foreign key (suppliers_id) references suppliers(id)
);
  CREATE TABLE Messages (
        MessageID INTEGER PRIMARY KEY,
        Content TEXT,
        Status TEXT,
        OperationID INTEGER,
        FOREIGN KEY (OperationID) REFERENCES Operations(OperationID)
    );
  CREATE TABLE FakeWebsites (
        WebsiteID INTEGER PRIMARY KEY,
        URL TEXT,
        Purpose TEXT,
        VictimCount INTEGER,
        Outcome TEXT,
        OperationID INTEGER,
        FOREIGN KEY (OperationID) REFERENCES Operations(OperationID)
    );
   CREATE TABLE  Locations (
        LocationID INTEGER PRIMARY KEY,
        address VARCHAR
    );
insert into user values(1,'Roman','admin');
	insert into user values(2,'Sergey','admin');
		insert into user values(3,'Elena','admin');
			insert into user values(4,'Khvicha','admin');
				insert into user values(5,'Pavel','admin');


insert into Operations values(1, 'Phishing Operation A', 'Phishing', 'Success');
	insert into Operations values(2, 'Identity Theft Operation B', 'Identity Theft', 'Success');
		insert into Operations values(3, 'Money Laundering Operation C', 'Money Laundering', 'Success');
			insert into Operations values(4, 'Fake Website Operation D', 'Fake Website', 'Success');
				insert into Operations values(5, 'Fake Website Operation D', 'Fake Website', 'Success');

insert into post values(1,'website developer');
	insert into post values(2,'website developer');
		insert into post values(3,'manager');
			insert into post values(4,'security developer');
				insert into post values(5,'security developer');

insert into staff values(1,'Roman','Barinov',1,1);
	insert into staff values(2,'Elena','Tretyakova',2,2);
		insert into staff values(3,'Pavel','Stromskoy',3,3);
			insert into staff values(4,'Kvicha','Kvaratskhelia',4,4);
				insert into staff values(5,'Sergey','marchenko',5,5);


insert into SecurityIncident values(1,1, 'Data Breach', 'Resolved');
	insert into SecurityIncident values(2,2, 'Unauthorized Access', 'Investigating');
		insert into SecurityIncident values(3,3, 'Physical Break-In', 'Resolved');
			insert into SecurityIncident values(4,4, 'Malware Attack', 'Ongoing');
				insert into SecurityIncident values(5,5, 'Phishing Incident', 'Resolved');

insert into SafetyInspection values(1, 1, '2023-05-28', 'Pass', 'No major issues found');
	insert into SafetyInspection values(2, 2, '2023-07-02', 'Fail', 'Security breach identified');
		insert into SafetyInspection values(3, 3, '2023-07-17', 'Pass', 'Routine check completed');
			insert into SafetyInspection values(4, 1, '2023-07-25', 'Fail', 'Security cameras offline');
				insert into SafetyInspection values(5, 2, '2023-08-05', 'Pass', 'No security issues detected');

insert into Victim values(1,'Alice Brown', 1, '$500', '2023-05-15');
	insert into Victim values(2,'Bob Evans', 2, '$1000', '2023-06-20');
		insert into Victim values(3,'Carol Davis',  3, '$800', '2023-07-05');
			insert into Victim values(4,'David Smith', 4, '$1200', '2023-07-12');
				insert into Victim values(5,'Emily Johnson',5, '$600', '2023-08-02');

insert into Locations values(1,'Proletarkaya 31');
	insert into Locations values(2,'Proletarkaya 32');
		insert into Locations values(3,'123 Main St, Cityville');
			insert into Locations values(4,'Undisclosed Location');
				insert into Locations values(5,'456 Elm St, Townsville');

insert into suppliers values(1,'10-12-2024','10:25:00','telephone');
	insert into suppliers values(2,'10-12-2024','17:00:00','telephone');
		insert into suppliers values(3,'10-11-2024','09:40:00','computer');
			insert into suppliers values(4,'05-06-2024','15:10:00','notebook');
				insert into suppliers values(5,'12-10-2024','12:24:00','computer,telephone');

insert into storehouse values(1,'telephone',10,1);
	insert into storehouse values(2,'computer',4,5);
		insert into storehouse values(3,'computer',30,4);
			insert into storehouse values(4,'computer',20,2);
				insert into storehouse values(5,'notebook',5,3);

insert into MoneyCashing values(1, 101, '$1000', 'bank', '2023-05-21', 'Success');
	insert into MoneyCashing values(2, 102, '$1500', 'bank', '2023-06-27', 'Failure');
		insert into MoneyCashing values(3, 103, '$800', 'bank', '2023-07-11', 'Success');
			insert into MoneyCashing values(4, 104, '$2000', 'bank', '2023-07-19', 'Success');
				insert into MoneyCashing values(5, 105, '$1200', 'bank', '2023-08-07', 'Failure');

insert into Messages values(1, 'Meet at the usual spot tomorrow.', 'Sent',4);
	insert into Messages values(2, 'Got it, see you then.',  'Received',3);
		insert into Messages values(3, 'Secure the location for tomorrow night.','Sent',3);
			insert into Messages values(4, 'Understood, I will take care of it.', 'Received',2);
				insert into Messages values(5, 'The plan is in motion, standby for updates.', 'Sent',1);

insert into FakeWebsites values(1, 'fakebank.com', 'Phishing', 500, 'Success',4);
	insert into FakeWebsites values(2, 'fakestore.com', 'E-commerce', 300, 'Failure',5);
		insert into FakeWebsites values(3, 'boguscharity.org', 'Charity Scam', 150, 'Success',2);
			insert into FakeWebsites values(4, 'scamlottery.net', 'Lottery Scam', 200, 'Success',2);
				insert into FakeWebsites values(5, 'notlegittravel.com', 'Travel Scam', 100, 'Failure',1);


