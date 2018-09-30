INSERT INTO hkpUser(username,password,email,is_superuser) values('admin', 'admin', 'admin@hkp.com', true);

INSERT INTO branch values(default);

INSERT INTO agent(username,password,email,is_superuser,branch_id) values
('agent1', 'agent1', 'agent1@hkp.com', false, 1),
('agent2', 'agent2', 'agent2@hkp.com', false, 1)
;

INSERT INTO customer(first_name, last_name, title, phone, email, preference_id) values
('Andy', 'Chan', 'Mr.', '93929192', null, null),
('Joey', 'Lo', 'Mrs.', '59192912', null, null)
;

INSERT INTO propertyAddress(district, estate, block, floor, flat) values
('Aberdeen', 'Yue Fai Court', 'B', '24', 'b'),
('Ap Lei Chau', 'Lei Tung Estae', 'Tung Pin', '35', 'a'),
('Aberdeen', 'Wa Fu', 'K', '2', '12')
;

INSERT INTO property(owner_id, address_id, gross_floor_area, number_of_bedrooms, provide_car_park,
    selling_price, rental_price, for_transaction_type) values
(1, 1, 500, 2, false, 4000000, null, 'sale'),
(2, 2, 300, 1, false, 2500000, null, 'sale'),
(2, 3, 400, 2, false, 3000000, 10000, 'both')
;