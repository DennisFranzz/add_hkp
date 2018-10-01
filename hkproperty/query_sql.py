QUERY_FIND_USER_BY_USERNAME = "Select * from hkpUser where username = :username and is_superuser = :is_superuser;"

QUERY_FIND_USER_BY_EMAIL = "Select * from hkpUser where email = :email;"

QUERY_FIND_AGENT_BY_USERNAME = "Select * from agent where username = :username;"

QUERY_FIND_PROPERTY_BY_TRANS_TYPE = "Select p.id, p.owner_id, p.address_id, p.gross_floor_area,"
"p.number_of_bedrooms, p.provide_car_park, p.selling_price, p.rental_price,"
"p.for_transaction_type, pa.district, pa.estate, pa.block, pa.floor, pa.flat"
"from property as p INNER JOIN propertyAddress as pa on p.address_id = pa.id"
"where p.for_transaction_type = :transType;"


