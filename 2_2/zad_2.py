import numpy as np


passwd = 'abc'
plaintxt = 'testtest'


class Vigenere:
    ALPHABET_LENGTH = 26

    def __init__(self, key, plaintext):
        self.key = key
        self.numeric_key = self.str_to_num(self.key)
        self.plaintext = plaintext.lower()
        self.numeric_plaintext = self.str_to_num(self.plaintext)
        self.numeric_key_ext = np.resize(self.numeric_key, len(self.plaintext))
        self.ciphertext = ''
        self.numeric_ciphertext = []
        self.encryption()

    def encryption(self):
        self.numeric_ciphertext = self.numeric_plaintext + self.numeric_key_ext
        self.numeric_ciphertext = [item % self.ALPHABET_LENGTH for item in self.numeric_ciphertext]
        print(self.plaintext)
        self.ciphertext = self.num_to_str(self.numeric_ciphertext)
        print(self.ciphertext)

    def decryption(self):
        pass


    @staticmethod
    def num_to_str(num_list):
        return ''.join([chr(n + 97) for n in num_list])

    @staticmethod
    def str_to_num(str):
        return [ord(c) - 97 for c in str]


if __name__ == '__main__':
    Vigenere(passwd, plaintxt)
