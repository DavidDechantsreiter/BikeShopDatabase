import psycopg2 as pg
import traceback

class customers:

    # Look Up Customer
    def get_customer_by_id(conn):
        
        """
        Returns Customer associated with inputted customer ID
        Params: PostgreSQL connection
        """

        ID = input("Input the customer's ID: ")
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM Customers WHERE customer_id = " + str(ID) + ";"
        )
        results = cur.fetchall()

        print('\n')

        print(f'{"Customer ID":<11} | {"First Name":<13} | {"Last Name":<15} | {"Phone":<14} | {"Email":<35} | {"Street":<20} | {"City":<18} | {"State":<8} | {"Zipcode":<8}')

        for result in results:
            print(f'{result[0]:<11} | {result[1]:<13} | {result[2]:<15} | {result[3]:<14} | {result[4]:<35} | {result[5]:<20} | {result[6]:<18} | {result[7]:<8} | {result[8]:<8}')
    
        print('\n')

    def get_customer_by_name(conn):
        
        """
        Returns Customer associated with inputted customer name
        Params: PostgreSQL connection
        """

        first_name = input("Input the customer's first name: ")
        last_name = input("Input the customer's last name: ")
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM Customers WHERE first_name = " + first_name + "AND last_name = " + last_name + ";"
        )
        results = cur.fetchall()

        print('\n')

        print(f'{"Customer ID":<11} | {"First Name":<13} | {"Last Name":<15} | {"Phone":<14} | {"Email":<35} | {"Street":<20} | {"City":<18} | {"State":<8} | {"Zipcode":<8}')

        for result in results:
            print(f'{result[0]:<11} | {result[1]:<13} | {result[2]:<15} | {result[3]:<14} | {result[4]:<35} | {result[5]:<20} | {result[6]:<18} | {result[7]:<8} | {result[8]:<8}')
        
        print('\n')

    # List of Orders made by a specific customer
    def get_orders_by_customer_id(conn):
        ID = input("Input the customer's ID: ")
        cur = conn.cursor()
        cur.execute(
            """
            SELECT customers.customer_id, order_id, first_name, last_name, order_status, order_date, required_date, shipped_date, store_id, staff_id
            FROM customers
            JOIN orders ON customers.CUSTOMER_ID = orders.CUSTOMER_ID
            WHERE customers.customer_id = %s;
            """, (ID,)
        )
        results = cur.fetchall()

        print('\n')
        
        print(f'{"Customer ID":<11} | {"Order ID":<8} | {"First Name":<13} | {"Last Name":<15} | {"Order Status":<14} | {"Order Date":<12} | {"Required Date":<14} | {"Shipped Date":<12} | {"Store ID":<8} | {"Staff ID":<8}')

        for result in results:
            print(f'{result[0]:<11} | {result[1]:<8} | {result[2]:<13} | {result[3]:<15} | {result[4]:<14} | {result[5]:<12} | {result[6]:<14} | {result[7]:<12} | {result[8]:<8} | {result[9]:<8}')
    
        print('\n')

    def get_orders_by_name(conn):
        first_name = input("Input the customer's first name: ")
        last_name = input("Input the customer's last name: ")
        cur = conn.cursor()
        cur.execute(
            """
            SELECT customers.customer_id, order_id, first_name, last_name, order_status, order_date, required_date, shipped_date, store_id, staff_id
            FROM customers
            JOIN orders ON customers.CUSTOMER_ID = orders.CUSTOMER_ID
            WHERE customers.first_name = %s AND customers.last_name = %s;
            """, (first_name, last_name)
        )
        results = cur.fetchall()
        
        print('\n')

        print(f'{"Customer ID":<11} | {"Order ID":<8} | {"First Name":<13} | {"Last Name":<15} | {"Order Status":<14} | {"Order Date":<12} | {"Required Date":<14} | {"Shipped Date":<12} | {"Store ID":<8} | {"Staff ID":<8}')

        for result in results:
            print(f'{result[0]:<11} | {result[1]:<8} | {result[2]:<13} | {result[3]:<15} | {result[4]:<14} | {result[5]:<12} | {result[6]:<14} | {result[7]:<12} | {result[8]:<8} | {result[9]:<8}')

        print('\n')

