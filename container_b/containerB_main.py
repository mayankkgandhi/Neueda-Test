#!/usr/bin/python3
from connection import establish_remote_conection, rabbitmq_listener


def main():
    """
    Main function to 
    1. Receive files frm container_a
    2. Decrypt and store files
    """
    try:
        pika_connection = establish_remote_conection()
        pika_connection.basic_consume(rabbitmq_listener, queue='json_data_queue', no_ack=True)
        pika_connection.start_consuming()

    except Exception as e:
        print("Error: {}".format(str(e)))

if __name__ == "__main__":
    main()
