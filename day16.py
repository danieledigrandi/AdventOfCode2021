from day1 import get_mode


def literal_packet(pack):

    i = 0
    packet = 0

    while True:
        label = pack[i]
        i += 1
        packet = packet << 4 | (int(pack[i:i + 4], 2))
        i += 4

        if label == "0":
            break

    return i, packet


def find_packets(message):
    global version_sum
    packet = 0
    idx = 0

    version = int(message[idx:3], 2)
    version_sum += version
    idx += 3
    type_id = int(message[idx:idx + 3], 2)
    idx += 3

    if type_id == 4:  # literal packet
        i, packet = literal_packet(message[idx:])
        idx += i

    else:
        length_type_id = message[idx]
        idx += 1
        packs = []

        if length_type_id == "0":
            sub_length = int(message[idx:idx + 15], 2)
            idx += 15
            k = idx + sub_length

            while idx < k - 6:
                j, p = find_packets(message[idx:idx + k])
                idx += j
                packs.append(p)

        else:
            sub_length = int(message[idx:idx + 11], 2)
            idx += 11

            for p in range(sub_length):
                j, p = find_packets(message[idx:])
                idx += j
                packs.append(p)

        if type_id == 0:
            packet = sum(packs)

        elif type_id == 1:
            packet = 1
            for p in packs:
                packet *= p

        elif type_id == 2:
            packet = min(packs)

        elif type_id == 3:
            packet = max(packs)

        elif type_id == 5:
            packet = int(packs[0] > packs[1])

        elif type_id == 6:
            packet = int(packs[0] < packs[1])

        elif type_id == 7:
            packet = int(packs[0] == packs[1])

    return idx, packet


def open_file(path):

    with open(path, 'r') as f:
        hexadecimal = [x for x in f.readline().strip()]

    hex_to_bin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    binary = "".join([hex_to_bin[digit] for digit in hexadecimal])

    return binary


def main():
    path = "./data/input_day_16.txt"
    binary = open_file(path)

    idx, packets = find_packets(binary)

    mode = get_mode()

    if mode == 1:
        print("p1", version_sum)

    elif mode == 2:
        print("p2", packets)


if __name__ == '__main__':
    versions = []
    version_sum = 0
    main()