class orders:

    # Look up an order
    def get_order_by_order_id(conn):
        
        """
        Returns Order associated with inputted order ID
        Params: PostgreSQL connection
        """

        ID = input("Input the order ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM Orders WHERE order_id = " + str(ID)
        )
        results = cur.fetchall()
        
        print(f'{"Order ID":<10} | {"Customer ID":<12} | {"Order Status":<13} | {"Order Date":<12} | {"Required Date":<14} | {"Shipped Date":<13} | {"Store ID":<8} | {"Staff ID":<8}')

        for result in results:
            print(f'{result[0]:<10} | {result[1]:<12} | {result[2]:<13} | {result[3]:<12} | {result[4]:<14} | {result[5]:<13} | {result[6]:<8} | {result[7]:<8}')
    
        print('\n')
    
    # Staff Information for Specific Order
    def get_staff_by_order_id(conn):
        """
        Returns Staff associated with inputted order ID
        Params: PostgreSQL connection
        """

        ID = input("Input the order ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT order_id, staff.staff_id, first_name, last_name, phone, email, active, staff.store_id, manager_id
            FROM staff
            JOIN orders ON staff.staff_id = orders.staff_id
            WHERE Orders.order_id = %s;
            """, (ID,)
        )
        results = cur.fetchall()

        print(f'{"Order ID":<10} | {"Staff ID":<12} | {"First Name":<15} | {"Last Name":<20} | {"Phone":<14} | {"Email":<30} | {"Active":<8} | {"Store ID":<8} | {"Manager ID":<8}')

        
        for result in results:
            print(f'{result[0]:<10} | {result[1]:<12} | {result[2]:<15} | {result[3]:<20} | {result[4]:<14} | {result[5]:<30} | {result[6]:<8} | {result[7]:<8} | {result[8]:<8}')
    
        print('\n')

    def get_list_of_order_placed_by_staff_name(conn):
        first_name = input("Input the customer's first name: ")
        last_name = input("Input the customer's last name: ")

        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT order_id, staff.staff_id, first_name, last_name, phone, email, active, staff.store_id, manager_id
            FROM staff
            JOIN orders ON staff.staff_id = orders.CUSTOMER_ID
            WHERE staff.first_name = %s AND staff.last_name = %s;
            """, (first_name, last_name)
        )
        results = cur.fetchall()
        print(f'{"Order ID":<10} | {"Staff ID":<12} | {"First Name":<15} | {"Last Name":<20} | {"Phone":<14} | {"Email":<30} | {"Active":<8} | {"Store ID":<8} | {"Manager ID":<8}')

        for result in results:
            print(f'{result[0]:<10} | {result[1]:<12} | {result[2]:<15} | {result[3]:<20} | {result[4]:<14} | {result[5]:<30} | {result[6]:<8} | {result[7]:<8} | {result[8]:<8}')
    
        print('\n')

    def get_total_price_for_order(conn):
        
        ID = input("Input the order ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT ROUND(CAST(SUM((quantity * list_price * (1 - discount))) AS numeric), 2) AS price
            FROM (
                SELECT order_items.order_id, quantity, list_price, order_items.discount
                FROM order_items
                JOIN orders
                ON order_items.order_id = orders.order_id
                ) ItemOrders
                WHERE ItemOrders.order_id = %s;
            """, (ID,)
        )
        results = cur.fetchall()

        print(f'{"Order ID":<10} | {"Total Price of Order":<12}')

        for result in results:
            print(f'{ID:<10} | {result[0]:<12}')
    
        print('\n')

    def get_store_by_order_id(conn):
        
        ID = input("Input the order ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT order_id, stores.store_id, store_name, phone, email, street, city, state, zipcode
            FROM stores
            JOIN orders ON stores.store_id = orders.store_id
            WHERE orders.order_id = %s;
            """, (ID,)
        )
        results = cur.fetchall()
        
        print(f'{"Order ID":<8} | {"Store ID":<8} | {"Store Name":<20} | {"Phone":<14} | {"Email":<25} | {"Street":<20} | {"City":<15} | {"State":<8} | {"Zipcode":<8}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<8} | {result[2]:<20} | {result[3]:<14} | {result[4]:<25} | {result[5]:<20} | {result[6]:<15} | {result[7]:<8} | {result[8]:<8}')
        
        print('\n')

