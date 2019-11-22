import random


class Polyalphabetic:
    def __init__(self, input_string, _mode):
        self.plaintext = ''
        self.ciphertext = ''
        self.flattened = []
        self.KEY = {}
        self.read_key()
        self.KEY[' '] = [' ', ' ']
        self.init_decrypt(input_string) if _mode == 'd' else self.init_encrypt(input_string)
        self.validate()
        self.decrypt() if _mode == 'd' else self.encrypt()

    def read_key(self):
        with open('key', 'r') as f:
            input_str = f.read()
            for item in input_str.split('\n'):
                entry = item.split()
                self.KEY[entry[0]] = [entry[1], entry[2]]
            print(self.KEY)

    def init_decrypt(self, input_string):
        self.ciphertext = input_string.lower()

    def init_encrypt(self, input_string):
        self.plaintext = input_string.lower()

    def validate(self):
        all_chars = []
        all_chars += self.KEY.keys()
        for val in self.KEY.values():
            all_chars += val
        assert (len(all_chars) % 3 == 0)
        for c in self.plaintext + self.ciphertext:
            assert (c in all_chars + [' '])

    def decrypt(self):
        flatten = lambda l: [item for sublist in l for item in sublist]
        self.flattened = [flatten(i) for i in list(self.KEY.items())]
        self.plaintext = ''.join([self.decrypt_char(c) for c in self.ciphertext])
        print(self.plaintext)

    def encrypt(self):
        self.ciphertext = ''.join([self.encrypt_char(c) for c in self.plaintext])
        print(self.ciphertext)

    def encrypt_char(self, c):
        return self.KEY[c][round(random.uniform(0, 1))]

    def decrypt_char(self, c):
        for i in range(len(self.flattened)):
            if c in self.flattened[i][1:]:
                return self.flattened[i][0]
        else:
            raise Exception


if __name__ == '__main__':
    input = 'l%d9 zt+)'
    mode = 'd'
    # mode = 'e'
    Polyalphabetic(input, mode)
