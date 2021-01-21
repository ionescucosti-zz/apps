import sys


def read_input(file):
    f = open(file, 'rb')
    data = bytearray(f.read())
    f.close()
    return [data, file]


def write_output(input_data):
    f = open('reversed_' + input_data[1], 'wb')
    reversed_data = input_data[0][::-1]
    f.write(reversed_data)
    f.close()
    return reversed_data


if __name__ == '__main__':
    try:
        for i in range(1, len(sys.argv)):
            data = read_input(sys.argv[i])
            write_output(data)
    except IOError as e:
        print("I/O error occurred:", str(e.errno))
