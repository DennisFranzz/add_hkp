
CREATE TYPE transactionType AS ENUM ('sale','rent','both');


CREATE TABLE hkpUser(
  id SERIAL PRIMARY KEY UNIQUE,
  username VARCHAR (50) UNIQUE NOT NULL,
  password VARCHAR (50) NOT NULL,
  created_on TIMESTAMP NOT NULL default current_timestamp,
  last_login TIMESTAMP,
  usergroup VARCHAR (50) NOT NULL
);

CREATE TABLE agent(
    agent_id SERIAL PRIMARY KEY UNIQUE,
	branch_id INTEGER NOT NULL,
	name VARCHAR (100) NOT NULL,
	email VARCHAR (100) UNIQUE NOT NULL,
	phone VARCHAR (100) NOT NULL
) INHERITS(hkpUser);

CREATE TABLE branch(
	id SERIAL PRIMARY KEY,
	manager_id INTEGER NOT NULL,
	address VARCHAR (300) NOT NULL
);
ALTER TABLE branch ADD CONSTRAINT branch_manager_id_fk FOREIGN KEY (manager_id)
		REFERENCES agent (agent_id) DEFERRABLE INITIALLY DEFERRED;
        
ALTER TABLE agent ADD CONSTRAINT agent_branch_id_fk FOREIGN KEY (branch_id)
		REFERENCES branch (id) DEFERRABLE INITIALLY DEFERRED;

CREATE TABLE district(
	id SERIAL PRIMARY KEY,
	name VARCHAR (100)
);

CREATE TABLE estate(
	id SERIAL PRIMARY KEY,
	name VARCHAR (100)
);

CREATE TABLE preference(
	id SERIAL PRIMARY KEY,
	district_id INTEGER,
	estate_id INTEGER,
	buying_budget INTEGER,
	rental_budget INTEGER,
	transactionType transactionType,
	CONSTRAINT preference_district_id_fk FOREIGN KEY (district_id)
		REFERENCES district(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT preference_estate_id_fk FOREIGN KEY (estate_id)
		REFERENCES estate(id) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE customer(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	title VARCHAR(30) NOT NULL,
	phone VARCHAR(30) NOT NULL,
	preference_id INTEGER,
	CONSTRAINT customer_preference_id_fk FOREIGN KEY (preference_id)
		REFERENCES preference(id) 
		DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE propertyOwner(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	title VARCHAR(30) NOT NULL,
	phone VARCHAR(30) NOT NULL
);

CREATE TABLE property(
	id SERIAL PRIMARY KEY,
	owner_id INTEGER NOT NULL,
	district_id INTEGER NOT NULL,
	estate_id INTEGER NOT NULL,
	block VARCHAR(3) NOT NULL,
	floor INTEGER NOT NULL,
	flat VARCHAR(3) NOT NULL,
	gross_floor_area INTEGER NOT NULL,
	number_of_bedrooms INTEGER NOT NULL,
	provide_car_park BOOLEAN NOT NULL,
	selling_price NUMERIC(15,2),
	rental_price NUMERIC(15,2),
	for_transaction_type transactionType NOT NULL,

	CONSTRAINT property_owner_id_fk FOREIGN KEY (owner_id)
		REFERENCES propertyOwner(id)
		ON UPDATE NO ACTION ON DELETE CASCADE,
		CONSTRAINT property_district_id_fk FOREIGN KEY (district_id)
		REFERENCES district(id) ON UPDATE NO ACTION ON DELETE CASCADE,
	CONSTRAINT property_estate_id_fk FOREIGN KEY (estate_id)
		REFERENCES estate(id) ON UPDATE NO ACTION ON DELETE CASCADE
);

CREATE TABLE transaction(
	ref_no SERIAL PRIMARY KEY,
	type transactionType NOT NULL,
	transaction_date TIMESTAMP NOT NULL,
	property_id INTEGER NOT NULL,
	sold_price NUMERIC(15,2),
	rental_price NUMERIC(15,2),
	customer_id INTEGER NOT NULL,
	agent_id INTEGER NOT NULL,
	commission  NUMERIC(15,2) NOT NULL,
	CONSTRAINT transaction_property_id FOREIGN KEY (property_id)
		REFERENCES property(id) ON UPDATE NO ACTION ON DELETE CASCADE,
	CONSTRAINT transaction_customer_id FOREIGN KEY (customer_id)
		REFERENCES customer(id) ON UPDATE NO ACTION ON DELETE CASCADE,
	CONSTRAINT transaction_agent_id FOREIGN KEY (agent_id)
		REFERENCES agent(agent_id) ON UPDATE NO ACTION ON DELETE CASCADE
);