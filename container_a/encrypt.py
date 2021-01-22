from cryptography.fernet import Fernet

CRYPTO_KEY = 'f375HkhAmE5V1OyuvYd0hH0KZkP8PPGgqiuQN74Eaxo='

def encrypt_files(xml):
    """
    Function to encrypt the xml data
    :param: xml - xml data to encrpyt
    :return: encrpyted xml data
    """

    f = Fernet(CRYPTO_KEY)
    return f.encrypt(xml.encode()).decode()
