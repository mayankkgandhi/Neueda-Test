from json import dumps, loads
from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties

QUEUE_NAME = "json_data_queue"
CONNECTION_NAME = "rabbitqueue"
CONNECTION_USERNAME = "guest"
CONNECTION_PASSWORD = "guest"
CONNECTION_PORT = 5672

def establish_remote_conection():
    """
    Function to create a pika blocking connection
    :return: pika connection for rabbitmq
    """
    try:
        # Set the connection parameters to connect to rabbitqueue on port 5672
        # on the / virtual host using the username "guest" and password "guest"
        connection = BlockingConnection(ConnectionParameters(CONNECTION_NAME, CONNECTION_PORT, "/", PlainCredentials(CONNECTION_USERNAME, CONNECTION_PASSWORD)))
        channel = connection.channel() 
        channel.queue_declare(queue=QUEUE_NAME, durable=True)
        return channel
    except Exception as e:
        print("Container_a Connection Failure {}".format(str(e)))


def send_message_to_queue(pika_connection, filename, encrypted_data):
    """
    Function to send data to rabbitmq queue
    :param: pika_connection - connection for rabbitmq
    :param: filename - name of encrpyted file
    :param: encrypted_data - converted and encrypted xml data
    """
    pika_connection.basic_publish(exchange='',
            routing_key=QUEUE_NAME,
            body=dumps({"metadata-filename":filename,"data":encrypted_data}),
            properties=BasicProperties(delivery_mode = 2 ))
