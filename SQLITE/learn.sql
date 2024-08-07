
-- Creating Table Users
CREATE TABLE "Users" ("name" TEXT, "email" TEXT);

-- Inserting values and info
INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu');
INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu');

-- Viewing the data
SELECT * FROM Users;

-- Delete for duplicated files
DELETE FROM Users WHERE email='ted@umich.edu'

-- Updating table Users

UPDATE TABLE Users SET name="Charles" WHERE email="csev@umich.edu"


--Multi-Table SQL:

-- Create the Artist table
CREATE TABLE IF NOT EXISTS Artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    name TEXT
);

-- Create the Album table
CREATE TABLE IF NOT EXISTS Album (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    artist_id INTEGER,
    title TEXT,
    FOREIGN KEY (artist_id) REFERENCES Artist(id)
);

-- Create the Genre table
CREATE TABLE IF NOT EXISTS Genre (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    name TEXT
);

-- Create the Track table
CREATE TABLE IF NOT EXISTS Track (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    album_id INTEGER, 
    genre_id INTEGER, 
    len INTEGER, 
    rating INTEGER, 
    title TEXT, 
    count INTEGER,
    FOREIGN KEY (album_id) REFERENCES Album(id),
    FOREIGN KEY (genre_id) REFERENCES Genre(id)
);

-- Insert data into Artist table
INSERT INTO Artist (name) VALUES ('Led Zepplin');
INSERT INTO Artist (name) VALUES ('AC/DC');

-- Insert data into Genre table
INSERT INTO Genre (name) VALUES ('Rock');
INSERT INTO Genre (name) VALUES ('Metal');

-- Insert data into Album table
INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

-- Insert data into Track table
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Black Dog', 5, 297, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Stairway', 5, 482, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('About to Rock', 5, 313, 0, 1, 2);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Who Made Who', 5, 207, 0, 1, 2);



-- Many-Many Relationship

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) ;

INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name 





