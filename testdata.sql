INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('JamesHype', 'Password1!', 'dj', 1);

INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('DJ Guv', 'Password1!', 'dj', 2);

INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('Admin', 'Password1!', 'admin', 3);

INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('Fusion', 'Password1!', 'customer', 4);

INSERT or REPLACE INTO djs (id,user_id,bio,genres)
VALUES (1,1,'This is James Hypes text for bio','1,2,3');

INSERT or REPLACE INTO djs (id,user_id,bio,genres)
VALUES (2,2,'This is DJ Guv text for bio','1,2,3');