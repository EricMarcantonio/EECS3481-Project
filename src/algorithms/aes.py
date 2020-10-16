encoding: str = "utf-8"

s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inverted_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)


def inverted_shift_rows(sub):
    sub[0][1], sub[1][1], sub[2][1], sub[3][1] = sub[3][1], sub[0][1], sub[1][1], sub[2][1]
    sub[0][2], sub[1][2], sub[2][2], sub[3][2] = sub[2][2], sub[3][2], sub[0][2], sub[1][2]
    sub[0][3], sub[1][3], sub[2][3], sub[3][3] = sub[1][3], sub[2][3], sub[3][3], sub[0][3]


def add_round_key(sub: list, key: list):
    for i in range(4):
        for j in range(4):
            sub[i][j] ^= key[i][j]


def xor_bytes(a: bytearray, b: bytearray):
    return bytearray(i ^ j for i, j in zip(a, b))


key_lengths = {
    16: 10,
    24: 12,
    32: 14,
}


def fix_byte_80(byte):
    if byte & 0x80:
        return ((byte << 1) ^ 0x1B) & 0xFF
    else:
        return byte << 1


def mix_single_column(state: list):
    a = state[0] ^ state[1] ^ state[2] ^ state[3]
    b = state[0]
    state[0] ^= a ^ fix_byte_80(state[0] ^ state[1])
    state[1] ^= a ^ fix_byte_80(state[1] ^ state[2])
    state[2] ^= a ^ fix_byte_80(state[2] ^ state[3])
    state[3] ^= a ^ fix_byte_80(state[3] ^ b)


def mix_columns(state: list):
    for i in range(4):
        mix_single_column(state[i])


def invert_mix_columns(state: list):
    for i in range(4):
        a = fix_byte_80(fix_byte_80(state[i][0] ^ state[i][2]))
        b = fix_byte_80(fix_byte_80(state[i][1] ^ state[i][3]))
        state[i][0] ^= a
        state[i][1] ^= b
        state[i][2] ^= a
        state[i][3] ^= b

    mix_columns(state)


def create_matrix(plain_text_in_bytes: bytearray):
    """
    :param plain_text_in_bytes: 16 byte array
    """
    # There is most likely better way but I suck at math
    '''
    Column Major (MATH-1025)
    [
        b0, b4, b8, b12,
        b1, b5, b9, b13,
        b2, b6, b10, b14,
        b3, b7, b11, b15,
    ]

    '''
    matrix = [bytearray() for _ in range(0, 4)]

    matrix[0] = bytearray([plain_text_in_bytes[0], plain_text_in_bytes[4], plain_text_in_bytes[8],
                           plain_text_in_bytes[12]])
    matrix[1] = bytearray([plain_text_in_bytes[1], plain_text_in_bytes[5], plain_text_in_bytes[9],
                           plain_text_in_bytes[13]])
    matrix[2] = bytearray([plain_text_in_bytes[2], plain_text_in_bytes[6], plain_text_in_bytes[10],
                           plain_text_in_bytes[14]])
    matrix[3] = bytearray([plain_text_in_bytes[3], plain_text_in_bytes[7], plain_text_in_bytes[11],
                           plain_text_in_bytes[15]])
    return matrix


round_constant = (
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x80, 0x1b, 0x36
)

hex_conversion = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
}


def new_sub(byte):
    # print(str(bytes(chr(byte), encoding=encoding).hex()))
    b0 = bytes([byte]).hex()[0]
    b1 = bytes([byte]).hex()[1]

    return int(hex(s_box[hex_conversion[b0] * 16 + hex_conversion[b1]]), base=16)


def gmul(a: int, b: int):
    p = 0
    while a and b:
        if b % 2 == 1:
            p ^= a
        if a >= 128:
            a = (a << 1) ^ 0x11b
        else:
            a <<= 1
        b >>= 1

    return p


def print_matrix(matrix: list):
    print("___________")
    for eachLine in matrix:
        for x in range(0, 8, 2):
            print(eachLine.hex().upper()[x: x + 2], end=" ")
        print()


def flippy(state: list):
    return [
        bytearray([
            state[0][0], state[1][0], state[2][0], state[3][0]
        ]),
        bytearray([
            state[0][1], state[1][1], state[2][1], state[3][1]
        ]),
        bytearray([
            state[0][2], state[1][2], state[2][2], state[3][2]
        ]),
        bytearray([
            state[0][3], state[1][3], state[2][3], state[3][3]
        ])
    ]


