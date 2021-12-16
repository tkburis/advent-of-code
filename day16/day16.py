# https://adventofcode.com/2021/day/16

# Helper functions
def get_version(bina):
    return int(bina[0:3], 2)

def get_type(bina):
    return int(bina[3:6], 2)

def get_lit_value(bina):
    i = 6
    val = ""
    while True:
        val += bina[i+1:i+5]
        if bina[i] == '0':
            break
        i += 5
    return int(val, 2), i+5

def get_length_type(bina):
    return 15 if bina[6] == '0' else 11

def get_length(bina):
    if get_length_type(bina) == 15:
        return int(bina[7:22], 2)
    return int(bina[7:18], 2)

def p1_parser(bina):
    if get_type(bina) == 4:
        return get_version(bina), get_lit_value(bina)[1]

    version_sum = get_version(bina)
    if get_length_type(bina) == 15:
        curr_index = 22
        while curr_index < get_length(bina) + 22:
            ret = p1_parser(bina[curr_index:])
            version_sum += ret[0]
            curr_index += ret[1]
    else:
        curr_index = 18
        for _ in range(get_length(bina)):
            ret = p1_parser(bina[curr_index:])
            version_sum += ret[0]
            curr_index += ret[1]
    return version_sum, curr_index

def p2_parser(bina):
    p_type = get_type(bina)
    if p_type == 4:
        return get_lit_value(bina)  # (literal value, current index)

    # Gather up the elements
    elems = []
    if get_length_type(bina) == 15:
        curr_index = 22
        while curr_index < get_length(bina) + 22:
            ret = p2_parser(bina[curr_index:])
            elems.append(ret[0])
            curr_index += ret[1]
    else:
        curr_index = 18
        for _ in range(get_length(bina)):
            ret = p2_parser(bina[curr_index:])
            elems.append(ret[0])
            curr_index += ret[1]

    # Do the operations
    if p_type == 0:
        res = sum(elems)
    elif p_type == 1:
        res = 1
        for x in elems: res *= x
    elif p_type == 2:
        res = min(elems)
    elif p_type == 3:
        res = max(elems)
    elif p_type == 5:
        res = int(elems[0] > elems[1])
    elif p_type == 6:
        res = int(elems[0] < elems[1])
    elif p_type == 7:
        res = int(elems[0] == elems[1])
    return res, curr_index

def driver(bina):
    print('Part 1:', p1_parser(bina)[0])
    print('Part 2:', p2_parser(bina)[0])

def main():
    with open("input.txt", "r") as f:
        hexa = f.readline().strip()
    bina = bin(int(hexa, 16))[2:].zfill(len(hexa) * 4)
    driver(bina)

if __name__ == "__main__":
    main()

