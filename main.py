
X8REDUX = int("00011011", 2)
MIXCOL = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]
MIXCOL_inverse = [['e', 'b', 'd', '9'], ['9', 'e', 'b', 'd'], ['d', '9', 'e', 'b'], ['b', 'd', '9', 'e']]
s_box = [
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
]

inverse_s_box = [
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
]

RC = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']

def safe_hex(x, length=2):
    ret = hex(x)[2:]
    if len(ret) < length:
        for i in range(length - len(ret)):
            ret = '0' + ret
    return ret

def ip_to_matrix(ip):
    a, b, c, d = [], [], [], []
    i, j = 0, 2
    a.append(ip[i:j])
    i = i + 2
    j = j + 2
    b.append(ip[i:j])
    i = i + 2
    j = j + 2
    c.append(ip[i:j])
    i = i + 2
    j = j + 2
    d.append(ip[i:j])
    for x in range(3):
        i = i + 2
        j = j + 2
        a.append(ip[i:j])
        i = i + 2
        j = j + 2
        b.append(ip[i:j])
        i = i + 2
        j = j + 2
        c.append(ip[i:j])
        i = i + 2
        j = j + 2
        d.append(ip[i:j])
    return [a, b, c, d]

def print_matrix(matrix):
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print(matrix[3])

def print_matrix_line(matrix):
    for i in range(4):
        for j in range(4):
            print(matrix[j][i], end='')
    print()

# multiply by 2 by shifting bits to left by 1. Takes in byte in hex form
# returns in hex form
def mult2(h):
    carry = False
    byte = int(h, 16)

    mask = int('10000000', 2)
    if mask & byte != 0:
        carry = True

    shifted = byte << 1

    if carry:
        ret = xor(safe_hex(shifted)[1:], safe_hex(X8REDUX))
    else:
        ret = safe_hex(shifted)

    return ret

# multiplies by 3. takes in and returns in hex form
def mult3(h):
    carry = False
    byte = int(h, 16)

    mask = int('10000000', 2)
    if mask & byte != 0:
        carry = True

    shifted = byte << 1

    if carry:
        m2 = xor(safe_hex(shifted)[1:], safe_hex(X8REDUX))
    else:
        m2 = safe_hex(shifted)

    m3 = int(m2, 16) ^ byte

    return safe_hex(m3)

# multiplies by 9
def mult9(h):
    byte = int(h, 16)
    og = byte

    #   X8
    for i in range(3):

        #   X2
        carry = check_overflow(byte)
        byte = byte << 1
        if carry:
            byte = xor(safe_hex(byte)[1:], safe_hex(X8REDUX))
        else:
            byte = safe_hex(byte)
        byte = int(byte, 16)

    #   + 1
    byte = byte ^ og

    return safe_hex(byte)

# multiplies by 11
def multB(h):
    byte = int(h, 16)
    og = byte

    #   X4 = 4x
    for i in range(2):

        #   X2
        carry = check_overflow(byte)
        byte = byte << 1
        if carry:
            byte = xor(safe_hex(byte)[1:], safe_hex(X8REDUX))
        else:
            byte = safe_hex(byte)
        byte = int(byte, 16)

    #   +1 = 5x
    byte = byte ^ og

    #   x2 = 10x
    carry = check_overflow(byte)
    byte = byte << 1
    if carry:
        byte = xor(safe_hex(byte)[1:], safe_hex(X8REDUX))
    else:
        byte = safe_hex(byte)
    byte = int(byte, 16)

    #   +1 = 11x
    byte = byte ^ og

    return safe_hex(byte)


# multiplies by 13
def multD(h):
    byte = int(h, 16)
    og = byte

    #   x 2 = 2x
    carry = check_overflow(byte)
    byte = byte << 1
    if carry:
        byte = xor(safe_hex(byte)[1:], safe_hex(X8REDUX))
    else:
        byte = safe_hex(byte)
    byte = int(byte, 16)

    #   + 1 = 3x
    byte = byte ^ og

    #   x 4 = 12x
    for i in range(2):

        #   X2
        carry = check_overflow(byte)
        byte = byte << 1
        if carry:
            byte = xor(safe_hex(byte)[1:], safe_hex(X8REDUX))
        else:
            byte = safe_hex(byte)
        byte = int(byte, 16)

    #   + 1 = 13x
    byte = byte ^ og

    return safe_hex(byte)

