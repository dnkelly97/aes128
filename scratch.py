byte1 = int('101100', 2)
byte2 = int('110', 2)

H = 2  # header (0x__, 0b__)
x = str(bin(byte1))[H+3:]  # what's going to be shifted off
byte3 = int(x + bin(byte1 >> 3)[H:])  # shift 3 with wraparound
# print(byte3)
# print(byte1 >> 3)


# print(byte1)
# print(byte2)
a = byte1 ^ byte2  # XOR

# print(bin(a))

byte1 = int('11000',2)
mask = int('01000',2)  # testing for specific bit set
# print(byte1 & mask)

a = int('1100',2)
b = int('1111',2)
c = int('0101',2)

print(a ^ b ^ c)