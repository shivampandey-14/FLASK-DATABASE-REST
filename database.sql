create database FLASK_DATABASE_REST;
use FLASK_DATABASE_REST;

create table product (
	id int auto_increment primary key,
	name varchar(50) unique,
    price int,
    qty int,
    description text
);
