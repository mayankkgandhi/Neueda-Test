#!/usr/bin/python3

import sys
from json import dumps, loads
from encrypt import encrypt_files
from connection import send_message_to_queue, establish_remote_conection
from read_json_files import read_json, get_json_files
from json_to_xml import json_to_xml_coverter


def main():
    """
    Main function to 
    1. convert all json files to xml 
    2. encrypt the files
    3. Transfer it to a remote location (container_b)
    """
    try:
        # get list of '.json' files to transfer from the /jsons/ dir
        json_files = get_json_files()
        
        if not json_files:
            print("Exiting")
            sys.exit(0)

        # make a pika connection
        pika_connection = establish_remote_conection()

        if not pika_connection:
            sys.exit(0)

        for file in json_files[1]:

            # read json data
            data = read_json(file)
            print("\tJson Data: {}".format(data))

            # convert data to xml
            xml = json_to_xml_coverter(loads(data))
            print("\n\tConverted XML: {}".format(xml))

            # encrypt the xml
            encrypted_xml = encrypt_files(str(xml))
            print("\n\tEncrypted XML: {}".format(encrypted_xml))

            # push the data to queue
            send_message_to_queue(pika_connection, file, encrypted_xml)

        # push special flag to indicate eof
        send_message_to_queue(pika_connection, "done", "exit")

    except Exception as e:
        print("Error: {}".format(str(e)))

    finally:
        if pika_connection != None:
            pika_connection.close()

if __name__ == "__main__":
    main()