# multiplies by 14
def multE(h):
    byte = int(h, 16)
    og = byte

    #   x 2 = 2x
    carry = check_overflow(byte)
    byte = byte << 1
    if carry:
        byte = xor(safe_hex(byte)[1:], safe_hex(X8REDUX))
    else:
        byte = safe_hex(byte)
    byte = int(byte, 16)

    #   + 1 = 3x
    byte = byte ^ og

    #   og x 2 = 2x og
    carry = check_overflow(og)
    og = og << 1
    if carry:
        og = xor(safe_hex(og)[1:], safe_hex(X8REDUX))
    else:
        og = safe_hex(og)
    og = int(og, 16)

    #   x 4 = 12x
    for i in range(2):

        #   X2
        carry = check_overflow(byte)
        byte = byte << 1
        if carry:
            byte = xor(safe_hex(byte)[1:], safe_hex(X8REDUX))
        else:
            byte = safe_hex(byte)
        byte = int(byte, 16)

    #   + 2 = 14x
    byte = byte ^ og

    return safe_hex(byte)

def check_overflow(byte):
    mask = int('10000000', 2)
    if mask & byte != 0:
        return True
    return False

# XOR between two Hex values. Returns a string in Hex
def xor(h1, h2, length=2):

    byte1 = int(h1, 16)
    byte2 = int(h2, 16)

    ret = safe_hex(byte1 ^ byte2, length)

    return ret

def mix_column_layer(state_matrix):
    col_state_matrix = list(map(list, zip(*state_matrix)))
    col_state_matrix[0] = mix_column_multiplication(col_state_matrix[0])
    col_state_matrix[1] = mix_column_multiplication(col_state_matrix[1])
    col_state_matrix[2] = mix_column_multiplication(col_state_matrix[2])
    col_state_matrix[3] = mix_column_multiplication(col_state_matrix[3])
    state_matrix = list(map(list, zip(*col_state_matrix)))
    return state_matrix

def mix_column_layer_inverse(state_matrix):
    col_state_matrix = list(map(list, zip(*state_matrix)))
    col_state_matrix[0] = mix_column_multiplication_inverse(col_state_matrix[0])
    col_state_matrix[1] = mix_column_multiplication_inverse(col_state_matrix[1])
    col_state_matrix[2] = mix_column_multiplication_inverse(col_state_matrix[2])
    col_state_matrix[3] = mix_column_multiplication_inverse(col_state_matrix[3])
    state_matrix = list(map(list, zip(*col_state_matrix)))
    return state_matrix

def mix_column_multiplication(col):
    new_col = []
    for i in range(4):
        xor_list = []
        mult_vals = MIXCOL[i]
        for j in range(4):
            if mult_vals[j] == 1:
                xor_list.append(col[j])
            elif mult_vals[j] == 2:
                xor_list.append(mult2(col[j]))
            elif mult_vals[j] == 3:
                xor_list.append(mult3(col[j]))
        new_val_dec = int(xor_list[0], 16) ^ int(xor_list[1], 16) ^ int(xor_list[2], 16) ^ int(xor_list[3], 16)
        new_col.append(safe_hex(new_val_dec))
    return new_col

def mix_column_multiplication_inverse(col):
    new_col = []
    for i in range(4):
        xor_list = []
        mult_vals = MIXCOL_inverse[i]
        for j in range(4):
            if mult_vals[j] == '9':
                xor_list.append(mult9(col[j]))
            elif mult_vals[j] == 'b':
                xor_list.append(multB(col[j]))
            elif mult_vals[j] == 'd':
                xor_list.append(multD(col[j]))
            elif mult_vals[j] == 'e':
                xor_list.append(multE(col[j]))
        new_val_dec = int(xor_list[0], 16) ^ int(xor_list[1], 16) ^ int(xor_list[2], 16) ^ int(xor_list[3], 16)
        new_col.append(safe_hex(new_val_dec))
    return new_col

def byte_sub_layer(state_matrix):
    for i in range(4):
        for j in range(4):
            state_matrix[i][j] = byte_sub(state_matrix[i][j])

def byte_sub(str_byte):
    byte = int(str_byte, 16)
    return safe_hex(s_box[byte])

def byte_sub_layer_inverse(state_matrix):
    for i in range(4):
        for j in range(4):
            state_matrix[i][j] = byte_sub_inverse(state_matrix[i][j])

def byte_sub_inverse(str_byte):
    byte = int(str_byte, 16)
    return safe_hex(inverse_s_box[byte])

def shift_rows_layer(state_matrix):
    for i in range(4):
        state_matrix[i] = state_matrix[i][i:] + state_matrix[i][:i]

def shift_rows_layer_inverse(state_matrix):
    for i in range(4):
        state_matrix[i] = state_matrix[i][4-i:] + state_matrix[i][:4-i]

