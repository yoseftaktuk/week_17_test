import kafka_publisher
import mongo_connection

def main():
    num = 0
    connection = mongo_connection.Mongo_manager()
    while True:
        result = connection.get_30(num)
        if len(result) == 0:
            break
        kafka_publisher.send_30(result)
        num += 30

if __name__ == "__main__":
    main()