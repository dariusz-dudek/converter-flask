CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username varchar not null unique,
    password varchar not null,
    name varchar,
    admin integer not null
);