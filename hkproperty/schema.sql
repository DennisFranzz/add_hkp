
CREATE TYPE transactionType AS ENUM ('sale','rent','both');
CREATE TYPE title AS ENUM ('Mr.','Ms.','Mrs.');

CREATE TABLE hkpUser(
	username VARCHAR (50) UNIQUE NOT NULL,
	password VARCHAR (50) NOT NULL,
	email VARCHAR (355) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	is_superuser BOOLEAN DEFAULT FALSE,
	last_login TIMESTAMP
);

CREATE TABLE agent(
  id SERIAL PRIMARY KEY UNIQUE,
	branch_id INTEGER NOT NULL,
	managing_branch_id INTEGER NOT NULL,
	CONSTRAINT agent_branch_id_fk FOREIGN KEY (branch_id)
		REFERENCES agent (id) ON UPDATE NO ACTION ON DELETE NO ACTION
)INHERITS (hkpUser);

CREATE TABLE branch(
	id SERIAL PRIMARY KEY,
	manager_id INTEGER NOT NULL,
	CONSTRAINT branch_manager_id_fk FOREIGN KEY (manager_id)
		REFERENCES agent (id)
		ON UPDATE NO ACTION ON DELETE NO ACTION
);

ALTER TABLE agent ADD CONSTRAINT agent_managing_branch_id_fk FOREIGN KEY (managing_branch_id)
		REFERENCES branch (id) ON UPDATE NO ACTION ON DELETE NO ACTION;



CREATE TABLE propertyAddress(
	id SERIAL PRIMARY KEY,
	district VARCHAR(50) NOT NULL,
	estate VARCHAR(50),
	block VARCHAR(50) NOT NULL,
	floor INTEGER NOT NULL,
	flat VARCHAR(3) NOT NULL
);

CREATE TABLE property(
	id SERIAL PRIMARY KEY,
	owner_id INTEGER NOT NULL,
	address_id INTEGER NOT NULL,
	gross_floor_area INTEGER NOT NULL,
	number_of_bedrooms INTEGER NOT NULL,
	provide_car_park BOOLEAN NOT NULL,
	selling_price NUMERIC(20,2) NOT NULL,
	rental_price NUMERIC(20,2) NOT NULL,
	for_transaction_type transactionType NOT NULL,
	CONSTRAINT property_address_id_fk FOREIGN KEY (address_id)
		REFERENCES propertyAddress(id)
		ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE preference(
	id SERIAL PRIMARY KEY,
	district VARCHAR(50),
	estate VARCHAR(50),
	buying_budget INTEGER,
	rental_budget INTEGER,
	transactionType transactionType
);

CREATE TABLE customer(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	title title,
	phone VARCHAR(20) NOT NULL,
	email VARCHAR(355),
	preference_id INTEGER,
	CONSTRAINT customer_preference_id_fk FOREIGN KEY (preference_id)
		REFERENCES preference(id) 
		ON UPDATE NO ACTION ON DELETE NO ACTION
);


CREATE TABLE transaction(
	ref SERIAL PRIMARY KEY,
	type transactionType NOT NULL,
	transaction_date TIMESTAMP NOT NULL,
	property_id INTEGER NOT NULL,
	sold_price NUMERIC(20,2),
	rental_price NUMERIC(20,2),
	owner_id INTEGER NOT NULL,
	customer_id INTEGER NOT NULL,
	agent_id INTEGER NOT NULL,
	commission  NUMERIC(20,2) NOT NULL,
	CONSTRAINT transaction_property_id FOREIGN KEY (property_id)
		REFERENCES property(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT transaction_owner_id FOREIGN KEY (owner_id)
		REFERENCES customer(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT transaction_customer_id FOREIGN KEY (customer_id)
		REFERENCES customer(id) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT transaction_agent_id FOREIGN KEY (agent_id)
		REFERENCES agent(id) ON UPDATE NO ACTION ON DELETE NO ACTION	
);

