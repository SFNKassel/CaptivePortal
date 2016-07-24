def read_file(filename):
    dictionary = {}
    f = open(filename, "r")
    for line in f:
        dictionary[line.split("#")[0]] = line.split("#")[1].strip()
    f.close()
    return dictionary


def write_file(filename, dictionary):
    f = open(filename, "w")
    for i in dictionary:
        f.write(str(i) + "#" + str(dictionary[i]) + "\n")
    f.flush()
    f.close()