def from_matrix_to_bytearray(matrix: list) -> bytearray:
    lol = bytearray()
    for i in range(0, 4):
        for j in range(0, 4):
            lol.append(matrix[i][j])
    return lol


def printf(text: str):
    for x in range(0, len(text), 2):
        print(text[x: x + 2].upper(), end=" ")
    print()


def sub_bytes(state):
    for x in range(0, 4):
        state[x] = bytearray(new_sub(w) for w in state[x])


def shift_rows(state):
    state[1] = bytearray([state[1][1], state[1][2], state[1][3], state[1][0]])
    state[2] = bytearray([state[2][2], state[2][3], state[2][0], state[2][1]])
    state[3] = bytearray([state[3][3], state[3][0], state[3][1], state[3][2]])


class AES:
    byte_array: list = None
    key_byte_array: bytearray = None
    key_matrix: list = None
    rcon_step = 0

    def __init__(self, byte_array: bytearray, secret_key: str):
        super().__init__()
        self.byte_array = create_matrix(byte_array)
        self.key_byte_array = bytearray(secret_key, encoding=encoding)
        self.key_matrix = create_matrix(self.key_byte_array)

    def g(self, matrix_4: bytearray):
        # Swap
        # printf(matrix_4.hex().upper())
        matrix_4.append(matrix_4.pop(0))
        # printf(matrix_4.hex().upper())

        # SubBytes
        for x in range(0, 4):
            matrix_4[x] = new_sub(matrix_4[x])
        # RCON
        # printf(matrix_4.hex().upper())

        matrix_4[0] ^= round_constant[self.rcon_step]
        # printf(matrix_4.hex().upper())
        self.rcon_step += 1
        return matrix_4

    def expand_128_key(self, key: bytearray):
        # print(key.hex().upper())
        k = [bytearray() for _ in range(0, 8)]
        k[0] = key[0:4]
        k[1] = key[4:8]
        k[2] = key[8:12]
        k[3] = key[12:16]
        k[4] = xor_bytes(k[0], self.g(key[12:16]))
        k[5] = xor_bytes(k[4], k[1])
        k[6] = xor_bytes(k[5], k[2])
        k[7] = xor_bytes(k[6], k[3])

        return k[4::]

    def encrypt(self):
        state = self.key_matrix
        # 0 XOR THE BYTES
        keys_ready_to_be_xored = [self.key_byte_array]

        for x in range(0, 9):
            keys_ready_to_be_xored.append(from_matrix_to_bytearray(self.expand_128_key(keys_ready_to_be_xored[x])))




        '''
        • Round 0: 54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75
        • Round 1: E2 32 FC F1 91 12 91 88 B1 59 E4 E6 D6 79 A2 93
        • Round 2: 56 08 20 07 C7 1A B1 8F 76 43 55 69 A0 3A F7 FA
        • Round 3: D2 60 0D E7 15 7A BC 68 63 39 E9 01 C3 03 1E FB
        • Round 4: A1 12 02 C9 B4 68 BE A1 D7 51 57 A0 14 52 49 5B
        • Round 5: B1 29 3B 33 05 41 85 92 D2 10 D2 32 C6 42 9B 69
        
        
        • Round 6: BD 3D C2 B7 B8 7C 47 15 6A 6C 95 27 AC 2E 0E 4E
        • Round 7: CC 96 ED 16 74 EA AA 03 1E 86 3F 24 B2 A8 31 6A
        • Round 8: 8E 51 EF 21 FA BB 45 22 E4 3D 7A 06 56 95 4B 6C
        • Round 9: BF E2 BF 90 45 59 FA B2 A1 64 80 B4 F7 F1 CB D8
        • Round 10: 28 FD DE F8 6D A4 24 4A CC C0 A4 FE 3B 31 6F 26

        '''


        # # 1
        state = [xor_bytes(state[x], keys_ready_to_be_xored[0]) for x in range(0, 4)]

        for x in range(1, 9):
            sub_bytes(state)
            shift_rows(state)
            state = flippy(state)
            mix_columns(state)
            state = flippy(state)
            state = [xor_bytes(state[x], keys_ready_to_be_xored[x]) for x in range(0, 4)]

        sub_bytes(state)
        shift_rows(state)
        state = [xor_bytes(state[x], keys_ready_to_be_xored[9]) for x in range(0, 4)]
        printf(from_matrix_to_bytearray(state).hex())

        #           TESTING


file_array_bytes = bytearray("Two One Nine Two", encoding="utf-8")

file = AES(file_array_bytes, "Thats my Kung Fu")
file.encrypt()
