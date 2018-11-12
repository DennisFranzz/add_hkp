QUERY_FIND_USER_BY_USERNAME = "Select * from hkpUser where username = :username;"

QUERY_FIND_USER_BY_ID = "Select * from hkpUser where id = :id;"

QUERY_FIND_AGENT_BY_USERNAME = "Select * from agent where username = :username;"

QUERY_FIND_PROPERTY_BY_TRANS_TYPE = "Select p.id, p.owner_id, p.address_id, p.gross_floor_area,"
"p.number_of_bedrooms, p.provide_car_park, p.selling_price, p.rental_price,"
"p.for_transaction_type, pa.district, pa.estate, pa.block, pa.floor, pa.flat"
"from property as p INNER JOIN propertyAddress as pa on p.address_id = pa.id"
"where p.for_transaction_type = :transType;"

QUERY_FIND_PROPERTY = (
    'select dist.name as District, est.name as Estate, pa.block, pa.floor, pa.flat, p.gross_floor_area as area,'
    'p.number_of_bedrooms as bedrooms, p.provide_car_park as hasCarPark, p.selling_price, p.rental_price, '
    'p.for_transaction_type, owner.name as Owner ' 
    'from property as p  join propertyAddress as pa on (p.address_id = pa.id) ' 
    'join estate as est on (pa.estate_id = est.id) ' 
    'join district as dist on (pa.district_id = dist.id) ' 
    'join propertyOwner as owner on(p.owner_id = owner.id) '
    'where LOWER(est.name) like LOWER(:estate) and p.for_transaction_type = :type  '
    'and LOWER(dist.name) like LOWER(:district) '
    'and LOWER(owner.name) like LOWER(:owner_name) '
    'order by p.id asc'
)

QUERY_LIST_TRANSACTION_TYPE = 'SELECT unnest(enum_range(NULL::transactiontype)) as transaction_type'