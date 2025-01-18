import psycopg2
import os
import csv

here = os.path.dirname(os.path.abspath(__file__))

def ConnectToDB():
    try:
        conn = psycopg2.connect("dbname='bikeshop' user='daviddechantsreiter' host='localhost' password='database'")
        print("Connection was successful!")
        return conn
    except psycopg2.OperationalError as e:
        print('Connection failed!')

#INSERT INTO BRANDS (brand_id, brand_name) VALUES (%s, %s), (brand_id, brand_name)


def InsertData(connection, cursor, insert_statement, data_index):

    try:
        cursor.execute(insert_statement, data_index)
    except psycopg2.OperationalError as e:
        print(f'Insert into Brands table failed! {e}')
        exit()

    connection.commit()


def Insert2Brands():
    
    with open(os.path.join(here, 'data/brands.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)
        count_line = 0

        #Some exception handling for connecting to the database
        try:
            conn = psycopg2.connect("dbname='bikeshop' user='daviddechantsreiter' host='localhost' password='database'")
            print('connection successful')
        except psycopg2.OperationalError as e:
            print(f'Unable to connect to database. {e}')
            exit()
        
        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        for row in csv_reader:

            brand_id = row['brand_id']
            brand_name = row['brand_name']

            try:
                cur.execute("INSERT INTO BRANDS (brand_id, brand_name) VALUES (%s, %s) ", (brand_id, brand_name))
            except psycopg2.OperationalError as e:
                print(f'Insert into Brands table failed! {e}')
                exit()

            conn.commit()
            count_line += 1
        
        cur.close()
        conn.close()
    
    print("Brands: " + str(count_line))
    f.close()

def Insert2Customers():

    with open(os.path.join(here, 'data/customers.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)

        conn = ConnectToDB()

        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        count_line = 0

        for row in csv_reader:
            insert_statement = 'INSERT INTO CUSTOMERS (customer_id, first_name, last_name, phone, email, street, city, state, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) '
            data_index = (row['customer_id'], row['first_name'], row['last_name'], row['phone'], row['email'], row['street'], row['city'], row['state'], row['zip_code'])
            InsertData(conn, cur, insert_statement, data_index)

            count_line += 1
        
        cur.close()
        conn.close()
    print("Customers: " + str(count_line))
    f.close()

def Insert2Categories():

    with open(os.path.join(here, 'data/categories.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)

        conn = ConnectToDB()

        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        count_line = 0

        for row in csv_reader:
            insert_statement = 'INSERT INTO CATEGORIES (category_id, category_name) VALUES (%s, %s) '
            data_index = (row['category_id'], row['category_name'])
            InsertData(conn, cur, insert_statement, data_index)

            count_line += 1
        
        cur.close()
        conn.close()
    print("Categories: " + str(count_line))
    f.close()

def Insert2Stores():
    with open(os.path.join(here, 'data/stores.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)

        conn = ConnectToDB()

        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        count_line = 0

        for row in csv_reader:
            insert_statement = 'INSERT INTO STORES (store_id, store_name, phone, email, street, city, state, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '
            data_index = (row['store_id'], row['store_name'], row['phone'], row['email'], row['street'], row['city'], row['state'], row['zip_code'])
            InsertData(conn, cur, insert_statement, data_index)

            count_line += 1
        
        cur.close()
        conn.close()
    print("Stores (expected) : 3, \t actual: " + str(count_line))
    f.close()

def Insert2Products():
    with open(os.path.join(here, 'data/products.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)

        conn = ConnectToDB()

        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        count_line = 0

        for row in csv_reader:
            insert_statement = 'INSERT INTO PRODUCTS (product_id, product_name, brand_id, category_id, model_year, list_price) VALUES (%s, %s, %s, %s, %s, %s) '
            data_index = (row['product_id'], row['product_name'], row['brand_id'], row['category_id'], row['model_year'], row['list_price'])
            InsertData(conn, cur, insert_statement, data_index)

            count_line += 1
        
        cur.close()
        conn.close()
    print("Stores (expected) : 321, \t actual: " + str(count_line))
    f.close()

def Insert2Stocks():
    with open(os.path.join(here, 'data/stocks.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)

        conn = ConnectToDB()

        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        count_line = 0

        for row in csv_reader:
            insert_statement = 'INSERT INTO STOCKS (store_id, product_id, quantity) VALUES (%s, %s, %s) '
            data_index = (row['store_id'], row['product_id'], row['quantity'])
            InsertData(conn, cur, insert_statement, data_index)

            count_line += 1
        
        cur.close()
        conn.close()
    print("Stores (expected) : 939, \t actual: " + str(count_line))
    f.close()

def Insert2Staff():
    with open(os.path.join(here, 'data/staffs2.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)

        conn = ConnectToDB()

        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        count_line = 0

        for row in csv_reader:

            if(row['manager_id'] != ''):
                manager = int(row['manager_id'])
            else:
                manager = None

            insert_statement = 'INSERT INTO STAFF (staff_id, first_name, last_name, email, phone, active, store_id, manager_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '
            data_index = (row['staff_id'], row['first_name'], row['last_name'], row['email'], row['phone'], row['active'], row['store_id'], manager)
            InsertData(conn, cur, insert_statement, data_index)

            count_line += 1
        
        cur.close()
        conn.close()
    print("Stores (expected) : 10, \t actual: " + str(count_line))
    f.close()

def Insert2Orders():

    with open(os.path.join(here, 'data/orders.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)

        conn = ConnectToDB()

        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        count_line = 0

        for row in csv_reader:
            insert_statement = 'INSERT INTO ORDERS (order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '
            data_index = (row['order_id'], row['customer_id'], row['order_status'], row['order_date'], row['required_date'], row['shipped_date'], row['store_id'], row['staff_id'])
            InsertData(conn, cur, insert_statement, data_index)

            count_line += 1
        
        cur.close()
        conn.close()
    print("Orders (expected) : 1615, \t actual: " + str(count_line))
    f.close()

def Insert2Order_Items():

    with open(os.path.join(here, 'data/order_items.csv'), 'r') as f:

        csv_reader = csv.DictReader(f)

        conn = ConnectToDB()

        #defining a cursor in order to be able to manipulate database
        cur = conn.cursor()

        count_line = 0

        for row in csv_reader:
            insert_statement = 'INSERT INTO ORDER_ITEMS (item_id, order_id, product_id, quantity, list_price, discount) VALUES (%s, %s, %s, %s, %s, %s) '
            data_index = (row['item_id'], row['order_id'], row['product_id'], row['quantity'], row['list_price'], row['discount'])
            InsertData(conn, cur, insert_statement, data_index)

            count_line += 1
        
        cur.close()
        conn.close()
    print("Order Items (expected) : 4722, \t actual: " + str(count_line))
    f.close()




