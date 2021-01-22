from pika import BlockingConnection, ConnectionParameters, PlainCredentials, BasicProperties
from json import dumps, loads
from decrypt import decrypt
import sys


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
        return channel
    except Exception as e:
        print("Container_b Connection Failure: {}".format(str(e)))


def rabbitmq_listener(channel, method, properties, body):
    """
    Function which listens to rabbitmqueue for new messages
    :param: channel - communication channel
    :param: method - meta-data about message delivery
    :param: properties - user-defined message properties
    :param: body - encrpted message
    """
    # load json data
    json_data = loads(body)
    if str(json_data["metadata-filename"]) == "done" and str(json_data["data"]) == "exit":
        print("\n\n --> Done and Exit")
        sys.exit(0)

    # decrypt the json data to get the XML
    decrypted_xml = decrypt(str(json_data["data"]))
    print("\n\t Decrypted data :", decrypted_xml)

    # save xml files unders /xmls dir
    with open("/xmls/" + str(json_data['metadata-filename']).split(".")[0] + ".xml","w") as ftw:
        ftw.write(decrypted_xml)

