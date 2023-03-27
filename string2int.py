# https://stackoverflow.com/questions/50237263/convert-string-to-64bit-integer-mapping-characters-to-custom-two-bit-values-mapp

"""
Map a string of characters (A, T, C, G) into a 64 bit integer where each letter is represented as two bits using this mapping:

mapping = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11} 
The "sequence" string will not be longer than 28 characters, and I intend for the integer to be zero-padded at the beginning to make it 64 bits. 
At typical sequence input would be something like: 'TGTGAGAAGCACCATAAAAGGCGTTGTG'
"""

"""
You are interpreting a string of 4 different 'digits' as a number, so a base 4 notation. If you had a string of actual digits, in the range 0-3, you could have int() produce an integer really fast.
"""

def seq_to_int(seq, _m=str.maketrans('ACGT', '0123')):
    return int(seq.translate(_m), 4)

# from random import choice
# print(testvalues := [''.join([choice('ATCG') for _ in range(28)]) for _ in range(10 ** 6)])

# from timeit import timeit
# timeit('seq_to_int(next(tviter))', 'from __main__ import testvalues, seq_to_int; tviter=iter(testvalues)')

def seq_to_int_alexhall_b(seq, mapping={'A': b'00', 'C': b'01', 'G': b'10', 'T': b'11'}):
    print(b''.join([mapping[c] for c in seq]), 2)
    print(b''.join([mapping[c] for c in seq]))
    return int(b''.join([mapping[c] for c in seq]), 2)

def seq_to_int_jonathan_may(seq, mapping={'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}):
    result = 0
    for char in seq:
        result = result << 2
        result = result | mapping[char]
    return result

sequence = 'TGTGAGAAGCACCATAAAAGGCGTTGTG'
print(result := seq_to_int(sequence))
print(result := seq_to_int_alexhall_b(sequence))
print(result := seq_to_int_jonathan_may(sequence))

print(result := format(seq_to_int(sequence), '016x'))
print(result := format(seq_to_int_alexhall_b(sequence), '016x'))
print(result := format(seq_to_int_jonathan_may(sequence), '016x'))

print(result := format(seq_to_int(sequence), '064b'))
print(result := format(seq_to_int_alexhall_b(sequence), '064b'))
print(result := format(seq_to_int_jonathan_may(sequence), '064b'))

print(result := format(int(sequence.translate(str.maketrans('ACGT', '0123')), 4), '016x'))
print(result := format(int(sequence.translate(str.maketrans('ACGT', '0123')), 4), '064b'))


