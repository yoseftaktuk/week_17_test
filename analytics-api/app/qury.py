import connection

class Mysql_Service:
        def __init__(self):
            self.connection = connection.MysqlManager()
        def get_top_10(self):
            qury = """SELECT * FROM Customer
             WHERH customerNumber in (SELECT customerNumber COUT(orderNumber) FROM Order 
             GROUP BY customerNumber
             ORDER BY COUT(orderNumber) DESC
             LIMIT 10)
             """
            cruser = self.connection.cruser()
            cruser.execute(qury)
            return cruser.fetchall()

        def get_customers_without_orders(self):
            qury = """SELECT * FROM Customer
            WHERE customerNumber NOT IN (SELECT customerNumber FROM
            Order)"""
            cruser = self.connection.cruser()
            cruser.execute(qury)
            return cruser.fetchall()

        def zero_credit_active_customers(self):
            qury = """SELECT * FROM Customer
            WHERE creditLimit = 0 and customerNumber in (
            SELECT customerNumber FROM ORDER)"""