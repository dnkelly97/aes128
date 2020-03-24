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
    if 'b' in h:
        h = h[2:]
    return h


# multiply by 2 by shifting bits to left by 1. Takes in byte in hex form
def mult2(h):
    # carry = False
    h = remove_prefix(h)
    byte = int(h, 16)
    print(byte)

    mask = int('10000000', 2)
    carry = mask & byte
    print(carry)

    ret = byte << 1
    print(ret)


# XOR between two Hex values. Returns a string in Hex
def xor(h1, h2):

    h1 = remove_prefix(h1)
    h2 = remove_prefix(h2)

    byte1 = int(h1, 16)
    byte2 = int(h2, 16)

    print(byte1)
    print(byte2)

    ret = hex(byte1 ^ byte2)[2:]
    print(ret)

    return ret


ip = "00112233445566778899aabbccddeeff"
matrix = ip_to_matrix(ip)
# print_matrix(matrix)

a = 'ee'
b = '01'
# xor(a,b)


c = '81'
mult2(c)
