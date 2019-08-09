from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
import sys


def keyCreate(password):
    key = RSA.generate(2048)
    private_key = key.exportKey(passphrase=password, pkcs=8)
    file_out = open("private.pem", "wb")
    file_out.write(private_key)

    public_key = key.publickey().export_key()
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)


def cryptoFile(file, password):
    with open('text_encrypted.txt', 'wb') as out_file:
        recipient_key = RSA.import_key(
            open('private.pem').read(),
            passphrase=password
        )
        session_key = get_random_bytes(16)

        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))

        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        # data = b'blah blah blah Python blah blah'
        with open(file, 'rb') as data:
            data = data.read()
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)

        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        out_file.write(ciphertext)


def decryptoFile(file, password):
    with open('text_encrypted.txt', 'rb') as out_file:
        recipient_key = RSA.import_key(
            open('private.pem').read(),
            passphrase=password
        )
        enc_session_key, nonce, tag, ciphertext = [
            out_file.read(x) for x in (recipient_key.size_in_bytes(), 16, 16, -1)
        ]

        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        with open('text_decrypted.txt', 'wb') as out_file:
            out_file.write(data)

if __name__ == "__main__":
    # keyCreate('qwerty123@')
    # cryptoFile('text.txt', 'qwerty123@')
    # decryptoFile('text_encrypted.txt', 'qwerty123@')
    if len(sys.argv) == 4 or sys.argv[-1] == 'keycreate' and len(sys.argv) == 3:
        if len(sys.argv) == 3:
            name, password, action = sys.argv
        else:
            name, filename, password, action = sys.argv
        try:
            if action == 'crypto':
                cryptoFile(str(filename), str(password))
            elif action == 'decrypto':
                decryptoFile(str(filename), str(password))
            elif action == 'keycreate':
                keyCreate(str(password))
        except ValueError:
            print('Не верный пароль')
        

            
    else:
        print('Введите в формате: "Имя файла" "Пароль от ключа" "Действие(создание ключе=keycreate,шифрование файла=crypto, расшифровка файла=decrypto)"')
        