
-- Customers: list of order’s made by specific customer
SELECT customers.customer_id, order_id, first_name, last_name, phone, email, street, city, state, zipcode, order_status, order_date, required_date, shipped_date, store_id, staff_id
FROM customers
JOIN orders ON customers.CUSTOMER_ID = orders.CUSTOMER_ID
WHERE customers.customer_id = 10;


------------------------------------------
-- Orders: Order placed by customer
-- (by name)
SELECT *
FROM (SELECT customers.customer_id, order_id, first_name, last_name, phone, email, street, city, state, zipcode, order_status, order_date, required_date, shipped_date, store_id, staff_id
      FROM customers, orders
      WHERE customers.CUSTOMER_ID = orders.CUSTOMER_ID
      ORDER BY customers.CUSTOMER_ID
      ) CustOrders
WHERE CustOrders.first_name = 'Johnathan' AND CustOrders.last_name = 'Velazquez';

-- (by customer_id)
SELECT *
FROM (SELECT customers.customer_id, order_id, first_name, last_name, phone, email, street, city, state, zipcode, order_status, order_date, required_date, shipped_date, store_id, staff_id
      FROM customers, orders
      WHERE customers.CUSTOMER_ID = orders.CUSTOMER_ID
      ORDER BY customers.CUSTOMER_ID
      ) CustOrders
WHERE CustOrders.customer_id = 1;

-- Orders: Order processed by staff
-- (by staff_id)
SELECT *
FROM (SELECT staff.staff_id, order_id, first_name, last_name, phone, email, order_status, order_date, required_date, shipped_date
      FROM staff, orders
      WHERE staff.staff_id = orders.CUSTOMER_ID
      ORDER BY staff.staff_id
      ) StaffOrders
WHERE StaffOrders.staff_id = 2;

-- (by name)
SELECT *
FROM (SELECT staff.staff_id, order_id, first_name, last_name, phone, email, order_status, order_date, required_date, shipped_date
      FROM staff, orders
      WHERE staff.staff_id = orders.CUSTOMER_ID
      ORDER BY staff.staff_id
      ) StaffOrders
WHERE StaffOrders.first_name = 'Mireya' AND StaffOrders.last_name = 'Copeland';

-- Orders: Order price and items included
-- (Items)
SELECT ROUND(CAST((quantity * list_price * (1 - discount)) AS numeric), 2) AS price
FROM (
    SELECT order_items.order_id, item_id, quantity, list_price, order_items.discount
    FROM order_items
    JOIN orders
    ON order_items.order_id = orders.order_id
     ) ItemOrders
WHERE ItemOrders.order_id = 16;

-- (Total Order Price)
SELECT ROUND(CAST(SUM((quantity * list_price * (1 - discount))) AS numeric), 2) AS price
FROM (
    SELECT order_items.order_id, item_id, quantity, list_price, order_items.discount
    FROM order_items
    JOIN orders
    ON order_items.order_id = orders.order_id
     ) ItemOrders
WHERE ItemOrders.order_id = 16;

-- Orders: Find Store where an order was placed
SELECT *
FROM (
    SELECT order_id, stores.store_id, store_name, phone, email, street, city, state, zipcode, order_status
    FROM stores
    JOIN orders
    ON stores.store_id = orders.store_id
    ) StoreOrders
WHERE StoreOrders.order_id = 2;


------------------------------------------
-- STAFF: identify manager
-- by id
SELECT *
FROM (
    SELECT staff_id, first_name, last_name, manager_id
    FROM STAFF
    WHERE Staff.staff_id = 2
     ) Subordinate,
    STAFF AS Manager
WHERE Subordinate.manager_id = Manager.staff_id;


-- Staff: identify store where staff works
SELECT staff_id, stores.store_id, first_name, last_name, manager_id, store_name, stores.phone
FROM staff
JOIN stores ON IdentStaff.store_id = stores.store_id
WHERE Staff.staff_id = 2;

------------------------------------------
-- Order_items: part of which order (order_id + item_id)

SELECT item_id, Orders.order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id
FROM Order_items
JOIN Orders ON Order_items.order_id = Orders.order_id
WHERE Order_items.order_id = 1 AND Order_items.item_id = 1;

-- Order_items: return product information
SELECT order_id, item_id, order_items.product_id, product_name, brand_id, category_id, model_year, products.list_price
FROM Order_items
JOIN Products ON Order_items.product_id = products.product_id
WHERE Order_items.order_id = 1 AND Order_items.item_id = 2;

------------------------------------------
-- Stores

-- Staff members that work at given store:
SELECT stores.store_id, store_name, staff_id, first_name, last_name, staff.email, staff.phone, active, manager_id
FROM stores
JOIN staff ON staff.store_id = stores.store_id
WHERE stores.store_id = 1;

-- How much of a specific item at a specific store is still left
SELECT quantity
FROM stores
JOIN stocks ON stores.store_id = stocks.store_id
WHERE stores.store_id = 1
  AND stocks.product_id = 313;

------------------------------------------
-- Categories

--specific store, categories --> products

SELECT store_id, stocks.product_id, product_name, categories.category_id, category_name, list_price, quantity
FROM stocks
JOIN products ON stocks.product_id = products.product_id
JOIN categories ON categories.category_id = products.category_id
WHERE store_id = 1
    AND products.category_id = 1
    OR products.category_id = 2
    OR products. category_id = 3
ORDER BY products.category_id, list_price;

------------------------------------------
-- Products

--psecifc store, specific product
SELECT products.product_id, store_id, quantity, product_name, list_price
FROM PRODUCTS
JOIN stocks ON stocks.product_id = products.PRODUCT_ID
WHERE stocks.store_id = 2 AND products.product_id = 4

------------------------------------------
-- Brands
SELECT store_id, brands.brand_id, brand_name, stocks.product_id, product_name, list_price, quantity
FROM stocks
JOIN products ON stocks.product_id = products.product_id
JOIN brands ON brands.brand_id = products.brand_id
WHERE store_id = 1
    AND brands.brand_id = 1
    OR brands.brand_id = 2
    OR brands.brand_id = 3
ORDER BY brands.brand_id, list_price;