def g(byte_block, round):
    shifted_byte_block = byte_block[2:] + byte_block[0:2]
    transform = []
    for i in range(4):
        transform.append(byte_sub(shifted_byte_block[2*i:2*i + 2]))
    transform[0] = xor(transform[0], RC[round - 1])
    return transform[0] + transform[1] + transform[2] + transform[3]

def compute_subkey_word_one(prev_w, round):
    return xor(prev_w[0:8], g(prev_w[24:], round), length=8)

def generate_subkeys(key):
    w = [key, '', '', '', '', '', '', '', '', '', '']
    for round in range(1, 11):
        w[round] = compute_subkey_word_one(w[round - 1], round)
        for j in range(1, 4):
            w[round] = w[round] + xor(w[round][-8:], w[round - 1][8 * j:8 * (j + 1)], length=8)
        # print(w[round] == gt[round - 1])
    return w

def key_addition_layer(state_matrix, key):
    key_matrix = ip_to_matrix(key)
    for i in range(4):
        for j in range(4):
            state_matrix[i][j] = xor(state_matrix[i][j], key_matrix[i][j])

def key_addition_layer_inverse(state_matrix, key):
    key_addition_layer(state_matrix, key)

def state_matrix_to_ciphertext(state_matrix):
    col_state_matrix = list(map(list, zip(*state_matrix)))
    ciphertext = ''
    for i in range(4):
        for j in range(4):
            ciphertext = ciphertext + col_state_matrix[i][j]
    return ciphertext

def hex_to_ascii(hex_str):
    bytes_object = bytes.fromhex(hex_str)
    ascii_string = bytes_object.decode("ASCII")
    return ascii_string

def encrypt(plaintext, key):
    print("round[ 0 ].input:", plaintext)
    print("round[ 0 ].k_sch:", key)
    state_matrix = ip_to_matrix(plaintext)
    subkeys = generate_subkeys(key)
    key_addition_layer(state_matrix, key)
    for round in range(1, 11):
        print("round[", round, "].start:", state_matrix_to_ciphertext(state_matrix))
        byte_sub_layer(state_matrix)
        print("round[", round, "].s_box:", state_matrix_to_ciphertext(state_matrix))
        shift_rows_layer(state_matrix)
        print("round[", round, "].s_row:", state_matrix_to_ciphertext(state_matrix))
        if round < 10:
            state_matrix = mix_column_layer(state_matrix)
            print("round[", round, "].m_col:", state_matrix_to_ciphertext(state_matrix))
        key_addition_layer(state_matrix, subkeys[round])
        print("round[", round, "].k_sch:", subkeys[round])
    print("round[10].output:", state_matrix_to_ciphertext(state_matrix))
    return state_matrix_to_ciphertext(state_matrix)

def decrypt(ciphertext, key):
    print("round[ 0 ].iinput:", ciphertext)
    subkeys = generate_subkeys(key)
    state_matrix = ip_to_matrix(ciphertext)
    for round in range(1, 11):
        print("round[", round, "].istart:", state_matrix_to_ciphertext(state_matrix))
        key_addition_layer_inverse(state_matrix, subkeys[11 - round])
        print("round[", round,"].ik_sch:", subkeys[11 - round])
        if round > 1:
            state_matrix = mix_column_layer_inverse(state_matrix)
            print("round[", round,"].im_col:", state_matrix_to_ciphertext(state_matrix))
        shift_rows_layer_inverse(state_matrix)
        print("round[", round,"].is_row:", state_matrix_to_ciphertext(state_matrix))
        byte_sub_layer_inverse(state_matrix)
        print("round[", round,"].is_box:", state_matrix_to_ciphertext(state_matrix))
    key_addition_layer_inverse(state_matrix, key)
    print("round[10].ioutput:", state_matrix_to_ciphertext(state_matrix))
    return state_matrix_to_ciphertext(state_matrix)

print("Deliverable 1: Appendix C.1 Example:\n")
plaintext = '00112233445566778899aabbccddeeff'
key = '000102030405060708090a0b0c0d0e0f'

ciphertext = encrypt(plaintext, key)
print()
plaintext = decrypt(ciphertext, key)
print()

print("Deliverable 2: Second Decryption:\n")
key2 = '303132333435363738393A3B3C3D3E3F'
ciphertext2 = 'F4351503AA781C520267D690C42D1F43'
plaintext2 = decrypt(ciphertext2, key2)
print("ASCII Representation:", hex_to_ascii(plaintext2))

