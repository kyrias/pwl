import sys


def split_by_2(seq):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:2]
        seq = seq[2:]


def build_word_list(path):
    with open(path, 'rb') as f:
        contents = f.read().decode('utf-8')

    word_dict = {}
    words = contents.splitlines()
    for idx, word in enumerate(words):
        key = format(idx, '02X')
        word_dict[key] = word

    return word_dict


def convert_fingerprint(fp):
    words = []
    for idx, byte in enumerate(fp):
        if idx % 2 == 0:
            words.append(even[byte])
        else:
            words.append(odd[byte])

    return words


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('error: No fingerprint given', file=sys.stderr)

    fp = sys.argv[1]
    fp = fp.replace(' ', '')

    odd = build_word_list('odd.txt')
    even = build_word_list('even.txt')

    encoded = convert_fingerprint(split_by_2(fp))
    print(' '.join(encoded))
