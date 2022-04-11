FIELDS = ['iface', 'inet', 'address', 'netmask', 'gateway', 'domain', 'nameserver', 'hostname']

data_dict = {
    FIELDS[0]: None,
    FIELDS[1]: None,
    FIELDS[2]: None,
    FIELDS[3]: None,
    FIELDS[4]: None,
    FIELDS[5]: None,
    FIELDS[6]: [],
    FIELDS[7]: None
}


def read_to_dict():
    """
    This function reads data from a txt file to a dictionary
    :param filename: file to read from
    :return: dictionary contining read data
    """
    filename = "input_dir/interfaces.txt"
    if filename == "interfaces.txt":
        f = open(filename, 'r')
        f = f.read()
        f = f.replace('\n', ' ')
        f = f.split(' ')
        # print(f)
        for i in range(len(f)):
            for j in range(len(FIELDS)):
                if f[i] == FIELDS[j]:
                    data_dict[FIELDS[j]] = f[i + 1]
    filename = "input_dir/resolve.txt"
    if filename == "resolve.txt":
        f = open(filename, 'r')
        f = f.read()
        f = f.replace('\n', ' ')
        f = f.split(' ')
        f = list(filter(None, f))
        f = list(filter(bool, f))
        f = list(filter(len, f))
        f = list(filter(lambda item: item, f))
        # print(f)
        for i in range(len(f)):
            for j in range(len(FIELDS)):
                if f[i] == FIELDS[j]:
                    if FIELDS[j] == 'nameserver':
                        data_dict[FIELDS[j]].append(f[i + 1])
                    else:
                        data_dict[FIELDS[j]] = f[i + 1]
    # TEMPORARY
    data_dict['hostname'] = "myhost"
    return data_dict


# print(read_to_dict("answers.txt"))
# print(read_to_dict("interfaces.txt"))
print(read_to_dict())
