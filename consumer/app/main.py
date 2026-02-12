import mysql_connection
import  kafka_consumer

connection = mysql_connection.MysqlManager()

def main():
   kafka_consumer.get_data(connection=connection)

if __name__ == "__main__":
    main()