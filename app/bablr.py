import hashlib
import binascii

def lookup(index):
    sha512 = hashlib.sha512()
    sha512.update(index)
    index_hash = sha512.hexdigest()
    return hash2string(index_hash)

def hash2string(input_hash):
    bstream = BitStream(input_hash)
    result = ''
    while len(bstream) >= 5:
        val = bstream.getBits(5)
        char = int2char(val)
        result += char
    return result

# 32 chars => mapped by 5 bits
charset = 'abcdefghijklmnopqrstuvwxyz,.@#  '
def int2char(x):
    return charset[x]

class BitStream():
    def __init__(self, string):
        self._barray = '{0:8b}'.format(int(string, 16))

    def __len__(self):
        return len(self._barray)

    def getBits(self, num_bits):
        if len(self) < num_bits:
            return None
        bits = self._barray[0:num_bits]
        self._barray = self._barray[num_bits:]
        return int(bits, 2)

if __name__ == '__main__':
    import sys
    print lookup(sys.argv[1])
