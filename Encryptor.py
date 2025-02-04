from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
import base64


def load_public_key(filename):
    with open(filename, 'rb') as f:
        return serialization.load_pem_public_key(f.read())


def encrypt_file(input_file, output_file, public_key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    shared_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    encrypted_data = base64.b64encode(shared_key + plaintext)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)


pub_key = load_public_key("ecc_public.pem")

infile = input('Enter file path(name if in same folder): ')

encrypt_file(infile, "encrypted.dat", pub_key)

print("Encryption Done!")
