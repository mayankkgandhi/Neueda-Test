from cryptography.fernet import Fernet

CRYPTO_KEY = 'f375HkhAmE5V1OyuvYd0hH0KZkP8PPGgqiuQN74Eaxo='

def decrypt(encrypted_data):
    """
    Function to decrypt the xml data
    :param: encrypted_data - encrypted xml data
    :return: decrypted xml data
    """
    f = Fernet(CRYPTO_KEY)
    return f.decrypt(encrypted_data.encode()).decode()
