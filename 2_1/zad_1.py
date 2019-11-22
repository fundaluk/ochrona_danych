class Caesar:
    '''This class can encrypt or decrypt given text within alphabet:
        [A-Ża-ż0-9] including white character: space.

        For encryption use mode 'e', for decryption: 'd' in method call.
    '''

    ALPHABET = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'

    def __init__(self, input_str, shift, mode):
        self.ALPHABET = self.ALPHABET + self.ALPHABET.lower() + ''.join([str(i) for i in range(10)])
        self.plaintext = ''
        self.ciphertext = ''
        self._mode = mode
        self._shift = shift
        self.init_encrypt(input_str) if self._mode == 'e' else self.init_decrypt(input_str)
        self.validate()
        self.decrypt() if self._mode == 'd' else self.encrypt()

    def init_decrypt(self, input_string):
        self.ciphertext = input_string

    def init_encrypt(self, input_string):
        self.plaintext = input_string

    def validate(self):
        for c in self.plaintext + self.ciphertext:
            assert(c in self.ALPHABET + ' ')

    def encrypt(self):
        self.ciphertext = ''.join([self.encrypt_decrypt_char(c)for c in self.plaintext])
        print(self.ciphertext)

    def encrypt_decrypt_char(self, c):
        return c if self.ALPHABET.find(c) == -1 \
            else self.ALPHABET[(self.ALPHABET.index(c) + self._shift) % len(self.ALPHABET)]

    def decrypt(self):
        self._shift = -self._shift
        self.plaintext = ''.join([self.encrypt_decrypt_char(c) for c in self.ciphertext])
        print(self.plaintext)


if __name__ == '__main__':
    Caesar('test test ', 1, 'd')
