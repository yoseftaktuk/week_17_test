import mysql.connector
import os


class MysqlManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST','mysql'),
            user=os.getenv('MYSQL_USER','appuser'),
            password=os.getenv('MYSQL_PASSWORD','apppass'),
            database=os.getenv('MYSQL_DATABASE','users'),
        )   
        except mysql.connector.Error as err:
            raise err  
        self.cruser = self.connection.cursor()
        self.create_customer_table()
        self.create_order_table()
    def create_customer_table(self):
        qury = '''CREATE TABLE IF NOT EXISTS Customer(
                customerNumber INT PRIMARY KEY,
                type VARCHAR(50),
                customerName VARCHAR(50),
                contactLastName VARCHAR(50),
                contactFirstName VARCHAR(50),
                phone int(10),
                addressLine1 VARCHAR(50),
                addressLine2 VARCHAR(50),
                city VARCHAR(50),
                state VARCHAR(50),
                postalCode VARCHAR(50),
                country ARCHAR(50),
                salesRepEmployeeNumber INT,
                creditLimit ARCHAR(50)
                ); '''
        self.cruser.execute(qury)
        self.connection.commit()
    def create_order_table(self):
        qury = '''CREATE TABLE IF NOT EXISTS Order(
        orderNumber INT PRIMARY KEY,
        type VARCHAR(50),
        orderDate VARCHAR(50),
        requiredDate VARCHAR(50),
        shippedDate VARCHAR(50),
        status VARCHAR(50),
        comments VARCHAR(50),
        FOREIGN KEY (customerNumber) REFERENCES Customer(customerNumber) 
        )'''
        self.cruser.execute(qury)
        self.connection.commit()

    def insert_to_customer(self, data: list):
        qury = '''INSERT IGNORE INTO Customer (customerNumber, type,
          customerName, contactLastName, contactFirstName, phone, 
          addressLine1, addressLine2, city, state, postalCode,
          country, salesRepEmployeeNumber, creditLimit) 
          VALUES (%s, %s,%s, %s, %s,%s, %s,%s, %s, %s,%s,%s, %s, %s);''' 
        for item in data:
            value = (item['customerNumber'], item['type'],
                      item['customerName'], item['contactLastName'], 
                      item['contactLastName'], item['contactFirstName'],
                      item['phone'], item['addressLine1'], item['addressLine2'],
                      item['city'], item['state'], item['postalCode'],
                      item['country'], item['salesRepEmployeeNumber'],
                      item['creditLimit'])
            self.cruser.execute(qury, value)
        self.connection.commit()    
    def insert_to_order(self, data):
        qury = '''INSERT IGNORE INTO Order (
        orderNumber, type, orderDate, requiredDate,
        shippedDate, status, comments, customerNumber
        )
        VALUES (%s, %s,%s, %s, %s,%s, %s,%s)'''
        for item in data:
            value = (item['orderNumber'], item['type'], item['orderDate'],
                     item['requiredDate'], item['shippedDate'], item['status'],
                     item['comments'], item['customerNumber']) 
            self.cruser.execute(qury, value)
        self.connection.commit()