class staff:

    def get_staff_by_id(conn):
        ID = input("Input the staff ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM Staff WHERE staff_id = " + str(ID)
        )
        results = cur.fetchall()
        
        print(f'{"Staff ID":<8} | {"First Name":<15} | {"Last Name":<20} | {"Email":<30} | {"Phone":<14} | {"Store ID":<8} | {"Manager ID":<8}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<15} | {result[2]:<20} | {result[3]:<30} | {result[4]:<14} | {result[5]:<8} | {result[6]:<8}')
        
        print('\n')

    def get_staff_by_name(conn):
        first_name = input("Input the staff's first name: ")
        last_name = input("Input the staff's last name: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM Staff WHERE first_name = %s AND last_name = %s", (first_name, last_name)
        )
        results = cur.fetchall()
        print(f'{"Staff ID":<8} | {"First Name":<15} | {"Last Name":<20} | {"Email":<30} | {"Phone":<14} | {"Store ID":<8} | {"Manager ID":<8}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<15} | {result[2]:<20} | {result[3]:<30} | {result[4]:<14} | {result[5]:<8} | {result[6]:<8}')

        print('\n')

    def get_manager_by_staff_id(conn):
        ID = input("Input the staff ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT *
            FROM (
                SELECT staff_id, first_name, last_name, manager_id
                FROM STAFF
                WHERE Staff.staff_id = %s
                ) Subordinate,
                STAFF AS Manager
            WHERE Subordinate.manager_id = Manager.staff_id;
            """, (ID,)
        )
        results = cur.fetchall()

        print(f'{"Subordinate ID":<15} | {"Subordinate First Name":<25} | {"Subordinate Last Name":<25}')

        for result in results:
            print(f'{result[0]:<15} | {result[1]:<25} | {result[2]:<25}')

        print ('------------------------------------------------------------------------------------------------------------------')

        print(f'{"Manager ID":<15} | {"Manager First Name":<18} | {"Manager Last Name":<18} | {"Email":<27} | {"Phone":<14} | {"Active":<8}')

        for result in results:
            print(f'{result[3]:<15} | {result[5]:<18} | {result[6]:<18} | {result[7]:<27} | {result[8]:<14} | {result[9]:<8}')

        print('\n')

    def get_store_by_staff_id(conn):
        ID = input("Input the staff ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT staff_id, stores.store_id, first_name, last_name, manager_id, store_name, stores.phone
            FROM staff
            JOIN stores ON staff.store_id = stores.store_id
            WHERE Staff.staff_id = %s;
            """, (ID,)
        )
        results = cur.fetchall()
        
        print(f'{"Staff ID":<8} | {"Store ID":<8} | {"First Name":<18} | {"Last Name":<18} | {"Manager ID":<12} | {"Store Name":<14} | {"Store Phone":<8}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<8} | {result[2]:<18} | {result[3]:<18} | {result[4]:<12} | {result[5]:<14} | {result[6]:<8}')
        
        print('\n')

class order_items:

    def get_order_information(conn):
        OrderID = input("Input the order ID: ")
        ItemID = input("Input the item ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT item_id, Orders.order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id
            FROM Order_items
            JOIN Orders ON Order_items.order_id = Orders.order_id
            WHERE Order_items.order_id = %s AND Order_items.item_id = %s;
            """, (ItemID, OrderID)
        )
        results = cur.fetchall()
        
        print(f'{"Item ID":<8} | {"Order ID":<8} | {"Customer ID":<12} | {"Order Status":<13} | {"Order Date":<12} | {"Required Date":<14} | {"Shipped Date":<13} | {"Store ID":<8} | {"Staff ID":<8}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<8} | {result[2]:<12} | {result[3]:<13} | {result[4]:<12} | {result[5]:<14} | {result[6]:<13} | {result[7]:<8} | {result[8]:<8}')
    
        print('\n')

    def get_product_information(conn):
        ItemID = input("Input the item ID: ")
        OrderID = input("Input the order ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT order_id, item_id, order_items.product_id, product_name, brand_id, category_id, model_year, products.list_price
            FROM Order_items
            JOIN Products ON Order_items.product_id = products.product_id
             WHERE Order_items.order_id = %s AND Order_items.item_id = %s;
            """, (ItemID, OrderID)
        )
        results = cur.fetchall()
         
        print(f'{"Order ID":<8} | {"Item ID":<8} | {"Product ID":<12} | {"Product Name":<65} | {"Brand ID":<8} | {"Category ID":<12} | {"Model Year":<10} | {"List Price":<8}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<8} | {result[2]:<12} | {result[3]:<65} | {result[4]:<8} | {result[5]:<12} | {result[6]:<10} | {result[7]:<8}')
    
        print('\n')

