UPSERT_USER = (
	'INSERT INTO hkpUser(id, username,password,usergroup) values '
	'(:id, :username, :password, :usergroup) '
	'ON CONFLICT (id) DO UPDATE '
  	'SET username = :username, password = :password, '
	'usergroup = :usergroup;'
)

UPDATE_USER = (
	'UPDATE hkpUser set (id, username,password,usergroup) = '
	'(:id, :username, :password, :usergroup) '
	'where id = :id;'
)

UPSERT_BRANCH = (
	'INSERT INTO branch(id, manager_id,address) values '
	'(:id, :manager_id, :address) '
	'ON CONFLICT (id) DO UPDATE '
	'SET manager_id = :manager_id, address = :address;'
)

UPSERT_AGENT = (
	'INSERT INTO agent(:agent_id, name, username,password,email,phone,usergroup,branch_id) values '
	'(:agent_id, :name, :username, :password, :email, :phone, :usergroup, :branch_id) '
	'ON CONFLICT (agent_id) DO UPDATE '
	'SET name = :name, password = :password, email = :email, phone = :phone, '
	'usergroup = :usergroup, branch_id = :branch_id;'
)

UPSERT_DISTRICT = (
	'INSERT INTO district(id, name) values '
	'(:id, :name) '
	'ON CONFLICT (id) DO UPDATE '
	'SET name= :name;'
)

UPSERT_ESTATE = (
	'INSERT INTO estate(id, name) values '
	'(:id, :name) '
	'ON CONFLICT (id) DO UPDATE '
	'SET name= :name;'
)

UPSERT_PREFERENCE = (
	'INSERT INTO preference(id, district_id, estate_id, buying_budget, rental_budget, transactionType) values '
	'(:id, :district_id, :estate_id, :buying_budget, :rental_budget, :trans_type) '
	'ON CONFLICT (id) DO UPDATE '
	'SET district = :district_id, estate_id = :estate_id, buying_budget = :buying_budget, '
	'rental_budget = :rental_budget, transactionType = :trans_type;'
)

UPSERT_CUSTOMER = (
	'INSERT INTO customer(id, name, title, phone, preference_id) values '
	'(:id, :name, :title, :phone, :preference_id) '
	'ON CONFLICT (id) DO UPDATE '
	'SET name = :name, title = :title, phone = :phone, preference_id = :preference_id;'
)



UPSERT_PROPERTY_OWNER = (
	'INSERT INTO propertyOwner(id, name, title, phone) values '
	'(:id, :name, :title, :phone) '
	'ON CONFLICT (id) DO UPDATE '
	'SET name = :name, title = :title, phone = :phone;'
)

UPSERT_PROPERTY = (
	'INSERT INTO property(id, owner_id, district_id, estate_id, block, floor, flat, gross_floor_area, '
	'number_of_bedrooms, provide_car_park, selling_price, rental_price, '
	'for_transaction_type) values '
	'(:id, :owner_id, :district_id, :estate_id, :block, :floor, :flat, :gross_floor_area, :number_of_bedrooms,'
	':provide_car_park, :selling_price, :rental_price, :trans_type) '
	'ON CONFLICT (id) DO UPDATE '
	'SET owner_id = :owner_id, district_id = :district_id, estate_id = :estate_id, block = :block, '
	'floor = :floor, flat = :flat, gross_floor_area = :gross_floor_area, '
	'number_of_bedrooms = :number_of_bedrooms, provide_car_park = :provide_car_park, '
	'selling_price = :selling_price, rental_price = :rental_price, for_transaction_type = :trans_type;'
)

UPSERT_TRANSACTION = (
	'INSERT INTO transaction(ref_no, property_id, customer_id, agent_id, type, '
	'transaction_date, rental_price, sold_price, commission) values '
	'(:ref_no, :property_id, :customer_id, :agent_id, :type, :transaction_date, '
	':rental_price, :sold_price, :commission)'
	'ON CONFLICT (ref_no) DO UPDATE '
	'SET property_id = :property_id, customer_id = :customer_id, agent_id = :agent_id, '
	'type = :type, transaction_date = :transaction_date, rental_price = :rental_price, '
	'sold_price = :sold_price, commission = :commission'
	';'
)

DELETE_HKPUSER = 'DELETE FROM hkpUser WHERE id = :id;'

DELETE_AGENT = 'DELETE FROM agent WHERE id = :id;'

DELETE_BRANCH = 'DELETE FROM branch WHERE id = :id;'

DELETE_DISTRICT = 'DELETE FROM district WHERE id = :id;'

DELETE_ESTATE = 'DELETE FROM estate WHERE id = :id;'

DELETE_PREFERENCE = 'DELETE FROM preference WHERE id = :id;'

DELETE_CUSTOMER = 'DELETE FROM customer WHERE id = :id;'

DELETE_PROPERTY_OWNER = 'DELETE FROM propertyOwner WHERE id = :id;'

DELETE_PROPERTY = 'DELETE FROM property WHERE id = :id;'

DELETE_TRANSACTION = 'DELETE FROM transaction WHERE ref_no = :ref_no;'
