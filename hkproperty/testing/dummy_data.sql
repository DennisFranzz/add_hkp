BEGIN TRANSACTION;

INSERT INTO hkpUser(username,password,usergroup) values
('admin', 'admin', 'admin@hkp.com', 'admin');

INSERT INTO branch(manager_id,address) values
(4,'branch address1'),
(5,'branch address2');

INSERT INTO agent(name, username,password,email,phone,usergroup,branch_id) values
('Dennis Chan', 'dennischan', 'dennis', 'dennis@hkp.com','50100123', 'agent', 1),
('Janice Mo', 'janicemo','janice', 'janice@hkp.com','51150123', 'agent', 2),
('Candy Ko', 'candymo', 'candy@hkp.com','50340123', 'agent', 1),
('Matt Ti', 'mattti', 'matt@hkp.com','39239109', 'branch_manager', 2),
('Cilly Fu', 'cillyfu', 'cilly@hkp.com','39439109', 'branch_manager', 1)
;

INSERT INTO district(name) values
('Tsuen Wan'),
('Aberdeen'),
('Sha Tin'),
('Wong Tai Sin'),
('Kwai Tsing');

INSERT INTO estate(name) values
('Kwai Chung Estate'),
('Lower Wong Tai Sin Estate'),
('Yue Kwong Estate'),
('Fuk Loi Estate'),
('Shek Wai Kok Estate'),
('Kwai Tsing Estate');

INSERT INTO customer(name, title, phone, preference_id) values
('Tommy Lee', 'Mr.', '93929192', 1),
('Justin Bo', 'Mr.', '59192912', 2),
('Ball Tsz', 'Mr.', '62939203', 3),
('France Ko', 'Ms.', '93919313', 4),
('May Yeung', 'Ms.', '63829392', 5)
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

END;