class stores:

    def get_store_by_id(conn):
        ID = input("Input the store ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            " SELECT * FROM Stores WHERE store_id = " + str(ID)
        )
        results = cur.fetchall()
         
        print(f'{"Store ID":<8} | {"Store Name":<18} | {"Phone":<14} | {"Email":<20} | {"Street":<20} | {"City":<12} | {"State":<8} | {"Zipcode":<10}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<18} | {result[2]:<14} | {result[3]:<20} | {result[4]:<20} | {result[5]:<12} | {result[6]:<8} | {result[7]:<10}')
    
        print('\n')

    def get_staff_members_by_id(conn):
        ID = input("Input the store ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT stores.store_id, store_name, staff_id, first_name, last_name, staff.email, staff.phone, active, manager_id
            FROM stores
            JOIN staff ON staff.store_id = stores.store_id
            WHERE stores.store_id = %s;
            """, (ID,)
        )
        results = cur.fetchall()
         
        print(f'{"Store ID":<8} | {"Store Name":<18} | {"Staff ID":<10} | {"First Name":<20} | {"Last Name":<20} | {"Staff Email":<30} | {"Staff Phone":<14} | {"Active":<8} | {"Manager ID":<12}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<18} | {result[2]:<10} | {result[3]:<20} | {result[4]:<20} | {result[5]:<30} | {result[6]:<14} | {result[7]:<8} | {result[7]:<12}')
    
        print('\n')

    def get_stock_by_productid_storeid(conn):
        productID = input("Input the product ID: ")
        store = input("Input the store ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT quantity
            FROM stores
            JOIN stocks ON stores.store_id = stocks.store_id
            WHERE stores.store_id = %s
                AND stocks.product_id = %s;
            """, (store, productID)
        )
        results = cur.fetchall()
        print(f'{"Product ID":<10} | {"Store ID":<8} | {"Quantity Available":<18}')

        for result in results:
            print(f'{productID:<10} | {store:<8} | {result[0]:<18}')
        
        print('\n')

class categories:

    def get_category_by_id(conn):
        ID = input("Input the category ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            " SELECT * FROM categories WHERE category_id = " + str(ID)
        )
        results = cur.fetchall()
        
        print(f'{"Category ID":<14} | {"Category Name":<25}')

        for result in results:
            print(f'{result[0]:<14} | {result[1]:<25}')
    
        print('\n')

    def get_products_at_store_by_categories(conn):
        storeID = input("Input the storeID: ")
        categories = input("What category IDs are you looking for (seperate by comma): ")
        print('\n')

        cats = [item.strip() for item in categories.split(',')]

        query = """ 
                SELECT store_id, stocks.product_id, product_name, categories.category_id, category_name, list_price, quantity
                FROM stocks
                JOIN products ON stocks.product_id = products.product_id
                JOIN categories ON categories.category_id = products.category_id
                WHERE store_id = %s
                """

        params = [storeID]

        for i, cat in enumerate(cats):
            
            if i == 0:
                query += " AND products.category_id = %s"
                params.append(cats[0])
            else:
                query += "OR products.category_id = %s"
                params.append(cat)
        
        query += " ORDER BY products.category_id, list_price;"

        cur = conn.cursor()
        cur.execute(query, params)
        results = cur.fetchall()
         
        print(f'{"Store ID":<8} | {"Category ID":<14} | {"Cateogry Name":<25} | {"Product ID":<12} | {"Product Name":<65} | {"List Price":<10} | {"Quantity":<10}')

        for result in results:
            print(f'{result[0]:<8} | {result[3]:<14} | {result[4]:<25} | {result[1]:<12} | {result[2]:<65} | {result[5]:<10} | {result[6]:<10}')
    
        print('\n')

