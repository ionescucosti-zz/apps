import os
import ssl
import sys

import requests

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

# education.pythoninstitute.org
# http://localhost:3000/cars

if len(sys.argv) not in [2, 3]:
    print('''Improper number of arguments: at least one is required and not more than two are allowed:
        - hhtp server's address (required)
        - port number(defaults to 80 if not specified)''')
    sys.exit(1)
else:
    server = sys.argv[1]
    port = '80'
    if len(sys.argv) == 3:
        if not sys.argv[2].isdigit():
            print('Port number is invalid - exiting')
            sys.exit(2)
        else:
            port = sys.argv[2]
    try:
        URL = server+':'+port
        reply = requests.head(URL)
    except requests.exceptions.Timeout:
        print('Connection timeout.')
        sys.exit(3)
    except Exception as e:
        print('Expception: ',e)
        sys.exit(4)
    else:
        print(reply.status_code)
