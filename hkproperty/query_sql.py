QUERY_FIND_USER_BY_USERNAME = "Select * from hkpUser where username = :username;"

QUERY_FIND_USER_BY_ID = "Select * from hkpUser where id = :id;"

QUERY_FIND_AGENT = (
    'Select a.id as id, a.name as name, a.email as email, a.phone as phone, '
    'a.branch_id as branch_id, b.address as address from agent as a join branch as b on (a.branch_id = b.id) '
)
QUERY_FIND_AGENT_BY_USERNAME = (
    QUERY_FIND_AGENT
    'where a.username = :username;'
)

QUERY_FIND_AGENT_BY_ID = (
    QUERY_FIND_AGENT
    'where a.agent_id = :id;'
)

QUERY_FIND_AGENT_BY_ID = (
    QUERY_FIND_AGENT
    'where b.id = :branch_id;'
)

QUERY_FIND_PROPERTY_BY_TRANS_TYPE = "Select p.id, p.owner_id, p.address_id, p.gross_floor_area,"
"p.number_of_bedrooms, p.provide_car_park, p.selling_price, p.rental_price,"
"p.for_transaction_type, pa.district, pa.estate, pa.block, pa.floor, pa.flat"
"from property as p INNER JOIN propertyAddress as pa on p.address_id = pa.id"
"where p.for_transaction_type = :transType;"

QUERY_FIND_PROPERTY = (
    'select p.id as property_id, dist.name as District, est.name as Estate, pa.block, pa.floor, pa.flat, p.gross_floor_area as area,'
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

QUERY_FIND_CUSTOMER_BY_ID = (
    'select c.name as name, c.title, c.id, c.preference_id, c.phone, '
    'pref.transactionType, pref.buying_budget, pref.rental_budget, '
    'dist.name as district, est.name as estate '
    'from customer as c join preference as pref on (c.preference_id = pref.id) '
    'left join district as dist on (pref.district_id = dist.id) '
    'left join estate as est on (pref.estate_id = est.id) '
    'where c.id = :id '
)

QUERY_FIND_PROPERTY_BY_PREFERENCE = (
    'select p.id as property_id, dist.name as district, '
    'est.name as estate, pa.block, pa.floor, pa.flat, p.gross_floor_area as area, '
    'p.number_of_bedrooms as bedrooms, p.provide_car_park as hascarpark, '
    'p.selling_price,p.rental_price, p.for_transaction_type, '
    'po.id as owner_id,po.name as owner '
    'from preference as pref  '
    'join property as p on (p.selling_price <= pref.buying_budget '
    '    and (p.for_transaction_type = \'both\' or p.for_transaction_type= \'sale\') '
    '    and (pref.transactionType = \'both\'   or pref.transactionType= \'sale\')) '
    'join propertyAddress as pa on(p.address_id = pa.id'
    '    and (pref.district_id is null or pa.district_id = pref.district_id)'
    '    and (pref.estate_id is null or pa.estate_id = pref.estate_id )'
    '    )    '
    'join propertyOwner as po on (p.owner_id = po.id) '
    'join district as dist on (pa.district_id = dist.id) '
    'join estate as est on (pa.estate_id = est.id) '
    'where pref.id = :prefId '
    'order by property_id asc '
)

QUERY_LIST_TRANSACTION_TYPE = 'SELECT unnest(enum_range(NULL::transactiontype)) as transaction_type'

QUERY_FIND_CUSTOMER = (
    'Select c.id, c.title, c.name, c.phone from customer as c '
    'where CAST(c.id AS TEXT) like :id '
    'and LOWER(c.name) like LOWER(:name) '
    'and LOWER(c.phone) like LOWER(:phone) '
    'order by c.id asc'
)


QUERY_FIND_TRANSACTION_BY_AGENT = (
    'select t.ref_no, t.type, t.transaction_date, t.property_id, t.sold_price, t.rental_price, '
    't.customer_id, t.agent_id, t.commission '
    'from transaction as t '
    'where t.agent_id = :agent_id '
    'and CAST(t.type AS TEXT) like :type '
)


QUERY_FIND_TRANSACTION_BY_BRANCH = (
    'select t.ref_no, t.type, t.transaction_date, t.property_id, t.sold_price, t.rental_price, '
    't.customer_id, t.agent_id, t.commission '
    'from transaction as t '
    'where t.agent_id in (select agent_id from agent where branch_id = :branch_id  )'
    'and CAST(t.type AS TEXT) like :type '
)

QUERY_FIND_TRANSACTION = (

)
