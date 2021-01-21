import socket
import sys

# CLI (Command Line Interface)
# run from terminal: filname server(required) port(optional)
import requests

if len(sys.argv) not in [2, 3]:
    print('''Improper number of arguments: at least one is required and not more than two are allowed:
        - hhtp server's address (required)
        - port number(defaults to 80 if not specified)''')
    sys.exit(1)
else:
    server = sys.argv[1]
    port = 80
    if len(sys.argv) == 3:
        if not sys.argv[2].isdigit():
            print('Port number is invalid - exiting')
            sys.exit(2)
        else:
            port = int(sys.argv[2])
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server, port))
        sock.send(b"HEAD / HTTP/1.1\r\nHost: " + bytes(server, "utf8") + b"\r\nConnection: close\r\n\r\n")
        reply = sock.recv(1000)
    except requests.exceptions.Timeout:
        print('Connection timeout.')
        sys.exit(3)
    except Exception as e:
        print(e)
        sys.exit(4)
    else:
        print(repr(reply).split('\\r\\n')[0][2:])