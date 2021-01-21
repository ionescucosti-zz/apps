import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.text)
        #print(reply.headers['Content-Type'])
        #print(reply.json())
    else:
        print("Server error")