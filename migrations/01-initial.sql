CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username varchar not null unique,
    password varchar not null,
    name varchar,
    admin integer not null
);

CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    nip varchar(10) not null ,
    name varchar not null ,
    iln varchar(13) not null
);