class products:

    def get_product_by_id(conn):
        ID = input("Input the product ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            " SELECT * FROM Products WHERE product_id = " + str(ID)
        )
        results = cur.fetchall()
        
        print(f'{"Product ID":<12} | {"Product Name":<65} | {"Brand ID":<12} | {"Cateogry ID":<12} | {"Model Year":<12} | {"List Price":<8}')

        for result in results:
            print(f'{result[0]:<12} | {result[1]:<65} | {result[2]:<12} | {result[3]:<12} | {result[4]:<12} | {result[5]:<12}')
    
        print('\n')

    def get_availability_of_product_id_at_store(conn):
        productID = input("Input the product ID: ")
        store = input("Input the store ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            """
            SELECT products.product_id, store_id, quantity, product_name, list_price
            FROM PRODUCTS
            JOIN stocks ON stocks.product_id = products.PRODUCT_ID
            WHERE stocks.store_id = %s AND products.product_id = %s
            """, (store, productID)
        )
        results = cur.fetchall()
        
        print(f'{"Product ID":<12} | {"Store ID":<10} | {"Quantity":<10} | {"Product Name":<65} | {"List Price":<8}')

        for result in results:
            print(f'{result[0]:<12} | {result[1]:<10} | {result[2]:<10} | {result[3]:<65} | {result[4]:<8}')
    
        print('\n')

class brands:

    def get_brand_by_id(conn):
        ID = input("Input the brand ID: ")
        print('\n')
        cur = conn.cursor()
        cur.execute(
            " SELECT * FROM Brands WHERE brand_id = " + str(ID)
        )
        results = cur.fetchall()
        
        print(f'{"Brand ID":<10} | {"Brand Name":<15}')

        for result in results:
            print(f'{result[0]:<10} | {result[1]:<15}')
    
        print('\n')

    def get_products_at_store_by_brand(conn):
        storeID = input("Input the storeID: ")
        brands_raw = input("What brand IDs are you looking for (seperate by comma): ")
        print('\n')

        brands = [item.strip() for item in brands_raw.split(',')]

        query = """ 
                SELECT store_id, brands.brand_id, brand_name, stocks.product_id, product_name, list_price, quantity
                FROM stocks
                JOIN products ON stocks.product_id = products.product_id
                JOIN brands ON brands.brand_id = products.brand_id
                WHERE store_id =  %s
                """

        params = [storeID]

        for i, brd in enumerate(brands):
            
            if i == 0:
                query += " AND products.brand_id = %s"
                params.append(brands[0])
            else:
                query += " OR products.brand_id = %s"
                params.append(brd)
        
        query += " ORDER BY brands.brand_id, list_price;"

        cur = conn.cursor()
        cur.execute(query, params)
        results = cur.fetchall()
         
        print(f'{"Store ID":<8} | {"Brand ID":<10} | {"Brand Name":<15} | {"Product ID":<14} | {"Product Name":<65} | {"List Price":<10} | {"Quantity":<10}')

        for result in results:
            print(f'{result[0]:<8} | {result[1]:<10} | {result[2]:<15} | {result[3]:<14} | {result[4]:<65} | {result[5]:<10} | {result[6]:<10}')
    
        print('\n')

class SearchEngine(brands, categories, customers, order_items, orders, products, staff, stores):

    def ConnectToDB(user_id, password):

        user_id = input("Please enter your user ID: ")
        password = input("Please enter your password: ")

        try:
            conn = pg.connect(
                dbname = 'bikeshop',
                user = user_id,
                host = 'localhost',
                password = password)
            print('Connection was Successful!')
            return conn
        except pg.OperationalError as e:
            print('Connection Failed!')
            traceback.print_exc()

    conn = ConnectToDB('daviddechantsreiter', 'database')

    while True:

        def ReturnToMM():
            answer = input("Return to Main Menu (type Y): ")
            if answer.strip().upper() == 'Y':
                return True
            else:
                print("OK! Have another look at the results")
                return False

        print('\n')
        print("""Hello! This search engine queries a sample database from sqlservertutorial.net for a retail bike store.
The backend was built using PostgreSQL and DataGrip. The database consists of 8 different tables: 
brands, categories, customers, order_items, orders, products, staff, stores.
There are a multitude of query options for each table. To proceed with the search engine, select a table to query!""")
    
        print(
        """
        ================================     Main Menu     ================================
        1. Brands
        2. Categories
        3. Customers
        4. Order Items
        5. Orders
        6. Products
        7. Staff
        8. Stores
        9. Exit
        """
        )

        table = int(input('Select a Table: '))
        
        print('\n')
        
        if table == 1:
            print("1. Brand Name (ID)")
            print("2. Product Availability by Brand at Specific Store (ID, Brand ID(s), Store ID)")
            print("3. Exit")
            print('\n')
            select = int(input("Make a Selection: "))
        
            if select == 1:
                brands.get_brand_by_id(conn)
                ReturnToMM()
            elif select == 2:
                brands.get_products_at_store_by_brand(conn)
                ReturnToMM()
            else:
                continue
        
        elif table == 2:
            print('1. Category Info (ID)')
            print("2. Product Availability by Category at Specific Store (ID, Category ID(s), Store ID)")
            print("3. Exit")
            print('\n')
            select = int(input("Make a Selection: "))
            
            if select == 1:
                categories.get_category_by_id(conn)
                ReturnToMM()
            elif select == 2:
                categories.get_products_at_store_by_categories(conn)
                ReturnToMM()
            else:
                continue

        elif table == 3:
            print('1. Customer Info (ID)')
            print('2. Customer Info (Name)')
            print('3. List of Orders (ID)')
            print('4. List of Orders (Name)')
            print("5. Exit")
            print('\n')
            select = int(input("Make a Selection: "))
            if select == 1:
                customers.get_customer_by_id(conn)
                ReturnToMM()
            elif select == 2:
                customers.get_customer_by_name(conn)
                ReturnToMM()
            elif select == 3:
                customers.get_orders_by_customer_id(conn)
                ReturnToMM()
            elif select == 4:
                customers.get_orders_by_name(conn)
                ReturnToMM()
            else:
                continue

        elif table == 4:
            print('1. Order Information (order ID, item ID)')
            print('2. Product Information (order ID, item ID)')
            print('3. Exit')
            print('\n')
            select = int(input("Make a Selection: "))
            if select == 1:
                order_items.get_order_information(conn)
                ReturnToMM()
            elif select == 2:
                order_items.get_product_information(conn)
                ReturnToMM()
            else :
                customers.get_orders_by_customer_id(conn)
                ReturnToMM()

        elif table == 5:
            print('1. Order Info (ID)')
            print('2. Processor/Seller [Staff] Info (ID)')
            print('3. List of Orders Placed By Staff (Name)')
            print('4. Total Price of Order (ID)')
            print("5. Order Location Inforamtion (ID) ")
            print("6. Exit")
            print('\n')
            select = int(input("Make a Selection: "))
            if select == 1:
                orders.get_order_by_order_id(conn)
                ReturnToMM()
            elif select == 2:
                orders.get_staff_by_order_id(conn)
                ReturnToMM()
            elif select == 3:
                orders.get_list_of_order_placed_by_staff_name(conn)
                ReturnToMM()
            elif select == 4:
                orders.get_total_price_for_order(conn)
                ReturnToMM()
            elif select == 5:
                orders.get_store_by_order_id(conn)
                ReturnToMM()
            else:
                continue

        elif table == 6:
            print('1. Product Info (ID)')
            print("2. Product Availability at Specific Store (ID, Store ID)")
            print("3. Exit")
            print('\n')
            select = int(input("Make a Selection: "))
            if select == 1:
                products.get_product_by_id(conn)
                ReturnToMM()
            elif select == 2:
                products.get_availability_of_product_id_at_store(conn)
                ReturnToMM()
            else:
                continue

        elif table == 7:
            print('1. Staff Info (ID)')
            print('2. Staff Info (Name)')
            print('3. Location of Employment Info (ID)')
            print('4. Manager Info (ID)')
            print("5. Exit")
            print('\n')
            select = int(input("Make a Selection: "))
            if select == 1:
                staff.get_staff_by_id(conn)
                ReturnToMM()
            elif select == 2:
                staff.get_staff_by_name(conn)
                ReturnToMM()
            elif select == 3:
                staff.get_store_by_staff_id(conn)
                ReturnToMM()
            elif select == 4:
                staff.get_manager_by_staff_id(conn)
                ReturnToMM()
            else:
                continue


        elif table == 8:
            print('1. Store Info (ID)')
            print('2. List of Staff (ID)')
            print('3. Specific Stock of Product (Proudct ID, ID)')
            print("4. Exit")
            print('\n')
            select = int(input("Make a Selection: "))
            if select == 1:
                stores.get_store_by_id(conn)
                ReturnToMM()
            elif select == 2:
                stores.get_staff_members_by_id(conn)
                ReturnToMM()
            elif select == 3:
                stores.get_stock_by_productid_storeid(conn)
                ReturnToMM()
            else:
                continue
        
        else:
            print("Exiting the Program! Goodbye!")
            print('\n')
            break