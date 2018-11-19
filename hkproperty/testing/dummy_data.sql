BEGIN TRANSACTION;

INSERT INTO hkpUser(username,password,usergroup) values
('admin', 'admin', 'admin');

INSERT INTO branch(manager_id,address) values
(4,'branch address1'),
(5,'branch address2');

INSERT INTO agent(name, username,password,email,phone,usergroup,branch_id) values
('Dennis Chan', 'dennischan', 'dennis', 'dennis@hkp.com','50100123', 'agent', 1),
('Janice Mo', 'janicemo','janice', 'janice@hkp.com','51150123', 'agent', 2),
('Candy Ko', 'candymo','candy', 'candy@hkp.com','50340123', 'agent', 1),
('Matt Ti', 'mattti','matt', 'matt@hkp.com','39239109', 'branch_manager', 2),
('Cilly Fu', 'cillyfu','cilly', 'cilly@hkp.com','39439109', 'branch_manager', 1)
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

INSERT INTO preference(district_id, estate_id, buying_budget, rental_budget, transactionType) values
(1, null, 15000000, null, 'sale'),
(4, 2, null, 30000, 'rent'),
(2, 2, 6000000, 10000, 'both'),
(2, 1, 7000000, 10000, 'both'),
(1, 1, 8000000, 10000, 'both');

INSERT INTO customer(name, title, phone, preference_id) values
('Tommy Lee', 'Mr.', '93929192', 1),
('Justin Bo', 'Mr.', '59192912', 2),
('Ball Tsz', 'Mr.', '62939203', 3),
('France Ko', 'Ms.', '93919313', 4),
('May Yeung', 'Ms.', '63829392', 5)
;




INSERT INTO propertyAddress(district_id, estate_id, block, floor, flat) values
(4, 2, 'M', 12, 'A'),
(2, 3, 'A', 2, 'O'),
(1, 3, '1', 5, '1'),
(1, 5, '2', 4, '2'),
(5, 6, 'A', 5, '3'),
(4, 2, '3', 1, '4'),
(5, 1, 'F', 4, '5'),
(5, 6, '5', 37, '6')
;

INSERT INTO propertyOwner(name, title, phone) values
('Tom Chan','Mr.','29199299'),
('Kelly Leung','Ms.','35353443'),
('Peter Lee','Mr.','34634643'),
('Amy Wong','Mrs.','66576834'),
('Kelvin Kwan','Mr.','65862345');

INSERT INTO property(owner_id, address_id, gross_floor_area, number_of_bedrooms, provide_car_park,
    selling_price, rental_price, for_transaction_type) values
(2, 1, 400, 1, true, 4000000, null, 'sale'),
(2, 2, 450, 1, false, null, 10000, 'rent'),
(1, 3, 300, 1, false, 2000000, 8000, 'both'),
(4, 4, 1200, 3, true, 14000000, null, 'sale'),
(3, 5, 1400, 4, false, 20000000, 20000, 'both'),
(5, 6, 850, 2, true, null, 15000, 'rent'),
(5, 7, 750, 2, true, 7500000, null, 'sale'),
(1, 8, 500, 2, true, 5000000, null, 'sale')
;

INSERT INTO transaction( property_id, customer_id, agent_id, type, transaction_date, rental_price, sold_price, commission) values 
(2, 3, 2, 'rent', current_timestamp, 240000, null, 20000),
(1, 3, 2, 'sale', current_timestamp, null, 6000000, 120000),
(3, 2, 2, 'sale', current_timestamp, null, 5000000, 100000),
(4, 2, 3, 'sale', current_timestamp, null, 4500000, 90000),
(5, 1, 3, 'sale', current_timestamp, null, 12000000, 240000),
(7, 5, 3, 'sale', current_timestamp, null, 10000000, 200000),
(6, 3, 1, 'rent', current_timestamp, 360000, null, 30000),
(2, 3, 1, 'sale', current_timestamp, null, 3000000, 60000),
(1, 2, 1, 'sale', current_timestamp, null, 7500000, 150000),

END;