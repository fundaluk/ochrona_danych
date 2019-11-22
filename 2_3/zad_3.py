import numpy as np

import itertools


class Playfair:
    ALPHABET = 'abcdefghiklmnopqrstuvwxyz'

    def __init__(self, input_str, key, mode):
        self.KEY = []
        self.generate_key(key)

        self.plaintext = ''
        self.ciphertext = ''
        self.extended = False

        self.init_encrypt(input_str) if mode == 'e' else self.init_decrypt(input_str)
        self.encrypt() if mode == 'e' else self.decrypt()

    @staticmethod
    def list_chunks(input_list, n):
        for i in range(0, len(input_list), n):
            yield input_list[i:i + n]

    def generate_key(self, key):
        key_string = key + self.ALPHABET
        result_string = ''
        for c in key_string:
            if c not in result_string:
                result_string += c
        # self.KEY = np.array(list(self.list_chunks(result_string, 5)))
        self.KEY = list(self.list_chunks(result_string, 5))

    def init_encrypt(self, input_str):
        self.plaintext = input_str
        if len(self.plaintext) % 2 != 0:
            self.plaintext += self.plaintext[-1]
            self.extended = True

    def init_decrypt(self, input_str):
        self.ciphertext = input_str
        if len(self.ciphertext) % 2 != 0:
            self.ciphertext += self.ciphertext[-1]
            self.extended = True

    def encrypt(self):
        chunks = list(self.list_chunks(self.plaintext, 2))
        output = [self.encrypt_chunk(c) for c in chunks]
        output = ''.join(list(itertools.chain.from_iterable(output)))
        print(output)

    def decrypt(self):
        chunks = list(self.list_chunks(self.ciphertext, 2))
        output = [self.decrypt_chunk(c) for c in chunks]
        output = ''.join(list(itertools.chain.from_iterable(output)))
        print(output)

    def encrypt_chunk(self, chunk):
        chunk = Chunk(chunk)

        for i in range(5):
            for j in range(5):
                if chunk.list[0] == self.KEY[i][j]:
                    chunk.x1 = i
                    chunk.y1 = j
                if chunk.list[1] == self.KEY[i][j]:
                    chunk.x2 = i
                    chunk.y2 = j

        if chunk.x1 == chunk.x2:
            chunk.x1 += 1
            chunk.x2 += 1
            chunk.x1 %= 5
            chunk.x2 %= 5
        elif chunk.y1 == chunk.y2:
            chunk.y1 += 1
            chunk.y2 += 1
            chunk.y1 %= 5
            chunk.y2 %= 5
        else:
            chunk.x1, chunk.y1 = chunk.x2, chunk.y2

        chunk.list = [self.KEY[chunk.x1][chunk.y1], self.KEY[chunk.x2][chunk.y2]]

        return chunk.list

    def decrypt_chunk(self, chunk):
        chunk = Chunk(chunk)

        for i in range(5):
            for j in range(5):
                if chunk.list[0] == self.KEY[i][j]:
                    chunk.x1 = i
                    chunk.y1 = j
                if chunk.list[1] == self.KEY[i][j]:
                    chunk.x2 = i
                    chunk.y2 = j

        if chunk.x1 == chunk.x2:
            chunk.x1 -= 1
            chunk.x2 -= 1
            chunk.x1 %= 5
            chunk.x2 %= 5
        elif chunk.y1 == chunk.y2:
            chunk.y1 -= 1
            chunk.y2 -= 1
            chunk.y1 %= 5
            chunk.y2 %= 5
        else:
            chunk.x1, chunk.y1 = chunk.x2, chunk.y2

        chunk.list = [self.KEY[chunk.x1][chunk.y1], self.KEY[chunk.x2][chunk.y2]]

        return chunk.list


class Chunk:
    def __init__(self, list):
        self.list = list
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None


if __name__ == '__main__':
    input_str = 'cdab'
    key = 'key'
    # mode = 'e'
    mode = 'd'
    Playfair(input_str, key, mode)
