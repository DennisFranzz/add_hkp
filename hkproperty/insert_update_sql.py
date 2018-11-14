INSERT_USER = (
	'INSERT INTO hkpUser(username,password,usergroup) values'
	'(:username, :password, :admin);'
)

INSERT_BRANCH = (
	'INSERT INTO branch(manager_id,address) values '
	'(:manager_id, :address);'
)

INSERT_AGENT = (
	'INSERT INTO agent(name, username,password,email,phone,usergroup,branch_id) values '
	'(:name, :username, :password, :email, :phone, :usergroup, :branch_id);'
)

INSERT_DISTRICT = (
	'INSERT INTO district(name) values '
	'(:name);'
)

INSERT_ESTATE = (
	'INSERT INTO dstate(name) values '
	'(:name);'
)

INSERT_PREFERENCE = (
	'INSERT INTO preference(district_id, estate_id, buying_budget, rental_budget, transactionType) values '
	'(:district_id, :estate_id, :buying_budget, :rental_budget, :trans_type);'
)

INSERT_CUSTOMER = (
	'INSERT INTO customer(name, title, phone, preference_id) values '
	'(:name, :title, :phone, :preference_id);'
)

INSERT_PROPERTY_ADDRESS = (
	'INSERT INTO propertyAddress(district_id, estate_id, block, floor, flat) values '
	'(:district_id, :estate_id, :block, :floor, :flat);'
)

INSERT_PROPERTY_OWNER = (
	'INSERT INTO propertyOwner(name, title, phone) values '
	'(:name, :title, :phone);'
)

INSERT_PROPERTY = (
	'INSERT INTO property(owner_id, address_id, gross_floor_area, '
	'number_of_bedrooms, provide_car_park, selling_price, rental_price, '
	'for_transaction_type) values '
	'(:owner_id, :address_id, :gross_floor_area, :number_of_bedrooms,'
	':provide_car_park, :selling_price, :rental_price, :trans_type'
	');'
)

INSERT_TRANSACTION = (
	'INSERT INTO transaction( property_id, customer_id, agent_id, type, '
	'transaction_date, rental_price, sold_price, commission) values '
	'(:property_id, :customer_id, :agent_id, :type, :transaction_date, '
	':rental_price, :sold_price, :commission'
	');'
)
