
X8REDUX = int("00011011", 2)
MIXCOL = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]

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

def remove_prefix(h):
    if h[0:2] == '0b' or h[0:2] == '0x':
        h = h[2:]
    return h


# multiply by 2 by shifting bits to left by 1. Takes in byte in hex form
# returns in hex form
def mult2(h):
    carry = False
    h = remove_prefix(h)
    byte = int(h, 16)

    mask = int('10000000', 2)
    if mask & byte != 0:
        carry = True

    shifted = byte << 1

    if carry:
        ret = xor(hex(shifted)[3:], hex(X8REDUX))
    else:
        ret = hex(shifted)[2:]

    return ret

# multiplies by 3. takes in and returns in hex form
def mult3(h):
    carry = False
    h = remove_prefix(h)
    byte = int(h, 16)

    mask = int('10000000', 2)
    if mask & byte != 0:
        carry = True

    shifted = byte << 1

    if carry:
        m2 = xor(hex(shifted)[3:], hex(X8REDUX))
    else:
        m2 = hex(shifted)[2:]

    m3 = int(m2, 16) ^ byte

    return hex(m3)[2:]

# XOR between two Hex values. Returns a string in Hex
def xor(h1, h2):

    h1 = remove_prefix(h1)
    h2 = remove_prefix(h2)

    byte1 = int(h1, 16)
    byte2 = int(h2, 16)

    ret = hex(byte1 ^ byte2)[2:]

    return ret

def mix_column_layer(state_matrix):
    col_state_matrix = list(map(list, zip(*state_matrix)))

    col_state_matrix[0] = mix_column_multiplication(col_state_matrix[0])
    col_state_matrix[1] = mix_column_multiplication(col_state_matrix[1])
    col_state_matrix[2] = mix_column_multiplication(col_state_matrix[2])
    col_state_matrix[3] = mix_column_multiplication(col_state_matrix[3])

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
        new_col.append(hex(new_val_dec)[2:])

    return new_col

ip = "00112233445566778899aabbccddeeff"
matrix = ip_to_matrix(ip)

print('input matrix')
print_matrix(matrix)

matrix = mix_column_layer(matrix)
print_matrix(matrix)
