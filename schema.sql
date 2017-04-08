drop table if exists user;
create table user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username text not null,
	phone INTEGER not null,
	password text not null,
	email text not null
);

CREATE TABLE orders ( 
	id INTEGER PRIMARY KEY, 
	order_status text not null, 
	order_id text not null, 
	product_name text not null, 
	product_url text not null, 
	cost_price INTEGER not null 
);