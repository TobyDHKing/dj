INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('JamesHype', 'Password1!', 'dj', 1);

INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('DJ Guv', 'Password1!', 'dj', 2);

INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('Admin', 'Password1!', 'admin', 3);

INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('Born On Road', 'Normz1!', 'dj', 4);

INSERT or REPLACE INTO users (username, password, type, id)
VALUES ('Fusion', 'Password1!', 'customer', 5);

INSERT or REPLACE INTO djs (id,user_id,bio,genres)
VALUES (1,1,'This is James Hypes text for bio','1,2,3');

INSERT or REPLACE INTO djs (id,user_id,bio,genres)
VALUES (2,2,'This is DJ Guv text for bio','1,2,3');

INSERT or REPLACE INTO djs (id,user_id,bio,genres)
VALUES (3,4,'This is Born on Road text for bio','1,2,3');

INSERT or REPLACE INTO bookings (id,booker_id,dj_id,bookedfor)
VALUES (1,2,1,'2022-03-20');

INSERT or REPLACE INTO bookings (id,booker_id,dj_id,bookedfor)
VALUES (2,4,2,'2022-03-21');

INSERT or REPLACE INTO bookings (id,booker_id,dj_id,bookedfor)
VALUES (3,2,1,'2022-03-21');

INSERT or REPLACE INTO bookings (id,booker_id,dj_id,bookedfor)
VALUES (4,4,2,'2022-03-21');

INSERT or REPLACE INTO bookings (id,booker_id,dj_id,bookedfor)
VALUES (5,2,1,'2022-03-19');

INSERT or REPLACE INTO bookings (id,booker_id,dj_id,bookedfor)
VALUES (6,4,2,'2022-03-22');
INSERT or REPLACE INTO bookings (id,booker_id,dj_id,bookedfor)
VALUES (7,2,1,'2022-03-20');

INSERT or REPLACE INTO bookings (id,booker_id,dj_id,bookedfor)
VALUES (8,4,2,'2022-03-26');