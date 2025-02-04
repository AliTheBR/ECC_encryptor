from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
import base64


def load_private_key(filename):
    with open(filename, 'rb') as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def decrypt_file(input_file, output_file, private_key):
    with open(input_file, 'rb') as f:
        encrypted_data = base64.b64decode(f.read())
    decrypted_data = encrypted_data[len(private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )):]
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)


priv_key = load_private_key("ecc_private.pem")

enfile = input('Enter file path(name if in same folder): ')

decrypt_file(enfile, "decrypted.txt", priv_key)

print("Decryption Done!")
