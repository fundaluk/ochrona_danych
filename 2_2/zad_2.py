import numpy as np


class Vigenere:
    ALPHABET_LENGTH = 26

    def __init__(self, input_str, key, mode):
        self.key = key
        self.mode = mode
        self.plaintext = ''
        self.numeric_plaintext = []
        self.ciphertext = ''
        self.numeric_ciphertext = []

        self.init_encryption(input_str) if self.mode == 'e' else self.init_decryption(input_str)

        self.numeric_key = self.str_to_num(self.key)
        self.numeric_key_ext = np.resize(self.numeric_key, len(self.plaintext + self.ciphertext))

        self.encryption() if self.mode == 'e' else self.decryption()

    def init_encryption(self, input_str):
        self.plaintext = input_str.lower()
        self.numeric_plaintext = self.str_to_num(self.plaintext)

    def encryption(self):
        self.numeric_ciphertext = self.numeric_plaintext + self.numeric_key_ext
        self.numeric_ciphertext = [item % self.ALPHABET_LENGTH for item in self.numeric_ciphertext]
        print(self.plaintext)
        self.ciphertext = self.num_to_str(self.numeric_ciphertext)
        print(self.ciphertext)

    def init_decryption(self, input_str):
        self.ciphertext = input_str.lower()
        self.numeric_ciphertext = self.str_to_num(self.ciphertext)

    def decryption(self):
        self.numeric_plaintext = self.numeric_ciphertext - self.numeric_key_ext
        self.numeric_plaintext = [item % self.ALPHABET_LENGTH for item in self.numeric_plaintext]
        print(self.ciphertext)
        self.plaintext = self.num_to_str(self.numeric_plaintext)
        print(self.plaintext)


    @staticmethod
    def num_to_str(num_list):
        return ''.join([chr(n + 97) for n in num_list])

    @staticmethod
    def str_to_num(str):
        return [ord(c) - 97 for c in str]


if __name__ == '__main__':
    key = 'abc'
    input_str = 'tfutugsu'
    # mode = 'e'
    mode = 'd'
    Vigenere(input_str, key, mode)
