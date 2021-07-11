import os
# import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import InvalidToken


backend = default_backend()
iterations = 100_000


def _derive_key(
    password: bytes,
    salt: bytes,
    iterations: int = iterations
        ) -> bytes:
    """Derive a secret key from a given password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=iterations, backend=backend)
    return b64e(kdf.derive(password))


def password_decrypt(token: str, password: str) -> str:
    token = token.encode()
    decoded = b64d(token)
    salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
    iterations = int.from_bytes(iter, 'big')
    key = _derive_key(password.encode(), salt, iterations)
    return Fernet(key).decrypt(token).decode()


def get_tokens():
    tokens = {}

    with open("tokens.txt") as f:
        for line in f.readlines():
            problem, token = line.split()
            tokens[problem] = token

    return tokens


def _create_encrypted_files():
    tokens = get_tokens()

    for problem, token in tokens.items():
        with open(os.path.join("python", f"p{problem}.py"), "w+") as f:
            f.write(token)


def decrypt_problem(tokens, problem, answer):
    try:
        _filedata = password_decrypt(tokens[problem], answer)
    except InvalidToken:
        print("Wrong answer")
        return False

    print("problem decrypted successfully")

    with open(os.path.join("python", f"p{problem}.py"), "w+") as f:
        f.write(_filedata)

    print(f"p{problem}.py constructed")


def main():
    tokens = get_tokens()

    password_input = input("Enter problem number to decrypt")
    answer_input = input(f"Enter answer for problem {password_input}")

    decrypt_problem(tokens, password_input, answer_input)


if __name__ == '__main__':
    # _create_encrypted_files()
    main()
