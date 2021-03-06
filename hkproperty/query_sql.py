QUERY_FIND_USER_BY_USERNAME = "Select * from hkpUser where username = :username;"

QUERY_FIND_USER_BY_ID = "Select * from hkpUser where id = :id;"

QUERY_FIND_ALL_USER = "Select id, username, usergroup from hkpUser order by id;"

QUERY_FIND_LAST_USER_ID = "Select id from hkpUser order by id desc limit 1;"

QUERY_FIND_AGENT = (
    'Select a.id as id, a.agent_id as agent_id, a.name as name, a.email as email, a.phone as phone, '
    'a.branch_id as branch_id, b.address as address from agent as a join branch as b on (a.branch_id = b.id) '
)
QUERY_FIND_AGENT_BY_USERNAME = QUERY_FIND_AGENT + (
    'where a.username = :username;'
)

QUERY_FIND_AGENT_BY_ID = QUERY_FIND_AGENT + (
    'where a.agent_id = :id;'
)

QUERY_FIND_AGENT_BY_BRANCH = QUERY_FIND_AGENT + (
    'where b.id = :branch_id;'
)

QUERY_FIND_PROPERTY_BY_TRANS_TYPE = ""

QUERY_FIND_PROPERTY = (
    'select p.id as property_id, dist.name as District, dist.id as district_id, '
    'est.name as Estate, est.id as estate_id, p.block, p.floor, p.flat, p.gross_floor_area as area,'
    'p.number_of_bedrooms as bedrooms, p.provide_car_park as hasCarPark, p.selling_price, p.rental_price, '
    'p.for_transaction_type, owner.name as Owner, p.owner_id '
    'from property as p  '
    'join estate as est on (p.estate_id = est.id) '
    'join district as dist on (p.district_id = dist.id) '
    'join propertyOwner as owner on(p.owner_id = owner.id) '
    'where LOWER(est.name) like LOWER(:estate) and p.for_transaction_type = :type  '
    'and LOWER(dist.name) like LOWER(:district) '
    'and LOWER(owner.name) like LOWER(:owner_name) '
    'order by p.id asc'
)

QUERY_FIND_PROPERTY_BY_ID = (
    'select p.id as property_id, dist.name as District, dist.id as district_id, '
    'est.name as Estate, est.id as estate_id, p.block, p.floor, p.flat, p.gross_floor_area as area,'
    'p.number_of_bedrooms as bedrooms, p.provide_car_park as hasCarPark, p.selling_price, p.rental_price, '
    'p.for_transaction_type, owner.name as Owner, p.owner_id '
    'from property as p  '
    'join estate as est on (p.estate_id = est.id) '
    'join district as dist on (p.district_id = dist.id) '
    'join propertyOwner as owner on(p.owner_id = owner.id) '
    'where p.id = :id '
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
QUERY_FIND_LAST_PROPERTY = "Select id from property order by id desc limit 1;"

QUERY_FIND_RENTAL_PROPERTY_BY_PREFERENCE = (
    'select p.id as property_id, dist.name as district, '
    'est.name as estate, p.block, p.floor, p.flat, p.gross_floor_area as area, '
    'p.number_of_bedrooms as bedrooms, p.provide_car_park as hascarpark, '
    'p.selling_price,p.rental_price, p.for_transaction_type, '
    'po.id as owner_id,po.name as owner '
    'from preference as pref  '
    'join property as p on (p.rental_price <= pref.rental_budget '
    '    and (p.for_transaction_type = \'both\' or p.for_transaction_type= \'rent\') '
    '    and (pref.transactionType = \'both\'   or pref.transactionType= \'rent\') '
    '    and (pref.district_id is null or p.district_id = pref.district_id)'
    '    and (pref.estate_id is null or p.estate_id = pref.estate_id )'
    '    )    '
    'join propertyOwner as po on (p.owner_id = po.id) '
    'join district as dist on (p.district_id = dist.id) '
    'join estate as est on (p.estate_id = est.id) '
    'where pref.id = :prefId '
    'order by property_id asc '
)

QUERY_FIND_SELLING_PROPERTY_BY_PREFERENCE = (
    'select p.id as property_id, dist.name as district, '
    'est.name as estate, p.block, p.floor, p.flat, p.gross_floor_area as area, '
    'p.number_of_bedrooms as bedrooms, p.provide_car_park as hascarpark, '
    'p.selling_price,p.rental_price, p.for_transaction_type, '
    'po.id as owner_id,po.name as owner '
    'from preference as pref  '
    'join property as p on (p.selling_price <= pref.buying_budget '
    '    and (p.for_transaction_type = \'both\' or p.for_transaction_type= \'sale\') '
    '    and (pref.transactionType = \'both\'   or pref.transactionType= \'sale\') '
    '    and (pref.district_id is null or p.district_id = pref.district_id)'
    '    and (pref.estate_id is null or p.estate_id = pref.estate_id )'
    '    )    '
    'join propertyOwner as po on (p.owner_id = po.id) '
    'join district as dist on (p.district_id = dist.id) '
    'join estate as est on (p.estate_id = est.id) '
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

QUERY_BRANCH_REPORT = (
    'SELECT t.agent_id, a.name, count(ref_no) as total_count, '
    'count(ref_no)  FILTER(where type = \'sale\' )as sale_count, '
    'sum(sold_price) FILTER(where type = \'sale\') as total_sold_price, '
    'sum(commission) FILTER(where type = \'sale\') as total_sale_comm, '
    'count(ref_no) FILTER(where type = \'rent\') as rent_count, '
    'sum(rental_price) FILTER(where type = \'rent\') as total_rent_price, '
    'sum(commission) FILTER(where type = \'rent\') as total_rent_comm '
    'FROM transaction as t join agent as a on(t.agent_id = a.agent_id) '
    'where a.branch_id = :branch_id '
    'group by t.agent_id, a.name order by t.agent_id;'
)


QUERY_BRANCH_REPORT_BRANCH_SUMMARY = (
    'SELECT a.branch_id, count(ref_no) as total_count, '
    'count(ref_no)  FILTER(where type = \'sale\' )as sale_count, '
    'sum(sold_price) FILTER(where type = \'sale\') as total_sold_price, '
    'sum(commission) FILTER(where type = \'sale\') as total_sale_comm, '
    'count(ref_no) FILTER(where type = \'rent\') as rent_count, '
    'sum(rental_price) FILTER(where type = \'rent\') as total_rent_price, '
    'sum(commission) FILTER(where type = \'rent\') as total_rent_comm '
    'FROM transaction as t join agent as a on(t.agent_id = a.agent_id) '
    'where a.branch_id = :branch_id '
    'group by a.branch_id, a.name'
)

QUERY_FIND_PROPERTY_OWNER = (
    'SELECT po.id, po.name, po.title, po.phone '
    'FROM propertyOwner as po '
    'order by po.id'
)

QUERY_FIND_DISTRICT = (
    'SELECT id, name '
    'FROM district '
    'order by id'
)

QUERY_FIND_ESTATE = (
    'SELECT id, name '
    'FROM estate '
    'order by id'
)
